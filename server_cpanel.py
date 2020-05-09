import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

import plotly.graph_objs as go
import pandas as pd
import json

covid19 = pd.read_csv("latest_data/covid19_statewise.csv")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)
app.title = 'Covid Dashboard'

state_options = [{'label':str(day), 'value':day} for day in covid19['State'].unique()]
day_options = [{'label':str(day), 'value':day} for day in covid19['Date'].unique()]

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
    
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})


app.layout = html.Div([
    html.Div([
        html.H1("Made by Blacknet with Love")
    ], style={'textAlign':'center'}),
    html.Div([
        html.Div([
            dcc.Graph(id='line_graph'),
            dcc.Dropdown(id='state_picker',options=state_options,value='Delhi',multi=True)
        ], className="six columns"),
        html.Div([
            dcc.Graph(id='bar_graph'),
            dcc.Dropdown(id='day_picker',options=day_options,value=covid19['Date'].max())
        ], className="six columns"),
    ], className="row"),
    html.Div([
    dcc.Graph(
        config={'displayModeBar': False},
        figure=fig,
        ),
    ])  
])

@app.callback(Output('line_graph','figure'),[Input('state_picker','value')])
def update_line_figure(selected_state):
    traces = []
    for state in selected_state:
        filtered_df = covid19[covid19['State'] == state]
        trace = go.Scatter(x=filtered_df.Date,y=filtered_df.TotalConfirmed,
                        mode='markers+lines',name=state)
        traces.append(trace)

    return {'data':traces,
            'layout':go.Layout(title='State-Wise',
                                xaxis= {'title':'Date'}, yaxis= {'title':'Total Cases'})}

@app.callback(Output('bar_graph','figure'),[Input('day_picker','value')])
def update_figure(selected_date):
    filtered_df = covid19[covid19['Date'] == selected_date]
    trace = go.Bar(
        x=filtered_df.State,
        y=filtered_df.TotalConfirmed,
        marker={'color':'#3CB371'})


    return {'data':[trace],
            'layout':go.Layout(title='Day-Wise',
                                yaxis= {'title':'Total Cases'})}


#server = app.server
#wsgi.py -> from base import server as application
if __name__ == '__main__':
    app.run_server(debug=True)