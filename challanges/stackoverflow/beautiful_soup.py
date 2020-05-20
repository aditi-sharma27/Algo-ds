import requests
from bs4 import BeautifulSoup

URL = 'https://stopgame.ru//topgames'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://stopgame.ru'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="lent-block game-block")
    print(items)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        items = get_content(html.text)

    else:
        print('Error')


parse()
