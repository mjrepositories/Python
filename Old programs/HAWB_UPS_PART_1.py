from selenium import webdriver
import time
import shutil
import logging
import datetime
import win32com.client




# creating logger for actions
logger = logging.getLogger("UPS Log")
# setting the level for the logger
logger.setLevel('INFO')
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\UPS\UPS {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of HAWB upload has been started')














# setting up chrome options and default folder for download
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\Users\310295192\Desktop\Python\Projects\HAWB\UPS\MJB"}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=chromeOptions)
# getting to Optilo
browser.get("https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")
browser.maximize_window()
# loggin in
emailElem = browser.find_element_by_id('inpLogin')
emailElem.send_keys('maciej.janowski@philips.com')
# inputting password
password = browser.find_element_by_id('inpPassword')
password.send_keys('Maciej0312@')

# submitting logon details
buttonlog = browser.find_element_by_id('submitLogin')
buttonlog.click()

# finding multi tab
multi = browser.find_element_by_id('menu-259381')
multi.click()
# finding multi job tab
joblist = browser.find_element_by_id('menu-259383')
joblist.click()

# select carrier table to chose from
car = browser.find_element_by_id('go_DF650000161_carrier_id_krt_kontrahent')
car.click()
time.sleep(3)
# switch focus to current window
x = browser.find_element_by_id('TB_iframeContent')
browser.switch_to.frame(x)
time.sleep(1)
# type in name of the carrier
name = browser.find_element_by_id('DF230000259_nazwa')
name.send_keys('UPS (AIR)')
time.sleep(1)
# click search
search = browser.find_element_by_id('action[230000259][2123]')
search.click()
time.sleep(1)
# select the carrier
selection = browser.find_element_by_xpath('//*[@id="DL230000260"]/tbody/tr[2]/td[1]/a')
selection.click()
time.sleep(1)
# click search on a main page
search_again = browser.find_element_by_id('action[650000161][3242]')
search_again.click()
time.sleep(3)
# downloaded report from Optilo
button = browser.find_element_by_link_text("XLS")
logger.info('file with MJB numbers for UPS AIR has been downloaded from Optilo')
button.click()


time.sleep(10)

browser.close()
