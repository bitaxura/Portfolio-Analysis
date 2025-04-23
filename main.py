import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def analyze_portfolio(price_data, weights):
    """Computes returns, portfolio performance, and plots."""

    daily_returns = price_data.pct_change().dropna()

    weights = np.array(weights)

    portfolio_returns = daily_returns.dot(weights)

    avg_return = np.mean(portfolio_returns)
    std_dev = np.std(portfolio_returns)
    cumulative_return = (1 + portfolio_returns).prod() - 1

    portfolio_value = (1 + portfolio_returns).cumprod()
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_value, label="Portfolio Value")
    plt.title("Portfolio Performance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value (normalized)")
    plt.legend()
    plt.grid(True)
    plt.show()

    return {
        'Average Daily Return': avg_return,
        'Standard Deviation': std_dev,
        'Cumulative Return': cumulative_return
    }
