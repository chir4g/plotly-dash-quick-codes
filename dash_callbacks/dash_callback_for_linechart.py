import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

import plotly.graph_objs as go
import pandas as pd

covid19 = pd.read_csv("latest_data/covid19_statewise.csv")

app = dash.Dash()


state_options = [{'label':str(day), 'value':day} for day in covid19['State'].unique()]

app.layout = html.Div([
            dcc.Graph(id='Graph'),
            dcc.Dropdown(id='state_picker',options=state_options,value='Delhi')
])

@app.callback(Output('Graph','figure'),[Input('state_picker','value')])
def update_figure(selected_state):
    filtered_df = covid19[covid19['State'] == selected_state]
    
    trace = go.Scatter(x=filtered_df.Date,y=filtered_df.TotalConfirmed,
                    mode='markers+lines',name=selected_state)

    return {'data':[trace],
            'layout':go.Layout(title='COVID-19',
                                xaxis= {'title':'State'}, yaxis= {'title':'Total Cases'})}

if __name__ == '__main__':
    app.run_server(debug=True)