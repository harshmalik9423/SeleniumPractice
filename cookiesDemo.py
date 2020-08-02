from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")

driver.get("https://amazon.in")

# To capture all cookies
cookies = driver.get_cookies()
print(len(cookies))        # num of cookies
print(cookies)

# Add new cookie
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Delete a cookie
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.quit()