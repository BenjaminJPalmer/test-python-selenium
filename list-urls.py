from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_base(self):
        self.open("http://gme-painting.dev.ascensor.co.uk/")
        elements = self.find_elements('li.menu-item a')
        for element in elements:
            print(element.get_attribute("href"))
