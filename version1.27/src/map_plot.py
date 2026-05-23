# %%
# SECTION 01 : Imports

import pandas as pd
import plotly.express as px

# %%
# SECTION 02 : Load Weather Data
from pathlib import Path
base_path = Path(__file__).parent
data_path = base_path / "../dataset/weather_data.csv"

df = pd.read_csv(data_path)

print(df.head())

# %%
# SECTION 03 : Create India Map

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude"
)

fig.show()

# %%
# SECTION 04 : Add City Hover Labels

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city"
)

fig.show()

# %%
# SECTION 05 : Temperature Color Mapping

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    color="temperature"
)

fig.show()

# %%
# SECTION 06 : Red Hot / Blue Cold

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    color="temperature",
    color_continuous_scale="RdYlBu_r"
)

fig.show()

# %%
# SECTION 07 : Bigger Markers

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    color="temperature",
    color_continuous_scale="RdYlBu_r",
    size="temperature"
)

fig.show()

# %%
# SECTION 08 : Better Map Style

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    color="temperature",
    color_continuous_scale="RdYlBu_r",
    size="temperature",
    map_style="carto-positron",
    zoom=3.5,
    center=dict(lat=22, lon=78)
)

fig.show()
# %%