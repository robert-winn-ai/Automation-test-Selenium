from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
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
inputElementuser = driver.find_element(by=By.ID, value= 'user-name')
inputElementuser.send_keys('standard_user')
inputElementpassword =  driver.find_element(by=By.ID, value= 'password') 
inputElementpassword.send_keys('secret_sauce')
driver.find_element_by_css_selector('submit-button btn_action').click()

