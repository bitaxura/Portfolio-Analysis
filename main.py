import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from dotenv import load_dotenv
import os
import finnhub
import yfinance as yf

load_dotenv()
api_key = os.getenv('FINNHUB_API_KEY')
finnhub_client = finnhub.Client(api_key=api_key)

def get_stock_price(symbol):
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
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def save_stock_quote_to_db(data, db_path):
    conn = sqlite3.connect(db_path)
    df = pd.DataFrame(data)
    df.to_sql('stock_quote', conn, if_exists='replace', index=False)
    conn.close()

def plot_stock_price(symbol, start_date, end_date):
    historical_data = get_historical_data(symbol, start_date, end_date)
    plt.figure(figsize=(10, 6))
    plt.plot(historical_data['Close'], label=f'{symbol} Stock Price')
    plt.title(f'{symbol} Stock Price from {start_date} to {end_date}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

current_price =  get_stock_price('AAPL')
historical_data = get_historical_data('AAPL', '2024-01-01', '2024-12-31')

plot_stock_price('AAPL', '2024-01-01', '2024-12-31')

portfolio = {
    'AAPL': {'quantity': 10, 'purchase_price': 150},
    'GOOGL': {'quantity': 5, 'purchase_price': 2500},
    'MSFT': {'quantity': 8, 'purchase_price': 200}
}