import requests
from bs4 import BeautifulSoup
import pandas as pd

aurl = "https://www.amazon.com/s?k=ddr5+ram+32gb"
burl = "https://www.bestbuy.com/site/searchpage.jsp?st=ddr5%20ram%2032gb"

a2url = "https://www.amazon.com/s?k=nvidia+rtx+5090"
b2url = "https://www.bestbuy.com/site/searchpage.jsp?st=nvidia%20rtx%205090"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
aheaders = {
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

bheaders = {
"Host": "www.bestbuy.com",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br, zstd",
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

ares = requests.get(a2url, headers=aheaders)
#bres = requests.get(b2url, headers=bheaders)

print(ares)
#print(bres)

asoup = BeautifulSoup(ares.content, 'html.parser')
#bsoup = BeautifulSoup(bres.content, 'html.parser')

#products = asoup.find_all('div', {'class': 's-main-slot s-result-list s-search-results sg-row'})
products = asoup.find_all('div', {'role': 'listitem'})
product_names = []
prices = []
for product in products:
    name = product.find('a', {'class': 'a-text-normal'})
    price = product.find('span', {'class': 'a-price-whole'})
    #name = product.find('a', {'class': 'a-text-normal'})
    #price = product.find('span', {'class': 'a-offscreen'})
    if name and price:
        product_names.append(name.text)
        prices.append(price.text)
        # Save to CSV
        data = {'Product Name': product_names, 'Price': prices}
        df = pd.DataFrame(data)
        df.to_csv('amazon_products.csv', index=False)

#res.raise_for_status()
