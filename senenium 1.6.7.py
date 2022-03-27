#Заполняем форму одинаковыми данными
#Find_elements


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
try:
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements(By.CSS_SELECTOR, '[type="text"]')
    for i in elements:
        i.send_keys("mama")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(20)
    browser.quit()