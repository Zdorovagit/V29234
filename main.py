import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://rozetka.com.ua/ua/notebooks/c80004/'

header = {
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

response = requests.get(url, headers=header)
print(response.status_code)
print(response.content)
print(response.text)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    all_product = soup.find('ul', class_='catalog-grid ng-star-inserted')
    # print(all_product)
    products = all_product.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
    for product in products:
        # print(product.text)
        # title = product.find('span', class_='goods-tile__title')
        # print(title.text)
        try:
            price = product.find('div', class_='goods-tile__price--old price--gray ng-star-inserted')
            print(price.text)
        except Exception:
            price = None
        if price != None:
            title = product.find('span', class_='goods-tile__title')
            with open('catalog.txt', 'w', encoding='utf-8') as file:
                file.write(f"{title.text} {price.text.replace('NBSP','')}" '\n')
