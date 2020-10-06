import requests
from bs4 import BeautifulSoup
 

URL = 'https://auto.ru/dolgoprudnyy/cars/mercedes/all/'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; CrOS x86_64 13310.93.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.133 Safari/537.36','accept':'*/*'}
HOST = 'https://auto.ru'

def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_content(html):
    
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'ListingItem-module__container')
    cars = []
    for item in items:
        cars.append({
            'title':item.find('a', class_ = 'ListingItemTitle-module__link').get_text()
            #'link':HOST + item.find('a').get('href'), 
            #'cost':item.find('span', class_ = 'size18').get_text(strip = True),
            #'fuel':item.find('span', class_ = 'i-block').get_text(strip = True),'volume':[i for i in item.find('span', class_ = 'size13').get_text().split()][1],
            #'transmission':item.find()
        })
    print(cars)
    print(len(cars))

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print('Error')
parse() 
