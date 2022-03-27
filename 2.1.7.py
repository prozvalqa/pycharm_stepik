#get_attribute - достать значение любого атрибута

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/get_attribute.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    sunduk = browser.find_element(By.ID, 'treasure')
    sunduk_value = sunduk.get_attribute('valuex')
    y = calc(sunduk_value)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(6)
    browser.quit()