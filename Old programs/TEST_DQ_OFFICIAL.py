import win32com.client
import datetime
import os
import shutil
import time
import PyPDF2
from selenium import webdriver
import logging

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
logger.info('Procedure of DQ Declaration upload has been started')






# WORKING - DOWNLOADING DOCUMENTS FROM EMAIL BOX
# getting to inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# getting to dq folder
dqmail = folder.Folders('DQ.PCT (Functional Account)')
print(dqmail)
subfolder = dqmail.Folders(15)
print(subfolder)
# getting to all emails
email = subfolder.Items
# checking the number of emails to further take this value into the loop
x = len(email)
print(x)

email.Sort('ReceivedTime')
first = x - 21 + 1
# starts the loop through the emails
for dq in range(21):
    # assigns proper data for mail scrapping
    message = email.Item(first + dq)
    bodyofemail = message.body
    sendermail = message.SenderEmailAddress.upper()
    subjectofemail = message.subject.upper()
    print(sendermail)
    print(subjectofemail)
    lookup = 'Purchase Order: 45'
    # checking if phrase for lookup is in the subject of the email
    if lookup.upper() in subjectofemail:
        # finding the proper purchase order number in body of the file
        purchaseorder = bodyofemail.find('Purchase Order: ')
        logger.info(f'email /{subjectofemail}/ will be verified as for DQ documentation')
        # assigning the proper purchase order number
        dqfile = bodyofemail[purchaseorder+16:purchaseorder+26]
        # opening the file with registered dq documents
        reading = open(r'C:\Users\310295192\Desktop\Python\Projects\DQ\DQ.txt','r')
        # reading up the content of the file
        opening = reading.read()
        # checking if the dq document was already registered
        if dqfile not in opening:
            # if not - saving document and registering in the file
            for attach in message.Attachments:
                if 'DQ_Attachment' in attach.FileName:
                    logger.info(f'document for{dqfile} has been found and will be added to Optilo')
                    reading.close()
                    # opening dq registery in append mode
                    appending = open(r'C:\Users\310295192\Desktop\Python\Projects\DQ\DQ.txt','a')
                    # adding dq number to the file with registry
                    appending.write(dqfile+'\n')
                    # saving the file with proper file name
                    k = r'C:\Users\310295192\Desktop\Python\Projects\DQ\downloaded\{}.pdf'.format(dqfile)
                    logger.info(f'file for {dqfile} has been saved on hard drive')
                    attach.SaveAsFile(k)
                    # closing the registry for dq
                    appending.close()



os.chdir(r'\Users\310295192\Desktop\Python\Projects\DQ\downloaded')
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)



#loops through all files that are available
dq_details = {}
for every in filenames:
    logger.info(f'program is checking {every[:11]} for product number')
#GETTING VALUES FROM DQ
# otwiera plik do zapisania
    with open(r'C:/Users/310295192/Desktop/Python/Projects/DQ/downloaded/{}'.format(every), 'rb') as file:
        # otwiera pdf
        pdfreader = PyPDF2.PdfFileReader(file)
        # dostaje sie do stron
        print(pdfreader.getNumPages())
        # otwiera pierwszą stronę
        paging = pdfreader.getPage(0)
        # wyciąga dane z pierwszej strony
        strona = paging.extractText()
        # zamienia kropki na przecinki
        print(strona)
        #finding system number
        fork = strona.find('Extended forks needed?')
        system = strona[fork+23:fork+29]
        print(system)
        # finding PO Number
        po = strona.find('PO Number')
        ponum = strona[po+10:po+20]
        print(ponum)
        dq_details[ponum] = system
        logger.info(f'program found item {system} for {ponum}')

        print(dq_details)










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





# WORKING - ADDING DQ TO SYSTEM -> Replace dictionary with
dq_num=[]
wrong_dq=[]
dictionary = {'4513300682': '781342'}

# loops through all files that are available
for docnum,product in dq_details.items():
    try:
        line = docnum
        # finding order tab
        # order = browser.find_element_by_id('menu-258839')
        order = browser.find_element_by_id('menu-259556')
        order.click()
        # finding order transport tab
        # ordertrans = browser.find_element_by_id('menu-258796')
        ordertrans = browser.find_element_by_id('menu-259513')
        ordertrans.click()
        # finding order list tab
        # orderlist = browser.find_element_by_id('menu-258800')
        orderlist = browser.find_element_by_id('menu-259517')
        orderlist.click()
        # finding box for delivery order number
        purchnumber = browser.find_element_by_id('DF690000217_f_referencja4')
        purchnumber.clear()
        # entering job number
        purchnumber.send_keys(line)
        time.sleep(3)
        # finding search button
        searching = browser.find_element_by_id('action[690000217][3971]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2)
        # setting up list for all order lines
        orderlines =[]
        # couting the number of rows
        row_count = len(browser.find_elements_by_xpath("//table[@id='DL690000216']/tbody/tr"))
        print(row_count)
        for x in range(2,row_count + 1):
            linkto = browser.find_element_by_xpath('//*[@id="DL690000216"]/tbody/tr[{}]/td[4]/a'.format(x))
            # getting reference number for proper webpage address
            getref = linkto.get_attribute('href')[-9:]
            getord = getref.split(',')
            reference = getord[1]
            #adding reference number for each page
            orderlines.append(reference)
            print(orderlines)
            time.sleep(3)
        for page in orderlines:
            # copy address from tab
            current_address = 'https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=zamowienie&s=ZamowienieTransportLinie&key=id_zam_zamowienie,{}'.format(page)
            # turn to string
            # web_address = str(current_address)
            # # replace jobdetails to jobcosts and go the site with costs
            # newaddress = web_address.replace('TransportDanePodstawowe', 'TransportPliki')
            # going to new files tab
            browser.get(current_address)
            time.sleep(11)
            # counting number of columns
            row_count_oline = len(browser.find_elements_by_xpath("//table[@id='DG690000215']/tbody/tr"))
            time.sleep(2)
            print(row_count_oline)
            # looping through each row for order lines
            for y in range(2,row_count_oline + 1):
            #extracting the number of rows in table for order lines
                mat_num = browser.find_element_by_xpath('//table[@id="DG690000215"]/tbody/tr[{}]/td[4]'.format(y)).text
                print(mat_num)
                print(product)
                # if material number is the same as we have in document then it will upload the file
                if mat_num == product:
                    # going to webpage for file upload
                    file_upload = 'https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=zamowienie&s=ZamowienieTransportPliki&key=id_zam_zamowienie,{}'.format(page)
                    browser.get(file_upload)
                    time.sleep(4)
                    # finding this freaking hidden option to upload
                    upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
                    # uploading the file
                    upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\DQ\downloaded\{}.pdf'.format(docnum))
                    time.sleep(7)
                    # FINDING PROPER ROW
                    # finding number of rows in table with documents
                    row_count_po = len(browser.find_elements_by_xpath("//table[@id='DP690000322']/tbody/tr"))
                    for rowing in range(2, row_count_po + 1):
                        # finding documents names
                        document = browser.find_element_by_xpath('//table[@id="DP690000322"]/tbody/tr[{}]/td[2]'.format(rowing)).text
                        # if names match - select proper document type
                        if document[0:10] == docnum:
                            # selectiong document
                            sel_doc = browser.find_element_by_xpath(f"//table[@id='DP690000322']/tbody/tr[{rowing}]/td[5]/select/option[28]")
                            time.sleep(2)
                            # clicking document
                            sel_doc.click()
                            #clicking save button
                            saving = browser.find_element_by_name('action_dp[690000322][Z][save]')
                            saving.click()
                            time.sleep(3)
                            dq_num.append(docnum)
                            logger.info(f'file for item {product} has been successfully uploaded to order {line}')
    except:
        wrong_dq.append(docnum)
        logger.info(f'document for order {docnum} with item {product} has not been uploaded.ZTO does not exist')








# we are logging summary info for the upload of files
logger.info(f'DG declarations upload has been acomplished. Successful uploads: {len(dq_num)}. Unsucessful uploads: {len(wrong_dq)}')
# delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DQ\downloaded', ignore_errors=True)
# adapting the current path to Panalpina HAWB folder with downloaded documents
os.chdir(r'\Users\310295192\Desktop\Python\Projects\DQ')
# if folder is not present - it creates it
if not os.path.isdir('downloaded'):
    os.mkdir('downloaded')


# creating string for correct and wrong mjbs
correct = "Correctly uploaded DQ for Order numbers:\n"
wrong = "Files not uploaded  because of lack of Order number in Optilo:\n"
if len(dq_num)!= 0  or len(wrong_dq) != 0:
    # looping through correct mjbs
    for x in dq_num:
        correct = correct + "<p><b>"+ x +"</b></p>"+ '\n'

    # looping through wrong mjbs
    for x in wrong_dq:
        wrong = wrong + "<p><b>"+x+"</b></p>"+ '\n'

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
# mail.To = 'DL_PCTPolandOptilo@philips.com'
mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'DG Declaration - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded DQ</p>'\
                '<p>Full log of upload in the attachment</p>'\
                +correct + wrong+'<p>Cheers,</p><p>Maciej Janowski</p>' \
                '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                '<p>PCT Poland</p>'
# attaching log file
attachment = logger
mail.Attachments.Add(attachment)
# sending email
mail.Send()
logger.info('Mail with the attachment has been generated and sent')
#closing browser
browser.close()







# getting to each href value for order
# linkto = browser.find_element_by_xpath('//*[@id="DL690000216"]/tbody/tr[2]/td[4]/a')
# x = linkto.get_attribute('href')[-5:]
# print(x)
# 31659