import yfinance as yf
import streamlit as st
import pandas as pd

# --------------------------------------------------------------
# Create Title and Description using markdown
# --------------------------------------------------------------
st.write(""" 
# Simple Price Stock App

Below you can find the closing stock price and volume from Twitter

""")

# --------------------------------------------------------------
# Define a Ticker Symbol
# --------------------------------------------------------------
tickerSymbol = 'TWTR'

# Get the ticker data
tickerData = yf.Ticker(tickerSymbol)

#Put the data into a DataFrame
Tickerdf = tickerData.history(period = '1d', start = '2010-5-31', end = '2022-11-30')

#Plot High Low Close stock price and Volume dividends using a line chart
st.line_chart(Tickerdf.Close)
st.line_chart(Tickerdf.Volume)