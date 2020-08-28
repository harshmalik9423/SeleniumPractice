import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_one(self):
        driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
        driver.get("https://www.google.com")

        # self.assertTrue(driver.title == "Google")
        self.assertFalse(driver.title == "Google12")
        driver.quit()

if __name__ == '__main__':
    unittest.main()
