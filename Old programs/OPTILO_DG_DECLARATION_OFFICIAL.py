# concept mis to download all reports from today and update them based on last day
import win32com.client
from selenium import webdriver
import time
import os
import shutil
import datetime
import logging

# creating logger for actions
logger = logging.getLogger("DG Log")
# setting the level for the logger
logger.setLevel("INFO")
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\Loggers\DG {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of DG Declaration upload has been started')


# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# getting to infodis folder
subfolder = folder.Folders(5)
# getting to all emails
email = subfolder.Items
# checkiing the number of emails to further take this value into the loop
x = len(email)
print(x)

# list for mjb numbers
dg_num = []

# sort all emails that we have in the folder
email.Sort('ReceivedTime')
first = x - 100 + 1
# starts the loop through the emails
for dg in range(100):
    # assigns proper data for mail scrapping
    message = email.Item(first + dg)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    dgdoc = 'DGD documents'
    dgdoc = dgdoc.upper()
    # checks if we have dg declaration
    if dgdoc in subjectofemail and len(message.Attachments) > 0:
        #print(message.SenderEmailAddress.upper())
        # we are logging info about mjb creation
        logger.info('dangerous goods declarations email has been detected')
        # we are indicating the subject of the email that was used
        logger.info(f'email: "{subjectofemail}" will be verified as for attachments')
        # now we will check if the document was already downloaded
        for attach in message.Attachments:
            declaration = attach.FileName[0:9]
            reading = open(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\DG_DECLARATION.txt', 'r')
            # checks the content of the file
            opening = reading.read()
            if declaration not in opening and 'image' not in declaration:
                logger.info(f' Declaration for {declaration} has been detected and will be added')
                # i am closing the file in read mode and opening in append mode
                reading.close()
                # opens overview in appending mode
                appending = open(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\DG_DECLARATION.txt', 'a')
                # i am adding the declaration number
                appending.write(declaration + '\n')
                k = r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded\\' + declaration + '.pdf'
                attach.SaveAsFile(k)
                # now we are logging info that file was downloaded
                logger.info(f'Declaration for ({declaration}) has been dowloaded')
                #it adds the declaration number to list
                dg_num.append(declaration)
                #closes the file that was in append mode
                appending.close()










# list for wrong mjbs
wrong_dg = []
browser = webdriver.Chrome()
# getting to Optilo
browser.get("https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")
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
os.chdir(r'\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded')
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)

counter = 0
#loops through all files that are available
for every in filenames:
    try:
        line = every[0:9]
        # finding order tab
        # order = browser.find_element_by_id('menu-258839')
        # order = browser.find_element_by_id('menu-259556') update 2019-06-15
        order = browser.find_element_by_id('menu-1-259789')
        order.click()
        # finding order transport tab
        # ordertrans = browser.find_element_by_id('menu-258796')
        # ordertrans = browser.find_element_by_id('menu-259513') update 2019-06-15
        ordertrans = browser.find_element_by_id('menu-1-259789-259883')
        ordertrans.click()
        # finding order list tab
        # orderlist = browser.find_element_by_id('menu-258800')
        # orderlist = browser.find_element_by_id('menu-259517') update 2019-06-15
        orderlist = browser.find_element_by_id('menu-1-259789-259883-259887')
        orderlist.click()
        # finding box for delivery order number
        jobnumber = browser.find_element_by_id('DF690000217_f_referencja1')
        jobnumber.clear()
        # entering job number
        jobnumber.send_keys(line)
        time.sleep(3)
        # finding search button
        # searching = browser.find_element_by_id('action[690000217][1530404]')
        # searching = browser.find_element_by_id('action[690000217][3971]') update 2019-06-15
        searching = browser.find_element_by_id('action[690000217][4004]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2)
        buttonforjob = browser.find_element_by_xpath('//*[@id="DL690000216"]/tbody/tr[2]/td[4]/a')
        buttonforjob.click()
        time.sleep(3)
        # copy address from tab
        current_address = browser.current_url
        # turn to string
        web_address = str(current_address)
        # replace jobdetails to jobcosts and go the site with costs
        newaddress = web_address.replace('TransportDanePodstawowe', 'TransportPliki')
        # going to new files tab
        browser.get(newaddress)
        time.sleep(3)
        # finding this freaking hidden option to upload
        upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
        # uploading the file
        upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded\{}.pdf'.format(line))
        time.sleep(11)
        # counting number of columns
        row_count = len(browser.find_elements_by_xpath("//table[@id='DP690000322']/tbody/tr"))
        time.sleep(2)
        print(row_count)
        # finding document type
        document = browser.find_element_by_xpath(f"//table[@id='DP690000322']/tbody/tr[{row_count}]/td[5]/select/option[30]")
        time.sleep(6)
        document.click()
        time.sleep(2)
        saving = browser.find_element_by_name('action_dp[690000322][Z][save]')
        saving.click()
        # we are logging information that HAWB for MJB was uploaded successfully
        logger.info(f' File for {line} successfully added to Optilo')
        time.sleep(3)

    except:
        # we are logging information that MJB number was not found in Optilo
        logger.warning(f'({line}) was not found in Optilo')
        dg_num.remove(line)
        wrong_dg.append(line)

# we are logging summary info for the upload of files
logger.info(f'DG declarations upload has been acomplished. Successful uploads: {len(dg_num)}. Unsucessful uploads: {len(wrong_dg)}')
# delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DG_DECLARATION\downloaded', ignore_errors=True)
# adapting the current path to Panalpina HAWB folder with downloaded documents
os.chdir(r'\Users\310295192\Desktop\Python\Projects\DG_DECLARATION')
# if folder is not present - it creates it
if not os.path.isdir('downloaded'):
    os.mkdir('downloaded')


# creating string for correct and wrong mjbs
correct = "Correctly uploaded DG declarations for Order numbers:\n"
wrong = "Files not uploaded  because of lack of Order number in Optilo:\n"
if len(dg_num)!= 0  or len(wrong_dg) != 0:
    # looping through correct mjbs
    for x in dg_num:
        correct = correct + "<p><b>"+ x +"</b></p>"+ '\n'

    # looping through wrong mjbs
    for x in wrong_dg:
        wrong = wrong + "<p><b>"+x+"</b></p>"+ '\n'

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'DL_PCTPolandOptilo@philips.com'
# mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'DG Declaration - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded DG Declarations</p>'\
                '<p>Full log of upload in the attachment</p>'\
                +correct + wrong+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>'
# attaching log file
attachment = location
mail.Attachments.Add(attachment)
# sending email
mail.Send()

#closing browser
browser.close()