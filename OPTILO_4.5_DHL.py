import datetime
import os
import logging
import win32com.client
import pandas as pd
import time
from selenium import webdriver
import shutil


print(datetime.datetime.now())
# creating logger for actions
logger = logging.getLogger("Load Plans Log")
# setting the level for the logger
logger.setLevel('INFO')
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Trucking_NEW\loggers\DHL Trucking {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of checking sent load plans upload has been started')


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to Optilo folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checking the number of emails to further take this value into the loop
x = len(email)
print(x)
first = x - 50 + 1
file_for_load_plans = ""
for loadplan in range(50):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + loadplan)
    bodyofemail = message.body.upper()
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    time_received = message.ReceivedTime
    date_received = message.ReceivedTime
    reporting_date = int(time_received.strftime("%d"))
    today = int(datetime.datetime.today().strftime('%d'))
    reporting_time = int(time_received.strftime("%H"))
    print(reporting_date,"_______",today)
    load_doc = "Order_Report " + datetime.datetime.today().strftime("%Y-%m-%d")
    # print(load_doc)
    # print(bodyofemail)
    # print("time of email---" + str(reporting_time))
    # checks the if ORDER REPORT in in subject
    if ('ORDER REPORT' in bodyofemail) and (reporting_time == 14) and (reporting_date == today) and (len(message.Attachments) > 0):
        #print(bodyofemail,subjectofemail,reporting)
        print('hello')
        for attach in message.Attachments:
            hawb_attach = attach.FileName
            #attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\' + load_doc + '.csv')
            attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\Python\\Projects\\DHL_Trucking_NEW\\Order_report\\'+ load_doc +'.csv')
            file_for_mjbs = r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\DHL_Trucking_NEW\\Order_report\\'+ load_doc +'.csv'




load_doc = "Trucking Report " + datetime.datetime.today().strftime("%Y-%m-%d")

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 100 + 1
# starts the loop through the emails
for dg in range(100):
    # assigns proper data for mail scrapping
    message = email.Item(first + dg)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    dxreport = 'DX96 Report'
    dxreport = dxreport.upper()
    # checks if we have dg declaration
    if dxreport in subjectofemail and len(message.Attachments) > 0:
        #print(message.SenderEmailAddress.upper())
        # we are logging info about mjb creation
        logger.info('email with Trucking number found')
        for attach in message.Attachments:
            trucking = attach.FileName
            attach.SaveAsFile(
                r'C:\\Users\\310295192\\Desktop\Python\\Projects\\DHL_Trucking_NEW\\Tracking\\' + load_doc + '.csv')
            file_for_trucking = r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\DHL_Trucking_NEW\\Tracking\\' + load_doc + '.csv'

#reading excel
df = pd.read_excel(file_for_mjbs)

# switching format of column
df.Remarks = df.Remarks.astype(str)

# creating filter for trucking numbers
filt = df.Remarks.str[0:2] == '47'

# leaving only filtered data
df = df[filt]

# creating catalog for tracking and DOs
order_catalog = {}
for index, rows in df.iterrows():
    order_official =rows[0]
    order_catalog[order_official] = rows[12]
print(order_catalog)

# reading order report
df_all = pd.read_csv(file_for_trucking,delimiter=';')

# creating data frame with only two columns out of order report
DOandMJB = df_all[['DO','Ref. number 1leg']]

# keeping DO as string with 9 digits
DOandMJB['DO']=DOandMJB['DO'].str[-9:]

# switching the format of DO column
DOandMJB['DO']=DOandMJB.DO.astype(str)

# creating new data frame for vlookup out of initially created dictionary
new_frame = pd.DataFrame(order_catalog.items(),columns=['DO', 'Tracking'])

# adjusting the format of DO
new_frame['DO']=new_frame.DO.astype(str)

# adding column for MJB and using vlookup to find proper MJB
new_frame['MJB']=new_frame['DO'].map(DOandMJB.set_index("DO")["Ref. number 1leg"].to_dict())

# creating a catalog for MJBs
mjb_catalog = {}
for index, rows in new_frame.iterrows():
    mjb_official =rows[2]
    mjb_catalog[mjb_official] = rows[1]
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
        browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')
        # finding box for job number
        jobnumber = browser.find_element_by_id('DF650000161_number')
        jobnumber.clear()
        # looping through each job number
        jobnumber.send_keys(line)
        time.sleep(3)

        searching = browser.find_element_by_name('action[650000161][3339]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2.5)
        buttonforjob = browser.find_element_by_link_text(line)
        buttonforjob.click()
        time.sleep(3)






        # new way of working

        reference = browser.find_element_by_id('DF650000229_carrier_reference1')
        # get attribute from reference number field
        numero = reference.get_attribute('value')
        # if the value is not present
        if len(numero) < 3:
            try:
                editing = browser.find_element_by_name('action[650000229][3306]')
            except:
                editing = browser.find_element_by_id('action[650000229][3243]')
            # time.sleep(1)
            # click edit button
            editing.click()
            time.sleep(1)
            reference.send_keys(car_ref)
            time.sleep(1)
            # save
            try:
                browser.find_element_by_id('action[650000229][3314]').click()
            except:
                browser.find_element_by_id('action[650000229][3315').click()
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

#delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Trucking_NEW\Tracking', ignore_errors=True)

#delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Trucking_NEW\Order_report', ignore_errors=True)

# check if folder is present
os.chdir(r'\Users\310295192\Desktop\Python\Projects\DHL_Trucking_NEW')
# if not - created folder for graphs
if not os.path.isdir('Tracking'):
    os.mkdir('Tracking')
    os.mkdir('Order_report')