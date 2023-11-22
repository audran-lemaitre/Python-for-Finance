import streamlit as st
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objects as go
import pandas as pd

st.title("🔮 Forecast model: ARIMA")
st.write(
    """
    Explore the future trajectory of the S&P500 with this simple forecasting tool. 


    In this app, we used ARIMA (more info below) to forecast the next week's closing prices of the S&P500 based on historical data.
    
    
    Visualize the forecast alongside historical trends, gaining insights into potential market movements. 
    A user-friendly interface makes it easy to grasp and engage with the predictions.
    """
)

def get_stock_data():
    # Download S&P500 historical data
    stock_data = yf.download('^GSPC', start='2021-07-01', end='2022-01-01', progress=False)
    return stock_data

def create_forecast(stock_data, forecast_steps=7):
    # Use ARIMA for forecasting
    model = ARIMA(stock_data['Close'], order=(5, 1, 0))
    results = model.fit()

    # Forecast the next week
    forecast_values = results.forecast(steps=forecast_steps)

    return forecast_values

def plot_stock_forecast(stock_data, forecast_values):
    # Plot historical data and forecast
    fig = go.Figure()

    # Historical data
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Historical Data'))

    # Forecast
    last_date = stock_data.index[-1]
    forecast_dates = [last_date + pd.DateOffset(days=i) for i in range(1, len(forecast_values) + 1)]
    fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_values,
                             mode='lines+markers', name='Forecast'))

    # Layout
    fig.update_layout(title='S&P500 Price Forecast',
                      xaxis_title='Date',
                      yaxis_title='S&P500 Close Price',
                      template='plotly_dark')

    return fig

def main():
    st.title('S&P500 Price Forecasting App')

    # Get historical data
    stock_data = get_stock_data()

    # Create forecast for one week
    forecast_values = create_forecast(stock_data, forecast_steps=7)

    # Plot the graph
    fig = plot_stock_forecast(stock_data, forecast_values)
    st.plotly_chart(fig)

    # Display model explanation
    st.subheader('Forecasting Model: ARIMA')
    st.write("""
    ### Financial Model Explanation:

    **ARIMA Model:**
    - ARIMA is a time series forecasting model that combines autoregression (AR) and moving average (MA) models. The parameters `(p, d, q)` in the ARIMA model determine the number of autoregressive terms, the degree of differencing, and the number of moving average terms, respectively.
    - In this case, the ARIMA model is initialized with `(5, 1, 0)`.
  
    ### Results:
    **Graphical Forecast:**
    - The interactive chart displays historical data and the forecasted S&P500 closing prices for the next week. Users can visually assess how well the model predicts future prices.

    **ARIMA Model Explanation:**
    - The app provides a brief explanation of the ARIMA model, emphasizing its combination of autoregressive and moving average components and the significance of the parameters `(p, d, q)`.

    """)

if __name__ == "__main__":
    main()

