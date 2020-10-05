from selenium import webdriver
import time
import shutil
import logging
import datetime
import win32com.client




# creating logger for actions
logger = logging.getLogger("UPS Log")
# setting the level for the logger
logger.setLevel('INFO')
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s','%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\Loggers\UPS\UPS {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure of HAWB upload has been started')













# going through list of mjbs from the excel file
import pandas as pd
import os
os.chdir(r'\Users\310295192\Desktop\Python\Projects\HAWB\UPS\MJB')
for filename in os.listdir("."):
        os.rename(filename, 'MJB_NUMBERS.xls')

filenaming = r'C:\Users\310295192\Desktop\Python\Projects\HAWB\UPS\MJB\MJB_NUMBERS.xls'
# setting up list for mjb numbers
mjb_list = []

# opening file with pandas
df = pd.read_excel(io=filenaming)
# looping through each row in "Number" column
for index,row in df.iterrows():
    # adding mjb number to list
    mjb_list.append(row['Number'])

logger.info("MJB list has been created")
print(mjb_list)
mjb_num=[]
# deleting the file with mjb numbers
os.remove(filenaming)
for nomjb in mjb_list:
    reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB UPS.txt', 'r')
    # checks the content of the file
    opening = reading.read()
    # #checks if mjb is already added in the list
    if nomjb not in opening:
        # we are logging info that number was not on list and program will upload the document
        logger.info(f'{nomjb} number is not on the list and HAWB will be checked for presence')
        print("nie ma takiej wartości")
        reading.close()
        # opens overview in appending mode
        appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB UPS.txt', 'a')
        # is adding mjb to file
        appending.write(nomjb + '\n')
        mjb_num.append(nomjb)
        appending.close()


# opening browser again
# looking for documents on UPS site
# setting up the folder for downloading the files
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\UPS"}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(options=chromeOptions)
# going to UPS page
browser.get('https://fgv.ups-scs.com/loginservices/logOn.nfdo')
time.sleep(4)
# inputing password
password = browser.find_element_by_id('auto_off')
password.send_keys('Philips@123')
# inputting userid
user = browser.find_element_by_name('userId')
user.send_keys('PCTPLFGV18')
# finding log in button and clicking
button = browser.find_element_by_xpath('/html/body/div[2]/section/div[2]/div[1]/div/div/form/input')
button.click()
logger.info('successfully logged into UPS website')
logger.info('starting the sequence to find HAWBs for respective MJB numbers')
time.sleep(4)
counter = 0
# creating a list of mjbs that were not found on ups site to avoid them in next loop for upload to Optilo
wrong_input_mjb = []
for upsmjb in mjb_num:
    try:
        # going to page with search enging
        browser.get('https://fgv.ups-scs.com/shipmentservices/shipmentDashBoard.do?defaultState=viewDb&defaultView=normal')
        # selecting customer reference point
        refby = browser.find_element_by_xpath('//*[@id="refBy"]/option[4]')
        refby.click()
        # inputting mjb number
        refnum = browser.find_element_by_id('refByValue')
        refnum.send_keys(upsmjb)
        # submitting the request for checking the data
        tracking = browser.find_element_by_id('submitBtn')
        tracking.click()
        time.sleep(14)
        # finding the ups reference number
        ups = browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[7]/td/table/tbody/tr[21]/td[4]')
        # extracting ups reference number
        upsnum = ups.text
        # going to page with documents
        try:
            browser.get(f'https://fgv.ups-scs.com/customsentryservices/e2kImaging.img?p_file_no={upsnum}&p_branch=5531&p_query_type=F&p_screen=SHIPMENT_DETAILS_SCREEN&p_key=T&p_dataSource=E2KEX&p_accountNumbers=710760091')
        except:
            browser.get(f'https://fgv.ups-scs.com/customsentryservices/e2kImaging.img?p_file_no={upsnum}&p_branch=4708&p_query_type=F&p_screen=SHIPMENT_DETAILS_SCREEN&p_key=T&p_dataSource=E2KEX&p_accountNumbers=710935388')
        # below sequence for downloading outside philips office
        # if counter == 0:
        #     time.sleep(10)
        #     userph = browser.find_element_by_id("pf.username")
        #     userph.send_keys("maciej.janowski@philips.com")
        #     passwording = browser.find_element_by_id('pf.pass')
        #     passwording.send_keys("0312")
        #     time.sleep(10)
        #     button = browser.find_element_by_name('button')
        #     button.click()
        #     time.sleep(5)
        #     counter = 1
        time.sleep(48)
        # checking number of rows for table
        row_c = len(browser.find_elements_by_xpath("//table[@id='tOrderHeaders']/tbody/tr"))
        logger.info("checking for HAWB in table with documents")
        for x in range(1,row_c):
            # checking for each row the 4th column with details for documents
            value = browser.find_element_by_xpath("//table[@id='tOrderHeaders']/tbody/tr[{}]/td[4]".format(x))
            doctype = value.text
            # if it finds HAWB -> it downloads it
            if "WAYBILL" in doctype.upper():
                rowing = x
        #it downloads the file
        element = browser.find_element_by_name(f'rDocumentListItems$ctl0{rowing-1}$lnkEdit')
        element.click()
        time.sleep(10)
        # now we have to adjust the names of the files
        # adjusting the folder with HAWBs for UPS
        os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\UPS')
        # going through each filename
        for dirpath,dirnames,filenames in os.walk(os.curdir):
            for naming in filenames:
                # if there is a file without MJB at the beginning
                if naming[:3] != "MJB":
                    # it corrects the name of the file -> saves it with mjb number
                    # every file in current directory will have MJB at the beginning
                    # except one that we are going to adjust
                    os.rename(naming, f'{upsmjb}.pdf')
    except:
        print('unable to find mjb number')
        logger.warning(f'unable to find HAWB for {upsmjb}')
        wrong_input_mjb.append(upsmjb)

# looping through the list of mjbs that were extracted from excel file
# and deleting the ones that files were not downloaded for from ups site
for single_mjb in wrong_input_mjb:
    mjb_num.remove(single_mjb)

browser.close()










# opening browser again
wrong_mjb=[]
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
time.sleep(5)

# procedure for inputting the values to the system
for every in mjb_num:
    try:
        line = every
        # finding multi tab
        multi = browser.find_element_by_id('menu-259381')
        multi.click()
        # finding multi job tab
        joblist = browser.find_element_by_id('menu-259383')
        joblist.click()
        # finding box for job number
        jobnumber = browser.find_element_by_id('DF650000161_number')
        jobnumber.clear()
        # looping through each job number
        jobnumber.send_keys(line)
        time.sleep(3)
        # finding search button
        searching = browser.find_element_by_id('action[650000161][3242]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2)
        buttonforjob = browser.find_element_by_link_text(line)
        buttonforjob.click()
        time.sleep(3)
        # copy address from tab
        current_address = browser.current_url
        # turn to string
        web_address = str(current_address)
        # replace jobdetails to jobcosts and go the site with costs
        newaddress = web_address.replace('JobDetails', 'JobFiles')
        # going to new files tab
        browser.get(newaddress)
        time.sleep(3)
        # finding this freaking hidden option to upload
        upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
        # uploading the file
        upload_file.send_keys(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\UPS\{}.pdf'.format(line))
        time.sleep(11)
        # counting number of columns
        row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
        time.sleep(2)
        print(row_count)
        # finding document type
        document = browser.find_element_by_xpath(f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[22]")
        time.sleep(6)
        document.click()
        time.sleep(2)
        saving = browser.find_element_by_name('action_dp[650000192][Z][save]')
        saving.click()
        # we are logging information that HAWB for MJB was uploaded successfully
        logger.info(f' File for {line} successfully added to Optilo')
        time.sleep(3)
    except:
        # we are logging information that MJB number was not found in Optilo
        logger.warning(f'({line}) was not found in Optilo')
        print("wrong MJB number")
        mjb_num.remove(line)
        wrong_mjb.append(line)

    # we are logging summary info for the upload of files
logger.info(f'HAWB upload has been acomplished. Successful uploads: {len(mjb_num)}. Unsucessful uploads: {len(wrong_mjb)}')
# delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded\UPS', ignore_errors=True)
# adapting the current path to Panalpina HAWB folder with downloaded documents
os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\downloaded')
# if folder is not present - it creates it
if not os.path.isdir('UPS'):
    os.mkdir('UPS')

# creating string for correct and wrong mjbs
correct = "Correctly uploaded HAWBs for:\n"
wrong = "Files not uploaded because of wrong MJB number:\n"
if len(mjb_num) != 0 or len(wrong_mjb) != 0:
    # looping through correct mjbs
    for x in mjb_num:
        correct = correct + "<p><b>" + x + "</b></p>" + '\n'

    # looping through wrong mjbs
    for x in wrong_mjb:
        wrong = wrong + "<p><b>" + x + "</b></p>" + '\n'

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
# mail.To = 'DL_PCTPolandOptilo@philips.com'
mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'UPS House Air Waybill (HAWB) - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Below overview of uploaded documents for UPS </p>' \
                '<p>Full log of upload in the attachment</p>' \
                + correct + wrong + '<p>Cheers,</p><p>Maciej Janowski</p>' \
                                    '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
                                    '<p>PCT Poland</p>'
# attaching log file
attachment = location
mail.Attachments.Add(attachment)
# sending email
mail.Send()

# closing browser
browser.close()

