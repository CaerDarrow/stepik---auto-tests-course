from selenium import webdriver
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector('button.btn').click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('button.btn').click()
finally:
    time.sleep(10)
    browser.quit()