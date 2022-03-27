from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    cifra = browser.find_element(By.ID, 'input_value')
    cifra_text = cifra.text
    print(cifra_text)
    y = calc(cifra_text)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.execute_script("window.scrollTo(0, 1080)")
    browser.find_element(By.ID, 'solve').click()

finally:
    time.sleep(16)
    browser.quit()
