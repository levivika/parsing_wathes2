
import requests
from bs4 import BeautifulSoup
import json
import os





def get_html(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    return response.text



def take_url(html_):
    soup = BeautifulSoup(html_, 'html.parser')
    all_a = soup.find(class_='pagen').find_all('a')
    urls =[]
    for i in range(len(all_a)):
        part_of_url = soup.find(class_='pagen').find_all('a')[i].get('href')
        url = 'https://parsinger.ru/html/' + part_of_url
        urls.append(url)
    return urls

def get_films(html_):
    soup = BeautifulSoup(html_, 'html.parser')
    watches_div = soup.find('div', class_='item_card')
    watches = watches_div.find_all('div', class_='item')
    info={}
    for i in range(len(watches)):
        name = watches[i].find(class_='name_item').text.encode('latin1').decode('utf-8')
        brand = \
        watches[i].find(class_='description').find_all('li')[0].text.encode('latin1').decode('utf-8').split(':')[
            -1].strip()
        type_watch = \
        watches[i].find(class_='description').find_all('li')[1].text.encode('latin1').decode('utf-8').split(':')[
            -1].strip()
        material = \
        watches[i].find(class_='description').find_all('li')[2].text.encode('latin1').decode('utf-8').split(':')[
            -1].strip()
        technology = \
        watches[i].find(class_='description').find_all('li')[3].text.encode('latin1').decode('utf-8').split(':')[
            -1].strip()
        price = watches[i].find(class_='price').text.encode('latin1').decode('utf-8')
        part_of_link = watches[i].find(class_='sale_button').find('a').get('href')
        link = 'https://parsinger.ru/html/' + part_of_link
        info[name]={
            'brand': brand,
            'type': type_watch,
            'material': material,
            'technology': technology,
            'link': link,
            'price': price

        }
    return info

'''
def write_info_json(info: dict):
    with open('file.json', 'w', encoding = 'utf-8') as file:
        json.dump(info, file, indent=2, ensure_ascii=False)







URL = 'https://parsinger.ru/html/index1_page_2.html'

html = get_html(URL)
take_url(html)
info = get_films(html)
write_info_json(info)
'''
def write_info_json(info: dict, filename: str):  # Add filename as argument
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(info, file, indent=2, ensure_ascii=False)
    print(f"Данные успешно записаны в {filename}")


URL = 'https://parsinger.ru/html/index1_page_1.html'
html = get_html(URL)

all_urls = take_url(html)
# all_data = {}  # No longer needed

for i, url in enumerate(all_urls):  # Use enumerate to get index
    html = get_html(url)
    page_data = get_films(html)
    filename = f'file_{i+1}.json'  # Create filename based on index
    write_info_json(page_data, filename)
