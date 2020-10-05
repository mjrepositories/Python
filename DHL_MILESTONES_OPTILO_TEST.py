from selenium import webdriver
import time
import os
import datetime
import win32com.client
import shutil

browser = webdriver.Chrome()
# getting to Optilo
optilo = 'https://ot3.optilo.eu/opt_ext_po0dyx/t010/main.php?m=cwlib&c=login'
browser.get(optilo)
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

DHL_LIST = [{'MJB': 'MJB9001137',
  'Last Event Date': '2019-06-28 11:29',
  'Status_To_Be': '600 Finished',
  'Status_As_Is': '290 Confirmed by carrier',
  'Actual Pickup Date': '2019-06-27 08:55',
  'Waybill': 3069377942},{'MJB': 'MJB9000939',
  'Last Event Date': '2019-06-28 11:29',
  'Status_To_Be': '600 Finished',
  'Status_As_Is': '450 On the way',
  'Actual Pickup Date': '2019-06-27 08:55',
  'Waybill': 3069377942},{'MJB': 'MJB9001121',
  'Last Event Date': '2019-06-28 11:29',
  'Status_To_Be': '450 On the way',
  'Status_As_Is': '290 Confirmed by carrier',
  'Actual Pickup Date': '2019-06-27 08:55',
  'Waybill': 3069377942}]
for processed_mjb in DHL_LIST:
    try:
        line = processed_mjb['MJB']
        # finding multi tab
        # multi = browser.find_element_by_id('menu-258664')
        # multi = browser.find_element_by_id('menu-259381') update 2019-06-15
        multi = browser.find_element_by_id('menu-1-309690')
        multi.click()
        # finding multi job tab
        # joblist = browser.find_element_by_id('menu-258666')
        # joblist = browser.find_element_by_id('menu-259383') update 2019-06-15
        joblist = browser.find_element_by_id('menu-1-309690-309692')
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
        print(load_tab)
        print(way_tab)
        print(finish_tab)
        # part for clicking loaded status
        print(f"Program is now checking the details for {processed_mjb['MJB']}")
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
            button_loaded = browser.find_element_by_id('action[650000270][3300]')
            # clicks button for loaded
            button_loaded.click()
            print(f"{processed_mjb['MJB']} has been switched to LOADED")
            # part for clicking on the way status
            # assigns element to the variable
            print('Tutaj wywali')
            browser.get(current_address)
            time.sleep(5)
            on_the_way = browser.find_element_by_xpath(
                '//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(way_tab))
            print(on_the_way)
            # is clicking the load button
            print('on the way znalazlo')
            on_the_way.click()
            time.sleep(5)
            # find buttons for status on the way
            button_way = browser.find_element_by_id('action[650000270][3300]')
            # clicks button for on the way
            button_way.click()
            print(f"{processed_mjb['MJB']} has been switched to ON THE WAY")
            time.sleep(2)
            # part for clicking finish status
            browser.get(current_address)
            time.sleep(5)
            # assigns element to the variable
            finishing = browser.find_element_by_xpath(
                '//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(finish_tab))
            # is clicking the load button
            finishing.click()
            time.sleep(2)
            # find fields for date entry on next page
            date_entry_finish = browser.find_element_by_name('DF650000270_param1')
            # finish the cancellation by clicking the second button
            date_entry_finish.send_keys(second)
            # find buttons for status finish
            button_ending = browser.find_element_by_id('action[650000270][3300]')
            # clicks button for on the way
            button_ending.click()
            time.sleep(2)
            print(f"{processed_mjb['MJB']} has been switched to FINISHED")
            # getting to dhl page
            print(f"Procedure for POD for {processed_mjb['MJB']} has been initiated")
            browser.get(f'https://www.dhl.nl/exp-en/express/tracking.html?AWB={waybill}&brand=DHL')
            pathing = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill)
            time.sleep(5)
            # making a screenshot with details regarding delivery
            browser.get_screenshot_as_file(pathing)
            print(f"File for {processed_mjb['MJB']} has been downloaded")
            # uploading the file
            time.sleep(2)
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
            print(f"File for {processed_mjb['MJB']} has been uploaded to the system")
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
            time.sleep(2)
            # find fields for date entry on next page
            date_entry_finish = browser.find_element_by_name('DF650000270_param1')
            # finish the cancellation by clicking the second button
            date_entry_finish.send_keys(first)
            # find buttons for finish
            button_ending = browser.find_element_by_id('action[650000270][3300]')
            # clicks button for on the way
            button_ending.click()
            time.sleep(5)
            print(f"{processed_mjb['MJB']} has been switched to FINISHED")
            # getting to dhl page
            print(f"Procedure for POD for {processed_mjb['MJB']} has been initiated")
            browser.get(f'https://www.dhl.nl/exp-en/express/tracking.html?AWB={waybill}&brand=DHL')
            time.sleep(5)
            pathing = r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill)
            # making a screenshot with details regarding delivery
            browser.get_screenshot_as_file(pathing)
            print(f"File for {processed_mjb['MJB']} has been downloaded")
            # uploading the file
            time.sleep(2)
            web_address = str(current_address)
            # replace jobdetails to jobcosts and go the site with costs
            newaddress = web_address.replace('JobDetails', 'JobFiles')
            # going to new files tab
            browser.get(newaddress)
            time.sleep(5)
            # finding this freaking hidden option to upload
            upload_file = browser.find_element_by_css_selector('.dz-hidden-input')
            # uploading the file
            upload_file.send_keys(
                r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD\Tracking {}.png'.format(waybill))
            time.sleep(11)
            # counting number of columns
            row_count = len(browser.find_elements_by_xpath("//table[@id='DP650000192']/tbody/tr"))
            time.sleep(3)
            print(row_count)
            # finding document type
            document = browser.find_element_by_xpath(
                f"//table[@id='DP650000192']/tbody/tr[{row_count}]/td[5]/select/option[53]")
            time.sleep(6)
            document.click()
            time.sleep(2)
            saving = browser.find_element_by_name('action_dp[650000192][Z][save]')
            saving.click()
            print(f"File for {processed_mjb['MJB']} has been uploaded to the system")
            # is deleting folder with POD
            shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones\POD')
            os.chdir(r'C:\Users\310295192\Desktop\Python\Projects\DHL_Milestones')
            # and creating the new one
            os.mkdir('POD')


        # OPTION 3 - DHL status indicates that shipment is on the way and Optilo stating confirmed by carrier
        elif to_be == otw and as_is == confirm:
            # part for clicking loaded
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
            button_loaded = browser.find_element_by_id('action[650000270][3300]')
            # clicks button for loaded
            button_loaded.click()
            print(f"{processed_mjb['MJB']} has been switched to LOADED")
            # part for clicking on the way status
            # assigns element to the variable
            print('Tutaj wywali')
            browser.get(current_address)
            time.sleep(5)
            on_the_way = browser.find_element_by_xpath(
                '//*[@id="ZrodloKontekst-Proces"]/div/ul/li[{}]/a'.format(way_tab))
            print(on_the_way)
            # is clicking the load button
            print('on the way znalazlo')
            on_the_way.click()
            time.sleep(5)
            # find buttons for status on the way
            button_way = browser.find_element_by_id('action[650000270][3300]')
            # clicks button for on the way
            button_way.click()
            print(f"{processed_mjb['MJB']} has been switched to ON THE WAY")
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
        browser.get('https://ot3.optilo.eu/opt_ext_po0dyx/t010/main.php?m=cwlib&c=login')
    except:
        print("Something went wrong")


# Creating text for email
e_text = "Test"

# preparing email for what has been added and what was wrong
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
print("Mail has been generated")
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

# sending email
mail.Save()