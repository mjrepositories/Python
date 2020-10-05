from selenium import webdriver
import time
import os
import pandas as pd
import logging
import datetime
import win32com.client

# creating a logger for the dq documents
# creating logger for actions
logger = logging.getLogger("DHL_TRACKING Log")
# setting the level for the logger
logger.setLevel("INFO")
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the  file
location = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Tracking\Loggers\DHL Tracking {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure for checking DHL tracking numbers has been started')



import numpy as np
# setting up chrome options and default folder for download
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\Users\310295192\Desktop\Python\Projects\DHL_Tracking\Tracking"}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=chromeOptions)

import datetime
# getting to the DHL page
logger.info("Entering DHL webpage")
browser.get('https://proview.dhl.com/proview/login')


# typing in the login details and submitting the details
browser.find_element_by_name('j_username').send_keys('Philipsmed')
browser.find_element_by_name('j_password').send_keys('Philips!19')
browser.find_element_by_class_name('buttonSubmit').click()

time.sleep(3)
# finding the total shipments
p = '/html/body/table[2]/tbody/tr/td[2]/div/div/div[4]/table[2]/tbody/tr[11]/td[3]/div/span/a'
# and clicking the value
browser.find_element_by_xpath(p).click()

# getting reference data as "shipped"
browser.find_element_by_xpath(r'//*[@id="filter"]/option[4]').click()

# checking the name of the today
checking_date = datetime.datetime.today().strftime("%A")

# if it is not monday it takes one day before
if not checking_date == 'Monday':
    datum = datetime.datetime.today() - datetime.timedelta(1)
    datum = datum.strftime('%m/%d/%Y')
# if it is monday it takes three days before
else:
    datum = datetime.datetime.today() - datetime.timedelta(3)
    datum = datum.strftime('%m/%d/%Y')




# getting the right dates for "date from" and "date to"

browser.find_element_by_id('filtervalue').send_keys(datum)
time.sleep(1)
browser.find_element_by_id('toDate').send_keys(datum)




# browser.find_element_by_id('filtervalue').send_keys(datum)
# time.sleep(1)
# browser.find_element_by_id('toDate').send_keys(datum)
time.sleep(2)
# click "find" option
browser.find_element_by_xpath('//*[@id="searchForm"]/table/tbody/tr/td[12]/div/a').click()
time.sleep(2)
# downloading the report
try:
    browser.find_element_by_xpath('//*[@id="exportTypes"]/a/span').click()

    time.sleep(3)
    logger.info("File with data has been downloaded")
    # setting up again date
    datum = datetime.datetime.today() - datetime.timedelta(1)
    datum = datum.strftime('%d-%m-%Y')

    # checking the name of the today
    # checking_date = datetime.datetime.today().strftime("%A")
    #
    # # if it is not monday it takes one day before
    # if not checking_date == 'Monday':
    #     datum = datetime.datetime.today() - datetime.timedelta(1)
    #     datum = datum.strftime('%m/%d/%Y')
    # # if it is monday it takes three days before
    # else:
    #     datum = datetime.datetime.today() - datetime.timedelta(3)
    #     datum = datum.strftime('%m/%d/%Y')




    browser.close()

    #going to directory
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Tracking\Tracking')
            # going through each filename
    for dirpath,dirnames,filenames in os.walk(os.curdir):
        for naming in filenames:
            # if there is a file without hello in name
            print(naming)
            if naming[:3] == "Exp":
                # it corrects the file to the name we need for easier processing
                os.rename(naming, f'{datum}_DHL.xls')
                break
    logger.info("Name of the file has been changed")
    # getting to the file
    new_df = pd.read_csv(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Tracking\Tracking\{}_DHL.xls'.format(datum))
    # changing empty values for Shipper Reference to value that won't generate rates
    new_df['Shipper Reference'].fillna('NOREFERENCENUMBER', inplace=True)
    # creating mjb catalog
    mjb_catalog = {}
    for index, rows in new_df.iterrows():
        mjb = new_df.iloc[index,4]
        found_mjb = mjb.upper().find('MJB')
        if found_mjb >= 0:
            mjb_official = mjb.upper()[found_mjb:found_mjb+10]
            mjb_catalog[mjb_official] = str(new_df.iloc[index, 1])
    print(mjb_catalog)
    logger.info(f'List of indicated mjbs has been generated and trucking numbers will be added {mjb_catalog}')
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
    # created list for mjbs checked
    DHL_ADDED = []
    #loops through all DHL reference numbers
    for mjb_no,car_ref in mjb_catalog.items():
        try:
            line = mjb_no[0:10]
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
            # finding box for job number
            jobnumber = browser.find_element_by_id('DF650000161_number')
            jobnumber.clear()
            # looping through each job number
            jobnumber.send_keys(line)
            time.sleep(3)
            # finding search button
            # searching = browser.find_element_by_id('action[650000161][1529675]')
            # searching = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
            # searching = browser.find_element_by_id('action[650000161][3275]')
            searching = browser.find_element_by_name('action[650000161][3311]')
            searching.click()
            # finding button button and clicking it
            time.sleep(2.5)
            buttonforjob = browser.find_element_by_link_text(line)
            buttonforjob.click()
            time.sleep(3)

            # # find reference number
            # reference = browser.find_element_by_id('DF650000229_carrier_reference1')
            # # get attribute from reference number field
            # numero = reference.get_attribute('value')
            # # if the value is not present
            # if len(numero) < 3:
            #     # edit mjb details
            #     ref = "action[650000229][3215]"
            #     edit_button = browser.find_element_by_id(ref)
            #     edit_button.click()
            #     time.sleep(2)
            #     # send the details regarding carrier reference number
            #     reference = browser.find_element_by_id('DF650000229_carrier_reference1')
            #     reference.send_keys(car_ref)
            #     time.sleep(2)
            #     # save
            #     browser.find_element_by_id('action[650000229][3221]').click()
            #     logger.info(f'For {mjb_no} reference number {car_ref} has been added')

           # had to change the methodology after update on 2019-06-15







            # switching the procedure

            # # find edit button
            # try:
            #     editing = browser.find_element_by_id('action[650000229][3242]')
            # except:
            #     editing = browser.find_element_by_id('action[650000229][3243]')
            # #editing = browser.find_element_by_xpath('//*[@id="action[650000229][3243]"]')
            # print("Edit found")
            # time.sleep(1)
            # # click edit button
            # editing.click()
            # time.sleep(1)
            # reference = browser.find_element_by_id('DF650000229_carrier_reference1')
            # # get attribute from reference number field
            # numero = reference.get_attribute('value')
            # # if the value is not present
            # if len(numero) < 3:
            #     time.sleep(1)
            #     # send the details regarding carrier reference number
            #     reference = browser.find_element_by_id('DF650000229_carrier_reference1')
            #     reference.send_keys(car_ref)
            #     time.sleep(2)
            #     # save
            #     try:
            #         browser.find_element_by_id('action[650000229][3250]').click()
            #     except:
            #         browser.find_element_by_id('action[650000229][3249]').click()
            #     logger.info(f'For {mjb_no} reference number {car_ref} has been added')
            #     DHL_ADDED.append(mjb_no)
            # # else:
            # #     browser.find_element_by_id('action[650000229][3243]').click()











            # new way of working

            reference = browser.find_element_by_id('DF650000229_carrier_reference1')
            # get attribute from reference number field
            numero = reference.get_attribute('value')
            # if the value is not present
            if len(numero) < 3:
                try:
                    editing = browser.find_element_by_name('action[650000229][3280]')
                except:
                    editing = browser.find_element_by_id('action[650000229][3243]')
                # time.sleep(1)
                # click edit button
                editing.click()
                time.sleep(1)
                # finding reference number
                reference = browser.find_element_by_id('DF650000229_carrier_reference1')
                reference.send_keys(car_ref)
                time.sleep(1)
                # save
                try:
                    browser.find_element_by_id('action[650000229][3290]').click()
                except:
                    browser.find_element_by_id('action[650000229][3249]').click()
                logger.info(f'For {mjb_no} reference number {car_ref} has been added')
                DHL_ADDED.append(mjb_no)

        except:
            # browser.close()
            pass


    browser.close()
    visible = ""
    for x in DHL_ADDED:
        visible = visible + "<p><b>" + x + "</b></p>" + '\n'


    # preparing email for what has been added and what was wrong
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    logger.info("Mail has been generated")
    mail.To = 'DL_PCTPolandOptilo@philips.com'
    # mail.To = 'maciej.janowski@philips.com'
    mail.Subject = 'DHL reference numbers - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Would like to inform you that reference numbers are checked</p>'\
                    '<p>Full log of procedure in the attachment</p>'\
                    '<p>Reference numbers added for:</p>' + visible+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                    '<p>PCT Poland</p>'
    # attaching log file
    attachment  = location
    mail.Attachments.Add(attachment)
    # sending email
    mail.Send()
except:
    print("No report is available for {}".format(datum))

    # preparing email for what has been added and what was wrong
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'DL_PCTPolandOptilo@philips.com'
    # mail.To = 'maciej.janowski@philips.com'
    mail.Subject = 'DHL reference numbers - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p>' \
                    '<p>Would like to inform you that reference numbers are checked and nothing was found</p>' \
                    '<p>Cheers,</p><p>Maciej Janowski</p>' \
                                        '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                                            '<p>PCT Poland</p>'
    # attaching log file
    attachment = location
    mail.Attachments.Add(attachment)
    # sending email
    mail.Send()
    browser.close()


'''
# getting only that starts with 081 or 81
df = df[(df['Shipper Reference'].str[0:3] =='081')|(df['Shipper Reference'].str[0:2] =='81')]

# creating a dictionary with delivery order numbers and waybill info
delivery_catalog = dict(zip(df['Shipper Reference'],df['Waybill']))

# empty mjb_catalog dictionary
mjb_catalog ={}

# getting to order list
brower.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=zamowienie&s=ZamowienieTransportLista#')

# finding delivery field
delivery_field = browser.find_element_by_id('DF690000217_f_referencja1')

# sendng delivery number from DHL dataframe
delivery_field.send_keys('81250015')

# finding search button and clicking it
search = browser.find_element_by_name('action[690000217][4096]')
search.click()

# trying to click summary
try:
summary = browser.find_element_by_xpath('//*[@id="DL690000216"]/tbody/tr[2]/td[1]/a')
summary.click()
except:
pass

# switching to frame that popped up
x = browser.find_element_by_id('TB_iframeContent')
browser.switch_to.frame(x)

# finding mjb number
mjb_finding = browser.find_element_by_id('DF100007365_job_1_nr_box')
# assigning mjb number to variable
>>> mjb_finding_number = mjb_finding.text



# adding mjb value based on extraction made from delivery order number
mjb_catalog[mjb_finding_number] = delivery_catalog['81250015']





'''