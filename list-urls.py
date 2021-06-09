from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_base(self):
        self.open(url)
        #TODO add csv with urls
        elements = self.find_elements('li.menu-item a')
        for element in elements:
            print(element.get_attribute("href"))
