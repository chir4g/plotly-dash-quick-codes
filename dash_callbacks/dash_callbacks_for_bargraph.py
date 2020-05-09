import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output

import plotly.graph_objs as go
import pandas as pd

covid19 = pd.read_csv("latest_data/covid19_statewise.csv")

app = dash.Dash()


day_options = [{'label':str(day), 'value':day} for day in covid19['Date'].unique()]

app.layout = html.Div([
            dcc.Graph(id='Graph'),
            dcc.Dropdown(id='day_picker',options=day_options,value=covid19['Date'].max())
])

@app.callback(Output('Graph','figure'),[Input('day_picker','value')])
def update_figure(selected_date):
    filtered_df = covid19[covid19['Date'] == selected_date]
    trace = go.Bar(
        x=filtered_df.State,
        y=filtered_df.TotalConfirmed,
        marker={'color':'#3CB371'})


    return {'data':[trace],
            'layout':go.Layout(title='COVID-19',
                                xaxis= {'title':'State'}, yaxis= {'title':'Total Cases'})}

if __name__ == '__main__':
    app.run_server(debug=True)