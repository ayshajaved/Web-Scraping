#scraping other elements
import streamlit as st
import pandas as pd
import yfinance as yf  #library to get yahoo finance data
import matplotlib.pyplot as plt

# Function to fetch stock data from yahoo fianance
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to perform basic analysis
def analyze_stock_data(stock_data):
    if 'Adj Close' in stock_data.columns:
        stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
        stock_data['Cumulative Return'] = (1 + stock_data['Daily Return']).cumprod()
    else:
        stock_data['Daily Return'] = stock_data['Close'].pct_change()
        stock_data['Cumulative Return'] = (1 + stock_data['Daily Return']).cumprod()
    return stock_data

# Function to visualize stock data
def visualize_stock_data(stock_data, ticker):
    fig, ax = plt.subplots(2, 1, figsize=(14, 10))
    
    # Plot Adjusted Close Price or Close Price
    if 'Adj Close' in stock_data.columns:
        ax[0].plot(stock_data['Adj Close'], label='Adjusted Close Price')
    else:
        ax[0].plot(stock_data['Close'], label='Close Price')
    ax[0].set_title(f'{ticker} Stock Price')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Price')
    ax[0].legend()
    
    # Plot Cumulative Return
    ax[1].plot(stock_data['Cumulative Return'], label='Cumulative Return', color='green')
    ax[1].set_title(f'{ticker} Cumulative Return')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Cumulative Return')
    ax[1].legend()
    
    plt.tight_layout()
    st.pyplot(fig)

# Streamlit app
def main():
    st.title("Stock Market Data Analysis and Visualization")
    
    # User inputs
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
    start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))
    
    if st.button("Fetch and Analyze Data"):
        with st.spinner("Fetching data..."):
            stock_data = fetch_stock_data(ticker, start_date, end_date)
            if not stock_data.empty:
                analyzed_data = analyze_stock_data(stock_data)
                st.success("Data fetched and analyzed successfully!")
                
                st.subheader("Stock Data")
                st.write(analyzed_data)
                
                st.subheader("Visualizations")
                visualize_stock_data(analyzed_data, ticker)
            else:
                st.error("Failed to fetch data. Please check the ticker symbol and date range.")

if __name__ == "__main__":
    main()