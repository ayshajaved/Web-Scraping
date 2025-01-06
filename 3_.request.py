import requests
from bs4 import BeautifulSoup

url = "https://www.rekhta.org/?lang=ur"
content = requests.get(url).content
soup = BeautifulSoup(content,'html.parser')
print(soup.prettify())