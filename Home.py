import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="📍",
)

st.write("# Financial dashboard with streamlit")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ## Summary
    - Stock's return comparaison
    - Brownian simulation
    - Portfolio management dashboard
    - Forecast model


    ## Report: Financial dashboard with streamlit


    ### 🎯 Goal of the project:
    In carrying out this project my goal was to familiarize myself with python, a language that I did not really know before this project. 
    Also familiarize myself with a text editor and github as well as the streamlit framework.


    In order to build this application, I was inspired by the code of our teacher UBEYDULLAH Ozcan, official streamlit resources, YouTube videos as well as ChatGPT for debugging.
    
    
    For the source of the data, I used yahoo Finance to extract prices of the S&P500 index and other stocks.

    
    
    ### 🏛 Python Project structure

    First, I had to choose a text editor. I opted for VS code, because I had already used it before to carry out other projects.



    I decided to create a multi-page streamlit application. To do this I first created a file like entrypoint “main.py” then a “pages” file. 
    In the latter I created my 4 projects.   

    Before starting my project, I created a virtual environment, “venv”, in my  terminal. 
    I then downloaded the libraries necessary for my projects: yfinance, streamlit, pandas, numpy, matplotlib, plotly & statsmodels.

        
    
    ### 💡 What I learned from this project & Feedback

    I already had some basis in coding, notably on projects in html, css, react, solidity… 
    But I had never been interested in the python language. 
    I realize that this language is more accessible than what I thought. 
    And that this language has many uses, particularly in data analysis, artificial intelligence, financial models, etc.


    **However, I encountered some problems while carrying out this project.**



    - First of all I had the problem of the blank sheet, I really didn't know what to do. So I turned to the streamlit library and YouTube to find some ideas.



    - Then, I had difficulty understanding the point of creating a development environment. But I quickly understood its interest by finding out about it on YouTube.

    
    - Finally, I encountered many bugs all over the place. The debugger of VS code helped me a lot to identified problems. In addition, I used ChatGPT as an assistant to help me resolve bugs. 
    I also spent an afternoon on a bug related to the installation of the fbprophet library on Mac. Impossible to find a way to make it work. So I used Yahoo finance for all of my projects.


    This project was very enriching in every way, I liked having the freedom to do what I wanted!

    ### 🔎 Want to learn more about me?
    - Check out my [LinkedIn](https://www.linkedin.com/in/audranlemaitre/)
    - Jump into my [GitHub](https://github.com/audran-lemaitre)
"""
)