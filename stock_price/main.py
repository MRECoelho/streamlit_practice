import streamlit as st

import pandas as pd

import yfinance as yf

tickerSymbol = 'GME'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2021-1-1', end='2021-1-29')
# Open High Low Close Volume Dividends Stock Splits


st.write("""
# Simple stock price graph app

Shown as the statistics for {}.
""".format(tickerSymbol))


st.write("""
### Opening price
""")
st.line_chart(tickerDf.Open)
st.write("""
### High price
""")
st.line_chart(tickerDf.High)
st.write("""
### Low price
""")
st.line_chart(tickerDf.Low)
st.write("""
### Closing price
""")
st.line_chart(tickerDf.Close)
