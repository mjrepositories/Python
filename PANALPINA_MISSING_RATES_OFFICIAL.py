import datetime
import pandas as pd

dating = datetime.datetime.today().strftime("%Y-%m-%d")
file_name = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR {}.xlsx'.format(dating)
k = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR 2019-06-18.xlsx'

print(file_name)