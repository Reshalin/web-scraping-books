# 📚 Book Information Web Scraper Using Python

## 1. Project Description

This is a beginner-friendly web scraping project developed using Python.

It extracts book information from the Books to Scrape website and stores the collected information in a CSV file.

## 2. Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV

## 3. Project Features

- Extract book titles.
- Extract book prices.
- Extract book ratings.
- Extract book availability.
- Store extracted information in a CSV file.

## 4. Website Used

https://books.toscrape.com/

## 5. Project Files

- `scraper.py` – Python web scraping program.
- `books.csv` – Extracted book information.
- `requirements.txt` – Required Python libraries.
- `.gitignore` – Files excluded from Git tracking.

## 6. Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 7. How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python scraper.py
```

5. The extracted information will be saved in `books.csv`.

## 8. Output

The CSV file contains:

- Book Title
- Price
- Rating
- Availability

**Note:** This version extracts books from the website's first page.

## 9. Conclusion

This project demonstrates the basic concepts of web scraping using Python, Requests and BeautifulSoup.
