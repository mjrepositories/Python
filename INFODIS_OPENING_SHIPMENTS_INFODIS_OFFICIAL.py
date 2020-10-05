'''Program was created to open a lot of shipments just to have the full visibility insteaad of click
multiple times shipments. And now i have the idea to also take it to "modify" mode if needed'''
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

modification = input('Open or modify shipments? Type "o" or "m": ')
# name of the file
x = r'C:\Users\310295192\Desktop\Python\Projects\OPENING_SHIPMENTS_INFODIS\shipments.xlsx'
df = pd.read_excel(x)

# create list of shipments to check
shipping = list(df['Shipment ID'])

browser= webdriver.Chrome()
counter = 0
# getting to infodis
browser.get("https://www.infodis.net/philips/net/LogOn/Authenticate?returnUrl=https%3a%2f%2fwww.infodis.net%2fphilips%2fnet%2f")
browser.find_element_by_id('LogOnName').send_keys('310295192')
browser.find_element_by_id('Password').send_keys("1993Maciej")
browser.find_element_by_xpath('//*[@id="form-login"]/div/div[1]/div[1]/div/span[1]').click()

# getting to infodis search engine
browser.get('https://www.infodis.net/philips/net/Shipment/Search')
time.sleep(3)
for ship in shipping:
    # sending the shipment number for checking
    searching = browser.find_element_by_name('Reference.ReferenceValue').send_keys(ship)
    time.sleep(5)
    # clicking search button
    browser.find_element_by_xpath('//*[@id="btnAdvSearch"]/span[2]').click()
    time.sleep(8)

    # double clicking
    try:
        # finding the firts row available
        selection = browser.find_element_by_xpath('//*[@id="ShipmentSearchResult"]/tbody/tr')
        # double click action
        actionChains = ActionChains(browser)
        actionChains.double_click(selection).perform()
        time.sleep(6)
    except:
        print(f'Shipment {ship} is not visible')
    # finding shipment tab
    # finding modify button
    if modification == 'm':
        browser.find_element_by_xpath('//*[@id="shipment-details-menu-opener-1"]/span[1]').click()
        time.sleep(2)
        # find number of buttons after clicking shipment
        no_of_options = len(browser.find_elements_by_xpath('//*[@id="shipment-details-menu-1"]/li'))
        lets_modify = 0
        # loop through all the buttons
        for x in range(1,no_of_options+1):
            title = browser.find_element_by_xpath('//*[@id="shipment-details-menu-1"]/li[{}]/a'.format(x)).get_attribute('title')
            # check if button has "Modify" in title. If has - assign location
            if "Modify" in title:
                lets_modify = x

        # click modify button
        browser.find_element_by_xpath('//*[@id="shipment-details-menu-1"]/li[{}]/a/span[1]'.format(lets_modify)).click()


        # unselecting send transportation order
        time.sleep(4)

        # checking table rows
        rows = len(browser.find_elements_by_xpath('//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr'))

# assigning rows for sending order and booking confirmation
        send_order = 0
        confirmation = 0

        for x in range(1, rows + 1):
            looking = browser.find_element_by_xpath('//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[{}]'.format(x))
            if 'Send transportation order' in looking.text:
                send_order = x
            elif 'Booking confirmation' in looking.text:
                confirmation = x

        #  click radio button
        browser.find_element_by_xpath('//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[2]/input[1]'.format(send_order)).click()

        # looking for checkbox

        checkbox = browser.find_element_by_xpath('//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[2]/table/tbody/tr/td[1]/input'.format(confirmation))

        if checkbox.get_property('checked') == True:
            checkbox.click()

    from selenium.webdriver.common.keys import Keys

    # browser.execute_script('window.open("https://www.infodis.net/philips/net/Shipment/Search","new window")')
    browser.execute_script("window.open('https://www.infodis.net/philips/net/Shipment/Search', '_blank')")

    counter += 1
    browser.switch_to.window(browser.window_handles[counter])










