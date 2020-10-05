from selenium import webdriver
import time
import pandas as pd


# reading file with new users
df = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\NEW_USERS\USER.xlsx')

# creating a list with users to be added to Optilo
list_of_users = []


# iterating throw each row to assign proper values that will be passed to the system like name, email, etc
for index,row in df.iterrows():
    new_user={}
    new_user['name']=row['Name']
    new_user['surname']= row['Surname']
    new_user['mail']= row['email']
    new_user['philips']=row['philips']
    new_user['planner']=row['planner']
    new_user['carrier'] =row['car_code']
    list_of_users.append(new_user)

print(list_of_users)
time.sleep(5)
browser = webdriver.Chrome()

# blue
# browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login')
# purple
browser.get("https://ot3.optilo.eu/opt_ext_po0dyx/t010/main.php?m=cwlib&c=login")
browser.maximize_window()
# loggin in
emailElem = browser.find_element_by_id('inpLogin')
emailElem.send_keys('maciej.janowski@philips.com')
# inputting password
password = browser.find_element_by_id('inpPassword')
password.send_keys('Maciej0312@')
browser.find_element_by_id('submitLogin').click()
for account in list_of_users:
    if account['planner']==1:
        # find admin tab
        # admin = browser.find_element_by_id('menu-1-259858').click()
        # # find adding tab
        # adding = browser.find_element_by_id('menu-1-259858-258928').click()
        # # find users tab
        # users = browser.find_element_by_id('menu-1-259858-258928-258929').click()

        # going directly to page
        # blue
        #browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=acl&c=uzytkownik')
        # purple
        browser.get('https://ot3.optilo.eu/opt_ext_po0dyx/t010/main.php?m=acl&c=uzytkownik')
        time.sleep(4)
        # find add user button
        adduser = browser.find_element_by_xpath('//*[@id="cw-page-left"]/div/div/ul/li[1]/a').click()

        # find login field
        login = browser.find_element_by_name('auz_login').send_keys(account['mail'])

        # find name field
        user_name = browser.find_element_by_name('auz_imie').send_keys(account['name'])

        # find surname field
        sur_name = browser.find_element_by_name('auz_nazwisko').send_keys(account['surname'])

        # find email field

        mailing = browser.find_element_by_name('auz_email').send_keys(account['mail'])

        # find language button

        english = browser.find_element_by_id('auz_jezyk_en').click()

        # finding latarka to select philips as a group

        philips  = browser.find_element_by_class_name('latarka').click()

        time.sleep(2)
        # find DI IGT option

        diigt = browser.find_element_by_xpath('//*[@id="oddzial_sel"]/select/option[2]').click()

        # click add button

        addbutton = browser.find_element_by_name('submit_dodaj').click()
        time.sleep(3)
        # finding role button
        current_address = browser.current_url
        role = current_address.replace('szczegoly', 'role')
        browser.get(role)

        time.sleep(5)

        # find checkbox for Philips Planner

        planner = browser.find_element_by_name('UPR[87]').click()

        # find saving button

        saving = browser.find_element_by_name('submit_zapisz').click()

        # find send new password button
        time.sleep(5)
        new_password = browser.find_element_by_xpath('//*[@id="cw-page-left"]/div/div/ul/li[3]/a').click()
        time.sleep(2)
        # get to user branch site
        # blue
        # browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=profil&s=UzytkownikOddzial')
        # purple
        browser.get('https://ot3.optilo.eu/opt_ext_po0dyx/t010/druid.php?m=profil&s=UzytkownikOddzial')
        time.sleep(4)
        # write code on getting the correct branch

        # creating new entry with branch for user
        browser.find_element_by_name('action[260000001][2251]').click()
        time.sleep(4)
        # finding the last row
        rows = len(browser.find_elements_by_xpath("//table[@id='DG260000001']/tbody/tr"))
        # finding number of users in optilo drop-down list
        no_of_options = len(browser.find_elements_by_xpath(f'//*[@id="DG260000001"]/tbody/tr[{rows}]/td[3]/select/option'))

        # selecting philips in company column
        company = browser.find_element_by_xpath(f'//*[@id="DG260000001"]/tbody/tr[{rows}]/td[2]/select/option[2]').click()
        person=0
        # select user name
        for x in range(2, no_of_options):
            name = browser.find_element_by_xpath(f'//*[@id="DG260000001"]/tbody/tr[{rows}]/td[3]/select/option[{x}]').text
            if account['name'] in name and account['surname'] in name:
                person = x

        # selecting the user
        user_select = browser.find_element_by_xpath(f'//*[@id="DG260000001"]/tbody/tr[{rows}]/td[3]/select/option[{person}]').click()

        # selecting DIIGT branch
        branch = browser.find_element_by_xpath(f'//*[@id="DG260000001"]/tbody/tr[{rows}]/td[4]/select/option[3]').click()
        # selecting department
        time.sleep(3)
        department = browser.find_element_by_xpath(f'//*[@id="DG260000001"]/tbody/tr[{rows}]/td[5]/select/option[2]').click()

        # saving options selected
        # browser.find_element_by_xpath('//*[@id="DG260000001"]/tbody/tr[99]/td[1]/input[2]').click()
        browser.find_element_by_name('action[260000001][2253]').click()
        time.sleep(3)
        # get to user service
        # blue
        # browser.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=profil&s=UzytkownikUsluga')
        # purlple
        browser.get("https://ot3.optilo.eu/opt_ext_po0dyx/t010/druid.php?m=profil&s=UzytkownikUsluga")
        # write code on getting two fields assigned for service handled

        # creating new entry for user
        time.sleep(5)
        browser.find_element_by_name('action[260000006][2260]').click()

        time.sleep(5)

        # create second entry for user

        browser.find_element_by_name('action[260000006][2260]').click()
        time.sleep(5)
        rows2 = len(browser.find_elements_by_xpath('//*[@id="DG260000006"]/tbody/tr'))

        # selecting company

        company2 = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2}]/td[2]/select/option[2]').click()
        company2_5 = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2-1}]/td[2]/select/option[2]').click()

        # selecting modules

        # multi order
        module2 = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2}]/td[4]/select/option[61]').click()
        # multijob
        module2_5 = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2-1}]/td[4]/select/option[55]').click()
        time.sleep(2)
        # selecting standard for order
        standard = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2}]/td[5]/select/option[8]').click()
        # selecting standard for job
        standard_2 = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2-1}]/td[5]/select/option[6]').click()

        time.sleep(2)
        # selecting service level for order
        browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2}]/td[6]/select/option[2]').click()

        # selective service level for job
        browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2-1}]/td[6]/select/option[2]').click()

        # person = 0
        #
        # for x in range(2,no_of_options):
        #     name = browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[102]/td[3]/select/option[{x}]').text
        #     if account['surname'] in name and account['name'] in name:
        #         person = x

        # selecting the person's name
        browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2}]/td[3]/select/option[{person}]').click()
        browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2-1}]/td[3]/select/option[{person}]').click()

        # saving options
        # browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2}]/td[1]/input[2]').click()
        # browser.find_element_by_xpath(f'//*[@id="DG260000006"]/tbody/tr[{rows2-1}]/td[1]/input[2]').click()

        browser.find_element_by_name('action[260000006][2262]').click()
        time.sleep(3)
        browser.find_element_by_name('action[260000006][2262]').click()
        time.sleep(3)

    # SETTING ACCOUNT IN EXTRANET

    # going to extranet page
    browser.get("https://ot3.optilo.eu/opt_ext_c4rtba/p001/main.php?m=acl&c=uzytkownik")
    try:
        # loggin in
        emailElem = browser.find_element_by_id('inpLogin')
        emailElem.send_keys('maciej.janowski@philips.com')
        # inputting password
        password = browser.find_element_by_id('inpPassword')
        password.send_keys('Maciej0312@')
        browser.find_element_by_id('submitLogin').click()
        time.sleep(3)
    except:
        print('Already logged into extranet')

    # finding and click add new user
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="cw-page-left"]/div/div/ul/li[1]/a').click()
    time.sleep(2)
    # finding and sending login
    browser.find_element_by_xpath('//*[@id="form1"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/input').send_keys(account['mail'])

    # finiding and sending name
    browser.find_element_by_xpath('//*[@id="form1"]/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/input').send_keys(account['name'])
    # finding and sending surname
    browser.find_element_by_xpath('//*[@id="form1"]/div[2]/div[1]/div/table/tbody/tr[2]/td[4]/input').send_keys(account['surname'])
    # finding and sending email
    browser.find_element_by_xpath('//*[@id="form1"]/div[2]/div[1]/div/table/tbody/tr[3]/td[4]/input').send_keys(account['mail'])
    # finding and selecting english
    browser.find_element_by_id('auz_jezyk_en').click()

    # selecting company
    browser.find_element_by_class_name('latarka').click()
    time.sleep(2)
    x = browser.find_element_by_id('TB_iframeContent')
    browser.switch_to.frame(x)
    if account['philips'] == 1:
        # selecting philips
        browser.find_element_by_xpath('//*[@id="DL220000002"]/tbody/tr[2]/td[1]/a').click()
        # selecting zero as branch
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="oddzial_sel"]/select/option[2]').click()
    else:
        # not philips but carrier
        browser.find_element_by_id('DF220000001_afi_nazwa').send_keys(account['carrier'])

        # click search to find carrier
        browser.find_element_by_id('action[220000001][58]').click()
        time.sleep(3)
        # click first available option
        browser.find_element_by_xpath('//*[@id="DL220000002"]/tbody/tr[2]/td[1]/a').click()
    time.sleep(3)
    # adding user
    browser.find_element_by_name('submit_dodaj').click()
    time.sleep(3)
    # going to role
    current_address = browser.current_url
    role = current_address.replace('szczegoly', 'role')
    browser.get(role)
    time.sleep(5)
    if account['philips'] == 0:
        # clicking carrier access
        browser.find_element_by_name('UPR[85]').click()
    else:
        # click access for manangers
        browser.find_element_by_name('UPR[86]').click()
        browser.find_element_by_name('UPR[87]').click()

    # saving changes
    browser.find_element_by_name('submit_zapisz').click()
    time.sleep(2)
    # sending new password
    browser.find_element_by_xpath('//*[@id="cw-page-left"]/div/div/ul/li[3]/a').click()

# close browser
# browser.close()


browser.find_element_by_css_selector('#DG100007321 > tbody > tr:nth-child(2) > td:nth-child(1) > input.button[name = "action[100007321][2769]"]')