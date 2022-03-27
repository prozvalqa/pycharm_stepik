from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'trollface.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    cifra = browser.find_element(By.ID, 'input_value')
    cifra_text = cifra.text
    print(cifra_text)
    y = calc(cifra_text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()

finally:
    time.sleep(6)
    browser.quit()