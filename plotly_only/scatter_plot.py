import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
X = np.random.randint(1,101,100)
y = np.random.randint(1,101,100)

data = [go.Scatter(x=X,
                    y=y,
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,204,295)',
                        symbol='pentagon',
                        line = {'width' : 2}
                    ))] # Contains actual plot

layout = go.Layout(title='Random Scatter Plot', 
                    xaxis={'title':'X-axis'},
                    yaxis= dict(title='Y-axis'),
                    hovermode='closest')    # Sets the beautification of the layout

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter_plot.html')