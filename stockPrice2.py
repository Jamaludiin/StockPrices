import yfinance as yf

def get_company_stock_prices(tickers):
    """
    Fetch the current stock prices for the given list of tickers.

    Args:
    tickers (list): List of stock ticker symbols.

    Returns:
    dict: Dictionary with ticker symbols as keys and their current stock prices as values.
    """
    company_stock_prices = {}

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        # Get the current stock price
        stock_price = stock.history(period='1d')['Close'].iloc[-1]
        company_stock_prices[ticker] = stock_price

    return company_stock_prices

def main():
    # List of ticker symbols for the top 10 companies by market capitalization
    top_10_companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'ADBE', 'CRM', 'INTU', 'ORCL', 'SAP',
        'NOW', 'TEAM', 'SNOW', 'WDAY', 'DOCU', 'ZM', 'CRWD', 'OKTA', 'PANW'
    ]
    
    # List of ticker symbols for major chip makers
    chip_makers = ['INTC', 'AMD', 'QCOM', 'TXN', 'AVGO']

    # Combine both lists
    all_tickers = top_10_companies + chip_makers

    # Get stock prices
    stock_prices = get_company_stock_prices(all_tickers)

    # Print the stock prices
    for company, price in stock_prices.items():
        print(f"{company}: ${price:.2f}")

if __name__ == "__main__":
    main()
