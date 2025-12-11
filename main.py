import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

from scrape import *
from visualize import *

class Search:
    def __init__(self, amazon, bestbuy):
        self.amazon = amazon  
        self.bestbuy = bestbuy  
    
    def scrape(self):
        try:
            amazon_scrape(self.amazon)
        except:
            print("Amazon scrape failed!")
        try:
            bestbuy_scrape(self.bestbuy)
        except:
            print("Bestbuy scrape failed!")

#RAM
aurl = "https://www.amazon.com/s?k=ddr5+ram+32gb"
burl = "https://www.bestbuy.com/site/searchpage.jsp?st=ddr5%20ram%2032gb"

#GPU
a2url = "https://www.amazon.com/s?k=nvidia+rtx+5090"
b2url = "https://www.bestbuy.com/site/searchpage.jsp?st=nvidia%20rtx%205090"

if __name__ == "__main__":
    # Run scrapers
    ram_search = Search(aurl, burl)
    ram_search.scrape()

    # Run Zain's data processing + charts
    amazon_df, bestbuy_df, combined_df = load_and_clean_data()
    export_to_excel(amazon_df, bestbuy_df, combined_df)

    plot_bar_chart(combined_df)
    plot_product_comparison(combined_df)

    print("Excel file and visualizations generated successfully!")
