from selenium import webdriver
import time
import os
import pandas as pd
import logging
import datetime
import win32com.client

# creating a logger for the dq documents
# creating logger for actions
logger = logging.getLogger("Ghosts")
# setting the level for the logger
logger.setLevel("INFO")
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\GHOSTS\Logger\Ghosts {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure for checking Ghosts initiated')


# making folders
folder = r'C:\Users\310295192\Desktop\Python\Projects\GHOSTS\REPORTS\Ghosts {}'.format(today)
os.mkdir(folder)

import numpy as np
# setting up chrome options and default folder for download
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : folder}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=chromeOptions)

# getting to Optilo and maximizing window

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
# multi = browser.find_element_by_id('menu-258664')
# multi = browser.find_element_by_id('menu-259381') update 2019-06-15
# multi = browser.find_element_by_id('menu-1-259756')
# multi.click()
# # finding multi job tab
# # joblist = browser.find_element_by_id('menu-258666')
# # joblist = browser.find_element_by_id('menu-259383') update 2019-06-15
# joblist = browser.find_element_by_id('menu-1-259756-259758')
# joblist.click()
browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')

# wait for js to be loaded
time.sleep(3)

blank = browser.find_element_by_xpath('//*[@id="DF650000161_status_operational"]/option[1]')
blank.click()
created = browser.find_element_by_xpath('//*[@id="DF650000161_status_operational"]/option[2]')
created.click()

# creating list of carriers to be checked
carriers = ['VTT','KHN','JDR','GAI','COI','BAR','SAF','BIE','TRA','FLE']

# symbols for carriers
# VTT for Versteijnen
# KHN for Kuhne
# JDR for Jan de Rijk
# GAI for Gailing
# COI for Convoi
# BAR for Barbieri
# SAF or Safewatcher
# BIE for Biencinto
# TRA for Transcarson
# FLE for 	Flegg Projects & Installation Services
pandasfiles = []
for road in carriers:
    logger.info('Program is checking the jobs for {}'.format(road))
    time.sleep(3)
    # select carrier table to chose from
    car = browser.find_element_by_id('go_DF650000161_carrier_id_krt_kontrahent')
    car.click()
    time.sleep(3)
    # switch focus to current window
    x = browser.find_element_by_id('TB_iframeContent')
    browser.switch_to.frame(x)
    time.sleep(1)
    # type in name of the carrier
    name = browser.find_element_by_id('DF230000259_symbol')
    name.send_keys(road)
    time.sleep(1)
    # click search
    # search = browser.find_element_by_id('action[230000259][2123]') update 2019-06-15
    search = browser.find_element_by_id('action[230000259][2136]')
    search.click()
    time.sleep(1)
    # select the carrier
    selection = browser.find_element_by_xpath('//*[@id="DL230000260"]/tbody/tr[2]/td[1]/a')
    selection.click()
    time.sleep(1)
    # click search on a main page
    # search_again = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
    search_again = browser.find_element_by_id('action[650000161][3275]')
    search_again.click()
    time.sleep(3)
    try:
    # checking if the file will be available. If not - going to another carrier
        first_row = browser.find_element_by_xpath('//*[@id="DL650000162"]/tbody/tr[2]/td[1]/a')
        # downloaded report from Optilo
        button = browser.find_element_by_link_text("XLS")
        logger.info('file for {} has been downloaded'.format(road))
        button.click()
        time.sleep(10)
        # now we have to adjust the naming of the file
        # going to directory
        os.chdir(folder)
        # going through each filename
        for dirpath, dirnames, filenames in os.walk(os.curdir):
            for naming in filenames:
                # if there is a file without hello in name
                print(naming)
                if 'Multi' in naming:
                    # it corrects the file to the name we need for easier processing
                    os.rename(naming, f'GHOSTS - {road} {today}.xls')
                    pandasfiles.append(r'C:\Users\310295192\Desktop\Python\Projects\GHOSTS\REPORTS\Ghosts {}\GHOSTS - {} {}.xls'.format(today,road,today))
                    break
    except:
         # indicate that no shipment was found
        print("no file for carrier")
        logger.info("No data for carrier {}".format(road))

    # clear field for carrier
    browser.find_element_by_xpath('//*[@id="clear_DF650000161_carrier_id_krt_kontrahent"]/img').click()

mjb_ghosts = []
logger.info('Program will now create the list for jobs to be cancelled')
for panda in pandasfiles:
    df = pd.read_excel(panda)
    try:
        for x in df['Number']:
            mjb_ghosts.append(x)
            print(mjb_ghosts)
    except:
        print('No data to be added')


if len(mjb_ghosts) < 1:
    print("no data to be presented")
    # if there is nothing for deletion - then we exit the procedure
    browser.close()
    exit()
logger.info('mjbs to be cancelled are {}'.format(mjb_ghosts))

browser.close()

browser = webdriver.Chrome()
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

visible=""

for every in mjb_ghosts:
    try:
        logger.info('JOB {} will be cancelled'.format(every))
        #finding multi tab
        # multi = browser.find_element_by_id('menu-258664')
        # multi = browser.find_element_by_id('menu-259381') update 2019-06-15
        # multi = browser.find_element_by_id('menu-1-259756')
        # multi.click()
        # # finding multi job tab
        # # joblist = browser.find_element_by_id('menu-258666')
        # # joblist = browser.find_element_by_id('menu-259383') update 2019-06-15
        # joblist = browser.find_element_by_id('menu-1-259756-259758')
        # joblist.click()
        browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')
        # finding box for job number
        jobnumber = browser.find_element_by_id('DF650000161_number')
        jobnumber.clear()
        # looping through each job number
        jobnumber.send_keys(every)
        time.sleep(3)
        # finding search button
        # searching = browser.find_element_by_id('action[650000161][1529675]')
        # searching = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
        searching = browser.find_element_by_id('action[650000161][3275]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2)
        buttonforjob = browser.find_element_by_link_text(every)
        buttonforjob.click()
        time.sleep(3)


        # find table "job process"
        table = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul')
        # check the number of rows in the table
        rows = len(table.find_elements_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li'))
        # loop through each row of the table
        bt = 0
        for x in range(2, rows):
            checking = table.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(x))
            # checking the text of each field
            value = checking.text
            # if CANCEL is in the field
            if "CANCEL" in value.upper():
                bt = x
        # it assigns the element to variable
        cancellation = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(bt))
        # is clicking the cancel button
        cancellation.click()
        # finds button 950 cancel on next page
        cancel_button = browser.find_element_by_name('action[650000270][3318]')
        # finish the cancellation by clicking the second button
        cancel_button.click()
        logger.info("job {} was cancelled".format(every))
    except:
        print('Something went wrong')
        logger.info('JOB {} was not cancelled. Some issue happened during the process')

browser.close()
if mjb_ghosts:
    for x in mjb_ghosts:
        visible = visible + "<p><b>" + x + "</b></p>" + '\n'


# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
logger.info("Mail has been generated")
# mail.To = 'maciej.janowski@philips.com'
mail.To = 'daniel.ciechanski@philips.com;paulina.szczesniewicz@philips.com;joanna.polak@philips.com;Mariusz.Mikinka@philips.com'
mail.Subject = 'Cancelling GHOSTS - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Would like to inform you GHOSTS have been cancelled</p>'\
                '<p>Full log of procedure in the attachment</p>'\
                '<p>Cancelled GHOSTS:</p>' + visible+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>'
# attaching log file
attachment  = location
mail.Attachments.Add(attachment)
# sending email
mail.Send()