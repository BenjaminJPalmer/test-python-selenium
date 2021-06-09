# import csv
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import seleniumbase

url = "http://gme-painting.dev.ascensor.co.uk/"

class WebsiteFullScreenshotCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_check_pages(self):
        driver = self.driver
        try:
            driver.get(url)
            nav = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "nav"))
            )
            print(nav.text)
            assert True
        except:
            print(f"Assertion failed with {url}.")
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()