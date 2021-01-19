from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/js/js_if_else.asp')

sleep(5)
browser.close()
browser.quit()

