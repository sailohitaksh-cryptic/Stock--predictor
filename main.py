import streamlit as st
from datetime import date

import yfinance as yf
import pmdarima as pm
import pandas as pd
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")

stocks = ("AAPL", "GOOG","MSFT","GME")
selected_stocks = st.selectbox("Select Dataset for Prediction", stocks)

n_years = st.slider("Years of Production:",1,4)
period = n_years * 365


@st.cache
def load_data(ticker):
    data = yf.download(ticker,START,TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load Data...")
data = load_data(selected_stocks)
data_load_state.text("Loading Data... Done!") 

st.subheader('Raw Data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Forecasting 
df_train = data[["Date", "Close"]]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
df_train['ds'] = pd.to_datetime(df_train['ds'])

model = pm.auto_arima(df_train['y'], seasonal=False, suppress_warnings=True)
forecast = model.predict(n_periods=period, return_conf_int=True)

forecast_values = forecast[0]
forecast_dates = pd.date_range(start=df_train['ds'].iloc[-1], periods=period + 1, freq='D')[1:]
forecast_ci = forecast[1]

st.subheader('Forecast Data')
st.write(forecast_values[-5:])

st.write('Forecast Data')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_train['ds'], y=df_train['y'], name='Actual'))
fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_values, name='Forecast'))
fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_ci[:, 0], fill=None, mode='lines', line_color='blue', name='Lower CI'))
fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_ci[:, 1], fill='tonexty', mode='lines', line_color='red', name='Upper CI'))
fig.update_layout(title_text='Forecast Data', xaxis_rangeslider_visible=True)
st.plotly_chart(fig)
