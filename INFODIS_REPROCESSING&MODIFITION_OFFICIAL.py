from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import pandas as pd



# time.sleep(120)
browser = webdriver.Chrome()
# getting to infodis


# path to file with shipment numbers
x = r'C:\Users\310295192\Desktop\Python\Projects\OPENING_SHIPMENTS_INFODIS\shipments.xlsx'
df = pd.read_excel(x)

# create list of shipments to check
shipping = list(df['Shipment ID'])

# logging into system

browser.get \
    ("https://www.infodis.net/philips/net/LogOn/Authenticate?returnUrl=https%3a%2f%2fwww.infodis.net%2fphilips%2fnet%2f")
browser.find_element_by_id('LogOnName').send_keys('310295192')
browser.find_element_by_id('Password').send_keys("Maciej1993")
browser.find_element_by_xpath('//*[@id="form-login"]/div/div[1]/div[1]/div/span[1]').click()


counter = 0

# go to shipment modification
browser.get('https://www.infodis.net/philips/modifybooking.asp')

for infodis_num in shipping:
    # find reference box and sending data
    ref = browser.find_element_by_name('txtReference')
    ref.send_keys(infodis_num)
    ref.send_keys(Keys.ENTER)
    time.sleep(5)

    # finding result table
    try:
        result_table = browser.find_element_by_xpath('//*[@id="layout-center"]/div/div[2]/div/form/table[2]')
        # checking row number

        row_num = browser.find_elements_by_xpath \
            ('//*[@id="layout-center"]/div/div[2]/div/form/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr')
        row_num = len(row_num) +1

        # looping through the whole table
        for x in range(2, row_num):

            table_attribute = browser.find_element_by_xpath(
                '//*[@id="layout-center"]/div/div[2]/div/form/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[{}]/td[1]/a'.format(
                    x))
            # assigning text from the attribute
            ref_check = table_attribute.text

            # checking if attribue name is the same as looked reference number
            if ref_check == infodis_num:
                # if it is - click on link
                table_attribute.click()
    except:
        # just passing if we entered direcly modification form
        pass

    time.sleep(5)

    # checking table rows
    rows = len(browser.find_elements_by_xpath('//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr'))

    # assigning rows for sending order and booking confirmation
    send_order = 0
    confirmation = 0

    for x in range(1, rows + 1):
        looking = browser.find_element_by_xpath(
            '//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[{}]'.format(x))
        if 'Send transportation order' in looking.text:
            # finding the row for send order
            send_order = x
        elif 'Booking confirmation' in looking.text:
            # finding the row for confirmation
            confirmation = x

    #  click radio button
    browser.find_element_by_xpath(
        '//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[2]/input[1]'.format(
            send_order)).click()

    # looking for checkbox

    checkbox = browser.find_element_by_xpath(
        '//*[@id="shipmentdetailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[2]/table/tbody/tr/td[1]/input'.format(
            confirmation))

    # if checkbox is clicked
    if checkbox.get_property('checked') == True:
        # then bot unclicks that
        checkbox.click()

    # looking for rows in service levels
    row1 = 0
    row2 = 0
    row3 = 0


# FIRST WAY
#
#     rows_leg1 = len(browser.find_elements_by_xpath(
#         '//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
#
#     # looping through all possible services to select sl 9
#     for x in range(1, rows_leg1+1):
#         looking = browser.find_element_by_xpath(
#             '//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
#         if '1' in looking.text:
#             row1 = x
#             break
#
#
#         # selecting service level 9
#     browser.find_element_by_xpath(
#         '//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(
#             row1)).click()
#     time.sleep(6)
#
#     rows_leg2 = len(browser.find_elements_by_xpath(
#         '//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
#
#     print(rows_leg2)
#     for x in range(1, rows_leg2+1):
#         looking = browser.find_element_by_xpath(
#             '//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
#         print(looking.text)
#         if '1' in looking.text:
#             row2 = x
#             break
#
#
#     browser.find_element_by_xpath(
#         '//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(
#             row2)).click()
#
#     time.sleep(6)
#
#     rows_leg3 = len(browser.find_elements_by_xpath(
#         '//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
#
#     for x in range(1, rows_leg3+1):
#         looking = browser.find_element_by_xpath(
#             '//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
#         if '1' in looking.text:
#             row3 = x
#             break
#
#     browser.find_element_by_xpath(
#         '//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(row3)).click()

# SECOND WAY


    # # #TURNED OFF SERVICE LEVEL
    #
    # rows_leg1 = len(browser.find_elements_by_xpath(
    #     '//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
    #
    # rows_leg2 = len(browser.find_elements_by_xpath(
    #     '//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
    #
    # rows_leg3 = len(browser.find_elements_by_xpath(
    #     '//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
    #
    # # looping through all possible services to select sl 9
    # for x in range(1, rows_leg1+1):
    #     looking = browser.find_element_by_xpath(
    #         '//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
    #     # if ('1' in looking.text) and ('10' not in looking.text):
    #     if '9' in looking.text:
    #         row1 = x
    #         break
    #
    #
    # for x in range(1, rows_leg2+1):
    #     looking = browser.find_element_by_xpath(
    #         '//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
    #
    #     # if ('1' in looking.text) and ('10' not in looking.text):
    #     if '9' in looking.text:
    #         row2 = x
    #         break
    #
    # for x in range(1, rows_leg3+1):
    #     looking = browser.find_element_by_xpath(
    #         '//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
    #     # if ('1' in looking.text) and ('10' not in looking.text):
    #     if '9' in looking.text:
    #         row3 = x
    #         break
    #
    # #if '9' in looking.text:
    # # time.sleep(35)
    #   # selecting service level 9
    # browser.find_element_by_xpath(
    #     '//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(
    #         row1)).click()
    #
    # browser.find_element_by_xpath(
    #     '//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(
    #         row2)).click()
    #
    # browser.find_element_by_xpath(
    #     '//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(
    #         row3)).click()
    # # #


    # opening new tab with modification link
    browser.execute_script("window.open('https://www.infodis.net/philips/modifybooking.asp', '_blank')")
    counter += 1
    # switching to current tab
    browser.switch_to.window(browser.window_handles[counter])

# row1 = 0
# row2 = 0
# row3 = 0
# rows_leg1 = len(browser.find_elements_by_xpath('//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
# rows_leg2 = len(browser.find_elements_by_xpath('//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
# rows_leg3 = len(browser.find_elements_by_xpath('//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option'))
#
# for x in range(1,rows_leg1):
#     looking =  browser.find_element_by_xpath('//*[@id="leg1detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
#     if '9' in looking:
#         row1 = x
#
#
# for x in range(1, rows_leg2):
#     looking = browser.find_element_by_xpath('//*[@id="leg2detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
#     if '9' in looking:
#         row2 = x
#
# for x in range(1, rows_leg3):
#     looking = browser.find_element_by_xpath('//*[@id="leg3detailsrow"]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select/option[{}]'.format(x))
#     if '9' in looking:
#         row3 = x

