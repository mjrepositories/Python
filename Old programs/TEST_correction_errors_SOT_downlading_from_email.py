#concept mis to download all reports from today and update them based on last day


import win32com.client
import datetime
import os
import time
import pyautogui
import openpyxl
#getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
#getting to infodis folder
subfolder=folder.Folders(13)
#getting to all emails
email = subfolder.Items
#checkiing the number of emails to further take this value into the loop
x=len(email)

#sort all emails that we have in the folder
email.Sort('ReceivedTime')
first=x-50
#starts the loop through the emails
for compwin in range(50):
#checks the number of email after sorting and extract data on it
    message = email.Item(first + compwin)
    bodyofemail = message.body
    subjectofemail=message.subject
#check if it is IDOC with attachment
    if subjectofemail[0:4]=="IDOC":
        #checks if it is shipping indicatior or transportation mode issue
        if ('indicator' in bodyofemail) or ('transportation' in bodyofemail):
            filenaming = subjectofemail[10:43]
            print(filenaming)
            #opening the overview file
            reading =open(r'C:\Users\310295192\Desktop\tes\downloaded overview.txt', 'r')
            #adapt the lines for reading
            opening = reading.read()

            #loop through all lines
            if filenaming not in opening:
                #if filename is encoutered
                print('nie ma takiej wartosci')
                #closes the file in reading mode
                reading.close()
                #is opening file in append mode
                appending =open(r'C:\Users\310295192\Desktop\tes\downloaded overview.txt', 'a')
                #is adding filenaming to file
                appending.write(filenaming+ '\n')
                #and it downloads the file to respective folder
                attachment = message.Attachments.Item(1)
                attachment.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\tes\\downloaded\\'+filenaming+'.xml')
                #closes the file that was in append mode
                appending.close()
                break


#Now we will work on assigning the file that were donwloaded
#with open(r'C:\Users\310295192\Desktop\tes\corrected and sent.txt','w+') as corrected:


