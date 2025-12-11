# CSI3680-Final
## Web scraper and price visualization tool for popular tech websites
As DRAM prices are rapidly increasing, people are looking for the best deals. This tool scrapes Amazon and Bestbuy and visualizes the results so you can get the best price.

To run, install the dependencies with `pip install -r requirements.txt`, then run `python3 main.py`

### Key Classes and Functions:
- The `Search` class represents a web search, containing the urls and a method using the functions describe below to scrape the web for prices.
- `amazon_scrape(url)` and `bestbuy_scrape(url)`
    - both of these scrape the search results for their respective websites. They contain request headers taken from firefox so the web requests sent via the `requests` module are allowed, and uses `beautifulsoup` to parse the web pages and get the product names and prices
- clean_price_column(df)
    - Removes symbols like commas and dollar signs from the Price column.
    - Converts the cleaned price values into numeric format so calculations and graphs work correctly.
    - Ensures that invalid or missing prices do not break your program.
- export_to_excel(amazon_df, bestbuy_df, combined_df)
    - Creates a single Excel workbook named prices_output.xlsx.
    - Saves each dataset (Amazon, BestBuy, Combined) into a separate sheet.
    - Makes the data organized and easy to review for the final project.
-  main execution block
    - Instantiates a Search object with the chosen Amazon and BestBuy URLs and triggers the full scraping process
    - Passes the scraped CSV data into your visualization functions (load, clean, export to Excel, and generate charts), completing the pipeline from raw data to processed data to visual output

### Team Members and Contributions
- River - Web Scraping, CSV export
- Zain - Excel, Visualizations
- Jeffrey - Presentation


