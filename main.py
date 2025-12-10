import requests
from bs4 import BeautifulSoup
import pandas as pd

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


#RAM
aurl = "https://www.amazon.com/s?k=ddr5+ram+32gb"
burl = "https://www.bestbuy.com/site/searchpage.jsp?st=ddr5%20ram%2032gb"

#GPu
a2url = "https://www.amazon.com/s?k=nvidia+rtx+5090"
b2url = "https://www.bestbuy.com/site/searchpage.jsp?st=nvidia%20rtx%205090"

if __name__ == '__main__':
    amazon_scrape (aurl)
    bestbuy_scrape(burl)

# =============================================
# ZAIN'S PART — Excel Export + Visualization
# =============================================

import pandas as pd
import matplotlib.pyplot as plt

def clean_price_column(df):
    # Remove commas, $, and convert to float
    df["Price"] = df["Price"].replace('[\$,]', '', regex=True)
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    return df

def load_and_clean_data():
    # load CSVs created by the scrapers
    amazon_df = pd.read_csv("amazon_products.csv")
    bestbuy_df = pd.read_csv("bestbuy_products.csv")

    # Add source labels
    amazon_df["Source"] = "Amazon"
    bestbuy_df["Source"] = "BestBuy"

    # price columns
    amazon_df = clean_price_column(amazon_df)
    bestbuy_df = clean_price_column(bestbuy_df)

    # combines datasets for visualization
    combined_df = pd.concat([amazon_df, bestbuy_df], ignore_index=True)
    return amazon_df, bestbuy_df, combined_df

def export_to_excel(amazon_df, bestbuy_df, combined_df):
    # this exports all data to one Excel workbook
    with pd.ExcelWriter("prices_output.xlsx") as writer:
        amazon_df.to_excel(writer, sheet_name="Amazon", index=False)
        bestbuy_df.to_excel(writer, sheet_name="BestBuy", index=False)
        combined_df.to_excel(writer, sheet_name="Combined", index=False)

def plot_bar_chart(combined_df):
    # Average price comparison bar chart
    plt.figure(figsize=(12,6))
    combined_df.groupby("Source")["Price"].mean().plot(kind="bar")
    plt.title("Average Price Comparison: Amazon vs BestBuy")
    plt.ylabel("Average Price ($)")
    plt.savefig("avg_price_comparison.png")
    plt.close()

def plot_product_comparison(combined_df):
    # Product by product line plot
    plt.figure(figsize=(12,6))
    for source in combined_df["Source"].unique():
        df = combined_df[combined_df["Source"] == source]
        plt.plot(df["Product Name"], df["Price"], marker="o", label=source)

    plt.title("Price Comparison for Scraped Products")
    plt.xticks(rotation=90)
    plt.ylabel("Price ($)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("product_price_comparison.png")
    plt.close()


if __name__ == "__main__":
    # Run scrapers
    amazon_scrape(aurl)
    bestbuy_scrape(burl)

    # Run Zain's data processing + charts
    amazon_df, bestbuy_df, combined_df = load_and_clean_data()
    export_to_excel(amazon_df, bestbuy_df, combined_df)

    plot_bar_chart(combined_df)
    plot_product_comparison(combined_df)

    print("Excel file and visualizations generated successfully!")
