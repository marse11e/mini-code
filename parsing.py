from bs4 import BeautifulSoup
import requests


URL = 'https://www.sulpak.kg/f/smartfoniy'
HOST = 'https://www.sulpak.kg/'

HEADERS = {
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }

def get_html(URL, HEADERS, params = ''):
    r = requests.get(URL, headers=HEADERS, verify=False, params=params)
    return r

html = get_html(URL, HEADERS)
def get_content(html):

    soup = BeautifulSoup(html.text, 'html.parser')

    items = soup.find_all('li', class_='tile-container')

    new_list = []

    for item in items:
        title = item.find('h3', class_='title').get_text(strip=True)
        new_list.append({
            'title': title
        })
    return new_list

def save(content, path):
    with open(path, 'w') as file:
        for num, item in enumerate(content,1):
            file.write(f"#{num} - {item['title']}\n")

def parser(URL, HEADERS):
    page = int(input('Введите количество страниц: '))
    html = get_html(URL, HEADERS)

    if html.status_code == 200:
        new_list = []
        for i in range(1,page+1):
            html = get_html(URL, HEADERS, params={'page':i})
            new_list.extend(get_content(html))
            print(f'Страница {i} готова')
        save(new_list, 'sulpak.txt')
        print('парсинг успешно завершен')
    else:
        print('Не удалось спарсить')
parser(URL,HEADERS)