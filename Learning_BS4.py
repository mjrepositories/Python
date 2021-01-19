# importing necessary libraries
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# creating options for Chrome
options = Options()
# adding argument to open chrome headless
options.add_argument('--headless')

options.add_argument('--disable-gpu')
# adding user-agent so that table is visible
options.add_argument('user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
# initiating driver
driver = webdriver.Chrome(options=options)
# getting page
driver.get('https://www.nba.com/standings')
# getting html
html = driver.page_source
# creating bs object for lxml parser
soup = BeautifulSoup(html,features="lxml")
# closing driver
driver.close()
# prettifying the code so that it looks like in a browser
print(soup.prettify())
print(soup.prettify().split('\n'))

with open(r'C:\Users\Maciek\Desktop\page.txt','a',encoding="utf-8") as my_file:
    for row in soup.prettify().split('\n'):
        my_file.write(row + '\n')
