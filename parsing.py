
import requests
from bs4 import BeautifulSoup
import json
import os

def get_html(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    return response.text

def get_films(html_):
    soup = BeautifulSoup(html_, 'html.parser')



    pass






URL='https://en.wikipedia.org/wiki/Lists_of_films'
html = get_html(URL)