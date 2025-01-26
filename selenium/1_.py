import selenium                               
from selenium import webdriver                 #importing webdrivers like chrome, firefox, IE, remote(for remote testing)
from selenium.webdriver.common.keys import Keys#Importing keys like all the keyboard keys 
from selenium.webdriver.common.by import By    #By for searching elements by name, id, xpath, class name, css selector
from selenium.webdriver.support.ui import WebDriverWait 
import time

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
        self.search = self.driver.find_element(By.NAME, "q")
        self.search.send_keys("python")         #searching for python
        self.search.send_keys(Keys.RETURN)#pressing enter after searching python
        time.sleep(10)                          #waiting for 10 seconds
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