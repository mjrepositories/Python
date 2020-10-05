import pandas as pd
import numpy as np
import datetime

print(r'C:\Users\310295192\Desktop\LCL ratecard DBS 2019-08-22.xlsx')
file_with_rates = input('Provide path to file: ')
print(datetime.datetime.now())
# reading file with lcl rates
df = pd.read_excel(file_with_rates,
                  sheet_name=0,skiprows=[1,2,3,4],header=[1],parse_cols='B:AE')

start_date = '2020-04-01'
end_date = '2021-03-31'
# creating leg 1 template
leg1 = pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})

# creating leg 2 template
leg2 = pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})
# creating leg 3 template
leg3 = pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})
# creating leg2 custom origin template
leg2custo=pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})
# creating leg2 custom destination template
leg2custd=pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})
# creating leg2 freight template
leg2freight=pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})
# creating leg2 handling origin template
leg2ho=pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})
# creating leg2 handling destination template
leg2hd=pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})


# extratcting data for leg 1 for each column
leg1['FromCountry'] = df['Leg 1'].str[0:2]
leg1['FromCity'] = df['From City']
leg1['FromUNLOCODE'] = df['From Door UNLOCODE']
leg1['ToCountry'] = df['Leg 1'].str[6:8]
leg1['ToCity'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg1['ToUNLOCODE'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg1['TransportMode'] = 'PRE'
leg1['CarrierName'] = 'DBS'
leg1['CarrierCode'] = ''
leg1['Predays'] = 0
leg1['Transitdays'] = df['Transit time A - door to CFS at origin (days)']
leg1['Postdays'] = 0
leg1['ChargeType'] = 'Pick-up from door'
leg1['CostDriver'] = 'volume'
leg1['ChargeCurr'] = 'USD'
leg1['MinVol'] = 1
leg1['Charge'] = df['Pick-up From City to CFS \n(per W/M)']
leg1['DateEffectiveFrom'] = start_date
leg1['DateEffectiveTo'] = end_date
leg1['id']=leg1['FromUNLOCODE'] + leg1['ToUNLOCODE']

#dropping duplicates and column that served as ID column
leg1.drop_duplicates(subset=['id'],inplace=True)
leg1.drop(columns=['id'],inplace=True)

# extracting data for leg 3 for each column
leg3['FromCountry'] = df['Leg 3'].str[0:2]
leg3['FromCity'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg3['FromUNLOCODE'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg3['ToCountry'] = df['Leg 3'].str[6:8]
leg3['ToCity'] = df['To City']
leg3['ToUNLOCODE'] = df['To Door UNLOCODE']
leg3['TransportMode'] = 'ONC'
leg3['CarrierName'] = 'DBS'
leg3['CarrierCode'] = ''
leg3['Predays'] = 0
leg3['Transitdays'] = df['Transit time C - CFS to door at destination (days)']
leg3['Postdays'] = 0
leg3['ChargeType'] = 'Delivery to door'
leg3['CostDriver'] = 'volume'
leg3['ChargeCurr'] = 'USD'
leg3['MinVol'] = 1
leg3['Charge'] = df['Delivery From CFS to City\n(per W/M)']
leg3['DateEffectiveFrom'] = start_date
leg3['DateEffectiveTo'] = end_date
leg3['id']= leg3['FromUNLOCODE'] + leg3['ToUNLOCODE']

# dropping duplicates and dropping column that served as ID column
leg3.drop_duplicates(subset=['id'],inplace=True)
leg3.drop(columns=['id'],inplace=True)

# creating data frames for Batam to copy (leg3)
bur3 = leg3.loc[leg3['ToCity'] == "BATAM"]
bth3 = leg3.loc[leg3['ToCity'] == "BATAM"]

# update 2020-05-26 - > previously i was taking only 0 but switched to whole (:) dataframe
# changing codes to IDBUR and IDBTH for leg3
bur3.loc[:,'FromCity'] = "IDBUR"
bur3.loc[:,'FromUNLOCODE'] = 'IDBUR'
bth3.loc[:,'FromCity'] = "IDBTH"
bth3.loc[:,'FromUNLOCODE'] = 'IDBTH'

# adding additional codes to official dataframe for leg3
leg3 = leg3.append(bur3,ignore_index=True)
leg3 = leg3.append(bth3,ignore_index=True)

leg3.to_excel(r'C:\Users\310295192\Desktop\bt3.xlsx')

# creating dataframe for Batam to copy (leg1)
bur1 = leg1.loc[leg1['FromCity'] == "BATAM"].reset_index(drop=True)
bth1 = leg1.loc[leg1['FromCity'] == "BATAM"].reset_index(drop=True)
# changing codes to IDBUr and IDBTH for leg1
bur1.loc[0,'ToCity'] = "IDBUR"
bur1.loc[0,'ToUNLOCODE'] = 'IDBUR'
bth1.loc[0,'ToCity'] = "IDBTH"
bth1.loc[0,'ToUNLOCODE'] = 'IDBTH'
# adding additional codes to official dataframe for leg1
leg1 = leg1.append(bur1,ignore_index=True)
leg1 = leg1.append(bth1,ignore_index=True)

# extracting data for le2 custom origin from respective columns
leg2custo['FromCountry'] = df['Leg 2'].str[0:2]
leg2custo['FromCity'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custo['FromUNLOCODE'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custo['ToCountry'] = df['Leg 2'].str[6:8]
leg2custo['ToCity'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custo['ToUNLOCODE'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custo['TransportMode'] = 'LCL'
leg2custo['CarrierName'] = 'DBS'
leg2custo['CarrierCode'] = ''
leg2custo['Predays'] = 2
leg2custo['Transitdays'] = df['Transit time B - CFS to CFS (days)']
leg2custo['Postdays'] = 2
leg2custo['ChargeType'] = 'Customs Clearance Origin'
leg2custo['CostDriver'] = 'Shipment'
leg2custo['ChargeCurr'] = 'USD'
leg2custo['MinVol'] = 1
leg2custo['Charge'] = df['Origin Customs Clearance (per shipment)']
leg2custo['DateEffectiveFrom'] = start_date
leg2custo['DateEffectiveTo'] = end_date

# creating dataframe for Batam to copy (leg2)
bur2custo = leg2custo.loc[leg2custo['FromCity'] == "IDBTM"].reset_index(drop=True)
bth2custo = leg2custo.loc[leg2custo['FromCity'] == "IDBTM"].reset_index(drop=True)

# creating dataframes for "To" location

bur2custodest = leg2custo.loc[leg2custo['ToCity'] == "IDBTM"].reset_index(drop=True)
bth2custodest = leg2custo.loc[leg2custo['ToCity'] == "IDBTM"].reset_index(drop=True)
# changing codes to IDBUR and IDBTH for leg2 custom origin
bur2custodest.loc[:,'ToCity'] = "IDBUR"
bur2custodest.loc[:,'ToUNLOCODE'] = 'IDBUR'
bth2custodest.loc[:,'ToCity'] = "IDBTH"
bth2custodest.loc[:,'ToUNLOCODE'] = 'IDBTH'




# changing codes to IDBUR and IDBTH for leg2 custom origin
bur2custo.loc[:,'FromCity'] = "IDBUR"
bur2custo.loc[:,'FromUNLOCODE'] = 'IDBUR'
bth2custo.loc[:,'FromCity'] = "IDBTH"
bth2custo.loc[:,'FromUNLOCODE'] = 'IDBTH'
# adding additional codes to official dataframe for leg2
leg2custo = pd.concat([leg2custo,bur2custo])
leg2custo = pd.concat([leg2custo,bth2custo])

# added for delivery
leg2custo = pd.concat([leg2custo,bur2custodest])
leg2custo = pd.concat([leg2custo,bth2custodest])

# leg2custo = leg2custo.append(bur2custo,ignore_index=True)
# leg2custo = leg2custo.append(bth2custo,ignore_index=True)
# resetting index
leg2custo['id']=leg2custo['FromUNLOCODE'] + leg2custo['ToUNLOCODE'] + leg2custo['ChargeType']

# dropping duplicates for custom origin as well as dropping column that served as an ID
leg2custo.drop_duplicates(subset=['id'],inplace=True)
leg2custo.drop(columns=['id'],inplace=True)

# Extracting data for custom destination from respective columns
leg2custd['FromCountry'] = df['Leg 2'].str[0:2]
leg2custd['FromCity'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custd['FromUNLOCODE'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custd['ToCountry'] = df['Leg 2'].str[6:8]
leg2custd['ToCity'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custd['ToUNLOCODE'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2custd['TransportMode'] = 'LCL'
leg2custd['CarrierName'] = 'DBS'
leg2custd['CarrierCode'] = ''
leg2custd['Predays'] = 2
leg2custd['Transitdays'] = df['Transit time B - CFS to CFS (days)']
leg2custd['Postdays'] = 2
leg2custd['ChargeType'] = 'Customs Clearance Destination'
leg2custd['CostDriver'] = 'Shipment'
leg2custd['ChargeCurr'] = 'USD'
leg2custd['MinVol'] = 1
leg2custd['Charge'] = df['Destination Customs Clearance (per shipment)']
leg2custd['DateEffectiveFrom'] = start_date
leg2custd['DateEffectiveTo'] = end_date


# creating dataframe for delivery

bur2custddest = leg2custd.loc[leg2custd['ToCity'] == "IDBTM"].reset_index(drop=True)
bth2custddest = leg2custd.loc[leg2custd['ToCity'] == "IDBTM"].reset_index(drop=True)
bur2custddest.loc[:,'ToCity'] = "IDBUR"
bur2custddest.loc[:,'ToUNLOCODE'] = 'IDBUR'
bth2custddest.loc[:,'ToCity'] = "IDBTH"
bth2custddest.loc[:,'ToUNLOCODE'] = 'IDBTH'

# creating dataframe for Batam to copy (leg2)
bur2custd = leg2custd.loc[leg2custd['FromCity'] == "IDBTM"].reset_index(drop=True)
bth2custd = leg2custd.loc[leg2custd['FromCity'] == "IDBTM"].reset_index(drop=True)
# changing codes to IDBUR and IDBTH for custom destination
bur2custd.loc[:,'FromCity'] = "IDBUR"
bur2custd.loc[:,'FromUNLOCODE'] = 'IDBUR'
bth2custd.loc[:,'FromCity'] = "IDBTH"
bth2custd.loc[:,'FromUNLOCODE'] = 'IDBTH'
# adding additional codes to official dataframe for leg2

leg2custd = pd.concat([leg2custd,bur2custd])
leg2custd = pd.concat([leg2custd,bth2custd])

# adding missing two data frames
leg2custd = pd.concat([leg2custd,bur2custddest])
leg2custd = pd.concat([leg2custd,bth2custddest])


# leg2custd = leg2custd.append(bur2custd,ignore_index=True)
# leg2custd = leg2custd.append(bth2custd,ignore_index=True)
# resetting index
leg2custd['id']=leg2custd['FromUNLOCODE'] + leg2custd['ToUNLOCODE'] + leg2custd['ChargeType']

# droppping dulicate values for custom destination as well as dropping column that served as an ID
leg2custd.drop_duplicates(subset=['id'],inplace=True)
leg2custd.drop(columns=['id'],inplace=True)

# extracting data for freight for leg 2 from respective columns
leg2freight['FromCountry'] = df['Leg 2'].str[0:2]
leg2freight['FromCity'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2freight['FromUNLOCODE'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2freight['ToCountry'] = df['Leg 2'].str[6:8]
leg2freight['ToCity'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2freight['ToUNLOCODE'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2freight['TransportMode'] = 'LCL'
leg2freight['CarrierName'] = 'DBS'
leg2freight['CarrierCode'] = ''
leg2freight['Predays'] = 2
leg2freight['Transitdays'] = df['Transit time B - CFS to CFS (days)']
leg2freight['Postdays'] = 2
leg2freight['ChargeType'] = 'Sea freight'
leg2freight['CostDriver'] = 'volume'
leg2freight['ChargeCurr'] = 'USD'
leg2freight['MinVol'] = 1
leg2freight['Charge'] = df['Ocean Freight CFS - CFS\n(per W/M)']
leg2freight['DateEffectiveFrom'] = start_date
leg2freight['DateEffectiveTo'] = end_date
#leg2freight['id']=leg2freight['FromUNLOCODE'] + leg2freight['ToUNLOCODE'] + leg2freight['ChargeType']


# creating missing data frames for delivery side
bur2freightdest = leg2freight.loc[leg2freight['ToCity'] == "IDBTM"].reset_index(drop=True)
bth2freightdest = leg2freight.loc[leg2freight['ToCity'] == "IDBTM"].reset_index(drop=True)
bur2freightdest.loc[:,'ToCity'] = "IDBUR"
bur2freightdest.loc[:,'ToUNLOCODE'] = 'IDBUR'
bth2freightdest.loc[:,'ToCity'] = "IDBTH"
bth2freightdest.loc[:,'ToUNLOCODE'] = 'IDBTH'



# creating dataframe for Batam to copy (leg2)
bur2freight = leg2freight.loc[leg2freight['FromCity'] == "IDBTM"].reset_index(drop=True)
bth2freight = leg2freight.loc[leg2freight['FromCity'] == "IDBTM"].reset_index(drop=True)
# changing codes to IDBUR and IDBTH for freight leg 2
bur2freight.loc[:,'FromCity'] = "IDBUR"
bur2freight.loc[:,'FromUNLOCODE'] = 'IDBUR'
bth2freight.loc[:,'FromCity'] = "IDBTH"
bth2freight.loc[:,'FromUNLOCODE'] = 'IDBTH'
# adding additional codes to official dataframe for leg2

leg2freight = pd.concat([leg2freight,bur2freight])
leg2freight = pd.concat([leg2freight,bth2freight])


# adding missing two dataframes
leg2freight = pd.concat([leg2freight,bur2freightdest])
leg2freight = pd.concat([leg2freight,bth2freightdest])

# leg2freight = leg2freight.append(bur2freight,ignore_index=True)
# leg2freight = leg2freight.append(bth2freight,ignore_index=True)
# resetting index
leg2freight['id']=leg2freight['FromUNLOCODE'] + leg2freight['ToUNLOCODE'] + leg2freight['ChargeType']

# dropping duplicates for freight for leg2 as well as dropping column that served as an ID
leg2freight.drop_duplicates(subset=['id'],inplace=True)
leg2freight.drop(columns=['id'],inplace=True)

# extracting data for handling origin leg 2 from respective columns
leg2ho['FromCountry'] = df['Leg 2'].str[0:2]
leg2ho['FromCity'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2ho['FromUNLOCODE'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2ho['ToCountry'] = df['Leg 2'].str[6:8]
leg2ho['ToCity'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2ho['ToUNLOCODE'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2ho['TransportMode'] = 'LCL'
leg2ho['CarrierName'] = 'DBS'
leg2ho['CarrierCode'] = ''
leg2ho['Predays'] = 2
leg2ho['Transitdays'] = df['Transit time B - CFS to CFS (days)']
leg2ho['Postdays'] = 2
leg2ho['ChargeType'] = 'Physical handling charge origin'
leg2ho['CostDriver'] = 'volume'
leg2ho['ChargeCurr'] = 'USD'
leg2ho['MinVol'] = 1
leg2ho['Charge'] = df['Handling Origin CFS (per W/M)']
leg2ho['DateEffectiveFrom'] = start_date
leg2ho['DateEffectiveTo'] = end_date
#leg2ho['id']=leg2ho['FromUNLOCODE'] + leg2ho['ToUNLOCODE'] + leg2ho['ChargeType']



# creating data frames for missing delivery

bur2hodest = leg2ho.loc[leg2ho['ToCity'] == "IDBTM"].reset_index(drop=True)
bth2hodest = leg2ho.loc[leg2ho['ToCity'] == "IDBTM"].reset_index(drop=True)
bur2hodest.loc[:,'ToCity'] = "IDBUR"
bur2hodest.loc[:,'ToUNLOCODE'] = 'IDBUR'
bth2hodest.loc[:,'ToCity'] = "IDBTH"
bth2hodest.loc[:,'ToUNLOCODE'] = 'IDBTH'

# creating dataframe for Batam to copy (leg2)
bur2ho = leg2ho.loc[leg2ho['FromCity'] == "IDBTM"].reset_index(drop=True)
bth2ho = leg2ho.loc[leg2ho['FromCity'] == "IDBTM"].reset_index(drop=True)
# changing codes to IDBUR and IDBTH for handling origin
bur2ho.loc[:,'FromCity'] = "IDBUR"
bur2ho.loc[:,'FromUNLOCODE'] = 'IDBUR'
bth2ho.loc[:,'FromCity'] = "IDBTH"
bth2ho.loc[:,'FromUNLOCODE'] = 'IDBTH'

# bth2ho.to_excel(r'C:\Users\310295192\Desktop\bth2ho.xlsx')

# adding additional codes to official dataframe for leg2

leg2ho = pd.concat([leg2ho,bur2ho])
leg2ho = pd.concat([leg2ho,bth2ho])

# adding two missing dataframes
leg2ho = pd.concat([leg2ho,bur2hodest])
leg2ho = pd.concat([leg2ho,bth2hodest])



# leg2ho = leg2ho.append(bur2ho,ignore_index=True)
# leg2ho = leg2ho.append(bth2ho,ignore_index=True)
# resetting index
leg2ho['id']=leg2ho['FromUNLOCODE'] + leg2ho['ToUNLOCODE'] + leg2ho['ChargeType']

# dropping duplicates for handling origin leg 2 as well as dropping column that served as ID
leg2ho.drop_duplicates(subset=['id'],inplace=True)
leg2ho.drop(columns=['id'],inplace=True)

# exracting data for handling destination leg 2 from respective columns
leg2hd['FromCountry'] = df['Leg 2'].str[0:2]
leg2hd['FromCity'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2hd['FromUNLOCODE'] = df['Origin CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2hd['ToCountry'] = df['Leg 2'].str[6:8]
leg2hd['ToCity'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2hd['ToUNLOCODE'] = df['Destination CFS \n(5 letters code: ISO COUNTRY + HUB)']
leg2hd['TransportMode'] = 'LCL'
leg2hd['CarrierName'] = 'DBS'
leg2hd['CarrierCode'] = ''
leg2hd['Predays'] = 2
leg2hd['Transitdays'] = df['Transit time B - CFS to CFS (days)']
leg2hd['Postdays'] = 2
leg2hd['ChargeType'] = 'Physical handling charge destination'
leg2hd['CostDriver'] = 'volume'
leg2hd['ChargeCurr'] = 'USD'
leg2hd['MinVol'] = 1
leg2hd['Charge'] = df['Handling Destination CFS (per W/M)']
leg2hd['DateEffectiveFrom'] = start_date
leg2hd['DateEffectiveTo'] = end_date
#leg2hd['id']=leg2hd['FromUNLOCODE'] + leg2hd['ToUNLOCODE'] + leg2hd['ChargeType']


# creating data frames for missing delivery
bur2hddest = leg2hd.loc[leg2hd['ToCity'] == "IDBTM"].reset_index(drop=True)
bth2hddest = leg2hd.loc[leg2hd['ToCity'] == "IDBTM"].reset_index(drop=True)
bur2hddest.loc[:,'ToCity'] = "IDBUR"
bur2hddest.loc[:,'ToUNLOCODE'] = 'IDBUR'
bth2hddest.loc[:,'ToCity'] = "IDBTH"
bth2hddest.loc[:,'ToUNLOCODE'] = 'IDBTH'


# creating dataframe for Batam to copy (leg2)
bur2hd = leg2hd.loc[leg2hd['FromCity'] == "IDBTM"].reset_index(drop=True)
bth2hd = leg2hd.loc[leg2hd['FromCity'] == "IDBTM"].reset_index(drop=True)
# changing codes to IDBUR and IDBTH for handling destination leg 2
bur2hd.loc[:,'FromCity'] = "IDBUR"
bur2hd.loc[:,'FromUNLOCODE'] = 'IDBUR'
bth2hd.loc[:,'FromCity'] = "IDBTH"
bth2hd.loc[:,'FromUNLOCODE'] = 'IDBTH'
# adding additional codes to official dataframe for leg2
leg2hd = pd.concat([leg2hd,bur2hd])
leg2hd = pd.concat([leg2hd,bth2hd])

# adding two missing data frames for delivery
leg2hd = pd.concat([leg2hd,bur2hddest])
leg2hd = pd.concat([leg2hd,bth2hddest])


# leg2hd = leg2hd.append(bur2ho,ignore_index=True)
# leg2hd = leg2hd.append(bth2ho,ignore_index=True)
# resetting index
leg2hd['id']=leg2hd['FromUNLOCODE'] + leg2hd['ToUNLOCODE'] + leg2hd['ChargeType']

# dropping duplicates for handling destination as well as dropping column that served as an ID
leg2hd.drop_duplicates(subset=['id'],inplace=True)
leg2hd.drop(columns=['id'],inplace=True)

# creating leg 2 template
leg2 = pd.DataFrame({'DateEffectiveFrom' : [],'DateEffectiveTo':[],'FromCountry':[],
                     'FromCity':[],'FromUNLOCODE':[],'ToCountry':[],
                    'ToCity':[],'ToUNLOCODE':[],'TransportMode':[],'CarrierName':[],
                    'CarrierCode':[],'Predays':[],'Transitdays':[],
                    'Postdays':[],'ChargeType':[],'CostDriver':[],
                    'ChargeCurr':[],'MinVol':[],'Charge':[]})


# adding all created dataframes with costs for leg 2 to one big dataframe
leg2 = pd.concat([leg2custo,leg2custd,leg2ho,leg2hd,leg2freight])
# leg2 = leg2.append(leg2custo,ignore_index=True)
# leg2 = leg2.append(leg2custd,ignore_index=True)
# leg2 = leg2.append(leg2ho,ignore_index=True)
# leg2 = leg2.append(leg2hd,ignore_index=True)
# leg2 = leg2.append(leg2freight,ignore_index=True)

# dropping na values from leg 1, leg 2 , leg 3
leg2.dropna(inplace=True)
leg1.dropna(inplace=True)
leg3.dropna(inplace=True)

# sorting leg 2, then changing four columns to integer values
leg2.sort_values(by=['FromCity','ToCity','ChargeType'],inplace=True)
leg2['Transitdays']=leg2['Transitdays'].astype(int)
leg2['Predays']=leg2['Predays'].astype(int)
leg2['Postdays']=leg2['Postdays'].astype(int)
leg2['MinVol']=leg2['MinVol'].astype(int)

# sorting leg 1, then changing four columns to integer values
leg1.sort_values(by=['FromUNLOCODE','ToCity','ChargeType'],inplace=True)
leg1['Transitdays']=leg1['Transitdays'].astype(int)
leg1['Predays']=leg1['Predays'].astype(int)
leg1['Postdays']=leg1['Postdays'].astype(int)
leg1['MinVol']=leg1['MinVol'].astype(int)

# sorting leg 3, then changing four columns to integer values
leg3.sort_values(by=['FromCity','ToCity','ChargeType'],inplace=True)
leg3['Transitdays']=leg3['Transitdays'].astype(int)
leg3['Predays']=leg3['Predays'].astype(int)
leg3['Postdays']=leg3['Postdays'].astype(int)
leg3['MinVol']=leg3['MinVol'].astype(int)


# update 2020-05-26 - > creating additional formula to pull proper country codes
leg1['FromCountry'] = leg1['FromUNLOCODE'].str[0:2]
leg1['ToCountry'] = leg1['ToUNLOCODE'].str[0:2]
leg2['FromCountry'] = leg2['FromUNLOCODE'].str[0:2]
leg2['ToCountry'] = leg2['ToUNLOCODE'].str[0:2]

# creating file and saving each dataframe to separate sheet
with pd.ExcelWriter(r'C:\Users\310295192\Desktop\lcltest.xlsx') as writer:
    leg1.to_excel(writer, sheet_name='Pre_leg1', index=False)
    leg2.to_excel(writer, sheet_name='LCL_leg2', index=False)
    leg3.to_excel(writer, sheet_name='ONC_leg3', index=False)

    worksheet1 = writer.sheets['Pre_leg1']
    worksheet2 = writer.sheets['LCL_leg2']
    worksheet3 = writer.sheets['ONC_leg3']
    # setting up the width of the columns
    worksheet1.set_column('A:H', 16)
    worksheet1.set_column('I:Q', 20)
    worksheet2.set_column('A:H', 16)
    worksheet2.set_column('I:Q', 20)
    worksheet3.set_column('A:H', 16)
    worksheet3.set_column('I:Q', 20)

print(datetime.datetime.now())

