#  Book Information Web Scraper & ETL Pipeline

## 1. Project Description

This project is developed using Python to extract book information from a website, transform the collected data and store it in CSV files.

It demonstrates basic Web Scraping and ETL (Extract, Transform, Load) concepts used in Data Engineering.

## 2. Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV
- Visual Studio Code
- GitHub

## 3. Project Features

- Extract book titles.
- Extract book prices.
- Extract book ratings.
- Extract book availability.
- Clean and transform extracted data.
- Convert book prices into numerical values.
- Convert ratings into numerical values.
- Store processed data in CSV files.

## 4. ETL Pipeline

### Extract
Collect book information from the Books to Scrape website using Python and BeautifulSoup.

### Transform
Clean the extracted information, remove unwanted characters and convert prices and ratings into numerical formats.

### Load
Save the transformed data into `books_etl.csv`.

## 5. Project Files

| File | Description |
|---|---|
| scraper.py | Basic web scraping program |
| etl_scraper.py | ETL pipeline implementation |
| books.csv | Original scraped data |
| books_etl.csv | Cleaned and transformed data |
| requirements.txt | Required Python libraries |
| README.md | Project documentation |
| .gitignore | Ignored files configuration |

## 6. Website Used

https://books.toscrape.com/

## 7. Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 8. How to Run

Run the basic scraper:

```bash
python scraper.py
```

Run the ETL pipeline:

```bash
python etl_scraper.py
```

## 9. Output

The project generates two CSV files:

- `books.csv` – Original scraped book information.
- `books_etl.csv` – Cleaned and transformed book information.

## 10. Conclusion

This project helped me understand Python programming, web scraping, data cleaning, CSV handling and the fundamentals of ETL pipelines in Data Engineering.

**Note:** The current implementation extracts books from the first page of the website.
