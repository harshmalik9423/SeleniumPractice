from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element(By.ID, "tab-flight-tab-hp").click()  # Flights button

driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("DEL")
time.sleep(2)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("DED")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/08/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("22/08/2020")

driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Explicit wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()

time.sleep(3)
driver.quit()