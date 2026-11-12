import requests
import csv
from bs4 import BeautifulSoup
import re
def extract_data():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all("article", class_="product_pod")
    extracted_data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")['class'][1]
        availability = book.select_one(".availability").get_text(strip=True)
        extracted_data.append({"title": title, "price": price, "rating": rating, "availability": availability})
    return extracted_data
def transform_data(data):
    transformed_data = []
    rating_values={"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for book in data:
        title = book["title"].strip()
        price = float(re.sub(r"[^0-9.]", "", book["price"]))
        rating = rating_values.get(book["rating"])
        availability = "In stock" if "In stock" in book["availability"] else "Out of stock"
        transformed_data.append({"Book Title": title, "Price(£)": price, "Rating": rating, "Availability": availability})
    return transformed_data
def load_data(data):
    with open("books_etl.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Book Title", "Price(£)", "Rating", "Availability"])
        writer.writeheader()
        writer.writerows(data)
if __name__ == "__main__":
    extracted = extract_data()
    transformed = transform_data(extracted)
    load_data(transformed)
    print("ETL Process Completed Successfully!")
    print("Total books processed:", len(transformed))
    print("Data saved to books_etl.csv")