from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)     # gives handle of current window

handles = driver.window_handles     # value of all windows

for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(3)
    if driver.title == "Frames & windows":
        driver.close()

driver.quit()