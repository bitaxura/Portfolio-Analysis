import os
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import finnhub
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('FINNHUB_API_KEY')
finnhub_client = finnhub.Client(api_key=api_key)

def get_stock_price(symbol):
    """Fetches current price and basic info from Finnhub."""
    quote = finnhub_client.quote(symbol)
    return {
        'Symbol': symbol,
        'Current Price': quote['c'],
        'Open': quote['o'],
        'High': quote['h'],
        'Low': quote['l'],
        'Previous Close': quote['pc']
    }

def get_historical_data(symbol, start_date, end_date):
    """Downloads historical data from Yahoo Finance."""
    return yf.download(symbol, start=start_date, end=end_date)

def plot_stock_price(symbol, start_date, end_date):
    """Plots historical closing prices."""
    historical_data = get_historical_data(symbol, start_date, end_date)
    plt.figure(figsize=(10, 6))
    plt.plot(historical_data['Close'], label=f'{symbol} Stock Price')
    plt.title(f'{symbol} Stock Price from {start_date} to {end_date}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

def save_stock_quote_to_db(data, db_path):
    """Saves stock quote data to database (optional use)."""
    conn = sqlite3.connect(db_path)
    df = pd.DataFrame(data)
    df.to_sql('stock_quote', conn, if_exists='replace', index=False)
    conn.close()
