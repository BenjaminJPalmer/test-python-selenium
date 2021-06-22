from seleniumbase import BaseCase
import csv

# Open csv to read and convert to a list
with open(r"C:\Users\benpa\Documents\GitHub\test-python-selenium\website-test.csv", newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

# Initiate list for converting items into strings
newData = []
for site in data:
    newSite = ''.join(site)
    newData.append(newSite)

class MyTestClass(BaseCase):
    def test_base(self):
        for url in newData:
            self.open(url)
            #TODO add csv with urls
            elements = self.find_elements('li.menu-item a')
            for element in elements:
                print(element.get_attribute("href"))
