from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Scroll by pixel
# driver.execute_script("window.scrollBy(0,1000)", "")

# Scroll by element
# flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll to end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.quit()