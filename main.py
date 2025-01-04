#Web Scraping by Beautiful soup
from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the first paragraph of wikipedia
first_paragraph = soup.find('p').text
print(first_paragraph)



