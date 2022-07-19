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
print(driver.title)
print(driver.current_url)
driver.find_elements(By.ID, "item_1_title_link")[0].click()
driver.find_elements(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")[0].click()
print(driver.current_url)
driver.find_elements(By.ID, "back-to-products")[0].click()
print(driver.current_url)
driver.find_elements(By.ID, "add-to-cart-sauce-labs-bike-light")[0].click()
elements = driver.find_element("xpath","/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
print(elements.text)
elementsbag = driver.find_element("xpath","/html/body/div/div/div/div[1]/div[1]/div[3]/a/span")
print(elementsbag.text)
elementsbag.click()
print(driver.current_url)
driver.find_element("xpath","/html/body/div/div/div/div[2]/div/div[2]/button[2]").click()
print(driver.current_url)
driver.find_elements(By.ID, "first-name")[0].send_keys('first-name')
driver.find_elements(By.ID, "postal-code")[0].send_keys('postal-code')
driver.find_element("xpath","/html/body/div/div/div/div[2]/div/form/div[2]/input").click()
print(driver.find_element("xpath","/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3").text)
driver.find_elements(By.ID, "last-name")[0].send_keys('postal-code')
driver.find_element("xpath","/html/body/div/div/div/div[2]/div/form/div[2]/input").click()
print(driver.find_element("xpath","/html/body/div/div/div/div[2]/div/div[2]/div[7]").text)
driver.find_element("xpath","/html/body/div/div/div/div[2]/div/div[2]/div[8]/button[2]").click()
print(driver.find_element("xpath","/html/body/div/div/div/div[2]/h2").text)
print(driver.find_element("xpath","/html/body/div/div/div/div[2]/img").get_attribute("src"))
driver.find_elements(By.ID, "menu_button_container")[0].click()
print(driver.current_url)
