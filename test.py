import unittest
import csv
from time import sleep
from selenium import webdriver

# Open csv to read and convert to a list
with open(r"C:\Users\benpa\Documents\GitHub\test-python-selenium\website-test.csv", newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

# Initiate list for converting items into strings
newData = []
for site in data:
    newSite = ''.join(site)
    newData.append(newSite)

# Start test case to search python.org
class WebsiteScreenshotCheck(unittest.TestCase):

    # Initiate the chrome browser
    def setUp(self):
        self.browser = webdriver.Chrome()

    # Visit webpage, wait for 1 second then save a screenshot
    def test_websites_and_screenshot(self):
        browser = self.browser
        for url in newData:
            try:
                browser.get(url)
                sleep(1)
                filename = 'screenshots/' + url.split('//')[-1] + '.png' # Removes / from the filename
                browser.save_screenshot(filename)
                # TODO number screenshots to correlate
                # TODO write screenshot name in csv
                # TODO export as simple HTML with url correlating to image link / error
                # TODO iterate through navbar links to check pages
            except:
                print(f"Assertion failed with {url}.")
        
    # Closes the browser once all webpages are visited
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()