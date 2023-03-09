import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

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

def get_sentiment_word_dict():

    df = pd.read_csv('https://drive.google.com/file/d/17CmUZM9hGUdGYjCXcjQLyybjTrcjrhik')
    df1 = df.drop(columns = ['Seq_num', 'Word Count', 'Word Proportion', 'Average Proportion', 'Std Dev', 'Doc Count', 'Syllables', 'Source'], axis=1)
    
    
    negative_list =[]    
    positive_list = []
    uncertainty_list = []
    for i in range(len(df1)):
        if df1['Negative'][i] != 0:
            negative_list.append(df1['Word'][i])
        elif df1['Positive'][i] != 0:
            positive_list.append(df1['Word'][i])
        elif df1['Uncertainty'][i] != 0:
            uncertainty_list.append(df1['Word'][i])



    my_dict = {'Negative': negative_list, 'Positive': positive_list, 'Uncertainty': uncertainty_list}

    return my_dict

