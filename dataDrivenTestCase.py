from selenium import webdriver
import xlUtils

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

path = r"C:\Users\harsh\Desktop\test.xlsx"

rows = xlUtils.getRowCount(path, "Sheet1")

for r in range(2,rows+1):
    username = xlUtils.readData(path, "Sheet1", r, 1)
    password = xlUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys(username)
    driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys(password)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

    if driver.current_url == "https://opensource-demo.orangehrmlive.com/" or driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials" or driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/auth/login":
        xlUtils.writeData(path, "Sheet1", r, 3, "Failed")
    else:
        xlUtils.writeData(path, "Sheet1", r, 3, "Passed")
        driver.find_element_by_xpath("//*[@id='welcome']").click()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")