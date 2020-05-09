import plotly.graph_objs as go
import json
import pandas as pd


covid19 = pd.read_csv("latest_data/covid19_statewise.csv")

with open("data_geojson/india_states_updated.geojson") as file:
    geo_locations = json.load(file)

fig = go.Figure(go.Choroplethmapbox(geojson=geo_locations, locations=covid19.State, z=covid19.TotalConfirmed,
            colorscale="Viridis", zmin=covid19.TotalConfirmed.min(), zmax=covid19.TotalConfirmed.max(),
            featureidkey="properties.NAME_1",marker_opacity=0.5, marker_line_width=0,showscale=False
            ))

fig.update_layout(
    autosize=False,width=550,height=500,geo_scope = 'asia', 
    title = "COVID-19 India",mapbox_style="carto-positron",mapbox_zoom=3, 
    mapbox_center = {"lat": 23.705185, "lon": 78.537927})
    
fig.update_layout(margin={"r":0,"t":80,"l":0,"b":0})