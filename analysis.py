from portfolio import get_stock_price

def calculate_portfolio_value(portfolio):
    total_value = 0
    for symbol, data in portfolio.items():
        current_data = get_stock_price(symbol)
        total_value += current_data['Current Price'] * data['quantity']
    return total_value

def calculate_returns(portfolio):
    returns = {}
    for symbol, data in portfolio.items():
        current_data = get_stock_price(symbol)
        stock_return = (current_data['Current Price'] - data['purchase_price']) / data['purchase_price']
        returns[symbol] = stock_return
    return returns

