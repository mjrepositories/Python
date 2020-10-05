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

# NIPPON

# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(1)

print(subfolder)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)


rates = pd.DataFrame({'Shipment' : [],
                    'Pricing':[],'Weight':[],'Service':[]})




rows_list = []
email.Sort('ReceivedTime')
first = x - 800 + 1
# starts the loop through the emails
for load in range(800):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + load)
    # getting the time of receiving the email
    timing = message.ReceivedTime
    # setting up the proper format email time
    day = datetime.datetime.strftime(timing,"%Y-%m-%d")
    # converting date of email to date format
    object_day = datetime.datetime.strptime(day,"%Y-%m-%d")
    # setting up the proper format for today
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    # conveting date of emila to date format
    object_today = datetime.datetime.strptime(today,"%Y-%m-%d")
    # assigning body of the email
    bodyofemail = message.body
    # assigning info on sender
    sendermail = message.SenderEmailAddress.upper()
    # assigning subject of the email
    subjectofemail = message.subject.upper()
    # if day of mail is today
    if day[5:7]=='07':
        if sendermail == ('Hasan.Koeybasi@neeur.com'.upper()) and ("ALREADY CONFIRMED" not in subjectofemail):
            print("Month: "+ object_today.strftime('%m'))
            reference = bodyofemail.find('Philips Refs')
            print(subjectofemail)
            mtastart = subjectofemail.find('MTA')
            print('Reference number: '+subjectofemail[mtastart:mtastart+10])
            spot = bodyofemail.find('Spot rate')
            reference_matc = bodyofemail[reference+13:spot+20]
            euro = bodyofemail.find('EUR')
            print('Pricing: ' +bodyofemail[spot+11:euro].strip())
            weight  = bodyofemail.find('CWT')
            weight_text = bodyofemail[weight:weight+15]
            weight_text = weight_text.replace(" ","").upper()
            if "MIN" in weight_text:
                print("Weight: MIN")
                weighing = 'MIN'
            else:
                wstart = weight_text.find(":")
                wend = weight_text.find('KG')

                weighing = weight_text[wstart+1:wend]
                print("Weight: "+weight_text[wstart+1:wend])

            service = bodyofemail.find('STR-')

            service_level = bodyofemail[service:service+15].strip()
            print(service_level)
            if 'SL' in service_level:
                service_level.replace('SL',"")

            sl=[s for s in service_level.split() if s.isdigit()]
            if not sl:
                if service_level[-1:] == '0':
                    sl=['10']
                else:
                    sl = [service_level[-1:]]
            print(sl)
            sl = sl[0]

            adding = {'Shipment':subjectofemail[mtastart:mtastart+10],
                      'Pricing':bodyofemail[spot+11:euro].strip(),
                      'Weight':weighing,'Service':sl}

            rows_list.append(adding)

df = pd.DataFrame(rows_list)
df.to_excel(r'C:\Users\310295192\Desktop\ratesfornippon.xlsx',index=False)
