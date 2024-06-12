import pandas as pd
import plotly.express as px
from pathlib import Path

# Load the data using pandas
file_path = Path("eq_data/world_fires_1_day.csv")
df = pd.read_csv(file_path)

# Display the first few rows to understand the data structure (optional)
print(df.head())

# Extract relevant data: latitude, longitude, and brightness
latitudes = df['latitude']
longitudes = df['longitude']
brightness = df['brightness']

# Create a scatter plot on a world map using Plotly Express
fig = px.scatter_geo(
    df,
    lat='latitude',
    lon='longitude',
    size='brightness',
    title='World Fires - 1 Day',
    color='brightness',
    color_continuous_scale='Viridis',
    labels={'color': 'Brightness'},
    projection='natural earth'
)

# Show the plot
fig.show()
