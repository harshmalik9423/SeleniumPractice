from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://fs10.formsite.com/tEUlfR/ymt8065ra9/index.html?1596339042118")

# Find num of textbox
inputs = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputs))

# Verify status
status = driver.find_element(By.ID,'RESULT_TextField-2').is_displayed()
print("Displayed?: ", status)

status = driver.find_element(By.ID,'RESULT_TextField-2').is_enabled()
print("Enabled?: ", status)

# Provide value into textbox
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Harsh")
driver.find_element(By.ID,'RESULT_TextField-3').send_keys("Malik")

driver.quit()