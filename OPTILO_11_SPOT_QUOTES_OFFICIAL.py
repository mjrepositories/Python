import win32com.client
from selenium import webdriver
import time
# import os
# import shutil
import datetime
import logging
# from collections import Counter
import pandas as pd

# opening file with spot quotes
spot = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\SPOT_QUOTES\SPOT_QUOTES.xlsx')

# selecting only not added
spots_to_add = spot.loc[spot['Added'].isna()]

if spots_to_add.shape[0] > 0:

    # creating string for correct and wrong mjbs
    correct = "Correctly added Spot quotes :\n"

    # creating a list for spot quotes added
    list_of_spots = []

    # creating logger for actions
    logger = logging.getLogger("DG Log")
    # setting the level for the logger
    logger.setLevel("INFO")
    # setting the date for logger
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    # setting up the format for logs
    formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
    # creating the location of the file where logger is stored
    # setting the feature regarding location of the file
    location = r'C:\Users\310295192\Desktop\Python\Projects\SPOT_QUOTES\Loggers\SP {}.log'.format(today)
    file_handler = logging.FileHandler(location)
    # indicating the format that we set
    file_handler.setFormatter(formatter)
    # combining the logger with file
    logger.addHandler(file_handler)
    # indicating that process is on the way
    logger.info('Procedure of  Spot quotes addition has been started')

    browser = webdriver.Chrome()

    browser.get(
        "https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")

    # loggin in
    emailElem = browser.find_element_by_id('inpLogin')
    emailElem.send_keys('maciej.janowski@philips.com')
    # inputting password
    password = browser.find_element_by_id('inpPassword')
    password.send_keys('Maciej0312@')

    # submitting logon details
    buttonlog = browser.find_element_by_id('submitLogin')
    buttonlog.click()

    # looping through the values
    for index, row in spots_to_add.iterrows():
        line = row['MJB_reference_number']
        charge = row['Cost']
        currency = row['Currency']
        print(line,charge,currency)
        correct = correct + "<p><b>" + line + f' {charge} {currency}' + "</b></p>" + '\n'

        browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')
        # finding box for job number
        jobnumber = browser.find_element_by_id('DF650000161_number')
        jobnumber.clear()
        # looping through each job number
        jobnumber.send_keys(line)
        time.sleep(3)
        # finding search button
        # searching = browser.find_element_by_id('action[650000161][1529675]')
        # searching = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
        # searching = browser.find_element_by_id('action[650000161][3269]') updated on 2019-11-18
        searching = browser.find_element_by_id('action[650000161][3275]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2)
        buttonforjob = browser.find_element_by_link_text(line)
        buttonforjob.click()
        time.sleep(3)
        # copy address from tab
        current_address = browser.current_url
        # turn to string
        web_address = str(current_address)
        # replace jobdetails to jobcosts and go the site with costs
        newaddress = web_address.replace('MultiJobDetails', 'MultiJobCosts')
        # going to new files tab
        browser.get(newaddress)
        time.sleep(3)
        row_count = len(browser.find_elements_by_xpath('//table[@id="DG650000281"]/tbody/tr'))

        # click option to add costs
        browser.find_element_by_name('action[650000281][918]').click()

        # add new cost

        browser.find_element_by_name('action[650000281][922]').click()
        time.sleep(3)
        # find quantity field and add 1

        browser.find_element_by_name(f'DG650000281[{row_count-1}][t][ilosc]').send_keys(charge)

        # find unit price field and add 1
        browser.find_element_by_name(f'DG650000281[{row_count-1}][t][plan_wartosc_linii_netto_jednostka]').send_keys(1)

        # find unit of measure and select pce
        row_count = len(browser.find_elements_by_xpath('//table[@id="DG650000281"]/tbody/tr'))
        time.sleep(2)
        uom = browser.find_element_by_xpath(f'//*[@id="DG650000281"]/tbody/tr[{row_count}]/td[5]/select/option[32]')
        uom.click()
        if currency == 'EUR':
            browser.find_element_by_xpath(f'//*[@id="DG650000281"]/tbody/tr[{row_count}]/td[8]/select/option[26]').click()
        elif currency == "USD":
            browser.find_element_by_xpath(f'//*[@id="DG650000281"]/tbody/tr[{row_count}]/td[8]/select/option[69]').click()

        print(row_count)
        #select the cost
        browser.find_element_by_xpath(f'//*[@id="go_DG650000281_{row_count-2}_t_asus_id_fin_asus"]/a').click()
        #browser.find_element_by_xpath(f'//*[@id="go_DG650000281_{row_count}_t_asus_id_fin_asus"]/a/img').click()
        time.sleep(3)
        x = browser.find_element_by_id('TB_iframeContent')
        time.sleep(1)
        browser.switch_to.frame(x)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="DL580000093"]/tbody/tr[46]/td[1]/a').click()
        time.sleep(1)
        # save input
        browser.find_element_by_name('action[650000281][927]').click()
        logger.info(f'cost for {line} has been added. Spot quote: {charge} {currency}')
        list_of_spots.append(line)
    # update that costs were added
    spot['Added'] = "yes"

    # dump data to file
    spot.to_excel(r'C:\Users\310295192\Desktop\Python\Projects\SPOT_QUOTES\SPOT_QUOTES.xlsx',index=False)






    # preparing email for what has been added and what was wrong
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    # mail.To = 'DL_PCTPolandOptilo@philips.com'
    mail.To = 'maciej.janowski@philips.com'
    mail.Subject = 'Spot quotes - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of added spot quotes </p>'\
                    '<p>Full log of upload in the attachment</p>'\
                    +correct +'<p>Cheers,</p><p>Maciej Janowski</p>' \
                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                    '<p>PCT Poland</p>'
    # attaching log file
    attachment = location
    mail.Attachments.Add(attachment)
    # sending email
    mail.Send()

    #closing browser
    browser.close()



''' Examples of MJB for testing

MJB8016167

MJB8014852

MJB8014193'''