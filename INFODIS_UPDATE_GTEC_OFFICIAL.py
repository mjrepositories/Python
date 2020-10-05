#it is working
import zipfile, os
import win32com.client
import datetime


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(8)
print(subfolder)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)

#sort all emails that we have in the folder
email.Sort('ReceivedTime')
first=x-2
#starts the loop through the emails
for infodis in range(3):
#checks the number of email after sorting and extract data on it
    message = email.Item(first + infodis)
    bodyofemail = message.body
    subjectofemail=message.subject
    #checks the date of the email and assing the proper date
    when = message.SentOn
    when_formated= datetime.datetime.strftime(when,'%Y-%m-%d')
    #now we will be checking each email subject and save it in proper folder
    print(subjectofemail)
    if subjectofemail == "Missing rates Part 1":
        attachment = message.Attachments.Item(1)
        # if the email is for FCL missing rates - it saves it in respective folder
        attachment.SaveAsFile(r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 1.zip')
    elif subjectofemail == "Missing rates Part 2":
        attachment = message.Attachments.Item(1)
        # if the email is for FCL missing rates - it saves it in respective folder
        attachment.SaveAsFile(
            r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 2.zip')
    elif subjectofemail == "Missing rates Part 3":
        attachment = message.Attachments.Item(1)
        # if the email is for AIR missing rates - it saves it in respective folder
        attachment.SaveAsFile(r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 3.zip')

path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 1.zip'
directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 2.zip'
directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 3.zip'
directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

# second extraction

path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 1.zip'
directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

#going to directory
os.chdir(r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files')
        # going through each filename
for dirpath,dirnames,filenames in os.walk(os.curdir):
    for naming in filenames:
        # if there is a file with Ruurd name
        print(naming)
        if naming[:3] == "Ruu":
            # it corrects the file to the name we need for easier processing
            os.rename(naming, f'rates_1.xlsx')
            break

path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 2.zip'
directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

        # going through each filename
for dirpath,dirnames,filenames in os.walk(os.curdir):
    for naming in filenames:
        # if there is a file with Ruurd name
        print(naming)
        if naming[:3] == "Ruu":
            # it corrects the file to the name we need for easier processing
            os.rename(naming, f'rates_2.xlsx')
            break

path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 3.zip'
directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

        # going through each filename
for dirpath,dirnames,filenames in os.walk(os.curdir):
    for naming in filenames:
        # if there is a file with Ruurd name
        print(naming)
        if naming[:3] == "Ruu":
            # it corrects the file to the name we need for easier processing
            os.rename(naming, f'rates_3.xlsx')
            break


os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 1.zip")
os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 2.zip")
os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 3.zip")
os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 1.zip")
os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 2.zip")
os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 3.zip")
