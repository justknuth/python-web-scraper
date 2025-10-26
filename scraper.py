import requests
from bs4 import BeautifulSoup
import json


URL = 'http://quotes.toscrape.com/'
print(f"Scraping {URL}...")


try:
    page = requests.get(URL, timeout=10)
    page.raise_for_status()
except requests.RequestException as e:
    print(f"Error making request: {e}")
    exit()
    
    
soup = BeautifulSoup(page.content, 'html.parser')
quote_elements = soup.find_all('div', class_='quote')
scraped_quotes = []


for quote_element in quote_elements:
    text = quote_element.find('span', class_='text').text.strip()
    author = quote_element.find('small', class_='author').text.strip()
    
    scraped_quotes.append({
        "text": text,
        "author": author
    })
    
    print(f"Found quote by: {author}")
    
    
output_file = 'quotes.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(scraped_quotes, f, indent=4, ensure_ascii=False)
    
    
print(f"\nSuccessfully scraped {len(scraped_quotes)} quotes.")
print(f"Data saved to {output_file}")




    
