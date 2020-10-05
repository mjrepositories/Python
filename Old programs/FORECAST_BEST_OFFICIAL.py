import pandas as pd
import numpy as np
import datetime


# providing name of the folder and file
ft_file = input ("provide path to file: ")

print(datetime.datetime.now().time())

# reading excel
forecast = pd.read_excel(ft_file,sheet_name=0,header=[1])

# dropping firts column
forecast.drop(forecast.columns[[0]],axis=1, inplace=True)

# taking only Best shipments
forecast = forecast[forecast['Origin Location'] =='Best']


# dropping unnecessary columns
forecast.drop(columns=['BG','BU','Market','SSD SO Item', 'RDD',
                       'CDD', 'ADD/IOD', 'Division','Plant'
                       ,'Haz. material number (Material)', 'Incoterm',
                       'Incoterm 2', 'Country',  'Correction\nWeight',
                       'Correction\nWeight2', 'Correction\nVolume',
                       'Correction\nVolume2','City','Customer','MBP SO','Shipping type'
                      ,'Realization date','Delivery item','Bill of Lading'],axis=1, inplace=True)


# checking the date range
todaying = datetime.datetime.today().strftime('%Y-%m-%d')
forecast = forecast[forecast.FSD> todaying]

# Deleting empty values for transport mode and selecting only AIR
forecast = forecast[forecast['Item Status'].notna()]
forecast = forecast[forecast['Item Status'].str.contains('Air',regex=True)]

# reading file for products
items = pd.read_excel(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Packing lists\SAP items 2019-07-31.xlsx',sheet_name='need to be corrected', index_col=0,parse_cols = 'AA:AD')

# dropping unnecessary values for product data frame
items.dropna(inplace=True)


# merging forecast with items dataframe
clean_forecast = forecast.merge(items, how='outer',left_on="Material",right_on="product no.")

clean_forecast.to_excel(r'C:\Users\310295192\Desktop\check3.xlsx')


# dropping values that are empty as for weight
clean_forecast.dropna(subset=['Weight'],inplace=True)

# selecting values with weight over 1 kg and weights that are not empty
clean_forecast = clean_forecast[(clean_forecast['higher weight']>0) & (clean_forecast['higher weight'].notna())]

# checking th length of the routing
clean_forecast['lenroute'] = clean_forecast.Route.str.len()

# selecting only relevant routing
clean_forecast = clean_forecast[clean_forecast['lenroute']>5]
clean_forecast.to_excel(r'C:\Users\310295192\Desktop\check1.xlsx')

# dropping "length of route" column
clean_forecast.drop(columns=['lenroute'],axis=1,inplace=True)

# dropping unnecesary columns
clean_forecast.drop(columns=['Weight','Weight2','Volume2',"average weight",'average chargeable weight'],inplace=True)

# renaming columns
clean_forecast=clean_forecast.rename({"higher weight":'chargeable weight',"Volume":"Routing"},axis='columns')
print('tutaj skonczylem')
clean_forecast.to_excel(r'C:\Users\310295192\Desktop\check2.xlsx')

# Extracting the values for routings
clean_forecast['Routing'] = clean_forecast['Route'].str.extract(r'\((.*?)\)')

# reading files with routings
routing_file = pd.read_excel(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Routings\Routings.xlsm')

# dropping irrelevant columns
routing_file.drop(routing_file.columns[[0,1,2,3,4,5,6,7]],axis=1, inplace=True)

# vlookuping ports
clean_forecast['Route'] = clean_forecast['Routing'].map(routing_file.set_index("Lookup for routing")["POD"].to_dict())

# creating table for white gloves
white_gloves=[718075,718132,718096,718095,718131,889114, 718133, 889123, 889119, 889122]

# creating dateframe without white gloves
normal_forecast=clean_forecast[~clean_forecast['Material'].isin(white_gloves)]

# deleting Magnets
normal_forecast = normal_forecast[~normal_forecast["Material Description"].str.contains("Magnet")]

# creating separate dataframe for Magnets
magnet_forecast = clean_forecast[clean_forecast["Material Description"].str.contains("Magnet")]

# loading MPS
mps = pd.read_excel(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Base file\MPS.xlsx',skiprows=1,parse_cols = 'D:K')

# selecting only BG DI allocation
mps = mps[mps.Sector=='BG DI']


magnet_forecast.to_excel(r'C:\Users\310295192\Desktop\magnet.xlsx')
normal_forecast.to_excel(r'C:\Users\310295192\Desktop\check2.xlsx')


# selection routings only for AMS
mps = mps[mps['airportzone from']=='AMS']

# dropping unnecesary columns
mps.drop(columns=['Sector','Airport-airport','airportzone from','country from','region from'],inplace=True)

# creating Lane ID
mps['Lane ID code'] = mps['Lane ID code'].astype(str).str[2:]

# creating pivot table for magnet forecast
new_table =pd.pivot_table(magnet_forecast,index=['FSD','Route'],values=['chargeable weight','SSD SO Number'],aggfunc={"chargeable weight":np.sum,'SSD SO Number': len})
forecast_for_magnet = new_table.reset_index()

# adding service level column with SL 7
forecast_for_magnet['Service Level'] = '7'

# adding week number
forecast_for_magnet['Week'] = forecast_for_magnet.FSD.dt.week

# creating Lane ID for mangnet forecast
forecast_for_magnet['Routing'] = "AMS-" + forecast_for_magnet.Route.astype(str).str[2:] + "-"+ forecast_for_magnet['Service Level']

# Selecting allocated carrier for lanes in magnet forecast
forecast_for_magnet['Carrier'] = forecast_for_magnet['Routing'].map(mps.set_index("Lane ID code")["TSP - Transport Service Provider"].to_dict())

# Replacing SO column name
forecast_for_magnet.rename(columns={'SSD SO Number':"No. of SOs"},inplace=True)

# Turning to integer for No. of SOs
forecast_for_magnet['No. of SOs']=forecast_for_magnet['No. of SOs'].astype(int)

forecast_for_magnet.to_excel(r'C:\Users\310295192\Desktop\magnet_forecast.xlsx')
# creating forecasts for magnets for each carriers
panalpina_magnet = forecast_for_magnet.loc[forecast_for_magnet.Carrier=='PANALPINA']
nippon_magnet = forecast_for_magnet.loc[forecast_for_magnet.Carrier=='Nippon']
nan_magnet = forecast_for_magnet.loc[forecast_for_magnet.Carrier=='nan']
dhl_magnet = forecast_for_magnet.loc[forecast_for_magnet.Carrier=='DHL']

# Selecting relevant columns for magnet forecasts
# carrier,lane id, service level,fsd,week,weight, no. of so
panalpina_magnet = panalpina_magnet[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]
nippon_magnet = nippon_magnet[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]
dhl_magnet = dhl_magnet[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]

# resetting indexes
panalpina_magnet.reset_index(drop=True,inplace=True)
nippon_magnet.reset_index(drop=True,inplace=True)
dhl_magnet.reset_index(drop=True,inplace=True)

# creating pivot tables for normal forecast
new_table_normal =pd.pivot_table(normal_forecast,index=['FSD','Route'],values=['chargeable weight','SSD SO Number'],aggfunc={"chargeable weight":np.sum,'SSD SO Number': len})
forecast_for_normal = new_table_normal.reset_index()

# creating column for service level for normal forecast
forecast_for_normal['Service Level'] = np.select([forecast_for_normal['chargeable weight'] >1000],['6'],default='1')

forecast_for_normal.to_excel(r'C:\Users\310295192\Desktop\normal_forecast.xlsx')
# deleting values below 75 kilos
forecast_for_normal = forecast_for_normal.loc[forecast_for_normal['chargeable weight']>75]

# creating week number column
forecast_for_normal['Week'] = forecast_for_normal.FSD.dt.week

# creating Land ID column for normal forecast
forecast_for_normal['Routing'] = "AMS-" + forecast_for_normal.Route.astype(str).str[2:] + "-"+ forecast_for_normal['Service Level']

# selecting the allocated carrier for normal forecast
forecast_for_normal['Carrier'] = forecast_for_normal['Routing'].map(mps.set_index("Lane ID code")["TSP - Transport Service Provider"].to_dict())

# replacing the SO to No. of SOs name for column
forecast_for_normal.rename(columns={'SSD SO Number':"No. of SOs"},inplace=True)

# switching to integers for No. of Sos
forecast_for_normal['No. of SOs']=forecast_for_normal['No. of SOs'].astype(int)

# creating normal forecast for carriers
panalpina_normal = forecast_for_normal.loc[forecast_for_normal.Carrier=='PANALPINA']
nippon_normal = forecast_for_normal.loc[forecast_for_normal.Carrier=='Nippon']
ups_normal = forecast_for_normal.loc[forecast_for_normal.Carrier=='UPS SCS']
ceva_normal = forecast_for_normal.loc[forecast_for_normal.Carrier=='CEVA']

# resetting index for normal forecasts
panalpina_normal.reset_index(drop=True,inplace=True)
nippon_normal.reset_index(drop=True,inplace=True)
ups_normal.reset_index(drop=True,inplace=True)
ceva_normal.reset_index(drop=True,inplace=True)

# selecting the necessary columns for normal forecasts
# carrier,lane id, service level,fsd,week,weight, no. of so
panalpina_normal = panalpina_normal[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]
nippon_normal = nippon_normal[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]
ups_normal = ups_normal[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]
ceva_normal = ceva_normal[['Carrier','Routing','Service Level','FSD','Week','chargeable weight','No. of SOs']]

# checking the week number
now = datetime.date.today()
next_week = now.isocalendar()[1]

# creating next week date
next_week_date = datetime.datetime.strptime('2019-' +str(next_week+1)+'-1', '%G-%V-%u')
next_week_date = next_week_date.strftime('%Y-%m-%d')

# selecting only values for next working week
panalpina_normal = panalpina_normal.loc[panalpina_normal['FSD']>next_week_date]
nippon_normal = nippon_normal.loc[nippon_normal['FSD']>next_week_date]
ups_normal = ups_normal.loc[ups_normal['FSD']>next_week_date]
ceva_normal = ceva_normal.loc[ceva_normal['FSD']>next_week_date]

panalpina_magnet = panalpina_magnet.loc[panalpina_magnet['FSD']>next_week_date]
nippon_magnet = nippon_magnet.loc[nippon_magnet['FSD']>next_week_date]

# concatenating panalpina and nippon forecast
panalpina_complex = pd.concat([panalpina_normal,panalpina_magnet],ignore_index=True).sort_values(by=['FSD'])
nippon_complex = pd.concat([nippon_normal,nippon_magnet],ignore_index=True).sort_values(by=['FSD'])

# creating lists for looping
carriers = [[panalpina_complex,"Panalpina","complex"],[nippon_complex,"Nippon","complex"],
            [ups_normal,"UPS","normal"],[ceva_normal,"CEVA","normal"]]
today = datetime.date.today().strftime("%Y-%m-%d")
# loping through all carriers that we create forecats for
for car in carriers:
    # getting the file name for respective forecast
    filename = r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Forecasts AIR\Best\{} {}.xlsx'.format(car[1],today)
    # creating an excel file for forecast
    writer = pd.ExcelWriter(filename, engine='xlsxwriter',date_format = 'yyyy-mm-dd', datetime_format='yyyy-mm-dd')

    # dump data to excel
    car[0].to_excel(writer, sheet_name='Forecast',index=False)

    # prepare worksheet for working and the formatting
    workbook  = writer.book

    # default cell format to size 9
    workbook.formats[0].set_font_size(9)

    worksheet = writer.sheets['Forecast']

    #set width of the columns
    worksheet.set_column('A:H',16)
    worksheet.set_column('F:F',20)
    # save file
    writer.save()



print(datetime.datetime.now().time())