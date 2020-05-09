import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("covid_19_india.csv")
states = list(set(df['State/UnionTerritory'].values))
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by='Date').reset_index(inplace=True)
df_by_state = df.groupby(['State/UnionTerritory','Date']).sum()

def getStateData(state):
    df_by_date = df_by_state.loc[state]
    return df_by_date.index,df_by_date.Confirmed


data = [go.Scatter(x=getStateData(state)[0],y=getStateData(state)[1],mode='lines',name=state) for state in states ]

pyo.plot(data)