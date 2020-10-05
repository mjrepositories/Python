# concept mis to download all reports from today and update them based on last day
import win32com.client
from selenium import webdriver
import time
import os
import shutil
import datetime
import logging

# creating logger for actions
logger = logging.getLogger("CEVA Log")
# setting the level for the logger
logger.setLevel('INFO')
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\CEVA\CEVA {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of HAWB upload has been started')


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)

# list for mjb numbers
mjb_num = []

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 600 + 1
# starts the loop through the emails
for hawb in range(600):
    # assigns proper data for mail scrapping
    message = email.Item(first + hawb)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    prealert = 'prealert@cevalogistics'
    prealert = prealert.upper()
    # checks the MJB number in sender data
    if prealert in sendermail and len(message.Attachments) > 0:
        print(message.SenderEmailAddress.upper())
        # if we have MJB in the body of the email
        if "MJB" in bodyofemail:
            # Then it is looking for MJB in body
            mjb_index = bodyofemail.find("MJB")
            # extracts the MJB number from subject
            mjb = bodyofemail[mjb_index:mjb_index + 10]
            print(mjb)
            # we are logging info about mjb creation
            logger.info(f'({mjb}) - indicated number has been created')
            # we are indicating the subject of the email that was used
            logger.info(f'email: "{subjectofemail}" has been used for {mjb}')
            # opens the file for checking if MJB was already extracted
            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB CEVA.txt', 'r')
            # checks the content of the file
            opening = reading.read()
            # #checks if mjb is already added in the list
            if mjb not in opening:
                # we are logging info that number was not on list and program will upload the document
                logger.info(f'{mjb} number is not on the list and HAWB will be checked for presence')
                print("nie ma takiej wartości")
                reading.close()
                # opens overview in appending mode
                appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB CEVA.txt', 'a')
                # is adding mjb to file
                appending.write(mjb + '\n')
                # and it downloads the file to respective folder
                for attach in message.Attachments:
                    hawb_attach = attach.FileName
                    if "BILL" in hawb_attach.upper():
                        attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\CEVA\\' + mjb + '.pdf')
                        # now we are logging info that file was downloaded
                        logger.info(f'HAWB for ({mjb}) has been dowloaded')
                        # it adds the MJB number to list
                        mjb_num.append(mjb)
                        # closes the file that was in append mode
                        appending.close()
                    else:
                        logger.info(f'File is not the HAWB in the email for "{mjb}')
                        logger.info(f'Name of the file is {hawb_attach}')








if len(mjb_num) > 0:
    # list for wrong mjbs
    wrong_mjb = []
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
    # checking the folder with files available
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\CEVA')
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print("Current Path: ", dirpath)
        print("Directories: ", dirnames)
        print("Files: ", filenames)
    #loops through all files that are available
    for every in filenames:
        try:
            line = every[0:10]
            # finding multi tab
            # multi = browser.find_element_by_id('menu-258664')
            # multi = browser.find_element_by_id('menu-259381') update 2019-06-15
            multi = browser.find_element_by_id('menu-1-259756')
            multi.click()
            # finding multi job tab
            # joblist = browser.find_element_by_id('menu-258666')
            # joblist = browser.find_element_by_id('menu-259383') update 2019-06-15
            joblist = browser.find_element_by_id('menu-1-259756-259758')
            joblist.click()
            # finding box for job number
            jobnumber = browser.find_element_by_id('DF650000161_number')
            jobnumber.clear()
            # looping through each job number
            jobnumber.send_keys(line)
            time.sleep(3)
            # finding search button
            # searching = browser.find_element_by_id('action[650000161][1529675]')
            # searching = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
            searching = browser.find_element_by_id('action[650000161][3268]')
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
            newaddress = web_address.replace('JobDetails', 'JobFiles')
            # going to new files tab
            browser.get(newaddress)
            time.sleep(3)
            # finding this freaking hidden option to upload
            upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
            # uploading the file
            upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\CEVA\{}.pdf'.format(line))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[23]")
            time.sleep(6)
            document.click()
            time.sleep(2)
            saving = browser.find_element_by_name('action_dp[650000192][Z][save]')
            saving.click()
            # we are logging information that HAWB for MJB was uploaded successfully
            logger.info(f' File for {line} successfully added to Optilo')
            time.sleep(3)
        except:
            # we are logging information that MJB number was not found in Optilo
            logger.warning(f'({line}) was not found in Optilo')
            print("wrong MJB number")
            mjb_num.remove(line)
            wrong_mjb.append(line)

# we are logging summary info for the upload of files
logger.info(f'HAWB upload has been acomplished. Successful uploads: {len(mjb_num)}. Unsucessful uploads: {len(wrong_mjb)}')
# delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\CEVA', ignore_errors=True)
# adapting the current path to Panalpina HAWB folder with downloaded documents
os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
# if folder is not present - it creates it
if not os.path.isdir('CEVA'):
    os.mkdir('CEVA')


# creating string for correct and wrong mjbs
correct = "Correctly uploaded HAWBs for:\n"
wrong = "Files not uploaded because of wrong MJB number:\n"
if len(mjb_num)!= 0  or len(wrong_mjb) != 0:
    # looping through correct mjbs
    for x in mjb_num:
        correct = correct + "<p><b>"+ x +"</b></p>"+ '\n'

    # looping through wrong mjbs
    for x in wrong_mjb:
        wrong = wrong + "<p><b>"+x+"</b></p>"+ '\n'

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'DL_PCTPolandOptilo@philips.com'
# mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'CEVA House Air Waybill (HAWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents for CEVA </p>'\
                '<p>Full log of upload in the attachment</p>'\
                +correct + wrong+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>'
# attaching log file
attachment = location
mail.Attachments.Add(attachment)
# sending email
mail.Send()

#closing browser
browser.close()