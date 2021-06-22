import os
import csv
from seleniumbase import BaseCase


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
            elements = self.find_elements('li a')
            nav_links = []
            for element in elements:
                nav_links.append(element.get_attribute("href"))
            unique_nav_links = []

            for nav_link in nav_links:
                if nav_link not in unique_nav_links:
                    unique_nav_links.append(nav_link)

            bad_links = []
            test_logpath = os.path.join(self.log_path, self.test_id)
            print("\n  Screenshot location: [%s]" % test_logpath)

            for nav_link in unique_nav_links:
                self.open(nav_link)
                if self.is_text_visible("404 Error", "h1"):
                    bad_links.append(nav_link)
                    print("* Bad page: [%s]" % nav_link)
                else:
                    self.save_screenshot_to_logs()
                    print("[%s] saved." % nav_link)
