from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://www.bb.org.bd/en/index.php/monetaryactivity/call_money_market")

infos = driver.find_elements(by=By.CSS_SELECTOR, value="tr")
for info in infos:
    print(info.text)

driver.quit()
