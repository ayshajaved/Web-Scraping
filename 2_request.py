import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

response = requests.get(url)
'''
There are 4 objects of beautifulsoup
-->tags tags of the html doc
-->navigable strings content in the tags
-->beautiful soup 
-->comments A special type of NavigableString that represents comments in the HTML or XML document.
-->ResultSet object, which is essentially a list of all matching elements.
'''
if response.status_code == 200:
    print("Success")
    content = response.content
    html = BeautifulSoup(content, 'html.parser') #html is the beautiful soup object having following methods
    #html.head                            
    #html.body
    #html.find()
    #html.find_all()

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
    resultObject = html.find_all('p') #Result object of beautiful soup returning all the paragraphs
    for result in resultObject: 
        print(result.text) #Printing all paragraphs
    print(resultObject[1])
else:
    print("Error")

'''


'''