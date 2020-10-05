# # setting up chrome options and default folder for download
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : r"C:\Users\310295192\Desktop\declarations\\"}
# chromeOptions.add_experimental_option("prefs",prefs)
# browser = webdriver.Chrome(options=chromeOptions)
#
#
# # Getting to SAP
#
# application = win32com.client.GetObject('SAPGUI').GetScriptingEngine
# connection = application.Children(0)
# session = connection.Children(0)
# session.findById("wnd[0]").maximize
# session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "310295192"
# session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "Ab71#S#A#P"
# session.findById("wnd[0]/usr/pwdRSYST-BCODE").setFocus
# session.findById("wnd[0]/usr/pwdRSYST-BCODE").caretPosition = 10
# session.findById("wnd[0]").sendVKey(0)


# from distutils.dir_util import copy_tree
# copy_tree(r'C:\\Users\\310295192\\Desktop\\Work\\Optilo\\tes\\corrected and sent', r'C:\Users\310295192\Desktop')

import win32com.client


# getting to freight and audit inbox
folder = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")
# getting to dq folder
audit = folder.Folders('Freight Audit and Payment Team (Functional Account)')
print(audit)
subfolder = audit.Folders(10).Folders(5)
print(subfolder)

email = subfolder.Items
# checking the number of emails to further take this value into the loop
x = len(email)
print(x)







