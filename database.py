import sqlite3

def initialize_database():
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        shares REAL NOT  NULL,
        price_per_share REAL NOT NULL,
        date_purchased TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS investments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        stock_symbol TEXT NOT NULL
    )'''
    )
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS portfolio_performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        portfolio_value REAL NOT NULL,
        roi REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close() 

def add_investment(amount: int, stock_symbol: str) -> None:
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO investments (date, amount, stock_symbol)
    VALUES (datetime('now'), ?, ?)
    ''', (amount, stock_symbol))

    conn.commit()
    conn.close()

def get_total_investments():
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(amount) FROM investments')
    total_invested = cursor.fetchone()[0] or 0

    conn.close()
    return total_invested

def insert_into_portfolio(symbol: str, shares: int, price_per_share: float) -> None:
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO portfolio (symbol, shares, price_per_share, date_purchased)
    VALUES (?, ?, ?, datetime('now'))
    ''', (symbol, shares, price_per_share))

    conn.commit()
    conn.close()

def get_portfolio_data():
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM portfolio')
    portfolio_data = cursor.fetchall()

    conn.close()
    return portfolio_data

def log_performance(portfolio_value: float, roi: float) -> None:
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO portfolio_performance (date, portfolio_value, roi)
    VALUES (datetime('now'), ?, ?)
    ''', (portfolio_value, roi))

    conn.commit()
    conn.close()

def get_portfolio_performance():
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM portfolio_performance')
    performance_data = cursor.fetchall()

    conn.close()
    return performance_data

def get_investment_history():
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM investments')
    investment_data = cursor.fetchall()

    conn.close()
    return investment_data

def update_investment(investment_id: int, new_amount: float) -> None:
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE investments
    SET amount = ?
    WHERE id = ?
    ''', (new_amount, investment_id))

    conn.commit()
    conn.close()

def delete_investment(investment_id: int) -> None:
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM investments WHERE id = ?', (investment_id,))

    conn.commit()
    conn.close()

def update_portfolio(symbol: str, new_shares: float, new_price_per_share: float) -> None:
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE portfolio
    SET shares = ?, price_per_share = ?
    WHERE symbol = ?
    ''', (new_shares, new_price_per_share, symbol))

    conn.commit()
    conn.close()

def get_portfolio_value_history():
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()

    cursor.execute('SELECT date, portfolio_value FROM portfolio_performance')
    value_history = cursor.fetchall()

    conn.close()
    return value_history

def safe_execute(query, params=()):
    conn = sqlite3.connect(r'Portfolio Analysis\portfolio.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


initialize_database()

print(get_portfolio_data())