from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

# reading data with spots
df = pd.read_excel(r"C:\Users\210295192\Desktop\Python\Projects\SPOT_QUOTES_INFODIS\SPOT_QUOTES_INFODIS.xlsx",sheet_name='AIR')

# creating dictionary for values
spots = {}

# iterating through rows
for index, row in df.iterrows():
    # if spot is for full value
    if row['full_or_breakdown'] == 'full':
        # assign total pricing and currency
        pricing = {'total': row['total'], 'currency': row['currency']}
        # add to dictionary storing all spot quotes
        spots[row['Ref_num']] = pricing
        # if spot is with cost breakdown
    elif row['full_or_breakdown'] == 'breakdown':
        # assign proper cost for each indicationn
        pricing = {'pickup': row['pickup'] * row['chargeable_weight'],
                   'handling_origin': row['handling_origin'] * row['chargeable_weight'],
                   "customs_origin": row['customs_origin'],
                   "airfreight": row['freight'] * row['chargeable_weight'],
                   "handling_dest": row['handling_dest'] * row['chargeable_weight'],
                   "customs_dest": row['customs_dest'],
                   "delivery": row['delivery'] * row['chargeable_weight'],
                   "screening": row['screening'] * row['chargeable_weight'],
                   'currency': row['currency']}
        # add to dictionary storing all spot quotes
        spots[row['Ref_num']] = pricing

# assigning info that spot is added
df['added'] = 'yes'

# saving data frame to file
df.to_excel(r"C:\Users\210295192\Desktop\Python\Projects\SPOT_QUOTES_INFODIS\SPOT_QUOTES_INFODIS.xlsx",sheet_name='AIR',index=False)

# opening browser and getting to infodis
browser = webdriver.Chrome()
browser.get \
    ("https://www.infodis.net/philips/net/LogOn/Authenticate?returnUrl=https%2a%2f%2fwww.infodis.net%2fphilips%2fnet%2f")
browser.find_element_by_id('LogOnName').send_keys('210295192')
browser.find_element_by_id('Password').send_keys("Maciej1992")
browser.find_element_by_xpath('//*[@id="form-login"]/div/div[1]/div[1]/div/span[1]').click()

# looping through all costs
for shipment,costs in spots.items():
    # typing shipment number
    browser.get('https://www.infodis.net/philips/net/Shipment/Search')
    search = browser.find_element_by_id('Reference_ReferenceValue')
    search.send_keys(shipment)
    # searching shipment
    button = browser.find_element_by_xpath('//*[@id="btnAdvSearch"]/span[2]')
    button.click()
    # double click to open the shipment
    selection = browser.find_element_by_xpath('//*[@id="ShipmentSearchResult"]/tbody/tr')
    actionChains = ActionChains(browser)
    actionChains.double_click(selection).perform()
    # if there is only total cost to be added
    if len(costs) == 2:
        # assign helping variables
        no_of_options = len(browser.find_elements_by_xpath('//*[@id="shipment-details-menu-2"]/li'))
        lets_modify = 0
        # looping through the menu to find cost addition option

        for x in range(1, no_of_options + 1):
            # finding the title of the button
            title = browser.find_element_by_xpath('//*[@id="shipment-details-menu-2"]/li[{}]/a'.format(x)).get_attribute(
                'title')
            # check if button has "cost" in the title. If yes - then assign value
            # if buttoon has costs leg
            if "costs leg" in title:
                # assign button number
                lets_modify = x
        #   clilck button to add costs
        browser.find_element_by_xpath('//*[@id="shipment-details-menu-opener-2"]/span[1]').click()
        browser.find_element_by_xpath('//*[@id="shipment-details-menu-2"]/li[{}]/a/span[1]'.format(lets_modify)).click()

        # assign windows 
        window_before = browser.window_handles[0]
        window_after = browser.window_handles[1]

    # switch window
        browser.switch_to.window(window_after)
        # finding and switching to new frame
        frame = browser.find_element_by_name('shipmentactionform')
        browser.switch_to.frame(frame)
        # selecting the type of cost
        browser.find_element_by_xpath('//*[@id="maintable"]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/select/option[26]').click()
        # sending value of cost
        browser.find_element_by_name('txtServiceAmount').send_keys(costs['total'])
        # finding and switching to frame with ok button
        frame = browser.find_element_by_name('popupbuttons')
        browser.switch_to.frame(frame)
        # clicking the button to submit cost
        cancel = browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/input[2]')
        cancel.click()
        # switching back to previous window
        browser.switch_to.window(window_before)
    else:
        for description, amount in costs.items():
            if description == 'pickup':
                # assign helping variables
                no_of_options = len(browser.find_elements_by_xpath('//*[@id="shipment-details-menu-2"]/li'))
                lets_modify = 0
                # looping through the menu to find cost addition option

                for x in range(1, no_of_options + 1):
                    # finding the title of the button
                    title = browser.find_element_by_xpath(
                        '//*[@id="shipment-details-menu-2"]/li[{}]/a'.format(x)).get_attribute(
                        'title')
                    # check if button has "cost" in the title. If yes - then assign value
                    # if buttoon has costs leg
                    if "costs leg" in title:
                        # assign button number
                        lets_modify = x
                #   clilck button to add costs
                browser.find_element_by_xpath('//*[@id="shipment-details-menu-opener-2"]/span[1]').click()
                browser.find_element_by_xpath(
                    '//*[@id="shipment-details-menu-2"]/li[{}]/a/span[1]'.format(lets_modify)).click()

                # assign windows 
                window_before = browser.window_handles[0]
                window_after = browser.window_handles[1]

                # switch window
                browser.switch_to.window(window_after)
                # finding and switching to new frame
                frame = browser.find_element_by_name('shipmentactionform')
                browser.switch_to.frame(frame)
                # selecting the type of cost
                browser.find_element_by_xpath(
                    '//*[@id="maintable"]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/select/option[26]').click()
                # sending value of cost
                browser.find_element_by_name('txtServiceAmount').send_keys(costs['total'])
                # finding and switching to frame with ok button
                frame = browser.find_element_by_name('popupbuttons')
                browser.switch_to.frame(frame)
                # clicking the button to submit cost
                cancel = browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/input[2]')
                cancel.click()
                # switching back to previous window
                browser.switch_to.window(window_before)
            elif description == 'delivery':
                # assign helping variables
                no_of_options = len(browser.find_elements_by_xpath('//*[@id="shipment-details-menu-4"]/li'))
                lets_modify = 0
                # looping through the menu to find cost addition option

                for x in range(1, no_of_options + 1):
                    # finding the title of the button
                    title = browser.find_element_by_xpath(
                        '//*[@id="shipment-details-menu-4"]/li[{}]/a'.format(x)).get_attribute(
                        'title')
                    # check if button has "cost" in the title. If yes - then assign value
                    # if buttoon has costs leg
                    if "costs leg" in title:
                        # assign button number
                        lets_modify = x
                #   clilck button to add costs
                browser.find_element_by_xpath('//*[@id="shipment-details-menu-opener-4"]/span[1]').click()
                browser.find_element_by_xpath(
                    '//*[@id="shipment-details-menu-4"]/li[{}]/a/span[1]'.format(lets_modify)).click()

                # assign windows 
                window_before = browser.window_handles[0]
                window_after = browser.window_handles[1]

                # switch window
                browser.switch_to.window(window_after)
                # finding and switching to new frame
                frame = browser.find_element_by_name('shipmentactionform')
                browser.switch_to.frame(frame)
                # selecting the type of cost
                browser.find_element_by_xpath(
                    '//*[@id="maintable"]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/select/option[26]').click()
                # sending value of cost
                browser.find_element_by_name('txtServiceAmount').send_keys(costs['total'])
                # finding and switching to frame with ok button
                frame = browser.find_element_by_name('popupbuttons')
                browser.switch_to.frame(frame)
                # clicking the button to submit cost
                cancel = browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/input[2]')
                cancel.click()
                # switching back to previous window
                browser.switch_to.window(window_before)
            else:
                # assign helping variables
                no_of_options = len(browser.find_elements_by_xpath('//*[@id="shipment-details-menu-2"]/li'))
                lets_modify = 0
                # looping through the menu to find cost addition option

                for x in range(1, no_of_options + 1):
                    # finding the title of the button
                    title = browser.find_element_by_xpath(
                        '//*[@id="shipment-details-menu-2"]/li[{}]/a'.format(x)).get_attribute(
                        'title')
                    # check if button has "cost" in the title. If yes - then assign value
                    # if buttoon has costs leg
                    if "costs leg" in title:
                        # assign button number
                        lets_modify = x
                #   clilck button to add costs
                browser.find_element_by_xpath('//*[@id="shipment-details-menu-opener-2"]/span[1]').click()
                browser.find_element_by_xpath(
                    '//*[@id="shipment-details-menu-2"]/li[{}]/a/span[1]'.format(lets_modify)).click()

                # assign windows 
                window_before = browser.window_handles[0]
                window_after = browser.window_handles[1]

                # switch window
                browser.switch_to.window(window_after)
                # finding and switching to new frame
                frame = browser.find_element_by_name('shipmentactionform')
                browser.switch_to.frame(frame)
                # selecting the type of cost
                browser.find_element_by_xpath(
                    '//*[@id="maintable"]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/select/option[26]').click()
                # sending value of cost
                browser.find_element_by_name('txtServiceAmount').send_keys(costs['total'])
                # finding and switching to frame with ok button
                frame = browser.find_element_by_name('popupbuttons')
                browser.switch_to.frame(frame)
                # clicking the button to submit cost
                cancel = browser.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/input[2]')
                cancel.click()
                # switching back to previous window
                browser.switch_to.window(window_before)


