import sqlite3

def get_portfolio_data():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM portfolio')
    data = cursor.fetchall()

    conn.close()
    return data

def insert_portfolio_data(data):
    while True:
        choice = input('Do you want to insert this data into the database? (y/n): ')

        if choice.lower() == 'n':
            break
        elif choice.lower() == 'y':
            symbol = input('Enter the symbol: ').upper()
            quantity = int(input('Enter the quantity: '))
            purchase_price = float(input('Enter the purchase price: '))

            conn = sqlite3.connect('portfolio.db')
            cursor = conn.cursor()
            
            cursor.execute("INSERT INTO portfolio (symbol, quantity, purchase_price) VALUES (?, ?, ?)", (symbol, quantity, purchase_price))