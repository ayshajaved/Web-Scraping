import requests
'''
yfinance (Yahoo Finance) is a Python library that simplifies fetching stock market data, such as historical prices, real-time data, dividends, splits, and more, directly from Yahoo Finance. Unlike traditional web scraping, it doesn't use requests or BeautifulSoup. Instead, it interacts with Yahoo Finance's internal endpoints and processes the returned data in a structured format.
'''
import yfinance as yf
#two methods of yf --> Ticker and download
data = yf.Ticker("AAPL")  #it is the method that gives the information of the one stock or ticker symbol, returns a python object
# print(data.info)  #it is the method that gives the information of the one stock or ticker
data_ = data.history(period="1d")  #gives the Returns a pandas DataFrame containing historical price data for the specified period
print(data_)
#Dividends: Provide direct financial rewards to shareholders.
# Stock Splits: Adjust the number of shares and price without changing overall value.
stock = data.splits
print(stock)
div = data.dividends
print(div)

#download  is used to fetch historical market data for one or multiple ticker symbols. It's especially useful for bulk data retrieval.
data = yf.download("AAPL MSFT GOOGL", start="2023-01-01", end="2023-12-31")
print(data)


