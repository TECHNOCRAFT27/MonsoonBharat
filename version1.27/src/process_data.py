import pandas as pd
import plotly.express as px
import plotly.io as pio

# Open plot in browser
pio.renderers.default = "browser"

# Load processed weather data
df = pd.read_csv("../dataset/weather_data.csv")

# Create heatmap
fig = px.density_map(
    df,
    lat="latitude",
    lon="longitude",
    z="temperature",
    radius=25,
    center=dict(lat=22, lon=78),
    zoom=3.5,
    map_style="carto-positron"
)

# Show map
fig.show()