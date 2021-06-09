import os
from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_base(self):
        self.open(url)        
        #TODO add csv with urls
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
        print("\n  Screenshot location: [%s]" % test_logpath)

        for nav_link in unique_nav_links:
            self.open(nav_link)
            if self.is_text_visible("404 Error", "h1"):
                bad_links.append(nav_link)
                print("* Bad page: [%s]" % nav_link)
            else:
                self.save_screenshot_to_logs()
                print("[%s] saved." % nav_link)
