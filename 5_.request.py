#Scraping all the images from a website

import requests
from bs4 import BeautifulSoup

url = "https://www.tutorialspoint.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')

for image in images:
    print(image['src'])   #getting all the images links