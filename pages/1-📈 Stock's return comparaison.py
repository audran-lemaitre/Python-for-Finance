import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Plotting Demo 2", page_icon="📈")

st.title("📈 Stock's return comparaison")
st.write(
"""
    Explore and compare the historical returns of your favorite assets with this simple dashboard. 
    Select assets from Tesla (TSLA), Apple (AAPL), Microsoft (MSFT), Bitcoin (BTC-USD), and Ethereum (ETH-USD). 
    Adjust the start and end dates to visualize the cumulative returns over time. 
    The line chart provides a clear comparison of how each asset has performed during the selected period.

    ### Financial Model:
    The main financial model involves calculating relative returns:

    - **Relative Return (`relativeret` function):**
    - Computes daily percentage change in adjusted closing prices.
    - Calculates cumulative returns using `(1 + rel).cumprod() - 1`.

    ### Result Interpretation:

    - The line chart visually represents cumulative returns of selected assets over the specified date range.
    - Y-axis shows cumulative returns as percentages, while the x-axis represents time.
    - Positive values indicate gains, negative values denote losses.
    - Users can compare how each asset performed historically, aiding in investment decision-making.
"""
) 

tickers = ('TSLA', 'AAPL', 'MSFT','BTC-USD', 'ETH-USD')

dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

#Creation of a fonction to compare more easily stocks (relative return)
def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

#Creation of a graph with the relative return of the stocks we selected before
if len(dropdown) > 0:
    df = relativeret(df = yf.download(dropdown, start, end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)