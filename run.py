from stock_data import load_data
from main import analyze_portfolio

def get_user_inputs():
    tickers = input("Enter comma-separated stock tickers (e.g., AAPL,MSFT,GOOG): ").split(",")
    weights_input = input(f"Enter weights for {len(tickers)} stocks (comma-separated, must sum to 1): ")
    weights = [float(w) for w in weights_input.split(",")]

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    return tickers, weights, start_date, end_date

def main():
    tickers, weights, start_date, end_date = get_user_inputs()

    print("\nFetching data...")
    df = load_data(tickers, start_date, end_date)
    
    print("\nAnalyzing portfolio...")
    results = analyze_portfolio(df, weights)
    
    print("\nResults:")
    print(results)

main()