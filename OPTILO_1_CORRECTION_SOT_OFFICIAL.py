# concept mis to download all reports from today and update them based on last day


import win32com.client
import os
import shutil
from distutils.dir_util import copy_tree

# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(13)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 150 + 1
# starts the loop through the emails
for compwin in range(150):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + compwin)
    bodyofemail = message.body
    subjectofemail = message.subject
    # check if it is IDOC with attachment
    if subjectofemail[0:4] == "IDOC":
        # checks if it is shipping indicatior or transportation mode issue
        if ('indicator' in bodyofemail) or ('transportation' in bodyofemail) or ('Unknown Delivery type' in bodyofemail):
            filenaming = subjectofemail[10:43]
            print(filenaming)
            # opening the overview file
            reading = open(r'C:\Users\310295192\Desktop\Work\Optilo\tes\downloaded overview.txt', 'r')
            # adapt the lines for reading
            opening = reading.read()

            # loop through all lines
            if filenaming not in opening:
                # if filename is encoutered
                print('nie ma takiej wartosci')
                # closes the file in reading mode
                reading.close()
                # is opening file in append mode
                appending = open(r'C:\Users\310295192\Desktop\Work\Optilo\tes\downloaded overview.txt', 'a')
                # is adding filenaming to file
                appending.write(filenaming + '\n')
                # and it downloads the file to respective folder
                attachment = message.Attachments.Item(1)
                attachment.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Work\\Optilo\\tes\\downloaded\\' + filenaming + '.xml')
                # closes the file that was in append mode
                appending.close()


os.chdir(r'\Users\310295192\Desktop\Work\Optilo\tes\downloaded')
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    #if list of files is empty it is going to end up the code
    if not filenames:
        exit()
#loops through all files that are available
for every in filenames:
    main_path=os.path.join(os.getcwd(),every)
    print(main_path)
    corr_path=main_path.split(".")
    print(corr_path)
    magic = corr_path[0][-33:]
    print(magic)
    #Now the correction rollercoster comes in place
    with open(main_path,'r',encoding="latin-1") as k, open(r'C:\\Users\\310295192\\Desktop\\Work\\Optilo\\tes\\corrected and sent\\'+magic+'-corrected.xml','w+', encoding="utf-8") as corrected:
    #then i read content so that we have it as ordered list
        content=k.read().splitlines()
        previous_line=''
    #checking the file for AIR, SEA, LND or UKN indicator
        for x in content:
            #if it finds AIR - mode is AIR
            if 'AIR' in x:
                trans_mode = 'AIR'
                break
                # if it finds SEA - mode is SEA
            elif "SEA" in x:
                trans_mode = "SEA"
                break
                # if it finds LND - mode is LND
            elif "LND" in x:
                trans_mode = "LND"
                break
                # if it finds nothing - it is UKN
            else:
                trans_mode = "UKN"


        i =0
        #loop through each line
        while i<len(content):
        #  if line had <IncoTerms> phrase -it assigns what is in previous line
            if content[i][:11] =="<IncoTerms>":
                previous_line=content[i-1]
                #if in previous line we do not have delivery type -> it adds it
                if previous_line !="<DeliveryType>D2D</DeliveryType>":
                    corrected.write("<DeliveryType>D2D</DeliveryType>\n"+content[i]+"\n")
                    i+=1
                    pass
                #if delivery type is present it assigns current lane
                else:
                    corrected.write(content[i]+'\n')
                    i+=1
                    pass
            #if lane had <TransportationMode/> phrase-> it addes UKN line
            elif content[i][:21]=="<TransportationMode/>":
                corrected.write("<TransportationMode>"+trans_mode+"</TransportationMode>\n")
                i+=1
                pass
        # just goes and assigns new lane (not considering incoterms
            corrected.write(content[i] + '\n')
            i+=1


#And now we will be adding all these files as attachments


outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'IDOC upload'
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Comp-Win,</p><p>Please upload the attached content to the system.</p>' \
                '<p>Kind Regards,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>' #this field is optional

os.chdir(r'\Users\310295192\Desktop\Work\Optilo\tes\corrected and sent')
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
#loops through all files that are available
for every in filenames:
    main_path=os.path.join(os.getcwd(),every)
    print(main_path)
    #Attach a file to the email
    attachment  = main_path
    mail.Attachments.Add(attachment)

mail.Send()

# copies the corrected files to desktop (to avoid downloading from mail box)
copy_tree(r'C:\Users\310295192\Desktop\Work\Optilo\tes\corrected and sent', r'C:\Users\310295192\Desktop')

#delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Work\Optilo\tes\downloaded', ignore_errors=True)
shutil.rmtree(r'C:\Users\310295192\Desktop\Work\Optilo\tes\corrected and sent', ignore_errors=True)
os.chdir(r'\Users\310295192\Desktop\Work\Optilo\tes')
if not os.path.isdir('downloaded'):
    os.mkdir('downloaded')
if not os.path.isdir('corrected and sent'):
    os.mkdir('corrected and sent')
