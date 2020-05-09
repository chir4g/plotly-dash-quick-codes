import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

cases = pd.read_html("https://www.mohfw.gov.in/#cases")
cases_df = cases[0]
cases_df = cases_df.iloc[:33,1:]
cases_df.columns = ['State','Confirmed','Cured','Death']
data_type_columns = {'State': object,'Confirmed': int, 'Cured': int, 'Death':int}
cases_df = cases_df.astype(data_type_columns)

app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='scatterplot',
                    figure = {'data':[
                        go.Scatter(
                            x=cases_df.Cured,
                            y=cases_df.Death,
                            text=cases_df.State,
                            mode='markers',
                            marker=dict(size=cases_df.Confirmed/20),
                        )
                    ],'layout':go.Layout(title='Plotly Plot in Dash',
                                            xaxis= {'title':'CURED'},yaxis= {'title':'DEATH'}
                    
                    )}),
                    dcc.Graph(id='scatterplot2',
                    figure = {'data':[
                        go.Scatter(
                            x=cases_df.Cured,
                            y=cases_df.Death,
                            text=cases_df.State,
                            mode='markers',
                            marker=dict(size=cases_df.Confirmed/20,color='rgb(255,100,200)'),
                        )
                    ],'layout':go.Layout(title='Second Plotly Plot in Dash',
                                            xaxis= {'title':'CURED'},yaxis= {'title':'DEATH'}
                    
                    )})
                    ])

if __name__ == '__main__':
    app.run_server(debug=True)