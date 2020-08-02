from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "C:\DownloadedFiles"})

driver = webdriver.Chrome(executable_path="C:\BrowserDrivers\chromedriver.exe", chrome_options=chromeOptions)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")

# Download text file
driver.find_element_by_id("textbox").send_keys("testing file downloading")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing file downloading")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()