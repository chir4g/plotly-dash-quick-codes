import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output


import plotly.graph_objs as go
import pandas as pd
import geopandas as gpd
import json

covid19 = pd.read_csv("latest_data/covid19_statewise.csv")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

with open("data_geojson/india_states_updated.geojson") as file:
    geo_locations = json.load(file)

app = dash.Dash(external_stylesheets=external_stylesheets)


app.title = 'Covid Dashboard'

#23.705185, "lon": 78.537927
fig = go.Figure(go.Choroplethmapbox(geojson=geo_locations, locations=covid19.State, z=covid19.TotalConfirmed,
            colorscale="Viridis", zmin=covid19.TotalConfirmed.min(), zmax=covid19.TotalConfirmed.max(),
            featureidkey="properties.NAME_1",marker_opacity=0.5, marker_line_width=0,showscale=False
            ))

fig.update_layout(
    autosize=False,width=550,height=500,geo_scope = 'asia', 
    title = "COVID-19 India",mapbox_style="carto-positron",mapbox_zoom=3, 
    mapbox_center = {"lat": 23.705185, "lon": 78.537927})
    
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



app.layout = html.Div([
    dcc.Graph(
        config={'displayModeBar': False},
        figure=fig,
        ),
])

if __name__ == '__main__':
    app.run_server(debug=True)

