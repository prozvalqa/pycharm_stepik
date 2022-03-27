#.text - достать из атрибута текст

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    input1 = browser.find_element(By.ID, 'input_value')
    x = input1.text
    y = calc(x)
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(5)
    browser.quit()