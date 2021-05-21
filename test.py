import unittest
import csv
from time import sleep
from selenium import webdriver

# Open csv to read and convert to a list
with open(r"C:\Users\benpa\Documents\GitHub\test-python-selenium\website-test.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# Initiate list for converting items into strings
newData = []
for s in data:
    s1 = ''.join(s)
    newData.append(s1)

# Start test case to search python.org
class PythonOrgsearch(unittest.TestCase):

    # Initiate the chrome browser
    def setUp(self):
        self.browser = webdriver.Chrome()

    # Visit webpage, wait for 1 second then save a screenshot
    def test_search_in_python_org(self):
        browser = self.browser
        for url in newData:
            browser.get(url)
            sleep(1)
            filename = 'screenshots/' + url.split('//')[-1] + '.png' # Removes / from the filename
            browser.save_screenshot(filename)
        
    # Closes the browser once all webpages are visited
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()