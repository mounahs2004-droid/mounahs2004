import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Failed to retrieve the webpage:", e)
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    book_data.append([title, price, availability])

filename = "books_scraped.csv"
try:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability'])
        writer.writerows(book_data)
    print(f"Data successfully saved to {filename}")
except IOError as e:
    print("Error writing to CSV:", e)
