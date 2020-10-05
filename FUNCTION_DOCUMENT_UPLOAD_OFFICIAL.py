import win32com.client
from selenium import webdriver
import time
import os
import shutil
import datetime
import logging
from collections import Counter

przewoznicy = ["KN","CEVA",'EXPEDITORS','NIPPON','PANALPINA']
# setting up today date
dzis = datetime.datetime.today().strftime('%Y-%m-%d')

def docs_upload(today, carriers):
    for car in carriers:
        # getting to inbox
        folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
        # getting to infodis folder
        subfolder = folder.Folders(7)
        # getting to all emails
        email = subfolder.Items
        # checkiing the number of emails to further take this value into the loop
        x = len(email)
        print(x)

        if car == 'KN':
            log_name = "K+N log"
            location = r'C:\Users\310295192\Desktop\Python\Projects\BL\Loggers\KN {}.log'.format(today)
        elif car == 'CEVA':
            log_name = "CEVA Log"
            location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\CEVA\CEVA {}.log'.format(today)
        elif car == 'EXPEDITORS':
            log_name = "EXPEDITORS Log"
            location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\Expeditors\Expeditors {}.log'.format(today)
        elif car == 'NIPPON':
            log_name = 'Nippon Log'
            location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\Nippon\Nippon {}.log'.format(today)
        elif car == 'PANALPINA':
            log_name = "Panalpina Log"
            location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\Panalpina\Panalpina {}.log'.format(today)

        # creating logger
        logger = logging.getLogger(log_name)
        # setting up the level of logger
        logger.setLevel("INFO")
        # setting up the format for logger
        formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s', '%Y-%m-%d %H:%M:%S')
        # creating logger under location
        file_handler = logging.FileHandler(location)
        # assigning the proper format for the file
        file_handler.setFormatter(formatter)
        # combining the logger with formatter
        logger.addHandler(file_handler)
        # indicating that process is on the way
        logger.info('Procedure of SWB/HAWB upload has been started')

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
            # checks the number of email after sorting and extract data on it
            message = email.Item(first + hawb)
            bodyofemail = message.body
            sendermail = message.SenderEmailAddress.upper()
            subjectofemail = message.subject.upper()
            # if carrier is Kuehne & Nagel
            if car == "K+N":
                # checks the MJB number in subject
                if "MJB" in subjectofemail:
                    if "FINAL" in bodyofemail.upper() and 'SWB' in bodyofemail.upper():
                        # print(message.SenderEmailAddress.upper())
                        # checkes if it is incoming from Panalpina
                        if "KUEHNE-NAGEL" in sendermail:
                            # looks for MJB in subject
                            mjb_index = subjectofemail.find("MJB")
                            # extracts the MJB number from subject
                            mjb = subjectofemail[mjb_index:mjb_index + 10]
                            print(mjb)
                            # we are logging info about mjb creation
                            logger.info(f'({mjb}) - indicated number has been created')
                            # we are indicating the subject of the email that was used
                            logger.info(f'email: "{subjectofemail}" has been used for {mjb}')
                            # opens the file for checking if MJB was already extracted
                            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\BL\BL.txt', 'r')
                            # checks the content of the file
                            opening = reading.read()
                            # checks if mjb is already added in the list
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
                                    attach.SaveAsFile(
                                        r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\BL\\downloaded\\' + mjb + '.pdf')
                                    # now we are logging info that file was downloaded
                                    logger.info(f'SWB for ({mjb}) has been dowloaded')
                                    # it adds the MJB number to list
                                    mjb_num.append(mjb)
                                    # closes the file that was in append mode
                                    appending.close()
                    else:
                        pass

            # if carrier is CEVA
            elif car == "CEVA":
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
                                    attach.SaveAsFile(
                                        r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\CEVA\\' + mjb + '.pdf')
                                    # now we are logging info that file was downloaded
                                    logger.info(f'HAWB for ({mjb}) has been dowloaded')
                                    # it adds the MJB number to list
                                    mjb_num.append(mjb)
                                    # closes the file that was in append mode
                                    appending.close()
                                else:
                                    logger.info(f'File is not the HAWB in the email for "{mjb}')
                                    logger.info(f'Name of the file is {hawb_attach}')


            # if carrier is EXPEDITORS
            elif car == "EXPEDITORS":
                prealert = 'AMS-Export-CSSV'
                prealert = prealert.upper()
                add1 = 'wattimena'
                add1 = add1.upper()
                # checks the MJB number in sender data
                if (prealert in sendermail or add1 in sendermail) and len(message.Attachments) > 0:
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
                                    attach.SaveAsFile(
                                        r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Expeditors\\' + mjb + '.pdf')
                                    # now we are logging info that file was downloaded
                                    logger.info(f'HAWB for ({mjb}) has been dowloaded')
                                    # it adds the MJB number to list
                                    mjb_num.append(mjb)
                                    # closes the file that was in append mode
                                    appending.close()
                                else:
                                    logger.info(f'File is not the HAWB in the email for "{mjb}')
                                    logger.info(f'Name of the file is {hawb_attach}')

            # if carrier is NIPPON
            elif car == "NIPPON":
                # checks the MJB number in subject
                if "NEEUR" in sendermail and len(message.Attachments) > 0:
                    if ("MJB" in bodyofemail and "D/I" in subjectofemail and len(message.Attachments) > 0) \
                            or (
                            "MJB" in subjectofemail and "PRE-ALERT" in subjectofemail and "D/I" not in subjectofemail and len(
                        message.Attachments) > 0):
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
                                        attach.SaveAsFile(
                                            r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
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
                                                attach.SaveAsFile(
                                                    r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
                                                # now we are logging info that file was downloaded
                                                logger.info(f'HAWB for ({mjb}) has been dowloaded')
                                                # it adds the MJB number to list
                                                mjb_num.append(mjb)
                                                # closes the file that was in append mode
                                                appending.close()
                                            else:
                                                logger.info(f'File is not the HAWB in the email for "{mjb}')
                                            logger.info(f'Name of the file is {hawb_attach}')

            # if carrier is PANALPINA
            elif car == "PANALPINA":
                # checks the MJB number in subject
                if "MJB" in subjectofemail:
                    # print(message.SenderEmailAddress.upper())
                    # checkes if it is incoming from Panalpina
                    if "PANALPINA" in sendermail:
                        # looks for MJB in subject
                        mjb_index = subjectofemail.find("MJB")
                        # extracts the MJB number from subject
                        mjb = subjectofemail[mjb_index:mjb_index + 10]
                        print(mjb)
                        # we are logging info about mjb creation
                        logger.info(f'({mjb}) - indicated number has been created')
                        # we are indicating the subject of the email that was used
                        logger.info(f'email: "{subjectofemail}" has been used for {mjb}')
                        # opens the file for checking if MJB was already extracted
                        reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Panalpina.txt', 'r')
                        # checks the content of the file
                        opening = reading.read()
                        # checks if mjb is already added in the list
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
                                    attach.SaveAsFile(
                                        r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Panalpina\\' + mjb + '.pdf')
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

    # checking if list is filled in. If not - skip to another section of program
    if mjb_num:
        # list for wrong mjbs
        wrong_mjb = []
        browser = webdriver.Chrome()
        # getting to Optilo
        browser.get(
            "https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")
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
        if car == "KN":
            os.chdir(r'\Users\310295192\Desktop\Python\Projects\BL\downloaded')
        elif car == 'CEVA':
            os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\CEVA')
        elif car == "EXPEDITORS":
            os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Expeditors')
        elif car == 'NIPPON':
            os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Nippon')
        elif car == 'PANALPINA':
            os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Panalpina')

        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            print("Current Path: ", dirpath)
            print("Directories: ", dirnames)
            print("Files: ", filenames)
        # loops through all files that are available
        for every in filenames:
            try:
                line = every[0:10]
                # finding multi tab
                browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')
                # finding box for job number
                jobnumber = browser.find_element_by_id('DF650000161_number')
                jobnumber.clear()
                # looping through each job number
                jobnumber.send_keys(line)
                time.sleep(3)
                # finding search button
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
                newaddress = web_address.replace('JobDetails', 'JobFiles')
                # going to new files tab
                browser.get(newaddress)
                time.sleep(3)
                # finding this freaking hidden option to upload
                upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
                # uploading the file
                if car == 'KN':
                    upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\BL\downloaded\{}.pdf'.format(line))
                elif car == 'CEVA':
                    upload_file.send_keys(
                        r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\CEVA\{}.pdf'.format(line))
                elif car == "EXPEDITORS":
                    upload_file.send_keys(
                        r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Expeditors\{}.pdf'.format(line))
                elif car == 'NIPPON':
                    upload_file.send_keys(
                        r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Nippon\{}.pdf'.format(line))
                elif car == 'PANALPINA':
                    upload_file.send_keys(
                        r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Panalpina\{}.pdf'.format(line))
                time.sleep(9)
                # counting number of columns
                # finding number of rows in table with documents
                row_count_po = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
                for rowing in range(2, row_count_po + 1):
                    # finding documents names
                    document = browser.find_element_by_xpath(
                        '//table[@id="DP650000192"]/tbody/tr[{}]/td[2]'.format(rowing)).text
                    # if names match - select proper document type
                    if document[0:10] == line:
                        # selectiong document
                        if car == 'KN':
                            sel_doc = browser.find_element_by_xpath(
                                f"//table[@id='DP650000192']/tbody/tr[{rowing}]/td[5]/select/option[50]")
                        else:
                            sel_doc = browser.find_element_by_xpath(
                                f"//table[@id='DP650000192']/tbody/tr[{rowing}]/td[5]/select/option[23]")
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
        logger.info(f'SWB/HAWB upload has been acomplished. Successful uploads: {len(mjb_num)}. Unsucessful uploads: {len(wrong_mjb)}')
        if car == 'KN':
            # delete the folders from place where files are managed and create them again
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\BL\downloaded', ignore_errors=True)
            # adapting the current path to BL folder with downloaded documents
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\BL')
            # if folder is not present - it creates it
            if not os.path.isdir('downloaded'):
                os.mkdir('downloaded')
        elif car == "CEVA":
            # delete the folders from place where files are managed and create them again
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\CEVA', ignore_errors=True)
            # adapting the current path to Panalpina HAWB folder with downloaded documents
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
            # if folder is not present - it creates it
            if not os.path.isdir('CEVA'):
                os.mkdir('CEVA')
        elif car == 'EXPEDITORS':
            # delete the folders from place where files are managed and create them again
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Expeditors', ignore_errors=True)
            # adapting the current path to Panalpina HAWB folder with downloaded documents
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
            # if folder is not present - it creates it
            if not os.path.isdir('Expeditors'):
                os.mkdir('Expeditors')
        elif car == "NIPPON":
            # delete the folders from place where files are managed and create them again
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Nippon', ignore_errors=True)
            # adapting the current path to Panalpina HAWB folder with downloaded documents
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
            # if folder is not present - it creates it
            if not os.path.isdir('Nippon'):
                os.mkdir('Nippon')
        elif car == "PANALPINA":
            # delete the folders from place where files are managed and create them again
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\Panalpina', ignore_errors=True)
            # adapting the current path to Panalpina HAWB folder with downloaded documents
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
            # if folder is not present - it creates it
            if not os.path.isdir('Panalpina'):
                os.mkdir('Panalpina')

        # creating string for correct and wrong mjbs
        correct = "Correctly uploaded SWBs/HAWBs for:\n"
        wrong = "Files not uploaded because of wrong MJB number:\n"
        if len(mjb_num) != 0 or len(wrong_mjb) != 0:
            # looping through correct mjbs
            for x in mjb_num:
                correct = correct + "<p><b>" + x + "</b></p>" + '\n'

            # looping through wrong mjbs
            for x in wrong_mjb:
                wrong = wrong + "<p><b>" + x + "</b></p>" + '\n'

        # preparing email for what has been added and what was wrong
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'DL_PCTPolandOptilo@philips.com'
        # mail.To = 'maciej.janowski@philips.com'
        if car == "KN":
            mail.Subject = 'Kuehne+Nagel Sea Waybill (SWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
        elif car == "CEVA":
            mail.Subject = 'Kuehne+Nagel Sea Waybill (SWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
        elif car == "EXPEDITORS":
            mail.Subject = 'Kuehne+Nagel Sea Waybill (SWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
        elif car == "NIPPON":
            mail.Subject = 'Kuehne+Nagel Sea Waybill (SWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
        elif car == 'PANALPINA':
            mail.Subject = 'Kuehne+Nagel Sea Waybill (SWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
        mail.Body = 'Test'
        mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents provided by {}</p>' \
                        '<p>Full log of upload in the attachment</p>'.format(car) \
                        + correct + wrong + '<p>Cheers,</p><p>Maciej Janowski</p>' \
                                            '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                                            '<p>PCT Poland</p>'
        # attaching log file
        attachment = location
        mail.Attachments.Add(attachment)
        # sending email
        mail.Send()

        # closing browser
        browser.close()


docs_upload(dzis,przewoznicy)

