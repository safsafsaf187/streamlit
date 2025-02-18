import yfinance as yf
import streamlit as st


st.image("https://preview.redd.it/where-the-fuck-did-the-apple-meme-come-from-v0-nlfhz8mj0y2e1.jpeg?auto=webp&s=3fec19ccdc1fdf9c81f6da2604cd23049fe5e3e3", caption="Apple is in da building", width=500)

st.write("""
# SUP BRO
# Тут ты увидишь цены акций Apple
На графиках отображены **Цена закрытия** и **Объем** компании **Apple**

""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2020-1-01', end='2025-2-17')

st.write("""
## Цена закрытия
**хотя мы обычно приходим после закрытия**
""")
st.line_chart(tickerDf.Close)
st.write("""
## Объем
**ну а кто из нас не любит большие объемы?**
""")
st.line_chart(tickerDf.Volume)