from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

source = driver.find_element_by_xpath("//*[@id='gallery']/li[1]")
dest = driver.find_element_by_xpath("//*[@id='trash']")

actions = ActionChains(driver)

actions.drag_and_drop(source, dest).perform()

driver.quit()
