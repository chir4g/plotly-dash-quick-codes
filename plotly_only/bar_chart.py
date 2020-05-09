import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("covid_19_india.csv")
df.drop(['Date','Confirmed'],axis=1,inplace=True)

df_by_state = df.groupby('State/UnionTerritory').sum()

trace1 = go.Bar(x=df_by_state.index,y=df_by_state.Cured,name='Cured',marker={'color':'#3CB371'})
trace2 = go.Bar(x=df_by_state.index,y=df_by_state.Deaths,name='Deaths',marker={'color':'#DC143C'})
data = [trace1,trace2]

layout = go.Layout(title='COVID-19')

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig)