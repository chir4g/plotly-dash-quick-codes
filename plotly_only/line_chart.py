import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

x_values = np.arange(1,101)
y_values = np.concatenate((np.random.randint(1,100,30), np.random.randint(200,1000,40), 
                            np.random.randint(1200,3000,30)))

trace0 = go.Scatter(x=x_values,y=y_values,
                    mode='markers',name='markers')

trace1 = go.Scatter(x=x_values,y=y_values+5,
                    mode='lines',name='linechart')

trace2 = go.Scatter(x=x_values,y=y_values+50,
                    mode='lines+markers',name='both')

data = [trace0,trace1,trace2]

layout = go.Layout(title='Line Charts')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure,'line_chart.html')