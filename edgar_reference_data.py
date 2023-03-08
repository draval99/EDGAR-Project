import requests
from bs4 import BeautifulSoup

def get_sp100():
    url = 'https://en.wikipedia.org/wiki/S%26P_100' # URL to scrape

    response = requests.get(url) # Sends a GET request to URL to get HTML content
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'class': 'wikitable sortable'}) # Find  table of S&P100 tickers

    # Extracts tickers from table
    tickers = []
    for row in table.find_all('tr')[1:]:
        ticker = row.find_all('td')[0].text.strip()
        tickers.append(ticker)

    return tickers