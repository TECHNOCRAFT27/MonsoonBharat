# %% # SECTION 01 : Imports

import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd
import requests

# %% # SECTION 02 : Project Paths

Base_dir = Path(__file__).parent.parent
input_dataset_path = Base_dir / "dataset" / "indian_cities.csv"
output_dataset_path = Base_dir / "dataset" / "weather_data.csv"


# %% SECTION 03 : Load India Cities Dataset

df = pd.read_csv(input_dataset_path)
print("Dataset Loaded Successfully ✅")
print(df.head())


# %% SECTION 04 : Fetch Weather Data function


def fetch_weather(row):

    city = row["city"]
    latitude = row["latitude"]
    longitude = row["longitude"]

    print(f"\nFetching weather for: {city}")

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        temperature = data["current"]["temperature_2m"]
        humidity = data["current"]["relative_humidity_2m"]

        print(f"✅ {city} added successfully")

        return {
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "temperature": temperature,
            "humidity": humidity,
        }

    except Exception as error:
        print(f"❌ Error fetching data for {city}")
        print(error)
        return None


# %% SECTION 05 : ThreadPoolExecutor

results = []
start_time = time.time()

with ThreadPoolExecutor(max_workers=10) as executor:
    weather_data = executor.map(fetch_weather, [row for index, row in df.iterrows()])


# %% SECTION 06 : Collect Results

for result in weather_data:
    if result is not None:
        results.append(result)

# %% SECTION 06 : Convert Results To DataFrame

weather_df = pd.DataFrame(results)

print("\nWeather DataFrame Created ✅")
print(weather_df.head())


# %% # SECTION 07 : Save Weather Data

weather_df.to_csv(output_dataset_path, index=False)

# execution time
end_time = time.time()
total_time = end_time - start_time

print("\nWeather data saved successfully ✅")
print(f"\nExecution Time: {total_time:.2f} seconds")

# %% #
