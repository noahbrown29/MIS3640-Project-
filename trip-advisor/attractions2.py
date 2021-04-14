# WHAT NEEDS TO BE DONE:
# 1. Is there a way to automatically click on the first google search result?
# 2. Is there a way to always have "TripAdvisor" within the search part of the url (q=) but still allow the user to input the rest of their query?

"""
Make sure chromedriver is installed (Below is the correct link for windows computers using Chrome version 90)
https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/
"""
  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,datetime,os,sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Taking input from user
search_string = input("Input the URL or string you want to search for: ")
  
# This is done to structure the string 
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+') 
  
# Assigning the browser variable with chromedriver of Chrome.
# Any other browser and its respective webdriver 
# like geckodriver for Chrome can be used
driver = webdriver.Chrome('chromedriver')
  
for i in range(1):
    matched_elements = driver.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))


driver.find_elements_by_tag_name('h3').send_keys("\n")
# time.sleep(3)
# results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')
# results[0].click()

# driver.implicitly_wait(5)

# driver.find_element_by_xpath('//a[starts-with(@href,"http://www.tripadvisor.com")]').click()