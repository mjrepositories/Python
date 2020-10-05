from bs4 import BeautifulSoup
import requests
import openpyxl
import time
import datetime
from selenium import webdriver

webpage = 'https://www.eia.gov/petroleum/gasdiesel/'
# i am getting the whole text from the page
source = requests.get(webpage).text

# creating beautifulsoup object
soup=BeautifulSoup(source,'lxml')
string = ""
# going through every table with class simpletable and saving text
for tbody in soup.find_all('table',class_='simpletable'):
    data = tbody.text
    string = string + data
    # print(data)

# creating list from data gathered
newstring=string.splitlines()
# print(newstring)
# checking how many items we have as blanks
how_many=newstring.count("")
# going through every blank object and deleting it
for x in range(1,how_many):
    newstring.remove("")
# print(newstring)
# checking at which place i have diesel price
where = newstring.index('U.S. On-Highway Diesel Fuel Prices*\xa0\xa0(dollars per gallon)full history')

# checking at which place is U.S. (after diesel price
us = newstring[where:].index("U.S.")
# print(newstring[where+us:])
#checking current price based on place in the list
current_price = newstring[where+us+3]
#switching to float
current_price = float(current_price)
print(current_price)
# print(type(current_price))



# THIS SECTION SELECTS THE VALIDTY DATE


for tbody in soup.find_all('table',class_='simpletable'):
    data = tbody.text
    break

# creates a table
changes = data.splitlines()
# counts blanks
how_many = changes.count("")
# going through every blank object and deleting it
for x in range(1,how_many):
    changes.remove("")

# counts this strange string
how_many = changes.count("\xa0")
# going through each strange string and deletes it
for x in range(1,how_many):
    changes.remove('\xa0')
# selects the current date for validity
date = changes[4]

# formats the date to specific format
day = datetime.datetime.strptime(date,"%m/%d/%y").strftime("%Y-%m-%d")







#opening excel
wb = openpyxl.load_workbook(r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\CHRobinsonPython\Diesel price.xlsx')
# finding the value for diesel price and updating the cell
sheet = wb['diesel price']
sheet['A2'].value = current_price
print(sheet['A2'].value)
# saving file
wb.save(r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\CHRobinsonPython\Diesel price.xlsx')
wb.close()

import win32com.client
xl_app = win32com.client.Dispatch("Excel.Application")
# running two three files - diesel price, US 90 and US 08
xl_app.Visible = False
xl_app.DisplayAlerts = False
# opens us 90 file
us90 = r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\CHRobinsonPython\US 90  - US CHRB5 TN Export (Base file) KG with surcharge.xlsx'
wbus90 = xl_app.Workbooks.Open(us90)
# opens us 08 file
us08 = r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\CHRobinsonPython\US 08  - US CHRB5 TN Export (Base file) KG with surcharge.xlsx'
wbus08 = xl_app.Workbooks.Open(us08)
# opens diesel price file
diesel = r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\CHRobinsonPython\Diesel price.xlsx'
wbdiesel=xl_app.Workbooks.Open(diesel)
time.sleep(1.5)
xl_app.AskToUpdateLinks = False
# assigns surcharges tabs
surcharge90 = wbus90.Sheets['Surcharge']
surcharge08 = wbus08.Sheets['Surcharge']
freight90 = wbus90.Sheets['Freight']
freight08 = wbus08.Sheets['Freight']

# assigns the validity date
freight90.Range("C8").Value = day
freight08.Range("C8").Value = day

# creates lists for iteration for us90 and us08
list08 = ['D','E']
list90 = ['D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q','R','S','T','U','V']
# looping through every cell and adjusting the value to float
for x in list08:
    charging = surcharge08.Range("{}40".format(x)).Value
    surcharge08.Range("{}40".format(x)).Value = charging

# looping through every cell and adjusting the value to float
for x in list90:
    charging = surcharge90.Range("{}40".format(x)).Value
    surcharge90.Range("{}40".format(x)).Value = charging

# Saving workbooks under new names
wbus08.SaveAs(r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\fuel surcharge project CH Robinson\Uploads\US 08 - US CHRB5 TN Export {} KG.xlsx'.format(day))
wbus90.SaveAs(r'C:\Users\310295192\Desktop\Work\Rates\Road\CH Robinson\fuel surcharge project CH Robinson\Uploads\US 90 - US CHRB5 TN Export {} KG.xlsx'.format(day))
# c = surcharge90.Range("H40").Value
# surcharge90.Range("H40").Value = c
# print(c)
# saving necessary workbooks
wbus90.Close(False)
wbus08.Close(False)
wbdiesel.Close(True)
# closing excel
xl_app.Quit()


browser = webdriver.Chrome()
# gets to infodis
browser.get('https://www.infodis.net/philips/net/LogOn/Authenticate?returnToPreviousPage=true')
#types in login
login = browser.find_element_by_id('LogOnName')
login.send_keys("310295192")
time.sleep(1)
#types in password
password = browser.find_element_by_id('Password')
password.send_keys('Maciej0312')
time.sleep(1)
# finds log-in butto
logon = browser.find_element_by_css_selector('#form-login > div > div.page-header.ui-widget-header.ui-corner-all > div.button-group > div > span.ui-button-text')
logon.click()
time.sleep(2)
# goes to rates
rates = browser.find_element_by_xpath('//*[@id="mainmenu"]/li[5]/a/span')
rates.click()
time.sleep(0.5)
# goes to uploads
upload = browser.find_element_by_xpath('//*[@id="mainmenu"]/li[5]/ul/li[2]/a/span')
upload.click()
time.sleep(2)
# selects new upload
newfile = browser.find_element_by_xpath('//*[@id="btnUploadNewR"]/span[2]')
newfile.click()
time.sleep(2)
# clicks new upload
attach = browser.find_element_by_xpath('//*[@id="upload-form"]/div/div[2]/div[2]/div/fieldset/div[1]/div[2]/div/div[1]/div/span')
attach.click()

