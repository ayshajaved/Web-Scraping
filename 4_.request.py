#getting the links of the page
import requests
from bs4 import BeautifulSoup

url = "https://www.tutorialsfreak.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')   #getting all the anchor tags

for link in links:
    print(link.get('href'))  #Scraping all the links