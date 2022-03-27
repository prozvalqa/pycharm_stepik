#Заполняем форму
#Find_element

from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get('http://suninjuly.github.io/find_link_text')
    browser.find_element(By.LINK_TEXT,  str(math.ceil(math.pow(math.pi, math.e)*10000))).click()
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrovskiy")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()