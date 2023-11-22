import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("📊 Investment Portfolio Dashboard")
st.write(
    """
    Effortlessly assess your investment portfolio's performance and risk with this interactive dashboard. 
    Input your assets, choose a starting date, and visualize cumulative returns. 
    Compare your portfolio against the S&P500 index to gauge its development. 
    Understand portfolio and benchmark risk, and explore the composition of your investments through an intuitive and informative dashboard.


    ### Financial Model Explanation:

    **Returns Calculation:** Daily percentage returns are calculated for each stock and the S&P500 index. This is a common metric in finance to assess the daily performance of an asset.

    **Cumulative Returns:** Cumulative returns show the total percentage change in value over time. It helps in understanding the overall performance of the portfolio and benchmark.

    **Portfolio Standard Deviation:**
    - The portfolio standard deviation is calculated using the formula for portfolio variance. The weights (`W`) are set to equal weights for simplicity (`np.ones(len(ret_df.cov()))/len(ret_df.cov())`).
    - The standard deviation of the portfolio returns is a measure of the portfolio's risk. A higher standard deviation indicates higher volatility and risk.

    ### Results:

    **Portfolio vs. Index Development:** The line chart visually compares the performance of the portfolio against the S&P500 index. Positive values indicate gains, while negative values represent losses.

    **Portfolio Risk:** The calculated standard deviation provides a measure of the risk associated with the portfolio.

    **Benchmark Risk:** The standard deviation of the S&P500 index returns gives an idea of the benchmark risk.

    **Portfolio Composition:** The pie chart shows the relative weights of each asset in the portfolio. In this case, each asset is given equal weight.
    """
)

assets = st.text_input("Provide your assets (comma-separated)","AAPL, MSFT, TSLA")
start = st.date_input("Pick a starting date for your analysis", value= pd.to_datetime('2022-06-01'))

data = yf.download(assets, start=start)['Adj Close']
ret_df = data.pct_change()
cumul_ret = (ret_df + 1).cumprod() - 1
pf_cumul_ret = cumul_ret.mean(axis=1)

benchmark = yf.download('^GSPC', start=start)['Adj Close']
bench_ret = benchmark.pct_change()
bench_dev = (bench_ret + 1).cumprod() - 1

W = (np.ones(len(ret_df.cov()))/len(ret_df.cov()))
pf_std = (W.dot(ret_df.cov()).dot(W)) ** (1/2)

st.subheader("Portfolio vs. Index Development")
tog = pd.concat([bench_dev, pf_cumul_ret], axis=1)
tog.columns = ['S&P500 Performance', 'Portfolio Performance']
st.line_chart(data=tog)

st.subheader("Portfolio Risk:")
pf_std

st.subheader("Benchmark Risk:")
bench_risk = bench_ret.std()
bench_risk

st.subheader("Portfolio composition:")
fig, ax = plt.subplots(facecolor='#121212')
ax.pie(W, labels=data.columns, autopct='%1.1f%%', textprops={'color': 'white'})
st.pyplot(fig)