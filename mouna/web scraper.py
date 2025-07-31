import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://books.toscrape.com/"

# Send request
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error if status is not 200
except requests.RequestException as e:
    print("Error fetching the URL:", e)
    exit()

# Parse the HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extract data
books = soup.find_all("article", class_="product_pod")
titles = []
prices = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    titles.append(title)
    prices.append(price)

# Store in DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

# Save to CSV
df.to_csv("books.csv", index=False)
print("Data saved to books.csv")
