import win32com.client
import datetime
import logging
import pandas as pd
import numpy as np


# creating a logger for the dq documents
# creating logger for actions
logger = logging.getLogger("DQ Log")
# setting the level for the logger
logger.setLevel("INFO")
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\DQ\loggers\DQ {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure for checking DQ declaration has been started')


# reading file
jojo = r'P:\IWD Łódż\3.pre planning files\pre planning\Current pre-planning file\Pre-planning_LMP_Europe.xlsx'
df = pd.read_excel(jojo)
# df = pd.read_excel(r'C:\Users\310295192\Desktop\Pre-planning_LMP_Europe.xlsx')

# takes values only with available Sales orders
df= df[np.isfinite(df['SSD Sales Order'])]

# is dropping values that for Planners are null
df = df.dropna(subset=['Planners name'])


# KOREKTA COS CO MA PREBOOKING MA BYC
# drops values that with preboooking date
#df = df.dropna(subset=['Prebooking date'])

# 2019-05-28 09:23 Makes DataFrame that has only empty cells
df = df[df['Prebooking date'].isnull()]

# only selects values that are connected with statuses Z4, Z5, Z6
df= df.loc[(df['Userstatus item'] == 'Z4') | (df['Userstatus item'] == 'Z5') | (df['Userstatus item'] == 'Z6')]

# we are creating a list and adding values to it regarding SO number
so_list=[]
for x in df['SSD Sales Order']:
    x = int(x)
    x= str(x)
    so_list.append(x)

# taking care that we do not have duplicates in the SO list
flip = set(so_list)
so_list = list(flip)
logger.info(f"List of indicated SO numbers has been created {so_list}")
# WORKING - DOWNLOADING DOCUMENTS FROM EMAIL BOX
# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# getting to dq folder
dqmail = folder.Folders('DQ.PCT (Functional Account)')
print(dqmail)
subfolder = dqmail.Folders(16)
print(subfolder)
# getting to all emails
email = subfolder.Items
# checking the number of emails to further take this value into the loop
x = len(email)
print(x)
# sorting all emails
email.Sort('ReceivedTime')
present_dq = []
absent_dq =[]
current_dq = []
dqset = set()
first = x - 3500 + 1
# starts the loop through the emails
for dq in range(3500):
    # assigns proper data for mail scrapping
    message = email.Item(first + dq)
    bodyofemail = message.body
    # sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    lookupsix = "660"
    lookupseven = '670'
    # print(sendermail)
    purchaseorder = 0
    dqfile = ""
    #checs if we have attachement
    if len(message.Attachments) > 0:
        # checking if one of 4 conditions is met. If yes - then it assigns it to set
        if lookupsix in subjectofemail:
            purchaseorder = subjectofemail.find(lookupsix)
            dqfile = subjectofemail[purchaseorder:purchaseorder + 10]
            dqset.add(dqfile)
            logger.info(f'mail {subjectofemail} was picked up for {dqfile}')
        elif lookupsix in bodyofemail:
            purchaseorder = bodyofemail.find(lookupsix)
            dqfile = bodyofemail[purchaseorder:purchaseorder + 10]
            dqset.add(dqfile)
            logger.info(f'mail {subjectofemail} was picked up for {dqfile}')
        elif lookupseven in subjectofemail:
            purchaseorder = subjectofemail.find(lookupseven)
            dqfile = subjectofemail[purchaseorder:purchaseorder + 10]
            dqset.add(dqfile)
            logger.info(f'mail {subjectofemail} was picked up for {dqfile}')
        elif lookupseven in bodyofemail:
            purchaseorder = bodyofemail.find(lookupseven)
            dqfile = bodyofemail[purchaseorder:purchaseorder + 10]
            dqset.add(dqfile)
            logger.info(f'mail {subjectofemail} was picked up for {dqfile}')


print(dqset)

# checks if every SO in list is present in created set
for every in so_list:
    if every in dqset:
        present_dq.append(every)
    else:
        absent_dq.append(every)


logger.info(f'For indicated SO Numbers DQ was detected {present_dq}')
logger.info(f'For indicated SO NUmbers DQ was not found {absent_dq}')
visible = "Program found DQ for:\n"
missing = "Program has not found DQ for:\n"

# creating list with integers for lookup in df
are_in = map(int,present_dq)
not_in = map(int,absent_dq)

#creating list out of these integers lists
are_in = list(are_in)
not_in = list(not_in)

# creating empty lists for storing the values with PO number, Planner Name and Country

new_dq_present=[]
new_dq_absent=[]

# going through present list
for x in are_in:
    for index, row in df.iterrows():
        # if PO number is matched
        if x == row["SSD Sales Order"]:
            # it is adding this PO number with details regarding Planner and Country
            #new_dq_present.append(str(x) + "-" + row['Planners name'] + "-" + row['FU Country'])
            new_dq_present.append(str(row['PO Number']) + "-" + str(x) + "-" + row['Material Description'] + "-" + row['Planners name'] + "-" + row['FU Country'] + "-" + str(row['CDD ']))
            break

# going through absent list
for x in not_in:
    for index, row in df.iterrows():
        # if PO number is matched
        if x == row["SSD Sales Order"]:
            # it is adding this PO number with details regarding Planner and Country
            #new_dq_absent.append(str(x) + "-" + row['Planners name'] + "-" + row['FU Country'])
            new_dq_absent.append(str(row['PO Number']) + "-" + str(x) + "-" + row['Material Description'] + "-" + row['Planners name'] + "-" + row['FU Country'] + "-" + str(row['CDD ']))
            break

# sort both tables firstly on name of the planner, secondly - on country
new_dq_present.sort(key= lambda name: (name.split("-")[1],name.split("-")[2]))
new_dq_absent.sort(key= lambda name: (name.split("-")[1],name.split("-")[2]))



if len(present_dq) != 0 or len(absent_dq) != 0:
    # looping through correct mjbs
    for x in new_dq_present:
        visible = visible + "<p><b>" + x + "</b></p>" + '\n'

    # looping through wrong mjbs
    for x in new_dq_absent:
        missing = missing + "<p><b>" + x + "</b></p>" + '\n'
logger.info("Mail has been generated")
# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
# mail.To = 'maciej.janowski@philips.com'
mail.To = 'daniel.ciechanski@philips.com;' \
          'Dominik.Wronkowski@philips.com;paulina.szczesniewicz@philips.com;joanna.polak@philips.com;Mariusz.Mikinka@philips.com'
mail.Subject = 'DQ presence check - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of DQ availibility on mailbox</p>'\
                '<p>Full log of procedure in the attachment</p>'\
                +visible + missing+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>'
# attaching log file
attachment  = location
mail.Attachments.Add(attachment)
# sending email

mail.Send()
