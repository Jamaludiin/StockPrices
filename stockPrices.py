# pip install yfinance


#

import yfinance as yf

def get_top_10_company_stock_prices():
    # List of ticker symbols for the top 10 companies by market capitalization
    top_10_companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK-B', 'NVDA', 'META', 'JPM', 'V']

    # Dictionary to hold company names and their current stock prices
    company_stock_prices = {}

    for ticker in top_10_companies:
        stock = yf.Ticker(ticker)
        # Get the current stock price
        stock_price = stock.history(period='1d')['Close'].iloc[-1]
        company_stock_prices[ticker] = stock_price

    return company_stock_prices

def main():
    stock_prices = get_top_10_company_stock_prices()
    for company, price in stock_prices.items():
        print(f"{company}: ${price:.2f}")

if __name__ == "__main__":
    main()
