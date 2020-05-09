import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['Div!!',
                        html.Div(['Div in Div 1 !!'],style={'color':'red'}),
                        html.Div(['Div in Div 2 !!'],style={'color':'blue'}),
                    ],
                    style={'color':'green'})


if __name__ == '__main__':
    app.run_server(debug=True)