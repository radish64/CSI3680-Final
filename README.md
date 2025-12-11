# CSI3680-Final
## Web scraper and price visualization tool for popular tech websites
As DRAM prices are rapidly increasing, people are looking for the best deals. This tool scrapes Amazon and Bestbuy and visualizes the results so you can get the best price.

To run, install the dependencies with `pip install -r requirements.txt`, then run `python3 main.py`

### Key Classes and Functions:
- The `Search` class represents a web search, containing the urls and a method using the functions describe below to scrape the web for prices.
-`amazon_scrape(url)` and `bestbuy_scrape(url)`
    - both of these scrape the search results for their respective websites. They contain request headers taken from firefox so the web requests sent via the `requests` module are allowed, and uses `beautifulsoup` to parse the web pages and get the product names and prices
- 

### Team Members and Contributions
- River - Web Scraping, CSV export
- Zain - Excel, Visualizations
- Heffrey - Presentation


