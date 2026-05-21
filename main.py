import requests


# Pune coordinates
latitude = 18.52
longitude = 73.85

# API URL
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m"
)

# Send request to API
response = requests.get(url)

# Convert JSON response into Python dictionary
data = response.json()

# Print full data
print(data)

# Extract and print current temperature
temperature = data["current"]["temperature_2m"]
print("Current temperature:", temperature)