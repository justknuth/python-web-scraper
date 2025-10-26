# Simple Python Web Scraper

This is a simple command-line web scraper built with Python, `requests`, and `BeautifulSoup`.

It's designed to demonstrate the basic workflow of:
1.  Fetching a web page's HTML.
2.  Parsing the HTML to find specific data.
3.  Saving that data to a structured `JSON` file.

This script scrapes all quotes and authors from `http://quotes.toscrape.com/`.

## Tech Stack
* **Python 3**
* **requests** (for making HTTP requests)
* **beautifulsoup4** (for parsing HTML)

## How to Run It

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/justknuth/python-web-scraper.git](https://github.com/justknuth/python-web-scraper.git)
    cd python-web-scraper
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On macOS/Linux (Bash):**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows (Command Prompt or PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the scraper:**
    ```bash
    python scraper.py
    ```

## Output
This script will print the authors it finds to the console and create a **`quotes.json`** file in the root of the project containing the full text and author for all scraped quotes.