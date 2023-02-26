import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://kups.club'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}

response = requests.get(url, headers=header)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    all_product = soup.find('div', class_='row mt-4')
    products = all_product.find_all('div', class_='card-body')
    for product in products:
        try:
            price = product.find('p', class_='card-text')
            print(price.text)
        except Exception:
            price = None
        if price != None:
            title = product.find('h3', class_='card-title')
            with open('catalog.txt', 'w', encoding='utf-8') as file:
                file.write(f"{title.text} {price.text.replace('NBSP','')}" '\n')
