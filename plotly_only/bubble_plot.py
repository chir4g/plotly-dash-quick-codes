import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df1 = pd.read_csv("covid_19_india.csv")
df1.drop(['Date','Confirmed'],axis=1,inplace=True)
df1 = df1.groupby('State/UnionTerritory').sum()
df2 = pd.read_csv("HospitalBedsIndia.csv")
df = pd.merge(df1,df2, left_on='State/UnionTerritory', right_on='State/UT')

print(df.head())

data = [go.Scatter(x=df['Cured'],y=df['Deaths'],text=df['State/UT'],mode='markers',
                    marker=dict(size=df['Total Beds']/1000,color=df['Deaths'],showscale=True))]

layout = go.Layout(title='COVID-19 Cured&Death VS No of Beds')

figure = go.Figure(data=data,layout=layout)

pyo.plot(figure)