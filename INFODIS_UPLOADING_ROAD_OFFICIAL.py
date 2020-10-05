from selenium import webdriver
import time
import os

address = input("Provide path to files: ")
browser = webdriver.Chrome()
browser.maximize_window()
# getting to infodis
browser.get("https://www.infodis.net/philips/net/LogOn/Authenticate?returnUrl=https%3a%2f%2fwww.infodis.net%2fphilips%2fnet%2f")
browser.find_element_by_id('LogOnName').send_keys('310295192')
browser.find_element_by_id('Password').send_keys("1993Maciej")
time.sleep(2)
browser.find_element_by_xpath('//*[@id="form-login"]/div/div[1]/div[1]/div/span[1]').click()

time.sleep(3)

os.chdir(address)
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
#loops through all files that are available
for every in filenames:
    try:
        file_upload = every
        # getting to uploads
        browser.get('https://www.infodis.net/philips/net/rates/uploads')
        time.sleep(4)
        # going to "new" tab
        browser.find_element_by_name('NewUpload').click()
        time.sleep(2)
        # for uploading files
        upload_f = browser.find_element_by_xpath("//input[@type='file']")
        time.sleep(1)
        file_add = '{}\{}'.format(address,file_upload)
        # finding the field with option to upload
        upload_f.send_keys(file_add)
        # uploading the file
        browser.find_element_by_xpath('//*[@id="UploadRates"]/span[2]').click()
        # searching for file
        time.sleep(4)
        browser.find_element_by_xpath('//*[@id="formRateUploads"]/div/div[1]/div[1]/div/span[2]').click()
        time.sleep(2)

        # selecting inactive
        browser.find_element_by_xpath('//*[@id="UploadStatus"]/option[2]').click()
        # browser.find_element_by_xpath('//*[@id="btnUploadNewR"]/span[2]').click()

        # clicking search for files
        browser.find_element_by_xpath('//*[@id="formRateUploads"]/div/div[1]/div[1]/div/span[2]').click()
        time.sleep(2)
        # sorting upload dates (descending order - that's why we have it two times)
        browser.find_element_by_xpath('//*[@id="upload-table"]/thead/tr[2]/th[3]/div/span').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="upload-table"]/thead/tr[2]/th[3]/div/span').click()
        time.sleep(2)
        # clicking the first available inactive file
        browser.find_element_by_xpath('//*[@id="upload-table"]/tbody/tr[1]').click()
        time.sleep(1)
        # clicking the process button
        browser.find_element_by_xpath('//*[@id="status-button"]/span[2]').click()
        time.sleep(2)
        # testing the file
        browser.find_element_by_xpath('//*[@id="upload-form"]/div/div[1]/div[2]/div[1]/span[2]').click()
        time.sleep(8)
        # and...finalizing upload with sip of champagne by click on "production" button
        browser.find_element_by_xpath('//*[@id="upload-form"]/div/div[1]/div[2]/div[1]/span[2]').click()
        time.sleep(5)
    except:
        er_handler = browser.find_element_by_xpath('//*[@id="upload-form"]/div/div[2]/div[1]/ul/li').text
        print(f'Issue with file "{every}"" occured in the process. Description: "{er_handler}"')
