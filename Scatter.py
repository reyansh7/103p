import pandas as pd 
import plotly.express as px

df=pd.read_csv('data2.csv')
fig = px.scatter(df, x="date", y="cases", color="country", title='Covid-19')
fig.show()

input('enter to exit')