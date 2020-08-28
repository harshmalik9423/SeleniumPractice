import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_driver(self):
        try:
            driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
            # self.assertIsNone(driver)
            self.assertIsNotNone(driver)
        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()
