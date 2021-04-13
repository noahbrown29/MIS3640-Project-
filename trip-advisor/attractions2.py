# WHAT NEEDS TO BE DONE:
# 1. Is there a way to automatically click on the first google search result?
# 2. Is there a way to always have "TripAdvisor" within the search part of the url (q=) but still allow the user to input the rest of their query?

"""
Make sure chromedriver is installed (Below is the correct link for windows computers using Chrome version 89)
https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip
"""
  
from selenium import webdriver
import time
  
# Taking input from user
search_string = input("Input the URL or string you want to search for: ")
  
# This is done to structure the string 
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+') 
  
# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver 
# like geckodriver for Chrome can be used
browser = webdriver.Chrome('chromedriver')
  
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))

