# #module 01 : Weather API
# import requests


# # Pune coordinates
# latitude = 18.52
# longitude = 73.85

# # API URL
# url = (
#     f"https://api.open-meteo.com/v1/forecast"
#     f"?latitude={latitude}"
#     f"&longitude={longitude}"
#     f"&current=temperature_2m"
# )

# # Send request to API
# response = requests.get(url)

# # Convert JSON response into Python dictionary
# data = response.json()

# # Print full data
# print(data)

# # Extract and print current temperature
# temperature = data["current"]["temperature_2m"]
# print("Current temperature:", temperature)





#module 02 : data handle panda

import pandas as pd

df = pd.read_csv("dataset/india_cities.csv")


df["city"]

for index, row in df.iterrows():
    print(row["city"])

#module 2.5 : data handle and api multiple city

import requests
import pandas as pd


df = pd.read_csv("dataset/india_cities.csv")

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
weather_df.to_csv("dataset/weather_data.csv", index=False)




# #module 2.7 : mini challenge compare pune and mumbai which one is hotter and and max temperature


    
# pune_temp = weather_df[weather_df["city"] == "Pune"]["temperature"].values[0]
# mumbai_temp = weather_df[weather_df["city"] == "Mumbai"]["temperature"].values[0]

# pune_humidity = weather_df[weather_df["city"] == "Pune"]["humidity"].values[0]
# mumbai_humidity = weather_df[weather_df["city"] == "Mumbai"]["humidity"].values[0]
    
# if pune_temp > mumbai_temp and pune_humidity < mumbai_humidity:
#     print("Pune is hotter than Mumbai.")
# elif pune_temp < mumbai_temp and pune_humidity > mumbai_humidity:
#     print("Mumbai is hotter than Pune.")
# else:
#     print("Pune and Mumbai have the same temperature.")     
    

# #Find hottest city.

# hottest_city = weather_df.loc[weather_df["temperature"].idxmax()]
# print(f"The hottest city is {hottest_city['city']} with a temperature of {hottest_city['temperature']}°C.")

