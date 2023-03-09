import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
import csv


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



def get_yahoo_data(start_date, end_date, tickers):
    from yahoofinancials import YahooFinancials
    import pandas as pd
    
    
    finaldf = pd.DataFrame()
    
    for ticker in tickers:
        

        data = YahooFinancials(ticker).get_historical_price_data(start_date, end_date, 'daily')
        df = data[ticker]['prices']
        df = pd.DataFrame(df)
        df = df[['formatted_date', 'high', 'low', 'volume', 'adjclose']]
        df['formatted_date'] = pd.to_datetime(df['formatted_date'], format='%Y-%m-%d')

        last_row_index = df.index[-1]
        #df['1daily_return'] = df.apply(lambda row: (df.loc[row.name + 1, 'adjclose']- row['adjclose']) /row['adjclose']  if row.name < len(df) else 0, axis=1)
        #df['2daily_return'] = df.apply(lambda row: (df.loc[row.name + 2, 'adjclose']- row['adjclose']) /row['adjclose']  if row.name < len(df) else 0, axis=1)

        df['1dailyreturn'] = (df['adjclose'].shift(-1) - df['adjclose'])/df['adjclose']
        df['2dailyreturn'] = (df['adjclose'].shift(-2) - df['adjclose'])/df['adjclose']
        df['5dailyreturn'] = (df['adjclose'].shift(-3) - df['adjclose'])/df['adjclose']
        df['5dailyreturn'] = (df['adjclose'].shift(-5) - df['adjclose'])/df['adjclose']
        df['10dailyreturn'] = (df['adjclose'].shift(-10) - df['adjclose'])/df['adjclose']
        df['Symbol'] = ticker
        df.rename(columns = {'adjclose':'price'}, inplace = True)
        df.rename(columns = {'formatted_date':'date'}, inplace = True)
        finaldf = pd.concat([df, finaldf], axis =0)
    
    return finaldf




def get_sentiment_word_dict():

    r = requests.get('https://drive.google.com/file/d/17CmUZM9hGUdGYjCXcjQLyybjTrcjrhik')
    text = r.iter_lines()
    reader = csv.reader(text, delimiter = ',')
    print(reader)
    print(text)
    df = pd.DataFrame()
    
    negative_list =[]    
    positive_list = []
    uncertainty_list = []
    for i in range(len(df)):
        if df['Negative'][i] != 0:
            negative_list.append(df['Word'][i])
        elif df['Positive'][i] != 0:
            positive_list.append(df['Word'][i])
        elif df['Uncertainty'][i] != 0:
            uncertainty_list.append(df['Word'][i])



    my_dict = {'Negative': negative_list, 'Positive': positive_list, 'Uncertainty': uncertainty_list}

    return my_dict

