import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "../dataset/weather_data.csv"

from scipy.interpolate import griddata

df = pd.read_csv(data_path)

latitudes = df["latitude"]
longitudes = df["longitude"]

temperatures = df["temperature"]
humidity = df["humidity"]

grid_lon, grid_lat = np.mgrid[
    68:97:300j,
    6:38:300j
]

grid_temp = griddata(
    (longitudes, latitudes),
    temperatures,
    (grid_lon, grid_lat),
    method="cubic"
)

plt.figure(figsize=(10, 8))

contour = plt.contourf(
    grid_lon,
    grid_lat,
    grid_temp,
    levels=20,
    cmap="coolwarm"
)

plt.colorbar(contour, label="Temperature (°C)")

plt.scatter(
    longitudes,
    latitudes,
    color="black",
    s=20
)

plt.scatter(
    longitudes,
    latitudes,
    color="black",
    s=20
)

plt.scatter(
    longitudes,
    latitudes,
    color="black",
    s=20
)