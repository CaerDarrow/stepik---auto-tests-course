from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_elem = browser.find_element_by_id("num1")
    x = int(x_elem.text)
    y_elem = browser.find_element_by_id("num2")
    y = int(y_elem.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x+y))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()