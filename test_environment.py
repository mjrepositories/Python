# # # filename = r'C:\Users\310295192\Desktop\pandas\population_data.json'
# # # import json
# # #
# # # from pygal.maps.world import COUNTRIES
# # # from pygal.maps.world import World
# # #
# # # def get_country_code(country_name):
# # #     '''zwraca kod panstwa, ktore jest na liscie. Jesli brak - zwraca None'''
# # #     for code,name in COUNTRIES.items():
# # #         if  country_name == name:
# # #             return code
# # #     return None
# # #
# # #
# # # data = {}
# # # # wczytanie pliku
# # # with open(filename) as f:
# # #     pop_data = json.load(f)
# # #     print(pop_data)
# # #     for pop_dict in pop_data:
# # #         country_name = pop_dict['Country Name']
# # #         if pop_dict['Year'] =='2010':
# # #             population = int(float(pop_dict['Value']))
# # #             code = get_country_code(country_name)
# # #             if code:
# # #                 print(code + ": " + str(population))
# # #                 data[code] = population
# # #             else:
# # #                 print('Lack of code for {}'.format(country_name))
# # #
# # # # Po zaimportowaniu klasy World tworzymy jej egzemplarz
# # # wm = World()
# # # # wskazujemy, ze chcemy miec to odpalone w przegladarce
# # # wm.force_uri_protocol = 'http'
# # # # nadajemy tytul tytul mapie
# # # wm.title = 'North America, Middle and South'
# # #
# # # # przypisujemy odpowiednie kody dla poszczegolnych regionow
# # # wm.add('North America',['ca','mx','us'])
# # # wm.add("Middle America",['bz','cr','gt','hn','ni','pa','sv'])
# # # wm.add("South America",['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
# # # # wyrzucamy dane do pliku
# # # wm.render_to_file(r'C:\Users\310295192\Desktop\map.svg')
# # #
# # #
# # # # stworzmy teraz mape tylko na ameryki polnocnej z danymi odnosnie ludnosci
# # #
# # # wm = World()
# # # wm.force_uri_protocol = 'http'
# # # wm.title = 'Populacja w krajach Ameryki Polnocnej'
# # # wm.add('North America',{'ca':30000000,'us':320000000,'mx':150000000})
# # # wm.render_to_file(r'C:\Users\310295192\Desktop\map_with_details.svg')
# # #
# # # # stworzmy teraz mape swiata z danymi
# # #
# # #
# # # wm = World()
# # # wm.force_uri_protocol = 'http'
# # # wm.title = 'Interactive world map with population'
# # # wm.add('World',data)
# # # wm.render_to_file(r'C:\Users\310295192\Desktop\world_map_population.svg')
# # #
# # # # podzielimy teraz mape na kilka grup, zeby zroznicowac cieniowanie
# # # from pygal.style import  RotateStyle, LightColorizedStyle
# # # pop_1,pop_2,pop_3,pop_4,pop_5 ={},{},{},{},{}
# # #
# # # for coding,people in data.items():
# # #     if people <10000000:
# # #         pop_1[coding] = people
# # #     elif people <50000000:
# # #         pop_2[coding] = people
# # #     elif people < 100000000:
# # #         pop_3[coding] = people
# # #     elif people < 400000000:
# # #         pop_4[coding] = people
# # #     else:
# # #         pop_5[coding] = people
# # # wm_style = RotateStyle("#336699",base_style=LightColorizedStyle)
# # # wm = World(style = wm_style)
# # #
# # # wm.force_uri_protocol = 'http'
# # # wm.title = "Populacja Swiata w 2010 roku"
# # # wm.add('Do 10 mln',pop_1)
# # # wm.add('Do 50 mln',pop_2)
# # # wm.add('Do 100 mln',pop_3)
# # # wm.add('Do 400 mln',pop_4)
# # # wm.add('Ponad 500 mln',pop_5)
# # # wm.render_to_file(r'C:\Users\310295192\Desktop\world_groups.svg')
# # #
# # # from pygal.maps.world import COUNTRIES
# # #
# # # def naming_country(country_name):
# # #     '''funkcja zwraca wartosc z katalogu'''
# # #     for code, name in COUNTRIES.items():
# # #         if name ==country_name:
# # #             return code
# # #     return None
# # #
# # # empty_dict={}
# # # import csv
# # # new_list = []
# # # with open(r'C:\Users\310295192\Desktop\gdp.csv') as file:
# # #     data = csv.reader(file)
# # #     header = next(data)
# # #     print(header)
# # #     for x in data:
# # #         new_list.append(x[0].split(","))
# # #
# # # print(new_list)
# # #
# # #
# # # for x in new_list:
# # #     cy_name = x[0]
# # #     gdp_2018 = x[-3]
# # #     if len(cy_name) > 5 and cy_name != None:
# # #         empty_dict[naming_country(cy_name)] = gdp_2018
# # #
# # # cor_dict = {}
# # # for x,y in empty_dict.items():
# # #     if x != None and len(y) > 5:
# # #         if "." in y:
# # #             number = y.find('.')
# # #             cor_dict[x]=round(float(y[1:number+2])/1000000,2)
# # #         else:
# # #             cor_dict[x]=round(float(y[1:-1])/1000000,2)
# # #
# # # for x,y in cor_dict.items():
# # #     print(x,y)
# # # from pygal.maps.world import World
# # #
# # # wd = World()
# # # wd.force_uri_protocol = 'http'
# # # wd.title = "GDP of countries in 2018"
# # #
# # # wd.add('Countries',cor_dict)
# # # wd.render_to_file(r'C:\Users\310295192\Desktop\gdp_2018.svg')
# #
# # # from selenium import webdriver
# # # # import time
# # # # import os
# # # # import pandas as pd
# # # # import logging
# # # # import datetime
# # # # import win32com.client
# # # #
# # # #
# # # #
# # # # import numpy as np
# # # # # setting up chrome options and default folder for download
# # # #
# # # # browser = webdriver.Chrome()
# # # #
# # # # # getting to Optilo and maximizing window
# # # #
# # # # browser.get("https://ot3.optilo.eu/opt_ext_smxc9a/p001/main.php?m=cwlib&c=login&return_url=main.php%3Fm%3Dcwlib%26c%3Dstartpage")
# # # # browser.maximize_window()
# # # # # loggin in
# # # # emailElem = browser.find_element_by_id('inpLogin')
# # # # emailElem.send_keys('maciej.janowski@philips.com')
# # # # # inputting password
# # # # password = browser.find_element_by_id('inpPassword')
# # # # password.send_keys('Maciej0312@')
# # # #
# # # # # submitting logon details
# # # # buttonlog = browser.find_element_by_id('submitLogin')
# # # # buttonlog.click()
# # # #
# # # #
# # # # # finding multi tab
# # # # # multi = browser.find_element_by_id('menu-258664')
# # # # multi = browser.find_element_by_id('menu-259381')
# # # # multi.click()
# # # # # finding multi job tab
# # # # # joblist = browser.find_element_by_id('menu-258666')
# # # # joblist = browser.find_element_by_id('menu-259383')
# # # # joblist.click()
# #
# # # first = [3,4,5]
# # # second = [3,7]
# # # import itertools
# # #
# # # common = [x for x in first if x in second]
# # #
# # # print(common)
# # #
# # # different = [(x,y) for x in first for y in second if x!=y]
# # #
# # # print(different)
# # #
# # # words = ['mciej','karol','MONIKA']
# # #
# # # new_words = [x.title() for x in words]
# # #
# # # print(new_words)
# # #
# # # # list of summing two digits
# # #
# # # digits = [1,2,3]
# # #
# # # sum_digits = itertools.combinations(digits,3)
# # # print(list(sum_digits))
# # #
# # # maciej = {'karol':25000,'maciej':10000000,'Mariusz':200000,'Danuta':100}
# # # from operator import attrgetter
# # # print(sorted(maciej.items(),key= lambda x: x[1]))
# # #
# # #
# # # import csv
# # # with open (r'C:\Users\310295192\Desktop\names.csv','r') as csv_file:
# # #     csv_reader = csv.DictReader(csv_file)
# # #
# # #     with open (r'C:\Users\310295192\Desktop\newnames.csv','w',newline="") as new_file:
# # #         k=['first_name','last_name','email']
# # #
# # #         csv_writer = csv.DictWriter(new_file,fieldnames=k, delimiter ='&')
# # #         csv_writer.writeheader()
# # #         for x in csv_reader:
# # #             csv_writer.writerow(x)
# # #
# #
# # # lista = [('maciej','python'),('karol',"SQL")]
# # #
# # # print(list(map(list,zip(*lista))))
# # #
# # # ak =('maciej','Karol','monika')
# # #
# # # import win32com.client
# # # import datetime
# # # import os
# # # import time
# # # import pyautogui
# # # import openpyxl
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import win32print, win32api,win32com.client
# # # import xlsxwriter
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # checking the name of the today
# # # checking_date = datetime.datetime.today().strftime("%A")
# # # datum = ""
# # # # if it is not monday it takes one day before
# # # if checking_date == 'Monday':
# # #     datum = datetime.datetime.today()
# # #     datum = datum.strftime('%Y-%m-%d')
# # # # creating variable for location
# # #     location = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR {}.xlsx'.format(datum)
# # #     # create dataframe
# # #     df = pd.read_excel(location)
# # #     # Indicated shipments with Panalpina as carrier
# # #     df = df[df['Leg 2, Carrier Name'] == 'Panalpina AIR S']
# # #     # creating only shipments that are not picked up anyhow
# # #     report = df[df['Pending/Solved'].isna()]
# # #     # cut columns
# # #     columing = [x for x in range(0, 13)] + [x for x in range(22, 28)] + [38, 39,43]
# # #     print(columing)
# # #     panalpina_air = report.iloc[0:, columing]
# # #     # change the format of dates
# # #     panalpina_air['Leg 2, Pickup Planned'].dt.strftime('%Y-%m-%d')
# # #     panalpina_air['Leg 2, Pickup Actual'].dt.strftime('%Y-%m-%d')
# # #     panalpina_air['Leg 2, Delivery Actual'].dt.strftime('%Y-%m-%d')
# # #     panalpina_air['Leg 3, Delivery Planned'].dt.strftime('%Y-%m-%d')
# # #     panalpina_air['Leg 3, Delivery Actual'].dt.strftime('%Y-%m-%d')
# # #     # create excel object in pandas with proper formatting
# # #     filename = r'C:\Users\310295192\Desktop\Work\Rates\Air\Panalpina\Sent reports on missing lanes - Panalpina\Panalpina missing rates {}.xlsx'.format(datum)
# # #     writer = pd.ExcelWriter(filename, engine='xlsxwriter', date_format='yyyy-mm-dd', datetime_format='yyyy-mm-dd')
# # #     # dump data to excel
# # #     panalpina_air.to_excel(writer, sheet_name='Missing_Rates', index=False)
# # #     # prepare worksheet for working and the formating
# # #     workbook = writer.book
# # #     worksheet = writer.sheets['Missing_Rates']
# # #     blueformat = workbook.add_format({'bg_color': '#AED6F1'})
# # #     darkformat = workbook.add_format({'bg_color': '#3498DB'})
# # #     rows = panalpina_air.shape[0]
# # #     columns = panalpina_air.shape[1]
# # #     # set width of the column
# # #     worksheet.set_column('A:V', 20)
# # #     # save file
# # #     writer.save()
# # #     # playing with openpyxl and formatting
# # #     import openpyxl
# # #     # import modules
# # #     from openpyxl.styles import PatternFill, Font, Color
# # #
# # #     # open worksheet
# # #     wb = openpyxl.load_workbook(filename)
# # #     # assign workbook and worksheet
# # #     sheet = wb['Missing_Rates']
# # #     # set up color for font
# # #     ft = Font(color="FFFFFFFF")
# # #     # table dimensions
# # #     rows_pan = panalpina_air.shape[0] + 1
# # #     columns_pan = panalpina_air.shape[1]
# # #     # loop through each row
# # #     for x in range(1, rows_pan + 1):
# # #         for y in range(1, columns_pan + 1):
# # #             if x % 2 == 0:
# # #                 # bright blue
# # #                 sheet.cell(row=x, column=y).fill = PatternFill(fgColor="83C8F7", fill_type="solid")
# # #                 sheet.cell(row=x, column=y).font = ft
# # #             # dark blue
# # #             else:
# # #                 sheet.cell(row=x, column=y).fill = PatternFill(fgColor="1192E8", fill_type="solid")
# # #                 sheet.cell(row=x, column=y).font = ft
# # #     # save workbook
# # #     wb.save(filename)
# # #     wb.close()
# # #
# # #
# # #
# # #
# # #
# # # # preparing email for what has been added and what was wrong
# # #     outlook = win32com.client.Dispatch('outlook.application')
# # #     mail = outlook.CreateItem(0)
# # #     #mail.To = 'DL_PCTPolandOptilo@philips.com'
# # #     mail.To = 'GBSCTPhilips.SMB@panalpina.com; philips.prebilling@philips.com'
# # #     mail.CC = 'peter.van.dijk@philips.com ; Herman.Houweling@panalpina.com'
# # #     mail.Subject = 'Panalpina AIR Missing Rates ' + str(datetime.datetime.today().strftime("%Y-%m-%d"))
# # #     mail.Body = 'Test'
# # #     mail.HTMLBody = '<p>Dear Panalpina,</p><p>Please find attached the overview of missing rates in infodis.</p>'\
# # #                     '<br><p>Kind Regards,</p><p>Maciej Janowski</p>' \
# # #                     '<p>Junior Transport Specialist</p><p>Philips Polska Sp. z o.o </p>' \
# # #                     '<p>PCT Poland</p>'
# # #     # attaching log file
# # #     attachment  = location
# # #     mail.Attachments.Add(attachment)
# # #     # sending email
# # #     mail.Save()
# #
# # # concept mis to download all reports from today and update them based on last day
# # import win32com.client
# # folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# # # getting to infodis folder
# # subfolder = folder.Folders(13)
# #
# # print(subfolder)
# # # getting to all emails
# # email = subfolder.Items
# # # checkiing the number of emails to further take this value into the loop
# # x = len(email)
# # print(x)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # #
# # # # list for mjb numbers
# # # mjb_num = []
# # #
# # # # sort all emails that we have in the folder
# # # email.Sort('ReceivedTime')
# # # first = x - 1670 + 1
# # # # starts the loop through the emails
# # # for hawb in range(1670):
# # #     # checks the number of email after sorting and extract data on it
# # #     message = email.Item(first + hawb)
# # #     bodyofemail = message.body
# # #     sendermail = message.SenderEmailAddress.upper()
# # #     subjectofemail = message.subject.upper()
# # #     # checks the MJB number in subject
# # #     if "Please send the corrected file to support@comp-win.pl" in bodyofemail:
# # #         # print(message.SenderEmailAddress.upper())
# # #         # checkes if it is incoming from Panalpina
# # #         if ("Unknown shipping indicator" in bodyofemail) or ("Unknown transportation mode" in bodyofemail) or ("Unknown Delivery type" in bodyofemail):
# # #             # looks for MJB in subject
# # #             # extracts the MJB number from subject
# # #             mjb_num.append(hawb)
# # #
# # # import pandas as pd
# # # import win32com.client
# # # import datetime
# # # # getting to inbox
# # # folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# # # # getting to infodis folder
# # # subfolder = folder.Folders(7)
# # # # getting to all emails
# # # email = subfolder.Items
# # # # checkiing the number of emails to further take this value into the loop
# # # x = len(email)
# # # # print(x)
# # #
# # # path_to_report =""
# # # # sort all emails that we have in the folder
# # # email.Sort('ReceivedTime')
# # # first = x - 70 + 1
# # # # starts the loop through the emails
# # # for load in range(70):
# # #     # checks the number of email after sorting and extract data on it
# # #     message = email.Item(first + load)
# # #     # getting the time of receiving the email
# # #     timing = message.ReceivedTime
# # #     # setting up the proper format email time
# # #     day = datetime.datetime.strftime(timing,"%Y-%m-%d")
# # #     # converting date of email to date format
# # #     object_day = datetime.datetime.strptime(day,"%Y-%m-%d")
# # #     # setting up the proper format for today
# # #     today = datetime.datetime.today().strftime('%Y-%m-%d')
# # #     # conveting date of emila to date format
# # #     object_today = datetime.datetime.strptime(today,"%Y-%m-%d")
# # #     # assigning body of the email
# # #     bodyofemail = message.body
# # #     #assign the hour
# # #     time_hour = timing.hour
# # #     # assigning info on sender
# # #     sendermail = message.SenderEmailAddress.upper()
# # #     # assigning subject of the email
# # #     subjectofemail = message.subject.upper()
# # #     if subjectofemail == 'Optilo - order report'.upper() and time_hour ==14:
# # #         for attach in message.Attachments:
# # #             csv_attach = attach.FileName
# # #             if "ALLORDERREPORT" in csv_attach.upper():
# # #                 report_name = csv_attach.split('.')[0]
# # #                 path_to_report = r'C:\Users\310295192\Desktop\Python\Projects\LOAD_PLAN\reports\{} {}.csv'.format(report_name,today)
# # #                 print(path_to_report)
# # #                 attach.SaveAsFile(path_to_report)
# # #                 break
# #
# # # from openpyxl import Workbook
# # # import csv
# # #
# # #
# # # wb = Workbook()
# # # ws = wb.active
# # # with open(path_to_report, 'r',encoding="utf8") as f:
# # #     for row in csv.reader(f):
# # #         ws.append(row)
# # # wb.save(path_to_report.split('.')[0] +'.xlsx')
# #
# #
# #
# # # import pandas as pd
# # # from matplotlib import pyplot as plt
# # #
# # # plt.style.use('fivethirtyeight')
# # # age = [18,19,21,25,26,26,30,32,38,45,55]
# # #
# # # plt.title('Age of respondents')
# # # plt.xlabel('Ages')
# # # plt.ylabel('Total respondents')
# # #
# # # plt.tight_layout()
# # # plt.show()
# #
# # # import win32com.client
# # # import datetime
# # # # getting to inbox
# # # folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# # # # getting to infodis folder
# # # subfolder = folder.Folders(7)
# # # # getting to all emails
# # # email = subfolder.Items
# # # # checkiing the number of emails to further take this value into the loop
# # # x = len(email)
# # # print(x)
# # # first = x - 50 + 1
# # # file_for_load_plans = ""
# # # for loadplan in range(50):
# # #     # checks the number of email after sorting and extract data on it
# # #     message = email.Item(first + loadplan)
# # #     bodyofemail = message.body.upper()
# # #     sendermail = message.SenderEmailAddress.upper()
# # #     subjectofemail = message.subject.upper()
# # #     time_received = message.ReceivedTime
# # #     date_received = message.ReceivedTime
# # #     reporting_date = int(time_received.strftime("%d"))
# # #     today = int(datetime.datetime.today().strftime('%d'))-1
# # #     reporting_time = int(time_received.strftime("%H"))
# # #     print(reporting_date,"_______",today)
# # #     load_doc = "Load plans " + datetime.datetime.today().strftime("%Y-%m-%d")
# # #     # print(load_doc)
# # #     # print(bodyofemail)
# # #     # print("time of email---" + str(reporting_time))
# # #     # checks the if ORDER REPORT in in subject
# # #     if ('ORDER REPORT' in bodyofemail) and (reporting_time == 14) and (reporting_date == today) and (len(message.Attachments) > 0):
# # #         #print(bodyofemail,subjectofemail,reporting)
# # #         print('hello')
# # #         for attach in message.Attachments:
# # #             hawb_attach = attach.FileName
# # #             #attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\' + load_doc + '.csv')
# # #             attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\Python\\Projects\\LOAD_PLAN\\LOAD_PLANS\\'+ load_doc +'.csv')
# # #             file_for_load_plans = r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\LOAD_PLAN\\LOAD_PLANS\\'+ load_doc +'.csv'
# #
# # import win32api,win32print
# #
# # f_name = r'C:\Users\310295192\Desktop\s.jpg'
# #
# #
# # import win32print
# # import win32ui
# # from PIL import Image, ImageWin
# #
# # #
# # # Constants for GetDeviceCaps
# # #
# # #
# # # HORZRES / VERTRES = printable area
# # #
# # HORZRES = 8
# # VERTRES = 10
# # #
# # # LOGPIXELS = dots per inch
# # #
# # # LOGPIXELSX = 88
# # LOGPIXELSX = 88
# # LOGPIXELSY = 90
# #
# #
# #
# # #
# # # PHYSICALWIDTH/HEIGHT = total area
# # #
# # # PHYSICALWIDTH = 110
# # PHYSICALWIDTH = 110
# # PHYSICALHEIGHT = 111
# # #
# # # PHYSICALOFFSETX/Y = left / top margin
# # #
# # PHYSICALOFFSETX = 112
# # PHYSICALOFFSETY = 113
# #
# # printer_name = win32print.GetDefaultPrinter ()
# # file_name = "test.jpg"
# #
# # #
# # # You can only write a Device-independent bitmap
# # #  directly to a Windows device context; therefore
# # #  we need (for ease) to use the Python Imaging
# # #  Library to manipulate the image.
# # #
# # # Create a device context from a named printer
# # #  and assess the printable size of the paper.
# #
# #
# #
# #
# #
# #
# # ###
# #
# #
# # ###WORKED BUT NOT SUFFICENT
# #
# #
# # hDC = win32ui.CreateDC ()
# # print('hDC')
# # print(hDC)
# # hDC.CreatePrinterDC (printer_name)
# # printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
# # print('printable_area')
# # print(printable_area)
# # printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
# # print('printer_size')
# # print(printer_size)
# # printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
# # print('printer_margins')
# # print(printer_margins)
# # #
# # # Open the image, rotate it if it's wider than
# # #  it is high, and work out how much to multiply
# # #  each pixel by to get it as big as possible on
# # #  the page without distorting.
# # #
# # bmp = Image.open (f_name)
# # if bmp.size[0] > bmp.size[1]:
# #   bmp = bmp.rotate (90)
# #
# # print('bmp.size[0],bmp.size[1]')
# # print(bmp.size[0],bmp.size[1])
# #
# # ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
# # scale = min (ratios)
# #
# #
# # print('ratios')
# # print(ratios)
# # print('scale')
# # print(scale)
# # #
# # # Start the print job, and draw the bitmap to
# # #  the printer device at the scaled size.
# # #
# # hDC.StartDoc ('testingwithinches')
# # hDC.StartPage ()
# #
# # dib = ImageWin.Dib (bmp)
# #
# # # scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
# # scaled_width, scaled_height = [int (scale * i*1.5) for i in bmp.size]
# #
# # print('scaled_width,scaled_height')
# # print(scaled_width,scaled_height)
# # x1 = int ((printer_size[0] - scaled_width) / 2)
# # y1 = int ((printer_size[1] - scaled_height) / 2)
# # x2 = x1 + scaled_width
# # y2 = y1 + scaled_height
# # dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))
# #
# # print(x1,y1,x2,y2)
# # hDC.EndPage ()
# # hDC.EndDoc ()
# # hDC.DeleteDC ()
# # #
#
#
# # import tempfile
# # import win32api
# # import win32print
# #
# #
# # with open (f_name, "rb") as obraz:
# #     win32api.ShellExecute (
# #       0,
# #       "printto",
# #       obraz,
# #       '"%s"' % win32print.GetDefaultPrinter (),
# #       ".",
# #       0
# #     )
#
#
# # import win32print
# # # import win32ui
# # # from PIL import Image, ImageWin
# # #
# # # # Create a device context from a named printer
# # # #  and assess the printable size of the paper.
# # # printer_name = win32print.GetDefaultPrinter ()
# # # hDC = win32ui.CreateDC()
# # # hDC.CreatePrinterDC(printer_name)
# # #
# # # bmp = Image.open (f_name)
# # #
# # # hDC.StartDoc(f_name)
# # # hDC.StartPage()
# # #
# # # dib = ImageWin.Dib(bmp)
# # # x1, y1, x2, y2=100,100,100,100
# # # dib.draw (hDC.GetHandleOutput(), (x1, y1, x2, y2))
# # # hDC.EndPage()
# # # hDC.EndDoc()
# # # hDC.DeleteDC()
#
# # filename = r'C:\Users\310295192\Desktop\Road missing rates 2019-07-24.xlsx'
# # from selenium import webdriver
# # import time
# # browser = webdriver.Chrome()
# # #getting to sharepoint
# # browser.get('https://share.philips.com/sites/STS020180301160509/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FSTS020180301160509%2FShared%20Documents%2FPCT%20Poland%2FMJ')
# # # logging into webpage
# # browser.find_element_by_name('loginfmt').send_keys('maciej.janowski@philips.com')
# # from selenium.webdriver.common.keys import Keys
# # browser.find_element_by_name('loginfmt').send_keys(Keys.ENTER)
# # time.sleep(12)
# # # finding upload button
# # button = browser.find_element_by_xpath('//*[@id="appRoot"]/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div[2]/button/div/i[2]')
# # button.click()
# # time.sleep(4)
# # # finding hidden option for upload
# # button2 = browser.find_element_by_xpath("//input[@type='file']")
# # # uploading file to sharepoint
# # button2.send_keys(filename)
#
#
# # for x in range(2,102):
# #   pole = browser.find_element_by_xpath('//*[@id="DG100007321"]/tbody/tr[{}]/td[3]/input'.format(x))
# #   text_pole = pole.get_attribute('value')
# #   numer = browser.find_element_by_xpath('//*[@id="DG100007321"]/tbody/tr[{}]/td[2]/input'.format(x))
# #   text_numer = numer.get_attribute('value')
# #   if text_numer not in text_pole:
# #     button = browser.find_element_by_xpath('//*[@id="DG100007321"]/tbody/tr[{}]/td[1]/input[1]'.format(x))
# #     button.send_keys(Keys.ENTER)
# #     time.sleep(4)
# #     browser.find_element_by_xpath('//*[@id="DG100007321"]/tbody/tr[{}]/td[3]/input'.format(x)).clear()
# #     browser.find_element_by_xpath('//*[@id="DG100007321"]/tbody/tr[{}]/td[3]/input'.format(x)).send_keys(text_pole + " - ORU " + text_numer)
# #     saving = browser.find_element_by_xpath('//*[@id="DG100007321"]/tbody/tr[{}]/td[1]/input[1]'.format(x))
# #     saving.send_keys(Keys.ENTER)
# #     time.sleep(4)
# #
# # from distutils.dir_util import copy_tree
# # copy_tree(r'C:\Users\310295192\Desktop\Others\Auto', r'C:\Users\310295192\Desktop')
# #
# #
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
# # CORRECTION OF THE CODE FOR EXPEDITORS (TO GET NECESSARY AIRWAYBILLS WITH PRE-ALERT INDICATION)
#
#
#
# #
# # # if we have MJB in the body of the email
# #         if ("MJB" in bodyofemail and "D/I" in subjectofemail and len(message.Attachments) > 0) or
# #         ("MJB" in subjectofemail and "PRE-ALERT" in subjectofemail and "D/I" not in subjectofemail and len(message.Attachments) > 0):
# #             # Then it is looking for MJB in body
# #             mjb_index = bodyofemail.find("MJB")
# #             # extracts the MJB number from subject
# #             mjb = bodyofemail[mjb_index:mjb_index + 10]
# #
# #
# #             # additional procedure to get HAWB from PRE-ALERT
# #             if len(mjb_index) < 10:
# #               mjb_index = subjectofemail.find("MJB")
# #               # extracts the MJB number from subject
# #               mjb = subjectofemail[mjb_index:mjb_index + 10]
# #
# #             print(mjb)
# #             # we are logging info about mjb creation
# #             logger.info(f'({mjb}) - indicated number has been created')
# #             # we are indicating the subject of the email that was used
# #             logger.info(f'email: "{subjectofemail}" has been used for creating {mjb}')
# #             # opens the file for checking if MJB was already extracted
# #             reading = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'r')
# #             # # checks the content of the file
# #             opening = reading.read()
# #             # #checks if mjb is already added in the list
# #             if mjb not in opening:
# #                 # we are logging info that number was not on list and program will upload the document
# #                 logger.info(f'{mjb} number is not on the list and HAWB will be checked for presence')
# #                 print("nie ma takiej wartości")
# #                 reading.close()
# #                 # opens overview in appending mode
# #                 appending = open(r'C:\Users\310295192\Desktop\Python\Projects\HAWB\HAWB Nippon.txt', 'a')
# #                 # is adding mjb to file
# #                 appending.write(mjb + '\n')
# #                 # and it downloads the file to respective folder
# #                 for attach in message.Attachments:
# #
# #                   if len(message.Attachments) = 1:
# #
# #                       hawb_attach = attach.FileName
# #                       # if "NEN" in hawb_attach.upper():
# #                       if "D/I" in subjectofemail:
# #                           print(subjectofemail)
# #                           attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
# #                           # now we are logging info that file was downloaded
# #                           logger.info(f'HAWB for ({mjb}) has been dowloaded')
# #                           # it adds the MJB number to list
# #                           mjb_num.append(mjb)
# #                           # closes the file that was in append mode
# #                           appending.close()
# #                       else:
# #                           logger.info(f'File is not the HAWB in the email for "{mjb}')
# #                           logger.info(f'Name of the file is {hawb_attach}')
# #
# #                   if len(message.Attachments) > 1:
# #
# #                       hawb_attach = attach.FileName
# #                       if "NEN" in hawb_attach.upper():
# #                           if "ALERT" in subjectofemail:
# #                               print(subjectofemail)
# #                               attach.SaveAsFile(r'C:\\Users\\310295192\\Desktop\\Python\\Projects\\HAWB\\downloaded\\Nippon\\' + mjb + '.pdf')
# #                               # now we are logging info that file was downloaded
# #                               logger.info(f'HAWB for ({mjb}) has been dowloaded')
# #                               # it adds the MJB number to list
# #                               mjb_num.append(mjb)
# #                               # closes the file that was in append mode
# #                               appending.close()
# #                           else:
# #                               logger.info(f'File is not the HAWB in the email for "{mjb}')
# #                               logger.info(f'Name of the file is {hawb_attach}')
#
# # import pandas as pd
# # lista = ['4513475299-6600383633-Allura Xper FD20-Daniel-IT-2019-11-27 00:00:00',
# #          '4514342672-6600402856-Allura Xper FD10-Daniel-IT-2019-11-26 00:00:00',
# #          '4513239522-6600423040-Azurion 7 M12-Mariusz-DE-2019-11-21 00:00:00',
# #          '4513973559-6600437300-Ingenia Elition X-Paulina-MC-2019-12-16 00:00:00'
# #         ]
# # # creating data frame based on data to be shared as "not available"
# # request = pd.DataFrame([x.split("-") for x in lista],columns=['PO','SO','Product','Planner',"Country",'Year','Month','Day'])
# #
# # # creating date column
# # request['Date'] = request['Year'] + "-" +request['Month'] + "-"+ request['Day'].str[:2]
# #
# # # dropping unnecessary columns
# # request.drop(columns=['Year','Month','Day'],inplace=True)
# #
# # # correcting the format of date column
# # request['Date'] = request['Date'].astype('datetime64[ns]')
# #
# #
# # # making the name of a product as uppercase
# # request['Product'] = request['Product'].str.upper()
# #
# # # opening file with data for emails
# # orderdesk = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\DQ\database for emails (DQ request).xlsx')
# #
# # # making the name of a product as uppercase for second data frame
# # orderdesk['System'] = orderdesk['System'].str.upper()
# #
# # # dropping unnecessary columns
# # orderdesk.drop(columns=['System.1','Type','Orderdesk'],inplace=True)
# #
# # # creating new index for emails data frame
# # orderdesk.set_index('System',inplace=True,drop=True)
# #
# # # creating new index for non-received documents data frame
# # request.set_index('Product',inplace=True,drop=False)
# #
# # # joining both tables
# # request = request.join(orderdesk)
# #
# # # what was requested (additional list for that)
# # requested_dq = []
# #
# # import win32com.client
# # # creting session in outlook
# # outlook = win32com.client.Dispatch('outlook.application')
# #
# # # iterating through each row
# # for index,rows in request.iterrows():
# #     # creating email
# #     mail = outlook.CreateItem(0)
# #     # indicating who has to be addressed
# #     mail.To = rows['email']
# #     #mail.To = 'daniel.ciechanski@philips.com;paulina.szczesniewicz@philips.com;joanna.polak@philips.com;Mariusz.Mikinka@philips.com'
# #
# #     # creating subject of the email
# #     mail.Subject = 'DQ required for - PO {} / SO {}'.format(str(rows['PO']),str(rows['SO']))
# #
# #     mail.Body = 'Test'
# #
# #     # creating body of the email
# #     mail.HTMLBody = '<p>Dear Order Desk,</p><p>Please provide DQ for below:</p>'+\
# #                 '<p>PO: <b>{}</b></p>'.format(str(rows['PO'])) +\
# #                 '<p>SO: <b>{}</b></p>'.format(str(rows['SO'])) +\
# #                 '<p>Product: <b>{}</b></p>'.format(rows['Product']) +\
# #                 '<p>Country: <b>{}</b></p>'.format(rows['Country']) +\
# #                 '<p>CDD: <b>{}</b></p>'.format(str(rows['Date'])[:10]) +\
# #                 '<p>Regards,</p><p>PCT Poland</p>'
# #
# #     # sending it under dq mailbox
# #     # mail.SentOnBehalfOfName = 'dq.pct@philips.com'
# #
# #     # registering that PO/SO was requested
# #
# #     # saving/sending the email
# #     mail.Save()
#
# # #it is working
# # import zipfile, os
# # import win32com.client
# # import datetime
# #
# #
# # # getting to inbox
# # folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI").GetDefaultFolder(6)
# # # getting to infodis folder
# # subfolder = folder.Folders(8)
# # print(subfolder)
# # # getting to all emails
# # email = subfolder.Items
# # # checkiing the number of emails to further take this value into the loop
# # x = len(email)
# # print(x)
# #
# # #sort all emails that we have in the folder
# # email.Sort('ReceivedTime')
# # first=x-2
# # #starts the loop through the emails
# # for infodis in range(3):
# # #checks the number of email after sorting and extract data on it
# #     message = email.Item(first + infodis)
# #     bodyofemail = message.body
# #     subjectofemail=message.subject
# #     #checks the date of the email and assing the proper date
# #     when = message.SentOn
# #     when_formated= datetime.datetime.strftime(when,'%Y-%m-%d')
# #     #now we will be checking each email subject and save it in proper folder
# #     print(subjectofemail)
# #     if subjectofemail == "Missing rates Part 1":
# #         attachment = message.Attachments.Item(1)
# #         # if the email is for FCL missing rates - it saves it in respective folder
# #         attachment.SaveAsFile(r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 1.zip')
# #     elif subjectofemail == "Missing rates Part 2":
# #         attachment = message.Attachments.Item(1)
# #         # if the email is for FCL missing rates - it saves it in respective folder
# #         attachment.SaveAsFile(
# #             r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 2.zip')
# #     elif subjectofemail == "Missing rates Part 3":
# #         attachment = message.Attachments.Item(1)
# #         # if the email is for AIR missing rates - it saves it in respective folder
# #         attachment.SaveAsFile(r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 3.zip')
# #
# # path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 1.zip'
# # directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted'
# # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
# #     zip_ref.extractall(directory_to_extract_to)
# #
# # path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 2.zip'
# # directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted'
# # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
# #     zip_ref.extractall(directory_to_extract_to)
# #
# # path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 3.zip'
# # directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted'
# # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
# #     zip_ref.extractall(directory_to_extract_to)
# #
# # # second extraction
# #
# # path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 1.zip'
# # directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files'
# # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
# #     zip_ref.extractall(directory_to_extract_to)
# #
# # #going to directory
# # os.chdir(r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files')
# #         # going through each filename
# # for dirpath,dirnames,filenames in os.walk(os.curdir):
# #     for naming in filenames:
# #         # if there is a file with Ruurd name
# #         print(naming)
# #         if naming[:3] == "Ruu":
# #             # it corrects the file to the name we need for easier processing
# #             os.rename(naming, f'rates_1.xlsx')
# #             break
# #
# # path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 2.zip'
# # directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files'
# # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
# #     zip_ref.extractall(directory_to_extract_to)
# #
# #         # going through each filename
# # for dirpath,dirnames,filenames in os.walk(os.curdir):
# #     for naming in filenames:
# #         # if there is a file with Ruurd name
# #         print(naming)
# #         if naming[:3] == "Ruu":
# #             # it corrects the file to the name we need for easier processing
# #             os.rename(naming, f'rates_2.xlsx')
# #             break
# #
# # path_to_zip_file = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 3.zip'
# # directory_to_extract_to = r'C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files'
# # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
# #     zip_ref.extractall(directory_to_extract_to)
# #
# #         # going through each filename
# # for dirpath,dirnames,filenames in os.walk(os.curdir):
# #     for naming in filenames:
# #         # if there is a file with Ruurd name
# #         print(naming)
# #         if naming[:3] == "Ruu":
# #             # it corrects the file to the name we need for easier processing
# #             os.rename(naming, f'rates_3.xlsx')
# #             break
# #
# #
# # os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 1.zip")
# # os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 2.zip")
# # os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\missing Rates - Part 3.zip")
# # os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 1.zip")
# # os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 2.zip")
# # os.remove(r"C:\Users\310295192\Desktop\SHIT HAPPENING\Ruurd files\Extracted\missing Rates - Part 3.zip")
# #
# #
# #
# #
#
#
#
#
#
# # looping through all the entries to find TNT folder
# import win32com.client
# # getting to freight and audit folder (TNT subfolder)
# folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# # getting to dq folder
# audit = folder.Folders('Freight Audit and Payment Team (Functional Account)')
# print(audit)
# for tabek in range(1,10):
#     subfolder = audit.Folders(9)
#     # print(subfolder)
#     # getting to all emails
#     print(subfolder)
#
#
#
#
# # looping through all the entries to find TNT folder
# import win32com.client
# # getting to freight and audit folder (TNT subfolder)
# folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# # getting to dq folder
# audit = folder.Folders('Freight Audit and Payment Team (Functional Account)')
# print(audit)
# for tabek in range(1,10):
#     subfolder = audit.Folders(9).Folders(tabek)
#     # print(subfolder)
#     # getting to all emails
#     email = subfolder.Items
#     # checking the number of emails to further take this value into the loop
#     x = len(email)
#     print(tabek,subfolder)
#
# # import mysql.connector
# #
# # n = 100
# #
# # # Generate single entry in data base
# # single_query = "INSERT INTO post (user_id,post_text)' \
# #                'VALUES (1,'I am creating my first posts in this database)"
# #
# #
# # big_query = "INSERT INTO post (user_id,post_text) VALUES "
# # # Generate big query based on single quary above
# # for i in range(n):
# #     big_query += "(1,'I am creating my 23{} posts in this database which shows {} rows'),".format(str(i),str(i+4))
# #
# # big_query = big_query.strip(',') +';'
# #
# # print(big_query)
# #
# #
# # # first we need to etablish the connection wth database
# # mydb = mysql.connector.connect(
# # host="127.0.0.1",
# #   user="root",
# # port=3306,
# # database="public"
# # )
# #
# # print(mydb)
# #
# # # then we are hiring a waiter to serve us
# # mycursor = mydb.cursor()
# #
# #
# # # then we are ordering what we want to do in the restaurant
# # mycursor.execute(big_query)
# #
# # # then what we want is execute
# # mydb.commit()
# #
# # # we give waiter free time to relax for next day
# # mycursor.close()
# #
# #
# # # we are closing the restaurant for next visits tomorrow
# # mydb.close()
#
#
# # import os
# #
# # os.chdir(r'\Users\310295192\Desktop\Python\django_project')
# # for dirpath, dirnames, filenames in os.walk(os.getcwd()):
# #     print("Current Path: ", dirpath)
# #     print("Directories: ", dirnames)
# #     print("Files: ", filenames)


# BRANDS = [
#     ('AUDI', 'AUDI'), ('BMW', 'BMW'), ('CITROEN', "CITROEN"), ("KIA", "KIA"),
#     ("MAZDA", "MAZDA"), ("CHEVROLET", "CHEVROLET"), ("FIAT", "FIAT"), ("MERCEDES", "MERCEDES"),
#     ("OPEL", "OPEL"), ("RENAULT", "RENAULT"), ("HYUNDAI", "HYUNDAI"), ("NISSA", "NISSAN"),
#     ("SEAT", "SEAT"), ("SKODA", "SKODA"), ("PEUGEOT", "PEUGEOT"), ("HONDA", "HONDA"),
#     ("VOLKSWAGEN", "VOLKSWAGEN"), ("MITSUBISHI", "MITSUBISHI"), ("FORD", "FORD"), ("TOYOTA", "TOYOTA")
# ]
#
# sorted_by_second = sorted(BRANDS, key=lambda tup: tup[0])
# print(sorted_by_second)
#
#
# [('AUDI', 'AUDI'), ('BMW', 'BMW'), ('CHEVROLET', 'CHEVROLET'), ('CITROEN', 'CITROEN'), ('FIAT', 'FIAT'),
#  ('FORD', 'FORD'), ('HONDA', 'HONDA'), ('HYUNDAI', 'HYUNDAI'), ('KIA', 'KIA'), ('MAZDA', 'MAZDA'),
#  ('MERCEDES', 'MERCEDES'), ('MITSUBISHI', 'MITSUBISHI'), ('NISSA', 'NISSAN'), ('OPEL', 'OPEL'),
#  ('PEUGEOT', 'PEUGEOT'), ('RENAULT', 'RENAULT'), ('SEAT', 'SEAT'), ('SKODA', 'SKODA'),
#  ('TOYOTA', 'TOYOTA'), ('VOLKSWAGEN', 'VOLKSWAGEN')]


import urllib.request
urllib.request.urlretrieve('http://localhost:8000/billing', r'C:\Users\310295192\Desktop\testing\out.pdf')



