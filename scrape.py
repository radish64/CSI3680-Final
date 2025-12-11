import requests
from bs4 import BeautifulSoup
import pandas as pd

# River's part - web scraping

def amazon_scrape(url):
    headers = {
    "Host": "www.amazon.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "DNT": "1",
    "Sec-GPC": "1",
    "Alt-Used": "www.amazon.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    products = soup.find_all('div', {'role': 'listitem'})
    product_names = []
    prices = []
    for product in products:
        name = product.find('a', {'class': 'a-text-normal'})
        price = product.find('span', {'class': 'a-price-whole'})
        if name and price:
            product_names.append(name.text)
            prices.append(price.text)
            # Save to CSV
            data = {'Product Name': product_names, 'Price': prices}
            df = pd.DataFrame(data)
            df.to_csv('amazon_products.csv', index=False)

def bestbuy_scrape(url):
    headers = {
    "Host": "www.bestbuy.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    #"Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.bestbuy.com/home",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "TE": "trailers"
    }
    res = requests.get(url, headers=headers)
    print(res)
    soup = BeautifulSoup(res.content, 'html.parser')
    #print(soup)
    #print(soup)
    productscontainer = soup.find_all('div', {'id': 'main-results'})
    #print(productscontainer)
    products = soup.find_all('li', {'class': 'product-list-item product-list-item-gridView'})
    product_names = []
    prices = []
    for product in products:
        name = product.find('h2', {'class': 'product-title'})
        #print(name)
        price = product.find('span', {'class': 'font-sans text-default text-style-body-md-400 font-500 text-6 leading-6'})
        #priced = product.find('div', {'data-testid': 'price-block-customer-price'})
        #print(price)
        if name and price:
            product_names.append(name.text)
            prices.append(price.text)
            # Save to CSV
            data = {'Product Name': product_names, 'Price': prices}
            df = pd.DataFrame(data)
            df.to_csv('bestbuy_products.csv', index=False)

