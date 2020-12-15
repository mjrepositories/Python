import os.path
import win32com.client
import os
import datetime
from distutils.dir_util import copy_tree

# # WORKING code for running macros using Python
#
# try:
#     xlApp = win32com.client.DispatchEx('Excel.Application')
#     xlsPath = os.path.expanduser(r'C:\Users\Maciek\Desktop\test1.xlsm')
#     wb = xlApp.Workbooks.Open(Filename=xlsPath)
#     xlApp.Run('maciej')
#     xlApp.Run('drugie')
#     wb.Save()
#     xlApp.Quit()
#     print("Macro ran successfully!")
# except:
#     print("Error found while running the excel macro!")
#     xlApp.Quit()
#
# # Code for creating a folder and copying existing file with change of naming

# x = datetime.datetime.today()
# last_month = x.replace(day=1) - datetime.timedelta(days=1)
# previous_month_name = last_month.strftime('%m')
# current_month_name = datetime.datetime.now().strftime('%m')
# print(current_month_name)
# os.chdir(r'C:\Users\Maciek\Desktop\test')
# previous = f'PeB {previous_month_name}.2020'
# file_name = f'PeB {current_month_name}.2020'
# if not os.path.isdir(file_name):
#     print('x')
#     os.mkdir(file_name)
#
# # copies the corrected files to desktop (to avoid downloading from mail box)
# copy_tree(r'C:\Users\Maciek\Desktop\test\{}'.format(previous),
#           r'C:\Users\Maciek\Desktop\test\{}'.format(file_name))
# os.chdir(r'C:\Users\Maciek\Desktop\test\{}'.format(file_name))
# os.rename(f'2020{previous_month_name} document.xlsm', f'2020{current_month_name} document.xlsm')

WB_PATH =   r'C:\Users\alank\Python training\Helloworld.xlsx'

PATH_TO_PDF = r'C:\Users\alank\Python training\Helloworld.pdf'


excel.Visible = False
try:
    # Open
    wb = excel.Workbooks.Open(WB_PATH)

    # Specify the sheet you want to save by index.
    #if you want all the sheets in excel try with:
    #wb.WorkSheets(wb.Sheets.Count) or wb.WorkSheets([i=1 for i in range(wb.Sheets.Count)]).Select()
    ws_index_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    wb.WorkSheets(ws_index_list).Select()

    # Save
    wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
except com_error as e:
    print('The convertion failed.')
else:
    print('Succeessful convertion')
finally:
    wb.Close()
    excel.Quit()