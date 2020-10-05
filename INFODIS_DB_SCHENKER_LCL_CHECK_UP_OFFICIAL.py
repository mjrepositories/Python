import pandas as pd
import numpy as np

# getting date for report and rates for further processing
rep_file = input("Provide the date for report: ")
rates_file = input("Provide the date for rates file: ")


# reading the file with rates
db_rates = r'C:\Users\310295192\Desktop\Work\Rates\LCL\DB Schenker\upload files\Rates LCL DB Schenker {}.xlsx'.format(rates_file)
leg1rates=pd.read_excel(db_rates,sheet_name='Pre_leg1')
leg2rates=pd.read_excel(db_rates,sheet_name='LCL_leg2')
leg3rates=pd.read_excel(db_rates,sheet_name='ONC_leg3')

# reading report for missing rates
db_schenker_report =r'C:\Users\310295192\Desktop\Work\Rates\LCL\LCL reports\DB LCL {} updated.xlsx'.format((rep_file))
db_report=pd.read_excel(db_schenker_report)

# filtering data with cases to be picked up and not analyse previously
db_report = db_report[(db_report['Pending/Solved'] == 'pending') | db_report['Pending/Solved'].isna()]

# dropping columns
db_report.drop(columns=['Booker id', 'Booker name (1)', 'Shipper id',
       'Consignee id', 'Del terms', 'Shipper name (1)',
       'Original shipper name (1)','Notify address (1)','Peter asked',
       'Mail sent to IMS/Key-user', 'Date of email', 'Email subject',
       'Delay in answer', 'Comments'],axis=1,inplace= True)

# assigning lane id for leg 2
leg2rates['id']= leg2rates['FromUNLOCODE'] +"-" + leg2rates['ToUNLOCODE']

# dropping duplicates for leg 2 rates
leg2rates.drop_duplicates(subset='id',inplace=True)

# getting the upper case pick up city for further mapping
db_report['Pickup city']= db_report['Pickup city'].str.split(',').apply(lambda x: x[0]).str.upper()

# getting the upper case delivery city for further mapping
db_report['Delivery city']= db_report['Delivery city'].str.split(',').apply(lambda x: x[0]).str.upper()


# switching potential wrong names for mount pleasant and hong kong
db_report['Pickup city']=np.select([db_report['Pickup city'] =='MT PLEASANT',
                                    db_report['Pickup city'] == 'HONGKONG'],
                                     ['MOUNT PLEASANT','HONG KONG'],
                              default = db_report['Pickup city'])

# switching potential wrong names for mount pleasant and hong kong
db_report['Delivery city']=np.select([db_report['Delivery city'] =='MT PLEASANT',
                                    db_report['Delivery city'] == 'HONGKONG'],
                                     ['MOUNT PLEASANT','HONG KONG'],
                              default = db_report['Delivery city'])

# Insert additional columns for PICK UP and DESTINATION
db_report.insert(loc = 3, column = 'ID_PICK_UP',value = db_report['Pickup city'].str[-4:])
db_report.insert(loc = 8, column = 'ID_DEST',value = db_report['Delivery city'].str[-4:])

# assigning ids for each leg
db_report['Leg1']= db_report['Pickup country'] + db_report['ID_PICK_UP']+ "-" + db_report['Leg 2, Pickup code']
db_report['Leg2']= db_report['Leg 2, Pickup code'] + "-" + db_report['Leg 2, Delivery code']
db_report['Leg3']= db_report['Leg 2, Delivery code'] + "-" +db_report['Delivery country'] + db_report['ID_DEST']

# getting main name of the city in rates file and assigning the value for mapping in new
leg1rates['FromCity'] = leg1rates['FromCity'].str.split(',').apply(lambda x: x[0]).str.upper()
leg1rates.insert(loc = 4, column = 'ID_PICK_UP',value = leg1rates['FromCity'].str[-4:])

# stripping the name of the city (to have it without spaces) and assigning additional column for mapping
leg1rates['FromCity'] = leg1rates['FromCity'].str.strip()
leg1rates['ID1'] = leg1rates['FromCountry'] + leg1rates['ID_PICK_UP'] + "-" + leg1rates['ToUNLOCODE']
leg1rates['start'] =leg1rates['FromCity'] + "-" + leg1rates['ToUNLOCODE']

# deleting rows that are duplicates for pickup cities
deleting_rows = ['BAOAN-HKHKG', 'NINGBO-CNNBO', 'SUZHOU-CNSHA', 'NEUSTADT-DEHAM', 'VILLINGEN-SCHWENNINGEN-DESTR',
                 'GAGGIO MONTANO-ITMIL', 'GLOUCESTER-USNYC', 'MOUNT PLEASANT-USNYC']
for x in deleting_rows:
    leg1rates.drop(leg1rates[leg1rates["start"] == x].index, inplace=True)

# gettting uppercase "tocity" entry, inserting column with id for mapping and creating additional column for mapping
leg3rates['ToCity'] = leg3rates['ToCity'].str.split(',').apply(lambda x: x[0]).str.upper()
leg3rates.insert(loc = 8, column = 'ID_DEST',value = leg3rates['ToCity'].str[-4:])
leg3rates['ToCity'] = leg3rates['ToCity'].str.strip()
leg3rates['ID3'] = leg3rates['FromUNLOCODE']+ "-" + leg3rates['ToCountry'] + leg3rates['ID_DEST']
leg3rates['stop'] = leg3rates['FromUNLOCODE']+ "-" + leg3rates['ToCity']


# deleting duplicate values for delivery cities
deleting_rows = ['CLSCL-SANTIAGO','CNSHA-SUZHOU','GBBAS-GLEMSFORD','GBBAS-TANGMERE','TRGEB-GEBZE',
                'TRHAY-GEBZE','USLAX-CARLSBAD','USPHL-NEW KENSINGTON']
for X in deleting_rows:
    leg3rates.drop(leg3rates[leg3rates["stop"]==x].index,inplace=True)

# renaming the column in leg2 rates
leg2rates.rename(columns={'id':"ID2"},inplace=True)


# creating data frames for checking rates
db_1 = pd.DataFrame(leg1rates['ID1'])
db_2 = pd.DataFrame(leg2rates['ID2'])
db_3 = pd.DataFrame(leg3rates['ID3'])


# adding new columns to created data frames
db_1['Leg1RatesPresent']=True
db_1.set_index('ID1', inplace=True, drop=True)

db_2['Leg2RatesPresent']=True
db_2.set_index('ID2', inplace=True, drop=True)

db_3['Leg3RatesPresent']=True
db_3.set_index('ID3', inplace=True, drop=True)


# setting new indices for db report and making joins with data frames containing info on rates availability
db_report.set_index('Leg1', inplace=True, drop=False)
db_report = db_report.join(db_1)
db_report.set_index('Leg2', inplace=True, drop=False)
db_report = db_report.join(db_2)
db_report.set_index('Leg3', inplace=True, drop=False)
db_report = db_report.join(db_3)


# assigning unkonwn carrier if leg is handled by unknown
db_report['Leg1RatesPresent'] = np.select([db_report['Leg 1, Carrier Name'] =='Unknown'], ['Unknown'],
                              default = db_report['Leg1RatesPresent'])

db_report['Leg3RatesPresent'] = np.select([db_report['Leg 3, Carrier Name'] =='Unknown'], ['Unknown'],
                              default = db_report['Leg3RatesPresent'])


# creating data frames for suggested consolidation points
db_1_suggest = leg1rates[['start','CarrierName']]
db_1_suggest['consol_1'] = leg1rates['start'].str[-5:]
db_1_suggest.drop(columns=['CarrierName'],inplace=True)
db_1_suggest.set_index('start', inplace=True, drop=True)

# setting index for suggesiton data frame
db_1_suggest.index = db_1_suggest.index.str[:-6]

# assigning new index to the report and joining data frames for consol point suggestions
db_report.set_index('Pickup city', inplace=True, drop=False)
db_report = db_report.join(db_1_suggest)

# creating data frame for suggested de-consolidation points
db_3_suggest = leg3rates[['stop','CarrierName']]
db_3_suggest['consol_2'] = leg3rates['stop'].str[:5]
db_3_suggest['stop'] = leg3rates['stop'].str[6:]
db_3_suggest.drop(columns=['CarrierName'],inplace=True)
db_3_suggest.set_index('stop', inplace=True, drop=True)


# assigning new index to the report and joining data frames for de-consol point suggestions
db_report.set_index('Delivery city', inplace=True, drop=False)
db_report = db_report.join(db_3_suggest)

# getting two-letters codes for countries and creating hyperlinks to unlocode site
db_report['UNLOCODE_FROM_fkpu']=[f'https://service.unece.org/trade/locode/{i}.htm' for i in db_report['Pickup country'].str.lower()]
db_report['UNLOCODE_TO_fkpu']=[f'https://service.unece.org/trade/locode/{i}.htm' for i in db_report['Delivery country'].str.lower()]

# saving data frame in excel
db_report.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\LCL\python check-up\DB_SCHENKER_CHECKUP_{}.xlsx'.format(rep_file),index=False)