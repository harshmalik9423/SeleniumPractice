from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://google.com")

ele = driver.find_element_by_name("q")

print(ele.is_displayed())       # returns true/false
print(ele.is_enabled())

ele.send_keys("Automation testing")
ele.send_keys(Keys.ENTER)

print(driver.title)

driver.quit()