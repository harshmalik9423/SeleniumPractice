from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://fs10.formsite.com/tEUlfR/ymt8065ra9/index.html?1596339042118")

# Working with radio buttons
status = driver.find_element(By.ID, "RESULT_RadioButton-12_0").is_selected()
print("Selected?: ", status)

driver.find_element(By.ID, "RESULT_RadioButton-12_0").click()

status = driver.find_element(By.XPATH, "//*[@id='q13']/table/tbody/tr[1]/td/label").is_selected()
print("Selected?: ", status)

# Working with checkboxes
driver.find_element_by_id("RESULT_CheckBox-13_0").click()
driver.find_element_by_id("RESULT_CheckBox-13_1").click()

driver.quit()

