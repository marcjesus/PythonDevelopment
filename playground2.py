import yfinance as yf
import json
from datetime import datetime

def fetch_apple_info(start_date, end_date):
    # Ticker symbol for Apple Inc.
    ticker_symbol = 'AAPL'

    # Fetch the company data
    apple = yf.Ticker(ticker_symbol)
    
    # Get all available information
    company_info = apple.info

    # Pretty-print the company information as JSON
    print("Company Information:")
    print(json.dumps(company_info, indent=4))

    # Fetch historical market data
    history = apple.history(start=start_date, end=end_date)
    print(f"\nHistorical Data from {start_date} to {end_date}:")
    print(history)

if __name__ == "__main__":
    # Set the date range for fetching historical data
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    # Validate date format
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
    else:
        fetch_apple_info(start_date, end_date)
 