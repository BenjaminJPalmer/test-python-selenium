import os
import csv
from seleniumbase import BaseCase
import requests
# import pytest_html

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
                print(f"FAIL: Status code for {url} = {urlStatus}.")
            # If valid proceed
            else:
                self.open(url)
                # Locate links on the page
                elements = self.find_elements('li a')
                nav_links = []
                # Append href links to array
                for element in elements:
                    nav_links.append(element.get_attribute("href"))
                # Remove duplicates by putting unique links in new array
                unique_nav_links = []
                for nav_link in nav_links:
                    if nav_link not in unique_nav_links:
                        unique_nav_links.append(nav_link)
                
                bad_links = []
                test_logpath = os.path.join(self.log_path, self.test_id) # TODO Change to (..., url)?
                #TODO update folder naming with iterator for each test run
                print(f"\n  Screenshot location: {test_logpath}")

                for nav_link in unique_nav_links:
                    try:
                        self.open(nav_link)
                        # Visual check in case of 404 error pages
                        # TODO change this to a request status code check?
                        if self.is_text_visible("404 Error", "h1"):
                            bad_links.append(nav_link)
                            print(f"* Bad page: {nav_link}")
                        else:
                            self.save_screenshot_to_logs()
                            print(f"{nav_link} saved.")
                    except:
                        bad_links.append(nav_link) # Added to collate bad links on page fail
                        print(f"Error trying to open {nav_link}.")
                        continue
