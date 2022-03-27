#Заполняем форму
#Find_element
#assert

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
# код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys('mama')
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys('mama')
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys('mama')
# Отправляем заполненную форму
    browser.find_element(By.CLASS_NAME, 'btn-default').click()
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
    time.sleep(2)
# находим элемент, содержащий текст
    welcome_text = browser.find_element(By.TAG_NAME, 'h1')
# записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text1 = welcome_text.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text1
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()