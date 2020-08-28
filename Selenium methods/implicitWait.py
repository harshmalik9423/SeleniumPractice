from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://google.com")

# wait sometime
driver.implicitly_wait(5)
assert "Google" in driver.title

ele = driver.find_element_by_name("q")
ele.send_keys("Automation testing")
ele.send_keys(Keys.ENTER)

driver.quit()