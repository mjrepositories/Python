from selenium import webdriver
import pandas as pd
import time
import datetime

print(datetime.datetime.now())
# name of the file
x = r'C:\Users\310295192\Desktop\Python\Projects\REPROCESSING_OPTILO\shipments.xlsx'
df = pd.read_excel(x)

# create list of shipments to check
mjb_catalog = list(df['Shipment ID'])


tt=""
change_truck = input('Want to change truck and reprocess (t) or only reprocess (r) : ')
if change_truck == "t":
    tt = input("Provide the type truck that has to be selected: ")

browser = webdriver.Chrome()
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
# created list for mjbs checked
#loops through all MJB numbers
for mjb_no in mjb_catalog:
    browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')
    # finding box for job number
    jobnumber = browser.find_element_by_id('DF650000161_number')
    jobnumber.clear()
    # looping through each job number
    jobnumber.send_keys(mjb_no)
    time.sleep(3)
    # finding search button
    # searching = browser.find_element_by_id('action[650000161][1529675]')
    # searching = browser.find_element_by_id('action[650000161][3242]') update 2019-06-15
    searching = browser.find_element_by_id('action[650000161][3275]')
    searching.click()
    # finding button button and clicking it
    time.sleep(2.5)
    buttonforjob = browser.find_element_by_link_text(mjb_no)
    buttonforjob.click()
    time.sleep(3)

    if change_truck == 't':
        try:
            editing = browser.find_element_by_id('action[650000229][3243]')
        except:
            editing = browser.find_element_by_id('action[650000229][3237]')

        # click edit button
        editing.click()
        time.sleep(1)

        rows = len(browser.find_elements_by_xpath('//*[@id="DF650000229_transport_id_slw_transport_grupa"]/option'))
        for trucking in range(2,rows+1):
            line  = browser.find_element_by_xpath('//*[@id="DF650000229_transport_id_slw_transport_grupa"]/option[{}]'.format(trucking))
            ciezarowka = line.get_attribute('value')
            if ciezarowka == tt:
                line.click()
                # save
                browser.find_element_by_id('action[650000229][3252]').click()

    current_address = browser.current_url
    # turn to string
    web_address = str(current_address)
    # replace jobdetails to jobcosts and go the site with costs
    newaddress = web_address.replace('JobDetails', 'JobCosts')
    browser.get(newaddress)
    time.sleep(5)
    # finding the recalculation button and clicks it
    recalculate = browser.find_element_by_name('action[650000281][920]')
    recalculate.click()
    time.sleep(3)

print(datetime.datetime.now())