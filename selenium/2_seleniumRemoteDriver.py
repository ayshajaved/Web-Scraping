'''
Using Selenium with remote WebDriver:

To use the remote WebDriver, you should have the Selenium server running. To run the server, use this command:
java -jar selenium-server-standalone-2.x.x.jar
While running the Selenium server, you could see a message looking like this:

15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
The above line says that you can use this URL for connecting to the remote WebDriver. Here are some examples:

from selenium import webdriver

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.ChromeOptions()
)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)
In the above code, webdriver.Remote() establishes a connection to the Selenium server running on your local machine (127.0.0.1:4444), and you can perform the same actions as if you were using a local browser.

If you're automating browser tasks like tests or scrapes, Selenium-controlled browsers offer great flexibility and speed. On the other hand, if you just want to browse or use the web manually, a local browser is your standard option.
'''

'''
I will not use this remote server, as i want to do automation
'''