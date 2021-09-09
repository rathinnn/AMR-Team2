import yfinance as yf

def getInfo(ticker):
    return yf.Ticker(ticker).info