


import requests
from bs4 import BeautifulSoup

def clean_html_text(html_text):

    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()


    import re
    clean_text = re.sub('[^A-Za-z0-9]+', ' ', text)
    print(clean_text)




