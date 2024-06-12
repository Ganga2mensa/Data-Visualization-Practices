import pandas as pd
import plotly.express as px

# Load the data from the CSV file
file_path = 'eq_data\world_fires_1_day.csv'
df = pd.read_csv(file_path)

# Display the first few rows to understand the data structure
print(df.head())

# Extract relevant data: latitude, longitude, and brightness
latitudes = df['latitude']
longitudes = df['longitude']
brightness = df['brightness']
print (latitudes)
# Create a scatter plot on a world map
fig = px.scatter_geo(
    df,
    lat=latitudes,
    lon=longitudes,
    size=brightness,
    size_max=10,
    title='World Fires - 1 Day',
    projection='natural earth',
    color=brightness,
    color_continuous_scale='YlOrRd',
    hover_name='brightness'
)

# Show the plot
fig.show()
