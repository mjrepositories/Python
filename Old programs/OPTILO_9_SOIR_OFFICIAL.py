# program is going to find the file on mailbox and open the file with routing
# concept mis to download all reports from today and update them based on last day
import win32com.client
import os
import datetime
# getting current date
curr = datetime.datetime.today().strftime('%Y.%m.%d')
# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)
td = datetime.datetime.today().strftime('%Y-%m-%d')
# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 100 + 1
# starts the loop through the emails
for hawb in range(100):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + hawb)
    bodyofemail = message.body.upper()
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    # checks if string is present in body of the email
    if " THE SOIR LIST " in bodyofemail:
        # checks the attachment with proper naming
        for attach in message.Attachments:
            soir_attach = attach.FileName
            if "SOIR" in soir_attach.upper():
                # save file on hard drive
                # splitting by dot
                q = soir_attach.split('.')
                # getting the proper naming of the file
                soir = 'SOIR {}.{}'.format(curr, q[-1])
                print(soir)
                attach.SaveAsFile((r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\SOIR (6 weeks)\\'+ soir))
                break
naming = r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\SOIR (6 weeks)\\'+ soir
print(naming)
#is opening the excel file when macro is stored
# os.system('start EXCEL.EXE 'r'"C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Routings\Routings.xlsm"')
# os.system('start EXCEL.EXE "{}"'.format(naming))

os.startfile(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Routings')
os.startfile(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\SOIR (6 weeks)')

