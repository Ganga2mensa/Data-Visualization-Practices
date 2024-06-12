from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path(r"eq_data\eq_data_30_day_m1.geojson")
contents = path.read_text(encoding='utf-8')

all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

# print(len(all_eq_dicts))d

mags, lons, lats, eq_titles = [], [], [], []

def _eq_dicts(dict):
    mags.append(dict['properties']['mag'])
    lons.append(dict['geometry']['coordinates'][0])
    lats.append(dict['geometry']['coordinates'][1])
    eq_titles.append(dict['properties']['title'])

for eq_dict in all_eq_dicts:
    _eq_dicts(eq_dict)
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]
    # eq_title = eq_dict['properties']['title']
    # mags.append(eq_dict['properties']['mag'])
    # lons.append(eq_dict['geometry']['coordinates'][0])
    # lats.append(eq_dict['geometry']['coordinates'][1])
    # eq_titles.append(eq_dict['properties']['title'])

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])
title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, size = mags, title=title, color= mags,
color_continuous_scale='Viridis',
labels={'color':'Magnitude'},
projection='natural earth', hover_name=eq_titles,)
fig.show()

