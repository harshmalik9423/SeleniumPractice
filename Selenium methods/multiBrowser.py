from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver = webdriver.Edge(executable_path="C:\BrowserDrivers\msedgedriver.exe")

driver.get("http://example.com")

print(driver.title)     # extracts title of page
print(driver.current_url)       # returns url
print(driver.page_source)       # returns HTML code
driver.close()      # close browser
