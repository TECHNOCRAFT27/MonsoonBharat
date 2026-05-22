import requests
import pandas as pd
from pathlib import Path

Base_dir = Path(__file__).parent.parent

dataset_path = Base_dir / "dataset" / "india_cities.csv"    


df = pd.read_csv(dataset_path)

results = []

for index, row in df.iterrows():
    city = row["city"]
    latitude = row["latitude"]
    longitude = row["longitude"]

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m"
    )

    response = requests.get(url)
    data = response.json()
    temperature = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]

    print(f"Current temperature in {city}: {temperature}°C")
    print(f"Current humidity in {city}: {humidity}%")

    results.append({
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "temperature": temperature,
        "humidity": humidity
    })
    

weather_df = pd.DataFrame(results)


dataset_path = Base_dir / "dataset" / "weather_data.csv"

weather_df.to_csv(dataset_path, index=False)

average_temp = weather_df["temperature"].mean()

print("Average temperature:", average_temp)