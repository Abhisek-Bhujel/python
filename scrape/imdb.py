import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

# Add headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Find movie rows
movies = soup.select("td.titleColumn")

for movie in movies[:10]:  # first 10 movies for demo
    title = movie.find("a").text
    year = movie.find("span", class_="secondaryInfo").text.strip("()")
    rating = movie.find_next_sibling("td").strong.text
    print(f"Title: {title}, Year: {year}, Rating: {rating}")
