import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input_id',value='Text',type='text'),
    html.Div(id='my_div')
])

@app.callback(Output(component_id='my_div',component_property='children'),
                [Input(component_id='input_id',component_property='value')])
def update_output_div(input_value):

    return "You entered {}".format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)