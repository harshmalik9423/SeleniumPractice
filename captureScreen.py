from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://google.com")

# driver.save_screenshot("C:\hompage.png")              # Can save any filetype
driver.get_screenshot_as_file("C:\homepage.png")        # Can save only png
driver.quit()