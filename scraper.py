from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
#driver.get('https://storage.googleapis.com/qa__test/Elements/index.html')
#SearchResults = driver.find_element("//*[@id="header"]/h1/a/span")
driver.get('http://www.saucedemo.com')
print(driver.title)
driver.find_elements(By.ID, "user-name")[0].send_keys('standard_user')
driver.find_elements(By.ID, "password")[0].send_keys('secret_sauce')
driver.find_elements(By.ID, "login-button")[0].click()

