from prophet import Prophet
import yfinance as yf
import numpy as np
import pandas as pd


def ensemble_prediction():
    pass


def run_prophet(data=data, predict_period=predict_period):
    # data1 = data.reset_index()
    # data1 = data1[["Date", "Open"]]
    data.columns = ["ds", "y"]
    m = Prophet()
    m.fit(data)
    future = m.make_future_dataframe(periods=predict_period)
    future.tail()
    forecast = m.predict(future)
    # forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    fig1 = m.plot(forecast)
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    return forecast


def run_holtswinter(data=data, predict_period=predict_period):
    pass


def run_arima(data=data, predict_period=predict_period):
    pass
