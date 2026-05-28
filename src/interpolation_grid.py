# %% # importing libraries
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd

# %% # defining the path to the dataset
Base_dir = Path(__file__).parent.parent

weather_dataset_path = (
    Base_dir / "dataset" / "weather_data.csv"
)
# %% # loading the dataset

weather_df = pd.read_csv(weather_dataset_path)

print("Weather Dataset Loaded ✅")

print(weather_df.head())

# %% # creating the interpolation grid
latitudes = weather_df["latitude"]

longitudes = weather_df["longitude"]

temperatures = weather_df["temperature"]


print(latitudes.head())

print(longitudes.head())

print(temperatures.head())

print(weather_df.shape)

# %% # Create Coordinate Ranges

latitude_range = np.linspace(

    latitudes.min(),
    latitudes.max(),
    100

)

longitude_range = np.linspace(

    longitudes.min(),
    longitudes.max(),
    100

)


print(latitude_range)

print(longitude_range)
# %% # Create Meshgrid

longitude_grid, latitude_grid = np.meshgrid(

    longitude_range,
    latitude_range

)


print("Longitude Grid Shape:")

print(longitude_grid.shape)


print("\nLatitude Grid Shape:")

print(latitude_grid.shape)

# %% # Temperature Interpolation

temperature_grid = griddata(

    # Known coordinate points
    (longitudes, latitudes),

    # Known temperature values
    temperatures,

    # New virtual grid coordinates
    (longitude_grid, latitude_grid),

    # Interpolation method
    method="linear"

)


print("Temperature Grid Created ✅")

print(temperature_grid.shape)

# %% #  Load World Map

map_path = (

    Base_dir
    / "dataset"
    / "map"
    / "ne_110m_admin_0_countries.shp"

)

world = gpd.read_file(map_path)

print(world.head())

# %% # filtering for India

india_map = world[

    world["ADMIN"] == "India"

]


print(india_map)

# %% # Temperature Heatmap

fig, ax = plt.subplots(figsize=(12, 8))

heatmap = ax.contourf(

    longitude_grid,
    latitude_grid,
    temperature_grid,

    levels=100,
    cmap="coolwarm"

)

contours = ax.contour(

    longitude_grid,
    latitude_grid,
    temperature_grid,

    levels=10,
    colors="black",
    linewidths=0.5

)


ax.clabel(

    contours,

    inline=True,
    fontsize=8

)

india_map.boundary.plot(

    ax=ax,

    color="black",
    linewidth=1

)

plt.colorbar(

    heatmap,
    ax=ax,

    label="Temperature (°C)"

)


ax.set_xlabel("Longitude")

ax.set_ylabel("Latitude")

ax.set_title("India Isothermal Temperature Map")

plt.show()


# %%
