# import shutil
# import openpyxl
#
# wb = openpyxl.load_workbook(r'C:\Users\310295192\Desktop\Tender 2019\Rate_lane_carrier _overview for rate upload.xlsx')
# sheet = wb['LTL cbm']
# for x in range(86,247):
#     row_c =2
#     start = sheet.cell(column=x,row=row_c).value
#     end= sheet.cell(column=x,row=row_c +2).value
#     exp = "Export"
#     carrier= sheet.cell(column=x,row=row_c+3).value
#     truck= sheet.cell(column=x,row=row_c+7).value
#     dzis= '2019-04-29'
#     unit = "M3"
# # source copy, name
#     sf = r'C:\Users\310295192\Desktop\Tender 2019\LTL CBM/tender.xlsx'
#     nf = r'C:\Users\310295192\Desktop\Tender 2019\LTL CBM/{} - {} {} {} {} {} {}.xlsx'.format(start,end,carrier,truck,exp,dzis,unit)
#     shutil.copy2(sf,nf)

# # renaming files
# path =r'C:\Users\310295192\Desktop\Work\Rates\Road\SRC\DHL Freight GmbH (DHCT4 case)'
# import openpyxl
# import os
# os.chdir(path)
# for fileName in os.listdir("."):
#     print(fileName)
#     os.rename(fileName, fileName.replace("2019-05-22", "2019-10-02"))

# # opening each file and switching the value in cell
# path =r'C:\Users\310295192\Desktop\Work\Rates\Road\SRC\DHL Freight GmbH (DHCT4 case)'
# path1 = r'C:\Users\310295192\Desktop\Work\Rates\Road\SRC\DHL Freight GmbH (DHCT4 case)\LTL'
# path3 = r'C:\Users\310295192\Desktop\DHL Freight GmbH (DHCT4 case)'
# path4 = r'C:\Users\310295192\Desktop\DHL Freight GmbH (DHCT4 case)\LTL'
# import openpyxl
# import os
# os.chdir(path4)
# for fileName in os.listdir("."):
#     if len(fileName)>6:
#         # opening excel
#         wb = openpyxl.load_workbook(r'{}\{}'.format(path4,fileName))
#         # finding the value for diesel price and updating the cell
#         sheet = wb['Freight']
#         sheet['C7'].value = 'DAP26'
#         print(sheet['C7'].value)
#         # saving file
#         wb.save(r'{}\{}'.format(path4,fileName))
#         wb.close()

# path2 = r'C:\Users\310295192\Desktop\new\new.xlsx'
# wb = openpyxl.load_workbook(path2)
# sheet = wb['Tabelle1']
# print(sheet['A1'].value)
# sheet['A1'].value = 'PR1CP'
# wb.save(path2)
# wb.close()

import shutil
import pandas as pd

rates = pd.read_excel(r"C:\Users\310295192\Desktop\SHIT HAPPENING\FTL 2020 allocation\FTL allocation 2020.xlsx",sheet_name='rates')
dating = '2020-05-22'

rates['orcode'] = rates['Lane'].str[6:8]
rates['descode'] = rates['Lane'].str[-2:]

rates['countryor'] = rates['Lane'].str[4:6]
rates['countrydest'] = rates['Lane'].str[-4:-2]

for x, y in rates.iterrows():
    carrier = y['carrier']
    starting = y['countryor'] + " " + y['orcode']
    endingcountry = y['countrydest']
    endingcode = y['descode']

    sf = r"C:\Users\310295192\Desktop\SHIT HAPPENING\FTL 2020 allocation\for_rates.xlsx"
    nf = r"C:\Users\310295192\Desktop\SHIT HAPPENING\FTL 2020 allocation\all files\{} - {} {} TN Export {}.xlsx".format(starting,endingcountry,carrier,dating)
    shutil.copy2(sf,nf)

