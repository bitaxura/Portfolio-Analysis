from stock_data import get_stock_price
import numpy as np

class Return:
    @staticmethod
    def calculate_portfolio_value(portfolio) -> float:
        """Calculates the total portfolio value based on current stock prices."""
        total_value = 0
        for symbol, data in portfolio.items():
            current_data = get_stock_price(symbol)
            if current_data and 'Current Price' in current_data:
                total_value += current_data['Current Price'] * data['shares']
        return total_value

    @staticmethod
    def calculate_returns(portfolio) -> dict:
        """Calculates percentage returns for each stock in the portfolio."""
        returns = {}
        for symbol, data in portfolio.items():
            current_data = get_stock_price(symbol)
            if current_data and 'Current Price' in current_data:
                stock_return = (current_data['Current Price'] - data['purchase_price']) / data['purchase_price']
                returns[symbol] = stock_return
        return returns

class Risk:
    @staticmethod
    def volatility(stock_returns: list) -> float:
        """Calculates the standard deviation of stock returns (Volatility)."""
        return np.std(stock_returns)

    @staticmethod
    def sharpe_ratio(stock_returns: list, risk_free_rate: float = 0.02) -> float:
        """Calculates the Sharpe Ratio, which measures risk-adjusted return."""
        avg_return = np.mean(stock_returns)
        std_dev = np.std(stock_returns)

        if std_dev == 0:
            return 0

        return (avg_return - risk_free_rate) / std_dev

class Performance:
    @staticmethod
    def compare(portfolio_returns: dict, benchmark_returns: dict) -> dict:
        """Compares portfolio performance against a benchmark (e.g., S&P 500)."""
        comparison = {}
        for symbol in portfolio_returns:
            if symbol in benchmark_returns:
                comparison[symbol] = portfolio_returns[symbol] - benchmark_returns[symbol]
            else:
                comparison[symbol] = portfolio_returns[symbol]
        return comparison
