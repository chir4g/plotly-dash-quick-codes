import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output
import geo_india as gi

import plotly.graph_objs as go
import pandas as pd
import json

#'https://codepen.io/chriddyp/pen/bWLwgP.css',
covid19 = pd.read_csv("latest_data/covid19_statewise.csv")
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(external_stylesheets=external_stylesheets)
app.title = 'Covid Dashboard'

state_options = [{'label':str(day), 'value':day} for day in covid19['State'].unique()]
day_options = [{'label':str(day), 'value':day} for day in covid19['Date'].unique()]

dbc.Row([
    dbc.Col([
        html.Div([
            dcc.Graph(id='line_graph'),
            dcc.Dropdown(id='state_picker',options=state_options,value='Delhi',multi=True)
        ])
    ],md=6),
        dbc.Col([
        html.Div([
            dcc.Graph(id='bar_graph'),
            dcc.Dropdown(id='day_picker',options=day_options,value=covid19['Date'].max())
        ])
    ],md=6)
])



html.Div([
        html.Div([
            dcc.Graph(id='line_graph'),
            dcc.Dropdown(id='state_picker',options=state_options,value='Delhi',multi=True)
        ], className="six columns"),
        html.Div([
            dcc.Graph(id='bar_graph'),
            dcc.Dropdown(id='day_picker',options=day_options,value=covid19['Date'].max())
        ], className="six columns"),
    ], className="row")


app.layout = html.Div([
    html.Div([
        dbc.Alert("Made by BlackNet with Love", color="success")
    ], style={'textAlign':'center','fontSize':30}),
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id='line_graph',config={'displayModeBar': False}),
                dcc.Dropdown(id='state_picker',options=state_options,value='Delhi',multi=True)
            ])
        ],md=6),
        dbc.Col([
        html.Div([
            dcc.Graph(id='bar_graph',config={'displayModeBar': False}),
            dcc.Dropdown(id='day_picker',options=day_options,value=covid19['Date'].max())
        ])
        ],md=6)
    ]),
    html.Div([
    dcc.Graph(
        config={'displayModeBar': False},
        figure=gi.fig,
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