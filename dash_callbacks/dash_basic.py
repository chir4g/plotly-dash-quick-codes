import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background':'#111111','text': '#7FDBFF'}

app.layout = html.Div(children=[
    html.H1('Hello Dash!',style={'textAlign':'center',
                                'color':colors['text']}),
    dcc.Graph(id='barchart',
                figure={'data':[
                    {'x':[1,2,3],'y':[4,5,6],'type':'bar','name':'DL'},
                    {'x':[1,2,3],'y':[9,10,11],'type':'bar','name':'MH'}
                ],
                'layout':{
                    'plot_bgcolor' : colors['background'],
                    'paper_bgcolor' : colors['background'],
                    'font' : {'color':colors['text']},
                    'title':'First Dash Board!!'}
    })
], style={'backgroundcolor':colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)