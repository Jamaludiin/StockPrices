# done  https://learnpythoneasily.com/company-info-with-llm/

import yfinance as yf
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

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
        "Headquarters": info.get('city', 'N/A') + ", " + info.get('state', 'N/A')
    }

    return company_info

def main():
    tickers = ['AAPL']  # Test with two tickers

    all_company_info = []

    for ticker in tickers:
        info = get_company_info(ticker)
        all_company_info.append(info)
        """print(f"Information for {ticker}:")
        for key, value in info.items():
            print(f"{key}: {value}")
        print("\n" + "-"*50 + "\n")"""

    return all_company_info

if __name__ == "__main__":
    all_info = main()

    # Convert the list of company information to a single string for LLM input
    info_str = "\n".join([str(info) for info in all_info])

    # Set up the Ollama model
    ollama_llm = Ollama(
        model="llama3",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    )

    # Make the request to the LLM with the gathered information
    response = ollama_llm(f""" Present the provided information in a meaninfull way and gues and fill the missing data{info_str}""")
    # Understand and explain the generated stock information, and provide more information about the comapny and try to provide N/A or unavailable information:

    print("###########")
    print(response)
