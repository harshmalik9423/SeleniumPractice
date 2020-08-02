from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("E:/Freshers 2018/20180910_111832.jpg")
driver.quit()