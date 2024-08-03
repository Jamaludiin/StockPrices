
import yfinance as yf

def get_company_info(ticker):
    """
    Fetch detailed information for the given stock ticker.

    Args:
    ticker (str): Stock ticker symbol.

    Returns:
    dict: Dictionary with various information about the stock.
    """
    stock = yf.Ticker(ticker)
    info = stock.info

    company_info = {
        "Name": info.get('shortName', 'N/A'),
        "Sector": info.get('sector', 'N/A'),
        "Industry": info.get('industry', 'N/A'),
        "Country": info.get('country', 'N/A'),
        "Market Cap": info.get('marketCap', 'N/A'),
        "Dividend Yield": info.get('dividendYield', 'N/A'),
        "52-Week High": info.get('fiftyTwoWeekHigh', 'N/A'),
        "52-Week Low": info.get('fiftyTwoWeekLow', 'N/A'),
        "P/E Ratio": info.get('trailingPE', 'N/A'),
        "EPS": info.get('trailingEps', 'N/A'),
        "Earnings Date": info.get('earningsDate', 'N/A'),
        "CEO": info.get('ceo', 'N/A'),
        "Website": info.get('website', 'N/A'),
        "Description": info.get('longBusinessSummary', 'N/A'),
        "Employees": info.get('fullTimeEmployees', 'N/A'),
        "Founders": info.get('founders', 'N/A'),  # Custom field, might not be available
        "Headquarters": info.get('city', 'N/A') + ", " + info.get('state', 'N/A')
    }

    return company_info

def main():
    tickers = [
        'AAPL', 'MSFT' , 'GOOGL', 'AMZN', 'TSLA', 'BRK-B', 
        'NVDA', 'META', 'JPM', 'V', 'ADBE', 'CRM', 'INTU', 
        'ORCL', 'SAP', 'NOW', 'TEAM', 'SNOW', 'WDAY', 'DOCU', 
        'ZM', 'CRWD', 'OKTA', 'SPLK', 'PANW', 'INTC', 'AMD', 
        'QCOM', 'TXN', 'AVGO', 'SONY', 'HPQ', 'DELL', 'BBY', 
        'HPE', 'SSNLF', 'LPL', 'CSCO', 'IBM'
    ]

    # let me check only the above two
    """
    
    
    
    """

    for ticker in tickers:
        info = get_company_info(ticker)
        print(f"Information for {ticker}:")
        for key, value in info.items():
            print(f"{key}: {value}")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
