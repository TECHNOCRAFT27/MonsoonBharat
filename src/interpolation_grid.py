# %% # importing libraries
from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
from shapely.geometry import Point

# %% # Define Project Paths
Base_dir = Path(__file__).parent.parent

weather_dataset_path = (
    Base_dir / "dataset" / "weather_data.csv"
)

map_path = (
    Base_dir
    / "dataset"
    / "map"
    / "ne_110m_admin_0_countries.shp"
)
# %% # Load Weather Dataset

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
    300

)

longitude_range = np.linspace(

    longitudes.min(),
    longitudes.max(),
    300

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

world = gpd.read_file(map_path)

print(world.head())

# %% # filtering for India

india_map = world[

    world["ADMIN"] == "India"

]


print(india_map)

# %% # extract India polygon

india_polygon = india_map.geometry.iloc[0]

# %% # Create India Mask Grid

mask = np.zeros(

    longitude_grid.shape,

    dtype=bool

)

print(mask.shape)

# %% # Check Every Grid Point

for row_index in range(longitude_grid.shape[0]):

    for column_index in range(longitude_grid.shape[1]):


        longitude = longitude_grid[

            row_index,
            column_index

        ]


        latitude = latitude_grid[

            row_index,
            column_index

        ]


        point = Point(

            longitude,
            latitude

        )


        if india_polygon.contains(point):

            mask[

                row_index,
                column_index

            ] = True



# %% # Apply India Mask

masked_temperature_grid = np.where(

    mask,

    temperature_grid,

    np.nan

)

print("India Mask Applied ✅")

# %% # Temperature Heatmap


# %% # plot temperature heatmap
fig, ax = plt.subplots(figsize=(12, 8))

heatmap = ax.contourf(

    longitude_grid,
    latitude_grid,
    masked_temperature_grid,

    levels=200,
    cmap="coolwarm"

)


india_map.boundary.plot(

    ax=ax,

    color="black",
    linewidth=1

)

#Plot Weather Cities
ax.scatter(

    longitudes,
    latitudes,

    color="black",

    s=10,

    label="Weather Cities"

)
#hot cites
top_hot_cities = weather_df.sort_values(

    by="temperature",
    ascending=False

).head(20)

print(top_hot_cities[
    ["city", "temperature"]
])


for index, row in top_hot_cities.iterrows():

    city_name = row["city"]

    latitude = row["latitude"]

    longitude = row["longitude"]

    temperature = row["temperature"]


    ax.text(

    longitude,
    latitude,

    f"{city_name}\n{temperature}°C",

    fontsize=7,

    color="black",

    bbox=dict(
        facecolor="white",
        alpha=0.7,
        edgecolor="none"
    )

)

print("\nCity Labels Added ✅")


plt.colorbar(

    heatmap,
    ax=ax,

    label="Temperature (°C)"

)


ax.set_xlabel("Longitude")

ax.set_ylabel("Latitude")

ax.set_title("India Isothermal Temperature Map")

ax.set_xlim(67, 98)

ax.set_ylim(6, 38)

table_data = top_hot_cities[

    ["city", "temperature"]

].values


table = plt.table(

    cellText=table_data,

    colLabels=["City", "Temp °C"],

    cellLoc="center",

    #loc="upper right"
    
    bbox=[1.35, 0.05, 0.3, 0.9]

)


table.auto_set_font_size(False)

table.set_fontsize(8)

table.scale(1, 1.5)

plt.show()

# %% # 

