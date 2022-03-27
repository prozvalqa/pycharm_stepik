from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome('C:\\browserdrivers\\chromedriver.exe')
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "label[for='peopleRule']")
    atribute = input1.get_attribute('People rule')
    x = atribute.text
    print(x)
finally:
    time.sleep(1)
    browser.quit()