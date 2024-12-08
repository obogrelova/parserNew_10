import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()

url = 'https://www.divan.ru/category/svet'

driver.get(url)

svets = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._Ud0k'))
)

parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'div.lsooF').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2').text
        url =  svet.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
        parsed_data.append([name, price, url])
    except Exception as e:
        print('Произошла ошибка при парсинге: {e}')
        continue



driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['название', 'цена', 'ссылка'])
    writer.writerows(parsed_data)