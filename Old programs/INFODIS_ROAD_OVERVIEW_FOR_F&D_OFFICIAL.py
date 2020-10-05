import pandas as pd
import datetime

# setting up today date
today = datetime.datetime.today().strftime("%Y-%m-%d")

# name of the file
x = r'C:\Users\310295192\Desktop\Work\Rates\Road\reports\report road {} updated.xlsx'.format(today)
# create data frame
df = pd.read_excel(x)

# # selecting only important data for further investigation
cols = [x for x in range(0,25)]

# create new dataframe with only relevant columns
new_df =df.iloc[:,cols]

# creating road dataframe
road = new_df.iloc[:,0:25]

# filter data
# road  = road.loc[:, road.columns != 'Bill?']
road = road.loc[:,road.columns!= 'Leg 1, Billable']

road = road.loc[:,road.columns != 'Leg 1, Carrier Code']

road  = road.loc[:, road.columns != 'Shipment']
# select only shipments that are without rates

road = road.loc[road['Leg 1, Total costs'] ==0]
# select shipments that are unsolved
road  = road.loc[road['Action taken']!='solved']

# delete DSV DP Road cases
road = road.loc[road['Leg 1, Carrier Name']!= 'DSV DP Road']

# delete shipments that are for Dmitrov
road = road.loc[road['Delivery city']!='Dmitrov']
# drop columns
road.drop(columns=['Action taken'], inplace = True)
# rename columns

road.rename(columns={"Leg 1, Carrier Name": 'Carrier Name',"Leg 1, Transport Mode":"Transport mode"},inplace=True)
# dropping my columns
road.drop(columns=['Mail sent to IMS/key-user','date of Email','Email subject','Delay','Comments'], inplace = True)

# reset index
road.reset_index(drop = True, inplace = True)

# create excel object in pandas with proper formatting
filename = r'C:\Users\310295192\Desktop\Work\Rates\Road\missing rates for F&D\reports\\Road missing rates {}.xlsx'.format(today)
writer = pd.ExcelWriter(filename, engine='xlsxwriter',date_format = 'yyyy-mm-dd', datetime_format='yyyy-mm-dd')

# dump data to excel
road.to_excel(writer, sheet_name='Missing_Rates',index=False)

# prepare worksheet for working and the formating
workbook  = writer.book

# default cell format to size 10
workbook.formats[0].set_font_size(9)

worksheet = writer.sheets['Missing_Rates']

#set width of the column
worksheet.set_column('A:V',16)

# save file
writer.save()

# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# #getting to sharepoint
# browser.get('https://share.philips.com/sites/STS020180301160509/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FSTS020180301160509%2FShared%20Documents%2FPCT%20Poland%2FMJ')
# # logging into webpage
# browser.find_element_by_name('loginfmt').send_keys('maciej.janowski@philips.com')
# from selenium.webdriver.common.keys import Keys
# browser.find_element_by_name('loginfmt').send_keys(Keys.ENTER)
# time.sleep(6)
# # finding upload button
# button = browser.find_element_by_xpath('//*[@id="appRoot"]/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div[2]/button/div/i[2]')
# button.click()
# time.sleep(2)
# # finding hidden option for upload
# button2 = browser.find_element_by_xpath("//input[@type='file']")
# # uploading file to sharepoint
# button2.send_keys(filename)



