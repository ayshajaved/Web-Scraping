import requests
#requesting the website of youtube to get th content
url = "https://www.youtube.com"
response = requests.get(url)
print(response)             #give response eg.200 successful 
print(response.status_code) #200: Success 404: Resource not found 500: Internal server error.403: Forbidden (e.g., access denied).
print(response.content)     #
'''Use response.content when:
You're working with binary data or need the raw response.
Example: Downloading an image file.
Use response.text when:
You're working with text data, and automatic decoding suffices.
Example: Scraping a webpage's HTML content.
'''
print(response.text)
print(response.headers)
print(response.encoding)
print(response.cookies) #cookies by server
print(response.elapsed) #To measure server response time.
