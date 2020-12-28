import requests
from bs4 import BeautifulSoup
 

URL = 'https://www.e-katalog.ru/list/30/'
HEADERS = {'user-agent':'Mozilla/5.0 (X11; CrOS x86_64 13310.93.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.133 Safari/537.36','accept':'*/*'}
HOST = 'https://www.e-katalog.ru/'

def make_inform(st):    
    st = 'Экран:8\xa0″, 1280x800\xa0пикс, 189\xa0ppiПамять:16\xa0ГБ, слот microSDКамера:5\xa0МП, камера для видеозвонковHardware:4\xa0ядер(а), 1.4\xa0ГГц, оперативка 2\xa0ГБАккумулятор:4800\xa0мАчКорпус:металл, 350\xa0г, толщина 8\xa0мм'
    st = st.replace(u'\xa0', ' ')
    st = st.replace('SDК', 'SD, К')
    st = st.replace('ppiП', 'ppi, П')
    st = st.replace('Hardware', ' встроенная')
    st = st.replace('я:4', 'я, 4')
    st = st.replace('ГБАк', 'ГБ, Ак')
    st = st.replace('АчК', 'Ач, К')
    st = st.replace('″, ', '″; ')
    inform = [i for i in st.split(',')]

    return(inform)

def make_price(st):
    st = st.replace(u'\xa0', ' ')
    st = st.replace('до', ' до ')
    st = st.replace('от', 'от ')
   
    price = [i for i in st.split('.')]
    del price[-1]
    
    return price[0]

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        pagination = [int(i) for i in soup.find('div', class_ = 'page-num').get_text(strip = True).split('...')]
        return(pagination[-1])  
    except:
        return 1
   
def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_content(html):
    
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'model-short-div list-item--goods')
    cars = []
    for item in items:
        cars.append({
            'title':item.find('span', class_ = 'u').get_text(strip = True),
            'price':make_price(item.find('div', class_ = 'model-price-range').get_text(strip = True)),
            'link':HOST + item.find('a').get('href'), 
            'additional information':make_inform(item.find('div', class_ = 'm-s-f2 no-mobile').get_text())
        })
    return(cars)    

def parse(URL):
    html = get_html(URL)
    device = []
    if html.status_code == 200:
        pages_count = int(get_pages_count(html.text))
        for page in range(1, pages_count +1):
            print(f'Идет парсинг страницы {page}')
            html = get_html(URL)
            device.append(get_content(html.text))
        return device
    else:
        print('Error')

if __name__ == "__main__":
    print(parse(URL))
    
