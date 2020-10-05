from selenium import webdriver
import time
import os
import pandas as pd
import logging
import datetime
import win32com.client
import shutil

# creating a logger for the dq documents
# creating logger for actions
logger = logging.getLogger("DHL_MILESTONES Log")
# setting the level for the logger
logger.setLevel("INFO")
# setting the date for logger
today = datetime.datetime.today().strftime("%Y-%m-%d")
# setting up the format for logs
formatter = logging.Formatter('%(asctime)s///%(name)s///%(levelname)s///%(message)s', '%Y-%m-%d %H:%M:%S')
# creating the location of the file where logger is stored
# setting the feature regarding location of the file
location = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\Loggers\DHL_Milestones {}.log'.format(today)
file_handler = logging.FileHandler(location)
# indicating the format that we set
file_handler.setFormatter(formatter)
# combining the logger with file
logger.addHandler(file_handler)
# indicating that process is on the way
logger.info('Procedure for checking DHL milestones has been started')

# setting up variable for files processed by pandas
dhl_td_optilo = ""
dhl_ltl_optilo = ""
dhl_report =""

# setting up chrome options and default folder for download
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\DATA"}
chromeOptions.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=chromeOptions)
browser.maximize_window()

# getting to the DHL page
logger.info("Entering DHL webpage")
browser.get('https://proview.dhl.com/proview/login')

# typing in the login details and submitting the details
browser.find_element_by_name('j_username').send_keys('Philipsmed')
browser.find_element_by_name('j_password').send_keys('Philips!19')
browser.find_element_by_class_name('buttonSubmit').click()

time.sleep(3)
# finding the total shipments
p = '/html/body/table[2]/tbody/tr/td[2]/div/div/div[4]/table[2]/tbody/tr[11]/td[3]/div/span/a'
# and clicking the value
browser.find_element_by_xpath(p).click()

# getting reference data as "shipped"
browser.find_element_by_xpath(r'//*[@id="filter"]/option[4]').click()

# checking the name of the today
checking_date = datetime.datetime.today().strftime("%A")

# if it is not monday it takes one day before
if not checking_date != 'Monday':
    datum = datetime.datetime.today() # - datetime.timedelta(1)
    datum = datum.strftime('%m/%d/%Y')
    datum_before = datetime.datetime.today() - datetime.timedelta(16)
    datum_before = datum_before.strftime('%m/%d/%Y')

# if it is monday it takes three days before
else:
    datum = datetime.datetime.today() #- datetime.timedelta(3)
    datum = datum.strftime('%m/%d/%Y')
    datum_before = datetime.datetime.today() - datetime.timedelta(16)
    datum_before = datum_before.strftime('%m/%d/%Y')

# getting the right dates for "date from" and "date to"

browser.find_element_by_id('filtervalue').send_keys(datum_before)
time.sleep(1)
browser.find_element_by_id('toDate').send_keys(datum)

# browser.find_element_by_id('filtervalue').send_keys(datum)
# time.sleep(1)
# browser.find_element_by_id('toDate').send_keys(datum)
time.sleep(2)
# click "find" option
browser.find_element_by_xpath('//*[@id="searchForm"]/table/tbody/tr/td[12]/div/a').click()
time.sleep(2)
# downloading the report
try:
    browser.find_element_by_xpath('//*[@id="exportTypes"]/a/span').click()

    time.sleep(3)
    logger.info("File with data has been downloaded")
    # setting up again date
    datum = datetime.datetime.today() # - datetime.timedelta(1)
    datum = datum.strftime('%d-%m-%Y')

    # going to directory
    os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\DATA')
    # going through each filename
    for dirpath, dirnames, filenames in os.walk(os.curdir):
        for naming in filenames:
            # if there is a file without hello in name
            print(naming)
            if naming[:3] == "Exp":
                # it corrects the file to the name we need for easier processing
                os.rename(naming, f'{datum}_DHL_Milestones.xls')
                dhl_report = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\DATA\{}_DHL_Milestones.xls'.format(datum)
                logger.info(f'File {dhl_report} will be verified with data extracted from Optilo in next steps')
                break
except:
    print("No data for indicated period or something went wrong while executing code")
# here is he code for downloading DHL reports from Optilo


browser.get("https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")
# loggin in
emailElem = browser.find_element_by_id('inpLogin')
emailElem.send_keys('maciej.janowski@philips.com')
# inputting password
password = browser.find_element_by_id('inpPassword')
password.send_keys('Maciej0312@')

# submitting logon details
buttonlog = browser.find_element_by_id('submitLogin')
buttonlog.click()


# finding multi tab
# multi = browser.find_element_by_id('menu-258664')
# multi = browser.find_element_by_id('menu-259381') update 2019-06-15
logger.info("Optilo TMS has been opened")
multi = browser.find_element_by_id('menu-1-259756')
multi.click()
# finding multi job tab
# joblist = browser.find_element_by_id('menu-258666')
# joblist = browser.find_element_by_id('menu-259383') update 2019-06-15
joblist = browser.find_element_by_id('menu-1-259756-259758')
joblist.click()

# wait for js to be loaded
time.sleep(3)

loadingdate = datetime.datetime.today() - datetime.timedelta(16)
loadingdate = loadingdate.strftime('%Y-%m-%d')
# finding loading date from field and sending date
startdate  = browser.find_element_by_id('DF650000161_start_plan_date_from')
startdate.send_keys(loadingdate)

# creating list of carriers to be checked
carriers = ['DHL-EXP-GL','DHL-LTL-EU']
# assign folder for adjusting names for the files
folder = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\DATA'
logger.info('Procedure for downloading the files for DHL TD and DHL LTL has been initiated')
for road in carriers:
    logger.info('Program is checking the jobs for {}'.format(road))
    time.sleep(3)
    # select carrier table to chose from
    car = browser.find_element_by_id('go_DF650000161_carrier_id_krt_kontrahent')
    car.click()
    time.sleep(3)
    # switch focus to current window
    x = browser.find_element_by_id('TB_iframeContent')
    browser.switch_to.frame(x)
    time.sleep(1)
    # type in name of the carrier
    name = browser.find_element_by_id('DF230000259_symbol')
    name.send_keys(road)
    time.sleep(1)
    # click search
    # search = browser.find_element_by_id('action[230000259][2123]') update 2019-06-15
    search = browser.find_element_by_id('action[230000259][2125]')
    search.click()
    time.sleep(1)
    # select the carrier
    selection = browser.find_element_by_xpath('//*[@id="DL230000260"]/tbody/tr[2]/td[1]/a')
    selection.click()
    time.sleep(1)
    # click search on a main page
    # search_again = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
    search_again = browser.find_element_by_id('action[650000161][3268]')
    search_again.click()
    time.sleep(3)
    try:
    # checking if the file will be available. If not - going to another carrier
        first_row = browser.find_element_by_xpath('//*[@id="DL650000162"]/tbody/tr[2]/td[1]/a')
        # downloaded report from Optilo
        button = browser.find_element_by_link_text("XLS")
        logger.info('file for {} has been downloaded'.format(road))
        button.click()
        time.sleep(10)

        # now we have to adjust the naming of the file
        # going to directory
        os.chdir(folder)
        # going through each filename
        for dirpath, dirnames, filenames in os.walk(os.curdir):
            for naming in filenames:
                # if there is a file without hello in name
                print(naming)
                if 'Multi' in naming:
                    # it corrects the file to the name we need for easier processing
                    os.rename(naming, f'MILESTONES - {road} {today}.xls')
                    logger.info(f' File "MILESTONES - {road} {today}.xls" has been downladed')
                    break
    except:
         # indicate that no shipment was found
        print("no file for carrier")

    # clear field for carrier
    browser.find_element_by_xpath('//*[@id="clear_DF650000161_carrier_id_krt_kontrahent"]/img').click()

# here is the code for extracting the data
dhl_ltl_optilo = r'MILESTONES - DHL-EXP-GL {}.xls'.format(today)
dhl_td_optilo =r'MILESTONES - DHL-LTL-EU {}.xls'.format(today)



logger.info("Procedure for verifying the data in pandas has been initiated")

# reading the csv file from DHL webpage
#dhl = pd.read_csv(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\Preparation\2019-06-22\DHL_MILESTONES_2019_06_22.csv')
dhl = pd.read_csv(dhl_report)

# is renaming the columns to help me a little bit with table management
dhl.rename({'Number of Pieces':'MJB_Number','Has Piece Identifier':'Status required in Optilo'},axis = 'columns',inplace=True)


# iterate through rows
for index, rows in dhl.iterrows():
    # assigns thata with potential MJB number
    mjb = dhl.iloc[index,4]
    # checks if we have string in mjb variable
    if isinstance(mjb,str):
        # finds location of MJB
        mjb_no = mjb.find('MJB')
        # extracts MJB number
        dhl.iloc[index,0] = mjb[mjb_no:mjb_no+10].strip()
        # checks the DHL status
    status = dhl.iloc[index,3]
    # checks if we have string in status variable
    if isinstance(status,str):
    # if shipment has delivered in cell
        if 'DELIVERED' in status.upper():
            # assigns "delivered" status from optilo
            dhl.iloc[index,6] = '600 Finished'
            # if shipment does not have data received in cell
        elif 'Shipment Data Received' not in status:
            # shipment is assigned with "on the way"  status
            dhl.iloc[index,6] = '450 On the way'

# deletes all rows that do not have any update regarding jobs
dhl = dhl[dhl['MJB_Number'].str.contains("MJB")]
logger.info("Cleaning of the data from DHL site has been done")


# create dataframe for both DHL carriers
# DHL_TD = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\OPTILO_REPORT\DHL_EXPRESS_TD_2019_06_22.xls')
# DHL_LTL = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\OPTILO_REPORT\DHL_LTL_2019_06_22.xls')
logger.info('Creating dataframes for DHL files')
DHL_TD = pd.read_excel(dhl_td_optilo)
DHL_LTL = pd.read_excel(dhl_ltl_optilo)


# concatonate the two DHL tables
DHL_TOTAL = pd.concat([DHL_TD,DHL_LTL],ignore_index=True)
logger.info("Reports from Optilo have been concatonated")

# joing both tables
DHL_JOIN = dhl.join(DHL_TOTAL.set_index('Number'),on = "MJB_Number")
logger.info("Data from Optilo has been joined with data from DHL site. Program is further adapting the data")


# columns to be delete DHL_JOIN.drop(columns=['Service Type','Receiver','Last Event date Offset','Further details','Next steps','Content Description','Signed by','External number','Service type','Service level','Transport type','Incoterms','Incoterms location','Vehicle group','Vehicle','Prebooked','Start type','End type','Start port','End port','Start terminal','End terminal','Carrier status','Custom Exit Point','Oru Payer','PF Requested','Reference1','Reference2','Reference3','Reference4','Reference5','Company','Cost contract','Income contract','Carrier symbol','Event list id','Documents List','Income status','Cost status','Order references','Carrier External Reference'],inplace=True)
DHL_JOIN.drop(columns=['Shipper','Service Type','Receiver','Last Event date Offset','Further details',
                       'Next steps','Content Description','Signed by','External number','Service type','Service level',
                       'Transport type','Incoterms','Incoterms location','Vehicle group','Vehicle','Prebooked',
                       'Start type','End type','Start port','End port','Start terminal','End terminal','Carrier status',
                       'Custom Exit Point','Oru Payer','PF Requested','Reference1','Reference2','Reference3',
                       'Reference4','Reference5','Company','Cost contract','Income contract','Carrier symbol',
                       'Event list id','Documents List','Income status','Cost status','Order references',
                       'Carrier External Reference'],inplace=True)

# leave only shipments that are not finished in Optilo
DHL_JOIN = DHL_JOIN[DHL_JOIN['Operational status']!= '600 Finished']
er_status = 0
# Creates a dataframe for those that has to be removed because parser didn't extract properly the data from file and
# Have some hiccup as for operational status
DHL_FOR_CHECKING = DHL_JOIN[DHL_JOIN['Operational status'].isna()]
error_file = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\ERRORS\DHL_ERRORS_{}.xls'.format(today)
try:
    # sends data with NA status to Excel file for further attaching it to the email
    DHL_FOR_CHECKING.to_excel(error_file)
    er_status = 1
    logger.info("File with errors for manual checking has been generated")
except:
    print("No file with errors to dump")

# Clears the dataframe and leaves only those values that are with something as for shipment status
DHL_JOIN = DHL_JOIN[DHL_JOIN['Operational status'].notna()]

# Leaves only those that have different status
DHL_JOIN[DHL_JOIN['Status required in Optilo'] != DHL_JOIN['Operational status']]


# Trimming the status columns
# DHL_JOIN['Status required in Optilo'] = DHL_JOIN['Status required in Optilo'].apply(lambda x: x.strip())
# DHL_JOIN['Operational status'] = DHL_JOIN['Operational status'].apply(lambda x: x.strip())

# leave only shipments that are not finished in Optilo and have relevant MJB number
DHL_JOIN = DHL_JOIN[DHL_JOIN['MJB_Number'].str.len() < 13]


DHL_JOIN.reset_index(inplace=True,drop = True)

# create list for changing the status of the shipment in the system
logger.info("Program will now generate the list of MJB numbers with details")
DHL_LIST =[]


# iterate through rows
for index, rows in DHL_JOIN.iterrows():
    # assigns thata with potential MJB number
    status_dhl = DHL_JOIN.iloc[index,5]
    status_optilo = DHL_JOIN.iloc[index,8]
    # if statuses are different
    if status_dhl != status_optilo:
        # create dictionary
        shipment = {}
        # assigns MJB number
        shipment['MJB'] = DHL_JOIN.iloc[index,0]
        # format and assign last event date
        lastevent = datetime.datetime.strptime(DHL_JOIN.iloc[index,2],"%d/%m/%Y %H:%M")
        shipment['Last Event Date'] = lastevent.strftime("%Y-%m-%d %H:%M")
        # assign status to be in optilo
        shipment['Status_To_Be'] = DHL_JOIN.iloc[index,5]
        shipment["Status_As_Is"] = DHL_JOIN.iloc[index,8]
        actualpickup = datetime.datetime.strptime(DHL_JOIN.iloc[index,6],"%d/%m/%Y %H:%M")
        shipment['Actual Pickup Date'] = actualpickup.strftime("%Y-%m-%d %H:%M")
        # assigns Waybill number
        shipment['Waybill'] = DHL_JOIN.iloc[index,1]
        # appending to the list
        DHL_LIST.append(shipment)

print(DHL_LIST)
logger.info("List has been generated")
logger.info(DHL_LIST)
k=""
for x in DHL_LIST:
    k = k+str(x)+"\n"


outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'DHL MILESTONES - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = k
mail.Send()


quit()
logger.info("Program is entering Optilo to update the statuses of the shipments")
# here is the code for playing with Optilo
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
mjb_catalog = {}
# loops through all DHL reference numbers
logger.info("Logged to Opitlo and now will loop through the list of DHL shipments")
for processed_mjb in DHL_LIST:
    try:
        line = processed_mjb['MJB']
        # finding multi tab
        # multi = browser.find_element_by_id('menu-258664')
        # multi = browser.find_element_by_id('menu-259381') update 2019-06-15
        multi = browser.find_element_by_id('menu-1-259756')
        multi.click()
        # finding multi job tab
        # joblist = browser.find_element_by_id('menu-258666')
        # joblist = browser.find_element_by_id('menu-259383') update 2019-06-15
        joblist = browser.find_element_by_id('menu-1-259756-259758')
        joblist.click()
        # finding box for job number
        jobnumber = browser.find_element_by_id('DF650000161_number')
        jobnumber.clear()
        # looping through each job number
        jobnumber.send_keys(line)
        time.sleep(3)
        # finding search button
        # searching = browser.find_element_by_id('action[650000161][1529675]')
        # searching = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
        searching = browser.find_element_by_id('action[650000161][3268]')
        searching.click()
        # finding button button and clicking it
        time.sleep(2)
        buttonforjob = browser.find_element_by_link_text(line)
        buttonforjob.click()
        time.sleep(3)
        # assigns variables that will enable me to further access site menu
        load_tab = 0
        way_tab = 0
        finish_tab = 0
        delivered = "600 Finished"
        otw = '450 On the way'
        confirm = '290 Confirmed by carrier'
        to_be = processed_mjb['Status_To_Be']
        as_is = processed_mjb['Status_As_Is']
        first = processed_mjb['Actual Pickup Date']
        second = processed_mjb['Last Event Date']
        waybill = processed_mjb['Waybill']
        logger.info(f"Variable for {processed_mjb['MJB']} has been generated")
        # get mail url for mjb
        current_address = browser.current_url
    # find table "job process"
        table = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul')
        # check the number of rows in the table
        rows = len(table.find_elements_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li'))
        # loop through each row of the table
        for x in range(2, rows):
            checking = table.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(x))
            # checking the text of each field
            value = checking.text
            # if LOAD is in the field
            if "LOAD" in value.upper():
                load_tab = x
            elif "ON THE WAY" in value.upper():
                way_tab = x
            elif "FINISH" in value.upper():
                finish_tab = x
        # part for clicking loaded status
        logger.info(f"Program is now checking the details for {processed_mjb['MJB']}")
        # OPTION 1 - DHL indicating delivered and Optilo is only on confirmed by carrier
        if to_be == delivered and as_is == confirm:
            # it assigns element to the variable
            ship_load = browser.find_element_by_xpath(
                '//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(load_tab))
            # is clicking the load button
            ship_load.click()
            # find fields for date entry on next page
            date_entry = browser.find_element_by_name('DF650000270_param1')
            # finish the cancellation by clicking the second button
            date_entry.send_keys(first)
            # find buttons for status loaded
            button_loaded = browser.find_element_by_id('action[650000270][3274]')
            # clicks button for loaded
            button_loaded.click()
            logger.info(f"{processed_mjb['MJB']} has been switched to LOADED")
            # part for clicking on the way status
            # assigns element to the variable
            on_the_way = browser.find_element_by_xpath(
                '//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(way_tab))
            # is clicking the load button
            on_the_way.click()
            # find buttons for status on the way
            button_way = browser.find_element_by_id('action[650000270][3274]')
            # clicks button for on the way
            button_way.click()
            logger.info(f"{processed_mjb['MJB']} has been switched to ON THE WAY")
            # part for clicking finish status
            # assigns element to the variable
            finishing = browser.find_element_by_xpath(
                '//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(finish_tab))
            # is clicking the load button
            finishing.click()
            # find fields for date entry on next page
            date_entry_finish = browser.find_element_by_name('DF650000270_param1')
            # finish the cancellation by clicking the second button
            date_entry_finish.send_keys(second)
            # find buttons for status finish
            button_ending = browser.find_element_by_id('action[650000270][3274]')
            # clicks button for on the way
            button_ending.click()
            logger.info(f"{processed_mjb['MJB']} has been switched to FINISHED")
            # getting to dhl page
            logger.info(f"Procedure for POD for {processed_mjb['MJB']} has been initiated")
            browser.get(f'https://www.dhl.nl/exp-en/express/tracking.html?AWB={waybill}&brand=DHL')
            pathing = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill)
            # making a screenshot with details regarding delivery
            browser.get_screenshot_as_file(pathing)
            logger.info(f"File for {processed_mjb['MJB']} has been downloaded")
            # uploading the file
            web_address = str(current_address)
            # replace jobdetails to jobcosts and go the site with costs
            newaddress = web_address.replace('JobDetails', 'JobFiles')
            # going to new files tab
            browser.get(newaddress)
            time.sleep(3)
            # finding this freaking hidden option to upload
            upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
            # uploading the file
            upload_file.send_keys(
                r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(
                f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[53]")
            time.sleep(6)
            document.click()
            time.sleep(2)
            saving = browser.find_element_by_name('action_dp[650000192][Z][save]')
            saving.click()
            logger.info(f"File for {processed_mjb['MJB']} has been uploaded to the system")
            # is deleting folder with POD
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD')
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones')
            # and creating the new one
            os.mkdir('POD')
















        # OPTION 2 - DHL stating that shipment is delivered but Optilo is on the way status
        elif to_be == delivered and as_is == otw:
            # part for clicking finish status
            # assigns element to the variable
            finishing = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(finish_tab))
            # is clicking the load button
            finishing.click()
            # find fields for date entry on next page
            date_entry_finish = browser.find_element_by_name('DF650000270_param1')
            # finish the cancellation by clicking the second button
            date_entry_finish.send_keys(first)
            # find buttons for finish
            button_ending = browser.find_element_by_id('action[650000270][3274]')
            # clicks button for on the way
            button_ending.click()
            logger.info(f"{processed_mjb['MJB']} has been switched to FINISHED")
            # getting to dhl page
            logger.info(f"Procedure for POD for {processed_mjb['MJB']} has been initiated")
            browser.get(f'https://www.dhl.nl/exp-en/express/tracking.html?AWB={waybill}&brand=DHL')
            pathing = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill)
            # making a screenshot with details regarding delivery
            browser.get_screenshot_as_file(pathing)
            logger.info(f"File for {processed_mjb['MJB']} has been downloaded")
            # uploading the file
            web_address = str(current_address)
            # replace jobdetails to jobcosts and go the site with costs
            newaddress = web_address.replace('JobDetails', 'JobFiles')
            # going to new files tab
            browser.get(newaddress)
            time.sleep(3)
            # finding this freaking hidden option to upload
            upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
            # uploading the file
            upload_file.send_keys(
                r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(2)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(
                f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[53]")
            time.sleep(6)
            document.click()
            time.sleep(2)
            saving = browser.find_element_by_name('action_dp[650000192][Z][save]')
            saving.click()
            logger.info(f"File for {processed_mjb['MJB']} has been uploaded to the system")
            # is deleting folder with POD
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD')
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones')
            # and creating the new one
            os.mkdir('POD')


        # OPTION 3 - DHL status indicates that shipment is on the way and Optilo stating confirmed by carrier
        elif to_be == otw and as_is == confirm:
            # part for clicking loaded
            # it assigns element to the variable
            ship_load = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(load_tab))
            # is clicking the load button
            ship_load.click()
            # find fields for date entry on next page
            date_entry = browser.find_element_by_name('DF650000270_param1')
            # finish the cancellation by clicking the second button
            date_entry.send_keys(first)
            # find buttons for status loaded
            button_loaded = browser.find_element_by_id('action[650000270][3274]')
            # clicks button for loaded
            button_loaded.click()
            logger.info(f"{processed_mjb['MJB']} has been switched to LOADED")
            # part for clicking on the way status
            # assigns element to the variable
            on_the_way = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(way_tab))
            # is clicking the load button
            on_the_way.click()
            # find buttons for status on the way
            button_way = browser.find_element_by_id('action[650000270][3274]')
            # clicks button for on the way
            button_way.click()
            logger.info(f"{processed_mjb['MJB']} has been switched to ON THE WAY")
        # # part for clicking finish status
        # # assigns element to the variable
        # finishing = browser.find_element_by_xpath('//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(finish_tab))
        # # is clicking the load button
        # finishing.click()
        # # find fields for date entry on next page
        # date_entry_finish = browser.find_element_by_name('DF650000270_param1')
        # # finish the cancellation by clicking the second button
        # date_entry_finish.send_keys('2019-06-20 13:35')
        # # find buttons for status on the way
        # button_ending = browser.find_element_by_id('action[650000270][3274]')
        # # clicks button for on the way
        # button_ending.click()
        browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=startpage')
    except:
        print("Something went wrong")


# Creating text for email
e_text = ""
for index,rows in DHL_JOIN.iterrows():
    if DHL_JOIN.iloc[index,5] != True :
        e_text = e_text +"<p><b>" +  f'{DHL_JOIN.iloc[index,0]} updated to {DHL_JOIN.iloc[index,5]}' + "</b></p>" + "\n"

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
logger.info("Mail has been generated")
# mail.To = 'DL_PCTPolandOptilo@philips.com'
mail.To = 'maciej.janowski@philips.com'
mail.Subject = 'DHL MILESTONES - ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
mail.Body = 'Test'
mail.HTMLBody = '<p>Dear Team,</p><p>Would like to inform you that DHL MILESTONES are processed</p>' \
                '<p>Full log of procedure in the attachment</p>' \
                '<p>Summary of updates:</p>' + e_text + '<p>Cheers,</p><p>Maciej Janowski</p>' \
              '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
              '<p>PCT Poland</p>'
# attaching log file
attachment = location
mail.Attachments.Add(attachment)
# checing if file wih errors has been generated
if er_status ==1:
    mail.Attachments.Add(error_file)
# sending email
mail.Save()

