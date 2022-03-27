from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
link = "http://suninjuly.github.io/selects1.html"

try:
    def summ(x,y):
        return x+y
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1')
    num1_text = num1.text
    print(num1_text)
    num_chislo1 = int(num1_text)
    num2 = browser.find_element(By.ID, 'num2')
    num2_text = num2.text
    print(num2_text)
    num_chislo2 = int(num2_text)
    summa = summ(num_chislo1, num_chislo2)
    summa_stroka = str(summa)
    print(summ(num_chislo1, num_chislo2))
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(summa_stroka)
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()
finally:
    time.sleep(5)
    browser.quit()