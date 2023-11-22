import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

pd.options.plotting.backend = "plotly"
st.set_page_config(layout="wide")
st.title('🎲 Simulation of Geometric Brownian Motion')

st.write(
    """
    Experience the dynamics of stock prices through a Geometric Brownian Motion simulation. 
    Adjust parameters like drift coefficient, time horizon, volatility, and more. 
    Run simulations to visualize possible stock price paths. 
    The interactive chart allows you to explore different scenarios 
    and gain insights into the potential variability of stock prices over time.


    **Explanation of GBM:**
    - The Geometric Brownian Motion (GBM) model is used to simulate the random movement of stock prices over time.
    - The formula used for simulation is based on the stochastic differential equation for GBM.
    - At each time step, the stock price is updated based on the current price, drift coefficient (`mu`), volatility (`sigma`), and a random normal variable.

    **Result Interpretation:**
    - The simulation generates multiple stock price paths based on the specified parameters.
    - The variability in these paths demonstrates the inherent uncertainty and randomness in stock price movements.
    - Users can gain insights into the potential range of stock prices over the given time horizon by adjusting the input parameters.
    """
)

# Parameters
# drift coefficent
mu = st.sidebar.number_input('Select the mu parameter : ', value=0.1)
# number of steps
n = st.sidebar.number_input('Select the steps of dicretization : ', value=100)
# time in years
T = st.sidebar.number_input('Select the time horizon in year : ', value=1)
# number of sims
M = st.sidebar.number_input('Select the number of simulation :', value=500)
# initial stock price
S0 = st.sidebar.number_input('Select the initial stock price', value=1)
# volatility
sigma = st.sidebar.number_input('Select the volatility factor : ', value=0.5)
run = st.button('Simulate ! ')
if run:
    # calc each time step
    dt = T / n
    # simulation using numpy arrays
    St = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(M, n)).T
    )
    # include array of 1's
    St = np.vstack([np.ones(M), St])
    # multiply through by S0 and return the cumulative product of elements along a given simulation path (axis=0).
    St = S0 * St.cumprod(axis=0)

    # Define time interval correctly
    time = np.linspace(0, T, n + 1)
    # Require numpy array that is the same shape as St
    tt = np.full(shape=(M, n + 1), fill_value=time).T
    St = pd.DataFrame(St)
    fig = px.line(St)
    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)