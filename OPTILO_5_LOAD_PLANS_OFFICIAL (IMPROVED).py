import datetime
import openpyxl
import logging
import win32com.client
import pandas as pd
print(datetime.datetime.now())
import time

# time.sleep(1500)
# creating logger for actions
logger = logging.getLogger("Load Plans Log")
# setting the level for the logger
logger.setLevel('INFO')
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\LOAD_PLAN\loggers\Load Plans {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of checking sent load plans upload has been started')


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)
first = x - 50 + 1
file_for_load_plans = ""
for loadplan in range(50):
    # checks the number of email after sorting and extract data on it
    message = email.Item(first + loadplan)
    bodyofemail = message.body.upper()
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    time_received = message.ReceivedTime
    date_received = message.ReceivedTime
    reporting_date = int(time_received.strftime("%d"))
    today = int(datetime.datetime.today().strftime('%d'))
    reporting_time = int(time_received.strftime("%H"))
    print(reporting_date,"_______",today)
    load_doc = "Load plans " + datetime.datetime.today().strftime("%Y-%m-%d")
    # print(load_doc)
    # print(bodyofemail)
    # print("time of email---" + str(reporting_time))
    # checks the if ORDER REPORT in in subject
    if ('ORDER REPORT' in bodyofemail) and (reporting_time == 14) and (reporting_date == today) and (len(message.Attachments) > 0):
        #print(bodyofemail,subjectofemail,reporting)
        print('hello')
        for attach in message.Attachments:
            hawb_attach = attach.FileName
            #attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\' + load_doc + '.csv')
            attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\Python\\Projects\\LOAD_PLAN\\LOAD_PLANS\\'+ load_doc +'.csv')
            file_for_load_plans = r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\LOAD_PLAN\\LOAD_PLANS\\'+ load_doc +'.csv'






mjb_set = set()
logger.info("Excel file with data has been opened for verification")
# opening the excel file
# skip list allows us to indicate which MJB numbers should be skipped (because there is some issue)
skip_list =['MJB9025160','MJB9025993','MJB9029102'] # Daniel; Karol; Bogna (zly tytul ostatni)
# read csv file downloaded from email
df = pd.read_csv(file_for_load_plans,delimiter=';')

# leaves only cells with values
df = df[df['Planned pickup date'].notnull()]

# rename the last column
df.rename(index=str,columns={"Unnamed: 88":"Dating"},inplace=True)

# turn object from Planned pickup date to datetime format
df['Planned pickup date'] = pd.to_datetime(df['Planned pickup date'],format='%Y-%m-%d')

# modification as for dates for planned pickup date
df['Planned pickup date'] = df['Planned pickup date'].dt.date

# Calculate dates for 6 days ahead
df['Dating']=datetime.datetime.today() + datetime.timedelta(6)

# modification as for setting up dates
df['Dating']=df['Dating'].dt.date

# create column for checking the dates
df['first_check']='Y'

td = datetime.datetime.today()

df['today']=datetime.datetime.today()

# modifcation as for date for today
df['today'] = df['today'].dt.date

#checks if dates are after today's
df['first_check']=(df["Planned pickup date"] >= df['today']) & (df["Planned pickup date"] <= df['Dating'])

# create dataframe for only those lanes that are valid
date_check = df[df['first_check']==True]

# dataframe that does not containes "Carmel"
date_check = date_check[~date_check['Pickup city'].str.contains("Carmel")]

# dataframe that only contains "Planned" string
date_check = date_check[date_check['Order status'].str.contains("Planned")]

# create list of MJBs
mjb_num = list(date_check['Ref. number 1leg'])

# if MJB is not in skip list - we can pass it to set
for x in mjb_num:
    if x not in skip_list:
        mjb_set.add(x)

# print(mjb_set)
logger.info("List with MJB number for shipments in range today + 6 days has been created")
# converting set to list
mjb_list = list(mjb_set)
logger.info(mjb_list)
# print(mjb_list)



logging.info("Checking the emails for load plans sent")
import win32com.client
import datetime
# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(7)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
# print(x)

address = set()
# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 6000 + 1
# starts the loop through the emails
for load in range(6000):
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
    #bodyofemail = message.body
    # assigning info on sender
    sendermail = message.SenderEmailAddress.upper()
    # assigning subject of the email
    subjectofemail = message.subject.upper()
    # if day of mail is today
    #if day == today:
    # if there is load in subject of the email
    if "LOAD" in subjectofemail[:14]:
        # and if there is no "re" in subject of the email
        if "RE" not in subjectofemail[:6]:
            # and we have an attachment
            if len(message.Attachments) > 0:
                # find index for mjb
                mjb_index = subjectofemail.find('MJB')
                # extract mjb number
                mjb_no = subjectofemail[mjb_index:mjb_index+10]
                # print(subjectofemail)
                # print(mjb_no)
                address.add(mjb_no)



mjb_list_email = list(address)
logging.info("List of sent load plans for MJBs (based on emails) has been created")
logging.info(mjb_list_email)
# print(mjb_list_email)
# print(len(mjb_list_email))

mjb_present = []
mjb_absent = []

# Checking matching MJBs between two lists
for shipment in mjb_list:
    #if mjb number is in
    if shipment in mjb_list_email:
        # add to list with present MJB numbers
        mjb_present.append(shipment)
        # else - > add number to absent MJB numbers
    else:
        mjb_absent.append(shipment)

print(mjb_absent)
# COMPARING THE DATA FROM EMAIL WITH REPORT
# dropping unnecessary columns
clean_frame = date_check.drop(columns=['PCT origin comments',
       'Responsible person 2nd/3rd leg', 'PCT destination comments',
       'Optilo order number', 'Transport order creation date', 'Order status',
       'Pickup country','Loading terminal', 'Customer address',
       'Destination country', 'OA', 'PM', 'OM', 'Main goods name', 'MOT',
       'Service lvl', 'Lead time E2E', 'FSD', 'Planned pickup date',
       'Real pickup date', 'Pickup delay', 'CDD week', 'CDD',
       'Revised CDD week', 'Revised CDD', 'Exception code of revised CDD',
       'Real cdd', 'CDD late', 'Event real CDD', 'Number of leg', 'FTN',
       'Start port', 'Final port', 'ETD', 'ATD', 'ETA', 'ATA', 'HAWB/SWB',
       'MAWB/vessel', 'Container ID', 'First job status', 'First leg status',
       'Exception code 1st leg', 'Carrier 1leg','X-dock 1', 'Planned delivery to 1st x-dock',
       'Actual delivery to 1st x-dock', 'Event actual delivery 1st x-dock',
       'Second job status', 'Second leg status', 'Exception code 2nd leg',
       'Carrier 2leg', 'Ref. number 2leg', 'Planned pickup from 1st x-dock',
       'Actual pickup from 1st x-dock', 'X-dock 2',
       'Planned delivery to 2nd x-dock', 'Actual delivery to 2nd x-dock',
       'Event actual delivery 2nd x-dock', 'Planned pickup from 2nd x-dock',
       'Actual pickup from 2nd x-dock', 'Planned delivery leg3',
       'Actual delivery leg3', 'Event actual delivery leg3',
       'Third job status', 'Third leg status', 'Exception code 3rd leg',
       'Carrier 3leg', 'Ref. number 3leg', 'Is blocked',
       'Job 1 parcel tracking number', 'Job 1 road waybill no',
       'Job 1 road driver1 name', 'Job 1 transport vehicle no',
       'Job 1 transport group', 'Job 2 road waybill no',
       'Job 2 road driver1 name', 'Job 2 transport vehicle no',
       'Job 2 transport group', 'Job 3 road waybill no',
       'Job 3 road driver1 name', 'Job 3 transport vehicle no',
       'Job 3 transport group'])

# removing duplicate values
clean_frame.drop_duplicates('Ref. number 1leg',inplace=True)
clean_frame.dropna(subset=['Operating user'],inplace=True)
# stripping MJB column from spaces
clean_frame['Ref. number 1leg'] =clean_frame['Ref. number 1leg'].str.strip()
# checking if reference numbers (MJBs) from report are matching values extracted from email
email_frame = clean_frame[clean_frame['Ref. number 1leg'].isin(mjb_absent)]
# creating column with data from email
email_frame['for_email'] = "<p><b>" + email_frame['Ref. number 1leg'] + '-' + email_frame['Operating user'] + '-' + email_frame['Pickup city'] + "</b></p>,"

# creating string for email
mjb_string=""
for index,rows in email_frame.iterrows():
    mjb_string += rows['for_email']

# taking everything from the string except last comma
mjb_string = mjb_string[:-1]

# splitting string by comas
mjb_string = mjb_string.split(',')
# creating set with unique values
set_mjb_string = set(mjb_string)
good_mjb = list(set_mjb_string)
if "" in good_mjb:
    good_mjb.remove("")
for x  in good_mjb:
    # print(x)
    pass

print(good_mjb)

# additional procedure to delete strange value
for x in good_mjb:
    if len(x) <= 15:
        good_mjb.remove(x)


good_mjb.sort(key= lambda name: name.split("-")[1].split(" ")[0])
mjb_string_unique = ""
print(good_mjb)
# parsing string to create info sent by mail
for x in good_mjb:
    if ("orres" not in x) and ("amela" not in x) and ("Mellen" not in x) and("Dew" not in x) and("anya" not in x) \
            and ("Jimen" not in x)and ("hadbol" not in x)and ("ungan" not in x)and ("Chen" not in x) \
            and ('Whitne' not in x) and ('Zajac' not in x) and ('Nato' not in x) and ('Vonnadie' not in x)\
            and('Joseph' not in x) and ('Rommer' not in x) and ('Dizon' not in x) and ('Hernandez' not in x)\
            and('SYS Cmd' not in x) and ('Huang' not in x) and ('Ferrer' not in x) and ('vian' not in x)\
            and('hang' not in x):
        mjb_string_unique += x +'\n'

print(mjb_string_unique)




# creating string for correct and wrong mjbs
correct = "Loadplans sent for below MJB numbers:\n"
wrong = "Loadplans not sent for below MJB numbers:\n"
if len(mjb_absent) != 0:
    # looping through present mjbs and adding to message
    # c = 0
    w = 0
    # for x in mjb_present:
    #     correct = correct + "<p><b>"+ x +"</b></p>"+ '\n'
    #     c += 1

    # looping through absent mjbs and adding to the message
    for x in mjb_absent:
        wrong = wrong + "<p><b>"+ x +"</b></p>"+ '\n'
        w += 1

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'DL_PCTPolandOptilo@philips.com'
#mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'Load plans UNsent overview - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of <b>un</b>sent loadplans</p>'\
                '<p>Scope of checking - last 6000 emails and 6-days-ahead pick-up date'\
                '<p>Full log of registry in the attachment</p>'\
                +mjb_string_unique+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>' +"<p></p>"+str(w)
# attaching log file
attachment  = location
mail.Attachments.Add(attachment)
# sending email
logging.info("Mail has been generated")
mail.Send()
print(datetime.datetime.now())
