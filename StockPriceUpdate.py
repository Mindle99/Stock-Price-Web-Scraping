import bs4
import requests
from bs4 import BeautifulSoup


def priceTracker():
    url = 'https://ca.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price



while True:
    print('Current Price of Apple: ' + priceTracker())
