import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
                html.Label('Dropdown'),
                dcc.Dropdown(options=[
                    {'label':'New York City','value': 'NYC'},
                    {'label':'San Francisco','value': 'SF'}],
                    value = 'SF'),

                html.Label('Slider'),
                dcc.Slider(min=-10,max=10,step=1,value=0)
])


if __name__ == '__main__':
    app.run_server(debug=True)