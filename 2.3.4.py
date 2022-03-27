#confirm allert
#print(browser.switch_to.alert.text) == сразу вывести текст из алерта

from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/alert_accept.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    browser.switch_to.alert.accept()
    chislo =  browser.find_element(By.ID, 'input_value')
    chislo_text = chislo.text
    print(chislo_text)
    y = calc(chislo_text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(6)
    browser.quit()
