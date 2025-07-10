import requests
from bs4 import BeautifulSoup
import csv

# Target website (legal demo site)
URL = "https://books.toscrape.com/catalogue/page-1.html"
base_url = "https://books.toscrape.com/catalogue/"
book_data = []

# Loop through multiple pages
for page in range(1, 3):  # Change to scrape more pages
    print(f"Scraping page {page}...")
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html")
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.p["class"][1]  # Example: "Three"
        book_data.append([name, price, rating])

# Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Rating"])
    writer.writerows(book_data)

print("Scraping complete! Data saved to books.csv ✅")