import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/"  # a practice website for scraping

# Step 1: Fetch the page
response = requests.get(url)
html = response.text

# Step 2: Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract all quotes
quotes = soup.find_all("span", class_="text")

# Step 4: Print quotes
for i, quote in enumerate(quotes, 1):
    print(f"{i}. {quote.text}")
