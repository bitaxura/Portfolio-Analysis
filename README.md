# Portfolio Analysis Tool

This is a Python-based command-line tool for analyzing stock portfolios using real-time and historical financial data. It integrates with Yahoo Finance and Finnhub for data retrieval, and uses a SQLite database to track investment performance.

## Features

- Fetch live and historical stock prices
- Analyze daily returns, volatility, Sharpe ratio, and cumulative performance
- Compare portfolio performance against benchmarks
- Log performance and ROI over time in a SQLite database
- Visualize portfolio value growth with Matplotlib

## Project Structure

- `main.py`: Computes returns and plots portfolio performance
- `analysis.py`: Handles return, risk, and benchmark comparison logic
- `portfolio.py`: CLI for user interaction and data updates
- `database.py`: Database schema and access utilities
- `stock_data.py`: Loads data using Yahoo Finance and Finnhub
- `run.py`: Main application entry point

## License

MIT License.