from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://google.com")

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
    print(link.text)

# Click on link
# driver.find_element(By.LINK_TEXT, "About").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Abo").click()

driver.quit()