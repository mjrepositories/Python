import win32com.client

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

#
#
# subfolder = audit.Folders(11).Folders(9)
# print(subfolder)
# # getting to all emails
# email = subfolder.Items
# # checking the number of emails to further take this value into the loop
# x = len(email)
# print(x)