from selenium import webdriver
import time
import os
browser= webdriver.Chrome()
browser.maximize_window()
browser.get("https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")
emailElem = browser.find_element_by_id('inpLogin')
emailElem.send_keys('maciej.janowski@philips.com')
passwordElem=browser.find_element_by_id('inpPassword')
passwordElem.send_keys('Maciej0312@')
login=browser.find_element_by_id('submitLogin')
login.click()
#257650 from 256937
importtab=browser.find_element_by_id('menu-257650')
importtab.click()
#257653 from 256840
transfer=browser.find_element_by_id('menu-257653')
transfer.click()
combobox = browser.find_element_by_id('DF590000016_status_operacyjny_box')
errors = combobox.find_element_by_xpath("select[@multiple='multiple']/option[5]")
unclick= combobox.find_element_by_xpath("select[@multiple='multiple']/option[1]")
unclick.click()
errors.click()
datatype = browser.find_element_by_id("DF590000016_transfer_typ1")
datatype.send_keys("PRJSOT")
datefrom = browser.find_element_by_id("DF590000016_add_data_od")
datefrom.send_keys("2019-02-05 00:00")
#action[590000016][1524183] from action[590000016][1520098]
excelform = browser.find_element_by_id("action[590000016][1524183]")
excelform.click()

time.sleep(3)

import pyautogui
#Point(x=128, y=1015) - downloaded file
#Point(x=531, y=50) - dialog window
#Point(x=790, y=510) - save button
#Opens the excel file after download
pyautogui.click(128,1015)
time.sleep(6)
#closes the browser
time.sleep(6)
#click f12 for "save as"
pyautogui.hotkey('f12')
time.sleep(2)
#type in the name of the file
pyautogui.typewrite('SOTreport.xls')
time.sleep(1)
#click the address window
pyautogui.click(530,50)
time.sleep(1)
#type in the folder where it should be saved and click applies it
pyautogui.typewrite(r'C:\Users\310295192\Desktop\VBA projects\Key-users app\reports')
pyautogui.typewrite(["enter"])
time.sleep(1)
#saves file under new name in specified folder
pyautogui.click(790,510)
time.sleep(2)
#closes the window
pyautogui.click(1896,13)
#getting the PAC report

pyautogui.click(1400,13)
#let's extract PAC from system
datatype1 = browser.find_element_by_id("DF590000016_transfer_typ1")
datatype1.clear()
datatype1.send_keys("PRJPAC")
datefrom2 = browser.find_element_by_id("DF590000016_add_data_od")
datefrom2.send_keys("2019-02-05 00:00")
# action[590000016][1524183] from action[590000016][1520098]
excelform1 = browser.find_element_by_id("action[590000016][1524183]")
excelform1.click()
time.sleep(3)

import pyautogui

# Point(x=128, y=1015) - downloaded file
# Point(x=531, y=50) - dialog window
# Point(x=790, y=510) - save button
# Opens the excel file after download
pyautogui.click(128, 1015)
time.sleep(6)
# closes the browser
browser.close()
time.sleep(6)
# click f12 for "save as"
pyautogui.hotkey('f12')
time.sleep(2)
# type in the name of the file
pyautogui.typewrite('PACreport.xls')
time.sleep(1)
# click the address window
pyautogui.click(530, 50)
time.sleep(1)
# type in the folder where it should be saved and click applies it
pyautogui.typewrite(r'C:\Users\310295192\Desktop\VBA projects\Key-users app\reports')
pyautogui.typewrite(["enter"])
time.sleep(1)
# saves file under new name in specified folder
pyautogui.click(790, 510)
time.sleep(2)
# closes the window
pyautogui.click(1896, 13)


#go to philips sharepoint
browser= webdriver.Chrome()
browser.maximize_window()
browser.get("https://share.philips.com/sites/STS020180301160509/Shared%20Documents/Forms/AllItems.aspx?viewpath=%2Fsites%2FSTS020180301160509%2FShared%20Documents%2FForms%2FAllItems%2Easpx&id=%2Fsites%2FSTS020180301160509%2FShared%20Documents%2FPCT%20Poland%2FRates%2FKey-User%20app")
time.sleep(6)
#Point(x=1065, y=576) position for picking account
pyautogui.click(1065,576)
#is adding email while logging and pass sthe email to browser
pyautogui.click(913,559)
pyautogui.typewrite('maciej.janowski@philips.com')
pyautogui.typewrite(['enter'])
#click on file
time.sleep(8)
pyautogui.click(519,447)

time.sleep(5)
#click on open menu
pyautogui.click(314,299)
time.sleep(5)
#click on open in excel
pyautogui.click(288,372)
time.sleep(5)

#Point(x=1018, y=174) open on desktop
pyautogui.click(1018,174)
time.sleep(23)
#editwork option
pyautogui.doubleClick(515,164)
time.sleep(5)

#update by using PACreport
#Point(x=1159, y=305) position for file opening
pyautogui.click(1159,309)
time.sleep(4)
#click on address window
pyautogui.click(125,50)
time.sleep(4)
#type in the folder where it should be saved and click applies it
pyautogui.typewrite(r'C:\Users\310295192\Desktop\VBA projects\Key-users app\reports')
pyautogui.typewrite(['enter'])
time.sleep(4)
#Point(x=270, y=144) position for file to update
pyautogui.click(270,144)
pyautogui.typewrite(['enter'])
time.sleep(4)
time.sleep(4)
os.remove(r'C:\Users\310295192\Desktop\VBA projects\Key-users app\reports\PACreport.xls')


#update by using SOTeport
#Point(x=1159, y=305) position for file opening
pyautogui.click(1159,309)
time.sleep(2)
#click on address window
pyautogui.click(125,50)
time.sleep(2)
#type in the folder where it should be saved and click applies it
pyautogui.typewrite(r'C:\Users\310295192\Desktop\VBA projects\Key-users app\reports')
pyautogui.typewrite(['enter'])
time.sleep(4)
#sort by date Point(x=513, y=112)
pyautogui.click(513,112)
time.sleep(4)
#Point(x=270, y=144) position for file to update
pyautogui.click(270,144)
pyautogui.typewrite(['enter'])
time.sleep(3)
#sort by date Point(x=513, y=112)
#pyautogui.click(513,112)
time.sleep(3)
time.sleep(3)
#saves the file and deletes the source for SOT report
pyautogui.hotkey('ctrl','s')
time.sleep(3)
os.remove(r'C:\Users\310295192\Desktop\VBA projects\Key-users app\reports\SOTreport.xls')
#should be ok...Let's check at office
# and if needed - adding email while logging into the philips web
# and then.... MONEY TIME :)
browser.close()
#saves the file and deletes the source for SOT report
pyautogui.hotkey('ctrl','s')
#closes the window with excel
pyautogui.click(1896,13)
#save changes in excel Point(x=876, y=554)
time.sleep(2)
pyautogui.click(876,554)



#Trzeba jeszcze wrzucić opcje aktualizowania z hasłem i będzie bailando