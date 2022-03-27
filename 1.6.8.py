#Заполняем форму
#Find_element

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()