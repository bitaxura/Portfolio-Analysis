import sqlite3
from database import get_portfolio_performance, log_performance
from analysis import Return
from stock_data import get_stock_price

def get_portfolio_data():
    """Fetches all portfolio data from the database."""
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM portfolio')
    data = cursor.fetchall()

    conn.close()
    return data

def insert_portfolio_data():
    """Allows the user to input a new investment and saves it to the database."""
    while True:
        choice = input('Do you want to insert this data into the database? (y/n): ').strip().lower()

        if choice == 'n':
            break
        elif choice == 'y':
            symbol = input('Enter the stock symbol: ').upper()
            quantity = int(input('Enter the quantity of shares: '))
            purchase_price = float(input('Enter the purchase price per share: '))

            conn = sqlite3.connect('portfolio.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO portfolio (symbol, shares, price_per_share, date_purchased)
                VALUES (?, ?, ?, datetime('now'))
            ''', (symbol, quantity, purchase_price))

            conn.commit()
            conn.close()
            print(f"Added {quantity} shares of {symbol} at ${purchase_price} per share to portfolio.")

def update_portfolio_value():
    """
    Calculates and logs the portfolio value and return on investment (ROI).
    """
    portfolio = get_portfolio_data()
    total_value = 0
    total_invested = 0

    for investment in portfolio:
        symbol, shares, purchase_price, _ = investment[1:]  # Extract relevant fields
        current_price = get_stock_price(symbol)['Current Price']
        total_value += shares * current_price
        total_invested += shares * purchase_price

    roi = (total_value - total_invested) / total_invested if total_invested else 0
    log_performance(total_value, roi)
    print(f"Current Portfolio Value: ${total_value:.2f}")
    print(f"ROI: {roi * 100:.2f}%")
    
def view_portfolio_performance():
    """
    Retrieves and displays past portfolio performance.
    """
    performance_data = get_portfolio_performance()
    print("\nPortfolio Performance History:")
    for entry in performance_data:
        date, value, roi = entry[1:]  # Skip ID
        print(f"Date: {date} | Value: ${value:.2f} | ROI: {roi * 100:.2f}%")


# insert_portfolio_data()
# update_portfolio_value()
# view_portfolio_performance()