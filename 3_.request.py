import requests
from bs4 import BeautifulSoup

url = "https://weather.com/en-PK/weather/hourbyhour/l/7aea6b4a0aa6a8dfd4a7f4da0b5bc92742638f3f065b16c48c7d629ad0656359"
webContent = requests.get(url).content
soup = BeautifulSoup(webContent,'html.parser')
# print(soup.prettify()) #to see the html code in an organized way

#Printing the weather of islamabad
headings = soup.find_all('h1')
for h in headings:
    print(h.text)        #displaying heading txt
# weather = soup.find_all('h2')
# print(weather[4].text)     #displaying weather for tomoorow
print("Weather for tommorow at 12:00 pm ", end="")
temp = soup.find_all('span',class_="DetailsSummary--tempValue--XM5sZ")
# for i in temp:
   # print(i.text)       #displaying temperature of all hours
#accessing 14th value of temp

print(temp[12].text)       #displaying temperature of 12:00 pm 