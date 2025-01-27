'''
Selenium is the module in python that is actually used for software testing. It is used to automate the web browsers. So, we can do webScraping through selenium, getting data in the html format from the websites and then parsing and using it through beautiful soup, processing or storing it through pandas.
'''
import selenium                               
from selenium import webdriver                 #importing webdrivers like chrome, firefox, IE, remote(for remote testing)
from selenium.webdriver.common.keys import Keys#Importing keys like all the keyboard keys 
from selenium.webdriver.common.by import By    #By for searching elements by name, id, xpath, class name, css selector
from selenium.webdriver.support.ui import WebDriverWait #dynamic way to wait for an element to appear
from selenium.webdriver.support import expected_conditions as EC #conditions for waiting
import time                                    #Useful only for static pages

class chromeAutomation():
    def __init__(self):
        self.driver = webdriver.Chrome()       #starting chrome
        self.driver.get("https://www.python.org")#opening python.com
        self.driver.maximize_window()          #maximizing the window
        '''
        assert 
        The assert function in Python is used as a debugging aid to test whether a certain condition evaluates to True. If the condition is False, the program raises an AssertionError and stops execution. If the condition is True, the program continues execution.
        assert condition, error
        '''
        try:
            assert "Python" in self.driver.title#asserting that the title of the page contains python
        except AssertionError:                  #error if title is not present
            print("Title is not correct")
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "q"))) #waiting for the search bar to appear
        self.search = self.driver.find_element(By.NAME, "q")
        self.search.send_keys("python")         #searching for python
        self.search.send_keys(Keys.RETURN)#pressing enter after searching python

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "content")))#Wait for the content to be loaded
        print("Search results are loaded.")

        main_content = self.driver.find_element(By.ID, "content")
        print(main_content.text)
       
        # time.sleep(10)                          #waiting for 10 seconds
        # self.search.clear()                   #clearing the search bar 
    def close(self):
        # self.driver.close()                   #closing the browser
        self.driver.quit()                      #quitting the driver
        '''
        whats the difference between close and quit?
        close() closes the current window, but the driver is still active and can be used to open another window
        quit() closes all the windows and ends the driver session
        '''
if __name__ == "__main__":
    chromeAutomation = chromeAutomation()
    chromeAutomation.close()