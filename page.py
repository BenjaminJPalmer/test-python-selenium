import os
import csv
from seleniumbase import BaseCase
import requests

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
            urlStatus = requests.get(url).status_code

            # Checks status code is valid
            if urlStatus != 200:
                print(f"Status code for {url} = {urlStatus}.")
            else:
                self.open(url)        
                elements = self.find_elements('li.menu-item a')
                nav_links = []
                for element in elements:
                    nav_links.append(element.get_attribute("href"))
                unique_nav_links = []

                for nav_link in nav_links:
                    if nav_link not in unique_nav_links:
                        unique_nav_links.append(nav_link)

                bad_links = []
                test_logpath = os.path.join(self.log_path, self.test_id)
                print(f"\n  Screenshot location: {test_logpath}")

                for nav_link in unique_nav_links:
                    try:
                        self.open(nav_link)
                        if self.is_text_visible("404 Error", "h1"):
                            bad_links.append(nav_link)
                            print(f"* Bad page: {nav_link}")
                        else:
                            self.save_screenshot_to_logs()
                            print(f"{nav_link} saved.")
                    except:
                        continue
