# content_scraper.py

import json
import requests
from bs4 import BeautifulSoup

def preprocess_text(html_content):
    # Use BeautifulSoup to remove HTML tags and get clean text
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

def scrape_content_from_links(links, json_output_file):
    urls = json.loads(links)
        
    url_content = {}

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract content inside the <body> tag
            body_content = soup.body.get_text(separator=' ', strip=True) if soup.body else "No body content"
            print(f"Content scraped in progress...")
            clean_content = preprocess_text(body_content)
            url_content[url] = clean_content
            
            

        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {str(e)}")

    # Save the scraped contents to another JSON file
    with open(json_output_file, 'w') as file:
        json.dump(url_content, file, indent=4)
    print(f"Scraped data saved to {json_output_file}")