import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
        driver.get("https://www.google.com")
        page_title = driver.title

        #self.assertEqual("Google",page_title,"Title of page in not same")
        self.assertNotEqual("Google12",page_title)


if __name__ == '__main__':
    unittest.main()
