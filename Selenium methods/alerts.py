from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()

time.sleep(3)

# driver.switch_to_alert().accept()   # clicks OK

driver.switch_to_alert().dismiss()  # clicks cancel
time.sleep(3)
driver.quit()