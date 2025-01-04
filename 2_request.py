import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

response = requests.get(url)
if response.status_code == 200:
    print("Success")
    content = response.content
    html = BeautifulSoup(content, 'html.parser')
    print(html)            #gives the incomprehensible html content
    print(html.prettify()) #gives the beautiful and clean html that is readable
    print(html.p)          #gives the first paragraph
    print(html.a)          #gives the first anchor tag
    print(html.a['href'])  #gives the href attribute of the first anchor tag
    print(html.h1)         #gives the first h1 tag
    print(html.h1.text)    #gives the text inside the first h1 tag
    print(html.title)      #gives the title of the webpage
    print(html.title.text) #gives the text inside the title tag
    print(html.title.string) #gives the text inside the title tag
else:
    print("Error")