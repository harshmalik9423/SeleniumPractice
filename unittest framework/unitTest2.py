import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):      # Always start with "test"
        self.driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
        self.driver.get("https://www.google.com")
        print("The title of the page is : " + self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
        self.driver.get("https://www.bing.com")
        print("The title of the page is : " + self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()