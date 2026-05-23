# %%
import pandas
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "../dataset/in.csv"

df = pandas.read_csv(data_path)


# %%
# Filter the data to only include the city, lat, and lng columns
df = df[["city","lat","lng"]]

df.columns = ["city","latitude","longitude"]
# %%

#save the filtered data to a new csv file
filtered_data_path = base_path / "../dataset/indian_cities.csv"
df.to_csv(filtered_data_path, index=False)


# %%