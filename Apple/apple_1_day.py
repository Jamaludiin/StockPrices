import requests
import pandas as pd
from datetime import datetime, timedelta

# Function to fetch minute-by-minute data from Alpha Vantage
def fetch_minute_data(symbol, api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_INTRADAY"
    interval = "1min"

    # Current date and time
    current_datetime = datetime.now()

    # Calculate the start and end date for fetching data (last trading day)
    if current_datetime.weekday() == 0:
        # If today is Monday, fetch data for Friday
        start_date = current_datetime - timedelta(days=3)
    else:
        start_date = current_datetime - timedelta(days=1)

    # Format dates for Alpha Vantage API
    start_date_str = start_date.strftime('%Y-%m-%d') + " 09:30:00"
    end_date_str = start_date.strftime('%Y-%m-%d') + " 16:00:00"

    # Construct the API request
    params = {
        "function": function,
        "symbol": symbol,
        "interval": interval,
        "apikey": api_key
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract and process data if successful
    if 'Time Series (1min)' in data:
        # Convert to DataFrame
        df = pd.DataFrame(data['Time Series (1min)']).T
        df.index = pd.to_datetime(df.index)
        df['close'] = pd.to_numeric(df['4. close'])
        df['change'] = df['close'].diff()

        return df[['close', 'change']].dropna()
    else:
        print("Error fetching data:", data)
        return None

# Replace with your Alpha Vantage API key
api_key = 'your_alpha_vantage_api_key'

# Example usage
ticker = "AAPL"
data = fetch_minute_data(ticker, api_key)

if data is not None:
    print("Minute-by-minute changes for", ticker)
    print(data)
else:
    print("Failed to fetch data from Alpha Vantage.")
