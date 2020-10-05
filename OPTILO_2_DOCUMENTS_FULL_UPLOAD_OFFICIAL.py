import win32com.client
from selenium import webdriver
import time
import os
import shutil
import datetime
import logging
from collections import Counter


# DGD



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
location = r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\Loggers\DG {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of DG Declaration upload has been started')


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(5)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)

# list for mjb numbers
dg_num = []

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
    dgdoc = 'DG documents'
    # dgdoc = 'OUTBOUND, DGD'
    dgdoc = dgdoc.upper()
    # checks if we have dg declaration
    if dgdoc in subjectofemail and len(message.Attachments) > 0:
        #print(message.SenderEmailAddress.upper())
        # we are logging info about mjb creation
        logger.info('dangerous goods declarations email has been detected')
        # we are indicating the subject of the email that was used
        logger.info(f'email: "{subjectofemail}" will be verified as for attachments')
        # now we will check if the document was already downloaded
        for attach in message.Attachments:
            declaration = attach.FileName[0:9]
            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\DG_DECLARATION.txt', 'r')
            # checks the content of the file
            opening = reading.read()
            if declaration not in opening and 'image' not in declaration:
                logger.info(f' Declaration for {declaration} has been detected and will be added')
                # i am closing the file in read mode and opening in append mode
                reading.close()
                # opens overview in appending mode
                appending = open(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\DG_DECLARATION.txt', 'a')
                # i am adding the declaration number
                appending.write(declaration + '\n')
                k = r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded\\' + declaration + '.pdf'
                attach.SaveAsFile(k)
                # now we are logging info that file was downloaded
                logger.info(f'Declaration for ({declaration}) has been dowloaded')
                print(f'Declaration for {declaration} was downloaded')
                #it adds the declaration number to list
                dg_num.append(declaration)
                #closes the file that was in append mode
                appending.close()







# checking if the dg_num list is filled with something. If it is - i goes through procedure, if not - skip to another
if dg_num:
    # list for wrong mjbs
    wrong_dg = []
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
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded')
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print("Current Path: ", dirpath)
        print("Directories: ", dirnames)
        print("Files: ", filenames)

    counter = 0
    #loops through all files that are available
    for every in filenames:
        try:
            line = every[0:9]
            # finding order tab
            # order = browser.find_element_by_id('menu-258839')
            # order = browser.find_element_by_id('menu-259556') update 2019-06-15
            # order = browser.find_element_by_id('menu-1-259789')
            # order.click()
            # # finding order transport tab
            # # ordertrans = browser.find_element_by_id('menu-258796')
            # # ordertrans = browser.find_element_by_id('menu-259513') update 2019-06-15
            # ordertrans = browser.find_element_by_id('menu-1-259789-259883')
            # ordertrans.click()
            # # finding order list tab
            # # orderlist = browser.find_element_by_id('menu-258800')
            # # orderlist = browser.find_element_by_id('menu-259517') update 2019-06-15
            # orderlist = browser.find_element_by_id('menu-1-259789-259883-259887')
            # orderlist.click()
            browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=zamowienie&s=ZamowienieTransportLista')
            # finding box for delivery order number
            jobnumber = browser.find_element_by_id('DF690000217_f_referencja1')
            jobnumber.clear()
            # entering job number
            jobnumber.send_keys(line)
            time.sleep(3)
            # finding search button
            # searching = browser.find_element_by_id('action[690000217][1530404]')
            # searching = browser.find_element_by_id('action[690000217][3971]') update 2019-06-15
            # searching = browser.find_element_by_id('action[690000217][4005]') update on 2019-11-18
            # searching = browser.find_element_by_id('action[690000217][4051]')
            searching = browser.find_element_by_name('action[690000217][4196]')
            searching.click()
            # finding button button and clicking it
            time.sleep(2)
            buttonforjob = browser.find_element_by_xpath('//*[@id="DL690000216"]/tbody/tr[2]/td[4]/a')
            buttonforjob.click()
            time.sleep(3)
            # copy address from tab
            current_address = browser.current_url
            # turn to string
            web_address = str(current_address)
            # replace jobdetails to jobcosts and go the site with costs
            newaddress = web_address.replace('TransportDanePodstawowe', 'TransportPliki')
            # going to new files tab
            browser.get(newaddress)
            time.sleep(3)
            # finding this freaking hidden option to upload
            upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
            # uploading the file
            upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded\{}.pdf'.format(line))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP690000322']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(f"//table[@id='DP690000322']/tbody/tr[{row_count}]/td[5]/select/option[30]")
            time.sleep(6)
            document.click()
            time.sleep(2)
            saving = browser.find_element_by_name('action_dp[690000322][Z][save]')
            saving.click()
            # we are logging information that HAWB for MJB was uploaded successfully
            logger.info(f' File for {line} successfully added to Optilo')
            time.sleep(3)

        except:
            # we are logging information that MJB number was not found in Optilo
            logger.warning(f'({line}) was not found in Optilo')
            dg_num.remove(line)
            wrong_dg.append(line)

    # we are logging summary info for the upload of files
    logger.info(f'DG declarations upload has been acomplished. Successful uploads: {len(dg_num)}. Unsucessful uploads: {len(wrong_dg)}')
    # delete the folders from place where files are managed and create them again
    shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded', ignore_errors=True)
    # adapting the current path to Panalpina HAWB folder with downloaded documents
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\DG_DECLARATION')
    # if folder is not present - it creates it
    if not os.path.isdir('downloaded'):
        os.mkdir('downloaded')


    # creating string for correct and wrong mjbs
    correct = "Correctly uploaded DG declarations for Order numbers:\n"
    wrong = "Files not uploaded  because of lack of Order number in Optilo:\n"
    if len(dg_num)!= 0  or len(wrong_dg) != 0:
        # looping through correct mjbs
        for x in dg_num:
            correct = correct + "<p><b>"+ x +"</b></p>"+ '\n'

        # looping through wrong mjbs
        for x in wrong_dg:
            wrong = wrong + "<p><b>"+x+"</b></p>"+ '\n'

    # preparing email for what has been added and what was wrong
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'DL_PCTPolandOptilo@philips.com'
    # mail.To = 'maciej.janowski@philips.com'
    mail.Subject = 'DG Declaration - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded DG Declarations</p>'\
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







# SWB Kuhne+Nagel


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)


# creating logger
logger = logging.getLogger("K+N log")
# setting up the level of logger
logger.setLevel("INFO")
# setting up today date
today = datetime.datetime.today().strftime('%Y-%m-%d')
# setting up the format for logger
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# set the location for the logger
location = r'C:\Users\310295192\Desktop\Python\Projects\BL\Loggers\KN {}.log'.format(today)
# creating logger under location
file_handler = logging.FileHandler(location)
# assigning the proper format for the file
file_handler.setFormatter(formatter)
# combining the logger with formatter
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of SWB upload has been started')










# list for mjb numbers
mjb_num = []

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 600 + 1
# starts the loop through the emails
for hawb in range(600):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + hawb)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    # checks the MJB number in subject
    if "MJB" in subjectofemail:
        if "FINAL" in bodyofemail.upper() and 'SWB' in bodyofemail.upper():
            # print(message.SenderEmailAddress.upper())
            # checkes if it is incoming from Panalpina
            if "KUEHNE-NAGEL" in sendermail:
                # looks for MJB in subject
                mjb_index = subjectofemail.find("MJB")
                # extracts the MJB number from subject
                mjb = subjectofemail[mjb_index:mjb_index+10]

                # # second menthod of extracting MJB number
                # # finding index for MJB
                # mjb_index = subjectofemail.find('MJB')
                # # extracting everything after MJB
                # extract_mjb = subjectofemail[mjb_index:]
                # # looking for first slashes after MJB indication
                # slash = extract_mjb.find('//')
                # # extracting the value from MJB to slashes and replacing spaces with empty places
                # mjb = extract_mjb[:slash].replace(" ", "")[:10]
                print(mjb)
                # we are logging info about mjb creation
                logger.info(f'({mjb}) - indicated number has been created')
                # we are indicating the subject of the email that was used
                logger.info(f'email: "{subjectofemail}" has been used for {mjb}')
                #opens the file for checking if MJB was already extracted
                reading = open(r'C:\Users\310295192\Desktop\Python\Projects\BL\BL.txt', 'r')
                # checks the content of the file
                opening = reading.read()
                #checks if mjb is already added in the list
                if mjb not in opening:
                    # we are logging info that number was not on list and program will upload the document
                    logger.info(f'{mjb} number is not on the list and SWB will be checked for presence')
                    print("nie ma takiej wartości")
                    reading.close()
                    # opens overview in appending mode
                    appending = open(r'C:\Users\310295192\Desktop\Python\Projects\BL\BL.txt', 'a')
                    # is adding mjb to file
                    appending.write(mjb + '\n')
                    # and it downloads the file to respective folder
                    for attach in message.Attachments:
                        # hawb_attach = attach.FileName
                        # if "AWB" in hawb_attach.upper() and "AMEND" not in bodyofemail.upper():
                        attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\BL\\downloaded\\' + mjb + '.pdf')
                        # now we are logging info that file was downloaded
                        logger.info(f'SWB for ({mjb}) has been dowloaded')
                        # it adds the MJB number to list
                        mjb_num.append(mjb)
                        # closes the file that was in append mode
                        appending.close()
                    # else:
                    #     logger.info(f'File is not the HAWB in the email for "{mjb}"')
                    #     logger.info(f'Name of the file is {hawb_attach}')




        else:
            pass


# checking if list is filled in. If not - skip to another section of program
if mjb_num:
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
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\BL\downloaded')
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
            # searching = browser.find_element_by_id('action[650000161][3269]') updated on 2019-11-18
            # searching = browser.find_element_by_id('action[650000161][3275]')
            searching = browser.find_element_by_name('action[650000161][3367]')
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
            upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\BL\downloaded\{}.pdf'.format(line))
            time.sleep(9)
            # counting number of columns
            # finding number of rows in table with documents
            row_count_po = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            for rowing in range(2, row_count_po + 1):
                # finding documents names
                document = browser.find_element_by_xpath('//table[@id="DP650000192"]/tbody/tr[{}]/td[2]'.format(rowing)).text
                # if names match - select proper document type
                if document[0:10] == line:
                    # selectiong document
                    sel_doc = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{rowing}]/td[5]/select/option[52]")
                    time.sleep(2)
                    # clicking document
                    sel_doc.click()
            time.sleep(2)
            saving = browser.find_element_by_name('action_dp[650000192][Z][save]')
            saving.click()
            # we are logging information that BL for MJB was uploaded successfully
            logger.info(f' File for {line} successfully added to Optilo')
            time.sleep(3)
        except:
            # we are logging information that MJB number was not found in Optilo
            logger.warning(f'({line}) was not found in Optilo')
            print("wrong MJB number")
            mjb_num.remove(line)
            wrong_mjb.append(line)


    # we are logging summary info for the upload of files
    logger.info(f'SWB upload has been acomplished. Successful uploads: {len(mjb_num)}. Unsucessful uploads: {len(wrong_mjb)}')
    # delete the folders from place where files are managed and create them again
    shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\BL\downloaded', ignore_errors=True)
    # adapting the current path to BL folder with downloaded documents
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\BL')
    # if folder is not present - it creates it
    if not os.path.isdir('downloaded'):
        os.mkdir('downloaded')

    # creating string for correct and wrong mjbs
    correct = "Correctly uploaded SWBs for:\n"
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
    mail.Subject = 'Kuehne+Nagel Sea Waybill (SWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents provided by Kuehne+Nagel</p>'\
                    '<p>Full log of upload in the attachment</p>'\
                    +correct + wrong+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                    '<p>PCT Poland</p>'
    # attaching log file
    attachment  = location
    mail.Attachments.Add(attachment)
    # sending email
    mail.Send()

    #closing browser
    browser.close()










# HAWB CEVA

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







# checking if there is something to be uploaded. If not - going to next carrier
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
            # searching = browser.find_element_by_id('action[650000161][3269]') updated on 2019-11-18
            # searching = browser.find_element_by_id('action[650000161][3275]')
            searching = browser.find_element_by_name('action[650000161][3367]')
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
            document = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[24]")
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


# HAWB Expeditors

# creating logger for actions
logger = logging.getLogger("EXPEDITORS Log")
# setting the level for the logger
logger.setLevel('INFO')
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\Expeditors\Expeditors {}.log'.format(today)
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
    prealert = 'AMS-Export-CSSV'
    prealert = prealert.upper()
    add1 = 'wattimena'
    add1 = add1.upper()
    # checks the MJB number in sender data
    if (prealert in sendermail or add1 in sendermail)  and len(message.Attachments) > 0:
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
            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Expeditors.txt', 'r')
            # checks the content of the file
            opening = reading.read()
            # #checks if mjb is already added in the list
            if mjb not in opening:
                # we are logging info that number was not on list and program will upload the document
                logger.info(f'{mjb} number is not on the list and HAWB will be checked for presence')
                print("nie ma takiej wartości")
                reading.close()
                # opens overview in appending mode
                appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Expeditors.txt', 'a')
                # is adding mjb to file
                appending.write(mjb + '\n')
                # and it downloads the file to respective folder
                for attach in message.Attachments:
                    hawb_attach = attach.FileName
                    # if 'HAWB' in bodyofemail.upper():
                    if "BILL" in hawb_attach.upper():
                        attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Expeditors\\' + mjb + '.pdf')
                        # now we are logging info that file was downloaded
                        logger.info(f'HAWB for ({mjb}) has been dowloaded')
                        # it adds the MJB number to list
                        mjb_num.append(mjb)
                        # closes the file that was in append mode
                        appending.close()
                    else:
                        logger.info(f'File is not the HAWB in the email for "{mjb}')
                        logger.info(f'Name of the file is {hawb_attach}')







# checking if there is something to be uploaded. If not - going to next carrier
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
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Expeditors')
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
            # searching = browser.find_element_by_id('action[650000161][3269]') updated on 2019-11-18
            # searching = browser.find_element_by_id('action[650000161][3275]')
            searching = browser.find_element_by_name('action[650000161][3367]')
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
            upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Expeditors\{}.pdf'.format(line))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[24]")
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
    shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Expeditors', ignore_errors=True)
    # adapting the current path to Panalpina HAWB folder with downloaded documents
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
    # if folder is not present - it creates it
    if not os.path.isdir('Expeditors'):
        os.mkdir('Expeditors')


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
    mail.Subject = 'Expeditors House Air Waybill (HAWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents for Expeditors </p>'\
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




# HAWB Nippon

# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)

# creating logger
logger = logging.getLogger('Nippon Log')
# setting the level of the logger
logger.setLevel("INFO")
# setting the date for the logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logger
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location for the file
location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\Nippon\Nippon {}.log'.format(today)
# setting up the feature for location of the file
file_handler = logging.FileHandler(location)
# indicating the set format for logs
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of HAWB upload has been started')


# list for mjb numbers
mjb_num = []

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 600 + 1
# starts the loop through the emails
for hawb in range(600):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + hawb)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    # checks the MJB number in subject
    if "NEEUR" in sendermail and len(message.Attachments) > 0:
        # print(message.SenderEmailAddress.upper())
        # checkes if it is incoming from Panalpina
        # if "MJB" in subjectofemail:
        #     # looks for MJB in subject
        #     mjb_index = subjectofemail.find("MJB")
        #     # extracts the MJB number from subject
        #     mjb = "MJB" + subjectofemail[-7:]
        #     print(mjb)
        #     # we are logging info about mjb creation
        #     logger.info(f'({mjb}) - indicated number has been created')
        #     # we are indicating the subject of the email that was used
        #     logger.info(f'email: "{subjectofemail}" has been used for {mjb}')
        #     #opens the file for checking if MJB was already extracted
        #     reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'r')
        #     # checks the content of the file
        #     opening = reading.read()
        #     #checks if mjb is already added in the list
        #     if mjb not in opening:
        #         # we are logging info that number was not on list and program will upload the document
        #         logger.info(f'{mjb} number is not on the list and HAWB will be added')
        #         print("nie ma takiej wartości")
        #         reading.close()
        #         # opens overview in appending mode
        #         appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'a')
        #         # is adding mjb to file
        #         appending.write(mjb + '\n')
        #         # and it downloads the file to respective folder
        #         for attach in message.Attachments:
        #             hawb_attach = attach.FileName
        #             if "NEN" in hawb_attach.upper():
        #                 attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
        #                 # now we are logging info that file was downloaded
        #                 logger.info(f'HAWB for ({mjb}) has been dowloaded')
        #                 # it adds the MJB number to list
        #                 mjb_num.append(mjb)
        #                 # closes the file that was in append mode
        #                 appending.close()

# TURNING OFF THE OPTION AND GOING WITH NEW

        # if we have MJB in the body of the email
        # if "MJB" in bodyofemail and "D/I" in subjectofemail and len(message.Attachments) > 0:
        #     # Then it is looking for MJB in body
        #     mjb_index = bodyofemail.find("MJB")
        #     # extracts the MJB number from subject
        #     mjb = bodyofemail[mjb_index:mjb_index + 10]
        #     print(mjb)
        #     # we are logging info about mjb creation
        #     logger.info(f'({mjb}) - indicated number has been created')
        #     # we are indicating the subject of the email that was used
        #     logger.info(f'email: "{subjectofemail}" has been used for creating {mjb}')
        #     # opens the file for checking if MJB was already extracted
        #     reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'r')
        #     # # checks the content of the file
        #     opening = reading.read()
        #     # #checks if mjb is already added in the list
        #     if mjb not in opening:
        #         # we are logging info that number was not on list and program will upload the document
        #         logger.info(f'{mjb} number is not on the list and HAWB will be checked for presence')
        #         print("nie ma takiej wartości")
        #         reading.close()
        #         # opens overview in appending mode
        #         appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'a')
        #         # is adding mjb to file
        #         appending.write(mjb + '\n')
        #         # and it downloads the file to respective folder
        #         for attach in message.Attachments:
        #             hawb_attach = attach.FileName
        #             # if "NEN" in hawb_attach.upper():
        #             if "D/I" in subjectofemail:
        #                 print(subjectofemail)
        #                 attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
        #                 # now we are logging info that file was downloaded
        #                 logger.info(f'HAWB for ({mjb}) has been dowloaded')
        #                 # it adds the MJB number to list
        #                 mjb_num.append(mjb)
        #                 # closes the file that was in append mode
        #                 appending.close()
        #             else:
        #                 logger.info(f'File is not the HAWB in the email for "{mjb}')
        #                 logger.info(f'Name of the file is {hawb_attach}')


        if ("MJB" in bodyofemail and "D/I" in subjectofemail and len(message.Attachments) > 0) \
            or ("MJB" in subjectofemail and "PRE-ALERT" in subjectofemail and "D/I" not in subjectofemail and len(message.Attachments) > 0):
            # Then it is looking for MJB in body
            mjb_index = bodyofemail.find("MJB")
            # extracts the MJB number from subject
            mjb = bodyofemail[mjb_index:mjb_index + 10]


            # additional procedure to get HAWB from PRE-ALERT
            if mjb_index < 10:
              mjb_index = subjectofemail.find("MJB")
              # extracts the MJB number from subject
              mjb = subjectofemail[mjb_index:mjb_index + 10]

            print(mjb)
            # we are logging info about mjb creation
            logger.info(f'({mjb}) - indicated number has been created')
            # we are indicating the subject of the email that was used
            logger.info(f'email: "{subjectofemail}" has been used for creating {mjb}')
            # opens the file for checking if MJB was already extracted
            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'r')
            # # checks the content of the file
            opening = reading.read()
            # #checks if mjb is already added in the list
            if mjb not in opening:
                # we are logging info that number was not on list and program will upload the document
                logger.info(f'{mjb} number is not on the list and HAWB will be checked for presence')
                print("nie ma takiej wartości")
                reading.close()
                # opens overview in appending mode
                appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'a')
                # is adding mjb to file
                appending.write(mjb + '\n')
                # and it downloads the file to respective folder
                for attach in message.Attachments:

                  if len(message.Attachments) == 1:

                      hawb_attach = attach.FileName
                      # if "NEN" in hawb_attach.upper():
                      if "D/I" in subjectofemail:
                          print(subjectofemail)
                          attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
                          # now we are logging info that file was downloaded
                          logger.info(f'HAWB for ({mjb}) has been dowloaded')
                          # it adds the MJB number to list
                          mjb_num.append(mjb)
                          # closes the file that was in append mode
                          appending.close()
                      else:
                          logger.info(f'File is not the HAWB in the email for "{mjb}')
                          logger.info(f'Name of the file is {hawb_attach}')

                  if len(message.Attachments) > 1:

                      hawb_attach = attach.FileName
                      if "NEN" in hawb_attach.upper():
                          if "ALERT" in subjectofemail:
                              print(subjectofemail)
                              attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
                              # now we are logging info that file was downloaded
                              logger.info(f'HAWB for ({mjb}) has been dowloaded')
                              # it adds the MJB number to list
                              mjb_num.append(mjb)
                              # closes the file that was in append mode
                              appending.close()
                          else:
                              logger.info(f'File is not the HAWB in the email for "{mjb}')
                              logger.info(f'Name of the file is {hawb_attach}')










# checking if there is something to be uploaded. If not - going to next carrier
if mjb_num:
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
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Nippon')
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
            # searching = browser.find_element_by_id('action[650000161][3269]') updated on 2019-11-18
            # searching = browser.find_element_by_id('action[650000161][3275]')
            searching = browser.find_element_by_name('action[650000161][3367]')
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
            upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Nippon\{}.pdf'.format(line))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[24]")
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
    shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Nippon', ignore_errors=True)
    # adapting the current path to Panalpina HAWB folder with downloaded documents
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
    # if folder is not present - it creates it
    if not os.path.isdir('Nippon'):
        os.mkdir('Nippon')

    # now we are checking duplicated mjbs for last 1000 emails

    # list for duplicated mjbs
    duplicate_mjb = []

    # sort all emails that we have in the folder
    first = x - 1000 + 1
    # starts the loop through the emails
    for hawb in range(1000):
        # checks the number of email after sorting and extract data on it
        message = email.Item(first + hawb)
        bodyofemail = message.body
        sendermail = message.SenderEmailAddress.upper()
        subjectofemail = message.subject.upper()
        # checks the MJB number in subject
        if "NEEUR" in sendermail and len(message.Attachments) > 0:

            # if we have MJB in the body of the email
            if "MJB" in bodyofemail and "DISPATCH" in subjectofemail and len(message.Attachments) > 0:
                # Then it is looking for MJB in body
                mjb_index = bodyofemail.find("MJB")
                # extracts the MJB number from subject
                mjb = bodyofemail[mjb_index:mjb_index + 10]

                duplicate_mjb.append(mjb)
    occur = Counter(duplicate_mjb)
    print(occur)
    cur_day = str(datetime.datetime.today().strftime("%Y-%m-%d"))
    duplicates = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\duplicates\Nippon duplicates {}.txt'.format(cur_day)
    with open(duplicates,"a") as file:
        for x,y in occur.items():
            if y > 1:
                file.write(x+'\n')



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
    mail.Subject = 'Nippon House Air Waybill (HAWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents for Nippon</p>'\
                    '<p>Full log of upload in the attachment</p>'\
                    '<p>Second file shows mjb numbers where email on HAWB was sent 2 times. Scope: last 1000 emails</p>'\
                    +correct + wrong+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                    '<p>PCT Poland</p>'
    # attaching log file
    attachment  = location
    mail.Attachments.Add(attachment)
    mail.Attachments.Add(duplicates)
    # sending email
    mail.Send()

    browser.close()



# HAWB Panalpina

# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)


# creating logger
logger = logging.getLogger("Panalpina Log")
# setting up the level of logger
logger.setLevel("INFO")
# setting up today date
today = datetime.datetime.today().strftime('%Y-%m-%d')
# setting up the format for logger
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# set the location for the logger
location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\Panalpina\Panalpina {}.log'.format(today)
# creating logger under location
file_handler = logging.FileHandler(location)
# assigning the proper format for the file
file_handler.setFormatter(formatter)
# combining the logger with formatter
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of HAWB upload has been started')


# list for mjb numbers
mjb_num = []

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 600 + 1
# starts the loop through the emails
for hawb in range(600):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + hawb)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    # checks the MJB number in subject
    if "MJB" in subjectofemail:
        # print(message.SenderEmailAddress.upper())
        # checkes if it is incoming from Panalpina
        if "PANALPINA" in sendermail or "NL.DSV" in sendermail:
            # looks for MJB in subject
            mjb_index = subjectofemail.find("MJB")
            # extracts the MJB number from subject
            mjb = subjectofemail[mjb_index:mjb_index+10]

            # # second menthod of extracting MJB number
            # # finding index for MJB
            # mjb_index = subjectofemail.find('MJB')
            # # extracting everything after MJB
            # extract_mjb = subjectofemail[mjb_index:]
            # # looking for first slashes after MJB indication
            # slash = extract_mjb.find('//')
            # # extracting the value from MJB to slashes and replacing spaces with empty places
            # mjb = extract_mjb[:slash].replace(" ", "")[:10]
            print(mjb)
            # we are logging info about mjb creation
            logger.info(f'({mjb}) - indicated number has been created')
            # we are indicating the subject of the email that was used
            logger.info(f'email: "{subjectofemail}" has been used for {mjb}')
            #opens the file for checking if MJB was already extracted
            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Panalpina.txt', 'r')
            # checks the content of the file
            opening = reading.read()
            #checks if mjb is already added in the list
            if mjb not in opening:
                # we are logging info that number was not on list and program will upload the document
                logger.info(f'{mjb} number is not on the list and HAWB will be checked for presence')
                print("nie ma takiej wartości")
                reading.close()
                # opens overview in appending mode
                appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Panalpina.txt', 'a')
                # is adding mjb to file
                appending.write(mjb + '\n')
                # and it downloads the file to respective folder
                for attach in message.Attachments:
                    hawb_attach = attach.FileName
                    if "AWB" in hawb_attach.upper() and "AMEND" not in bodyofemail.upper():
                        attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Panalpina\\' + mjb + '.pdf')
                        # now we are logging info that file was downloaded
                        logger.info(f'HAWB for ({mjb}) has been dowloaded')
                        # it adds the MJB number to list
                        mjb_num.append(mjb)
                        # closes the file that was in append mode
                        appending.close()
                    else:
                        logger.info(f'File is not the HAWB in the email for "{mjb}"')
                        logger.info(f'Name of the file is {hawb_attach}')




        else:
            pass

# checking if there is something to be uploaded. If not - terminating the program
if mjb_num:
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
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Panalpina')
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
            # searching = browser.find_element_by_id('action[650000161][3269]') updated on 2019-11-18
            # searching = browser.find_element_by_id('action[650000161][3275]')
            searching = browser.find_element_by_name('action[650000161][3367]')
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
            upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Panalpina\{}.pdf'.format(line))
            time.sleep(9)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[24]")
            time.sleep(4)
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
    shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Panalpina', ignore_errors=True)
    # adapting the current path to Panalpina HAWB folder with downloaded documents
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
    # if folder is not present - it creates it
    if not os.path.isdir('Panalpina'):
        os.mkdir('Panalpina')

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
    mail.Subject = 'DSV House Air Waybill (HAWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents for DSV</p>'\
                    '<p>Full log of upload in the attachment</p>'\
                    +correct + wrong+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                    '<p>PCT Poland</p>'
    # attaching log file
    attachment  = location
    mail.Attachments.Add(attachment)
    # sending email
    mail.Send()

    #closing browser
    browser.close()