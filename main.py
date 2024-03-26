# Créé par croqu, le 22/07/2022 en Python 3.7
# Créé par croqu, le 04/07/2022 en Python 3.7
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import yfinance as yf
import math
import datetime

inter="15m"
np.random.seed(1)

stock_price=str(input("Enter the stock name: ")).upper()

data = yf.download(tickers=stock_price, period = "60d", interval = inter, rounding= bool)

data_medium=[]
for i in range(len(data.index)):
    data_medium.append((data["Open"][i]+ data["Close"][i])/2)

fig = go.Figure()
fig.add_trace(go.Candlestick (x=data.index,open = data["Open"], high=data["High"], low=data["Low"], close=data["Close"], name = "Candle chart"))
fig.add_trace(go.Scatter(x=data.index,y=data_medium,marker_color='blue',name='Line chart'))


dt_all = pd.date_range(start=data.index[0],end=data.index[-1])
dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(data.index)]
dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

fig.update_layout(margin=go.layout.Margin(
    l=20, #left margin
    r=20, #right margin
    b=20, #bottom margin
    t=80,  #top margin
))
fig.update_layout(title= stock_price)

# hide dates with no values
fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
#fig.update_xaxes(rangebreaks=[dict(values=nonbusinesshours),
#                               ])

fig.update_xaxes(
rangeslider_visible=True,

rangeselector=dict(buttons=list(
[dict(count=15, label="15m", step="minute", stepmode="backward"),
dict(count=45, label="45m", step="minute", stepmode="backward"),
dict(count=1, label="1h", step="hour", stepmode="backward"),
dict(count=6, label="6h", step="hour", stepmode="backward"),
dict(count=1, label="1d", step="day", stepmode="backward"),
dict(count=15, label="15d", step="day", stepmode="backward"),
dict(count=30, label="30d", step="day", stepmode="backward"),
dict(step="all")])))



fig.show()
