from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

driver.get("https://www.bb.org.bd/en/index.php/monetaryactivity/call_money_market")
product = []
maturity = []
amount = []
highest = []
lowest = []
average = []
deals_no = []
infos = driver.find_elements(by=By.CSS_SELECTOR, value="tr")
row = 2
for info in infos:
    if row <= 9:
        product.append(info.find_element(by=By.XPATH, value="//table/tbody/tr[" + str(row) + "]/td[1]").text)
        maturity.append(info.find_element(by=By.XPATH, value="//table/tbody/tr[" + str(row) + "]/td[2]").text)
        amount.append(info.find_element(by=By.XPATH, value="//table/tbody/tr["+str(row)+"]/td[3]").text)
        highest.append(info.find_element(by=By.XPATH, value="//table/tbody/tr[" + str(row) + "]/td[4]").text)
        lowest.append(info.find_element(by=By.XPATH, value="//table/tbody/tr[" + str(row) + "]/td[5]").text)
        average.append(info.find_element(by=By.XPATH, value="//table/tbody/tr[" + str(row) + "]/td[6]").text)
        deals_no.append(info.find_element(by=By.XPATH, value="//table/tbody/tr[" + str(row) + "]/td[7]").text)
        row += 1
driver.quit()

df = pd.DataFrame({'product':product, 'maturity':maturity, 'amount':amount, 'highest':highest, 'lowest':lowest, 'average':average, 'deals_no':deals_no})
df.to_csv('call_money.csv', index=False)
print(df)
