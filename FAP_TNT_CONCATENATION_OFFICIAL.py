import win32com.client
# from selenium import webdriver
# import time
import os
import shutil
import datetime
import logging
# from collections import Counter
import pandas as pd
print(datetime.datetime.now())

# FAP TNT INVOICES



# creating logger for actions
logger = logging.getLogger("TNT INVOICES Log")
# setting the level for the logger
logger.setLevel("INFO")
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\FAP\Logger\TNT {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of TNT concatenation has been started')

# PREVIOUS VERSION WHEN FOLDER WAS HARD CODEDE
# # getting to freight and audit inbox
# folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# # getting to dq folder
# audit = folder.Folders('Freight Audit and Payment Team (Functional Account)')
# print(audit)
# subfolder = audit.Folders(9)
# print(subfolder)
# # getting to all emails
# email = subfolder.Items
# # checking the number of emails to further take this value into the loop
# x = len(email)
# print(x)





# getting to freight and audit inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# getting to dq folder
audit = folder.Folders('Freight Audit and Payment Team (Functional Account)')
print(audit)

# checking the number of Folders
print(len(audit.Folders))

# assigning number of folders
ranging = len(audit.Folders)+1

# creating a variable for looping
folder_inbox=1
folder_no = 0

# looping over all folders
for x in range(1,ranging):
    # assigning the folder
    subfolder = audit.Folders(x)
    # printing the name of the folder
    print(subfolder)
    # checking if name is Inbox
    if (str(subfolder)=='Inbox'):
        # if it is Inbox - assigning folder to variable
        folder_inbox = audit.Folders(x)
        folder_no = x
# getting to all emails from Inbox
email = folder_inbox.Items
# checking the number of emails to further take this value into the loop
x = len(email)
print(x)













# list for mjb numbers
inv_num = []

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 180 + 1
# starts the loop through the emails
for inv in range(180):
    # assigns proper data for mail scrapping
    message = email.Item(first + inv)
    bodyofemail = message.body.upper()
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    inv_subject = 'TNT Invoice'
    inv_subject = inv_subject.upper()
    bodycheck = 'retrieve via the enclosed link'.upper()
    # checks if we have dg declaration
    if inv_subject in subjectofemail and len(message.Attachments) > 0:
        if bodycheck in bodyofemail:
            #print(message.SenderEmailAddress.upper())
            # we are logging info about mjb creation
            logger.info('TNT invoice email has been detected')
            # we are indicating the subject of the email that was used
            logger.info(f'email: "{subjectofemail}" will be verified as for attachments')
            # now we will check if the document was already downloaded
            for attach in message.Attachments:
                invoice = attach.FileName[-12:-4]
                reading = open(r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_CONCAT.txt', 'r')
                # checks the content of the file
                opening = reading.read()
                if invoice not in opening:
                    logger.info(f' Invoice {invoice} has been detected and will be added')
                    # i am closing the file in read mode and opening in append mode
                    reading.close()
                    # opens overview in appending mode
                    appending = open(r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_CONCAT.txt', 'a')
                    # i am adding the invoice nuber
                    appending.write(invoice + '\n')
                    k = r'C:\Users\310295192\Desktop\Python\Projects\\FAP\INVOICES\\' + invoice + '.csv'
                    attach.SaveAsFile(k)
                    # now we are logging info that file was downloaded
                    logger.info(f'Invoice ({invoice}) has been downloaded')
                    print(f'Invoice {invoice} was downloaded')
                    #it adds the invoice number to list
                    inv_num.append(invoice)
                    #closes the file that was in append mode
                    appending.close()


# PREVIOUS VERSION WHEN FOLDER WAS HARDCODED
# # getting to freight and audit folder (TNT subfolder)
# folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# # getting to dq folder
# audit = folder.Folders('Freight Audit and Payment Team (Functional Account)')
# print(audit)
# subfolder = audit.Folders(9).Folders(9)
# print(subfolder)
# # getting to all emails
# email = subfolder.Items
# # checking the number of emails to further take this value into the loop
# x = len(email)
# print(x)





# getting folders from the inbox
folders_in_inbox = folder_inbox.Folders

# printing the number of folders in inbox
print(len(folders_in_inbox))

# assigning number of folders
ranging = len(folders_in_inbox)+1

# assigning variable for looping
folder_inbox_tnt=1

# looping over all folders
for x in range(1,ranging):
    # assigning the folder
    subfolder = audit.Folders(folder_no).Folders(x)
    # printing the name of the folder
    print(subfolder)
    # checking if name is Inbox
    if (str(subfolder)=='TNT'):
        # if it is Inbox - assigning folder to variable
        folder_inbox_tnt = audit.Folders(folder_no).Folders(x)
        break
# getting to all emails
email = folder_inbox_tnt.Items
# checking the number of emails to further take this value into the loop
x = len(email)
print(x)








# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 180 + 1
# starts the loop through the emails
for inv in range(180):
    # assigns proper data for mail scrapping
    message = email.Item(first + inv)
    bodyofemail = message.body.upper()
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    inv_subject = 'TNT Invoice'
    inv_subject = inv_subject.upper()
    bodycheck = 'retrieve via the enclosed link'.upper()
    # checks if we have dg declaration
    if inv_subject in subjectofemail and len(message.Attachments) > 0:
        if bodycheck in bodyofemail:
            #print(message.SenderEmailAddress.upper())
            # we are logging info about mjb creation
            logger.info('TNT invoice email has been detected')
            # we are indicating the subject of the email that was used
            logger.info(f'email: "{subjectofemail}" will be verified as for attachments')
            # now we will check if the document was already downloaded
            for attach in message.Attachments:
                invoice = attach.FileName[-12:-4]
                reading = open(r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_CONCAT.txt', 'r')
                # checks the content of the file
                opening = reading.read()
                if invoice not in opening:
                    logger.info(f' Invoice {invoice} has been detected and will be added')
                    # i am closing the file in read mode and opening in append mode
                    reading.close()
                    # opens overview in appending mode
                    appending = open(r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_CONCAT.txt', 'a')
                    # i am adding the invoice nuber
                    appending.write(invoice + '\n')
                    k = r'C:\Users\310295192\Desktop\Python\Projects\\FAP\INVOICES\\' + invoice + '.csv'
                    attach.SaveAsFile(k)
                    # now we are logging info that file was downloaded
                    logger.info(f'Invoice ({invoice}) has been downloaded')
                    print(f'Invoice {invoice} was downloaded')
                    #it adds the invoice number to list
                    inv_num.append(invoice)
                    #closes the file that was in append mode
                    appending.close()



# if there is something to be added
if inv_num:

    # opening file with all invoices
    together = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_INVOICES.xlsx')
    os.chdir(r'\Users\310295192\Desktop\Python\Projects\FAP\INVOICES')
    # looping through all the files available with data
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        print("Current Path: ", dirpath)
        print("Directories: ", dirnames)
        print("Files: ", filenames)
        for name in filenames:
            # opening invoice
            invoice_df = r'C:\Users\310295192\Desktop\Python\Projects\FAP\INVOICES\{}'.format(name).lower()
            try:
                data = pd.read_csv(invoice_df,encoding='iso-8859-1')
            except:
                data = pd.read_csv(invoice_df, encoding='utf-8')
            # concatenating file with current overview of invoices
            together = pd.concat([together, data])

    # saving file with new dataframe (with all invoices attached)
    together.to_excel(r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_INVOICES.xlsx', index=False)

    inv_file = r'C:\Users\310295192\Desktop\Python\Projects\FAP\TNT_INVOICES.xlsx'

    logger.info(f'Process has been executed. Mail is generated now')

    # delete the folders from place where files are managed and create them again
    shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\FAP\INVOICES', ignore_errors=True)
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\FAP')
    if not os.path.isdir('INVOICES'):
        os.mkdir('INVOICES')




    # preparing email for what has been added and what was wrong
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    #mail.To = 'FAP_Team@philips.com'
    mail.To = 'maciej.janowski@philips.com;FAP_Team@philips.com'
    mail.Subject = 'TNT Invoice - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
    mail.Body = 'Test'
    mail.HTMLBody = '<p>Dear Team,</p><p>Attached TNT invoices concatenated in one file</p>'\
                    '<p>Full log of the process in the attachment</p>'\
                    '<p>Cheers,</p><p>Maciej Janowski</p>' \
                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                    '<p>PCT Poland</p>'
    # attaching log file
    attachment = location
    mail.Attachments.Add(attachment)
    mail.Attachments.Add(inv_file)
    # sending email
    # mail.Send()
    mail.Save()
    print(datetime.datetime.now())