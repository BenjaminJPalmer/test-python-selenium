# import csv
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import seleniumbase

url = "http://gme-painting.dev.ascensor.co.uk/"

driver = webdriver.Chrome()

try:
    driver.get(url)
    nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "nav"))
    )
    print(nav.text)
    
except:
    print(f"Assertion failed with {url}.")
    driver.quit()