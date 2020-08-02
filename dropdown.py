from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://fs10.formsite.com/tEUlfR/ymt8065ra9/index.html?1596339042118")

drop = Select(driver.find_element_by_id("RESULT_RadioButton-10"))

# Select by Visible text
drop.select_by_visible_text("Choice A")
time.sleep(2)

# Select by index
drop.select_by_index(2)
time.sleep(2)

# Select by value
drop.select_by_value("Radio-2")
time.sleep(2)

# Count num of options
print(len(drop.options))

# Capture all options and print
all_options = drop.options

for option in all_options:
    print(option.text)

driver.quit()