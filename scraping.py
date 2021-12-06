import numpy as np
import pandas as pd
import datetime

# Data Source
import yfinance as yf
import quandl
quandl.ApiConfig.api_key =  " qT522Nuw1rd-D5-4fhDR " # Johnathan's API key

# Data viz
import plotly.graph_objs as go

# Interval required 1 minute
data = yf.download(tickers='UBER', period='1d', interval='1m')

# declare figure
fig = go.Figure()

# Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))

# Add titles
fig.update_layout(
    title='Uber live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# Show
fig.show()


def scrape_data(start_period, end_period, ticker_stock='AAPL'):
    data = yf.download(tickers=ticker_stock, start=start_period, end=end_period)
    return data

# ticker_stock: a valid ticker symbol
# start_period/end_period: datetime.date type
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# get_open_and_close returns a 'pandas.core.frame.DataFrame'
def get_open_and_close(ticker_stock, start_period, end_period, interval):
    data = yf.download(ticker_stock,start_period, end_period, interval)
    return data[["Open","Close"]]

# get_volume has the same parameters as get_open_and_close
# returns a 'pandas.core.series.Series'
def get_volume(ticker_stock, start_period, end_period, interval):
    data = yf.download(ticker_stock, start_period, end_period, interval)
    return data["Volume"]
import numpy as np
import pandas as pd
import datetime

# Data Source
import yfinance as yf
import quandl
quandl.ApiConfig.api_key =  " qT522Nuw1rd-D5-4fhDR " # Johnathan's API key

# Data viz
import plotly.graph_objs as go

# Interval required 1 minute
data = yf.download(tickers='UBER', period='1d', interval='1m')

# declare figure
fig = go.Figure()

# Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))

# Add titles
fig.update_layout(
    title='Uber live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# Show
fig.show()


def scrape_data(start_period, end_period, ticker_stock='AAPL'):
    data = yf.download(tickers=ticker_stock, start=start_period, end=end_period)
    return data

# ticker_stock: a valid ticker symbol
# start_period/end_period: datetime.date type
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# get_open_and_close returns a 'pandas.core.frame.DataFrame'
def get_open_and_close(ticker_stock, start_period, end_period, interval):
    data = yf.download(ticker_stock,start_period, end_period, interval)
    return data[["Open","Close"]]

# get_volume has the same parameters as get_open_and_close
# returns a 'pandas.core.series.Series'
def get_volume(ticker_stock, start_period, end_period, interval):
    data = yf.download(ticker_stock, start_period, end_period, interval)
    return data["Volume"]
