import unittest
import csv
from time import sleep
from selenium import webdriver

with open(r"C:\Users\benpa\Documents\GitHub\test-python-selenium\website-test.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

newData = []

for s in data:
    s1 = ''.join(s)
    newData.append(s1)

print(newData)

# Start test case to search python.org
class PythonOrgsearch(unittest.TestCase):

    # Initiate the chrome browser
    def setUp(self):
        self.browser = webdriver.Chrome()

    # Visit webpage, assert it is correct
    def test_search_in_python_org(self):
        browser = self.browser
        for url in newData:
            browser.get(url)
            sleep(1)
            filename = 'screenshots/' + url.split('//')[-1] + '.png'
            browser.save_screenshot(filename)
        
    # Closes the browser
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()