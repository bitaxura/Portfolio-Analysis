from stock_data import get_stock_price, get_historical_data, plot_stock_price


current_price = get_stock_price('AAPL')
print("Current Price Data:", current_price)

historical_data = get_historical_data('AAPL', '2024-01-01', '2024-12-31')
print("Historical Data Sample:")
print(historical_data.head())

plot_stock_price('AAPL', '2024-01-01', '2024-12-31')
