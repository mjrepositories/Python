import pandas as pd
import numpy as np
import datetime

start_date = '2020-01-01'
end_date = '2020-12-31'

input('Check if all files are present. new boss should be "new", old should be "old", file for upload should be "FCL"')
# new_boss = input('Provide path to new boss')
# old_boss = input('Provide path to old boss')
# preparing approriate columns to be read
columns =list(range(0,18)) + list(range(21,26)) + list(range(29,34)) + list(range(37,42)) + list(range(45,50))
columns.append(93)

# reading files (previous and new boss
previous = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\old.xlsx',sheet_name='Selected Bids',header=0,skip_rows=[0,1],usecols=columns)
new = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\new.xlsx',sheet_name='Selected Bids',header=0,skip_rows=[0,1],usecols=columns)

# setting up columns for new and previous file
previous.columns  = ['ID Number', 'Carrier', 'Origin_Region', 'Origin_Country',
       'Origin_City', 'Origin_Port',
       'Origin_Type_of_Departure', 'Destination_region',
       'Destination_Country', 'Destination_City',
       'Destination_Port', 'Destination_Type_of_Entry',
       'Projected_Volume', 'Origin_Haulage', 'OH20', 'OH40',
       'OH40HC', 'OH45',
       'Origin_Terminal_Handling', 'OTHC20', 'OTHC40',
       'OTHC40HC', 'OTHC45', 'Ocean_Rates', 'OF20',
       'OF40', 'OF40HC', 'OF45',
       'Destination_Terminal_Handling', 'DTHC20', 'DTHC40',
       'DTHC40HC', 'DTHC45', 'Destination_Haulage', 'DH20',
       'DH40', 'DH40HC', 'DH45',
       'Lead_Time']

new.columns  = ['ID Number', 'Carrier', 'Origin_Region', 'Origin_Country',
       'Origin_City', 'Origin_Port',
       'Origin_Type_of_Departure', 'Destination_region',
       'Destination_Country', 'Destination_City',
       'Destination_Port', 'Destination_Type_of_Entry',
       'Projected_Volume', 'Origin_Haulage', 'OH20', 'OH40',
       'OH40HC', 'OH45',
       'Origin_Terminal_Handling', 'OTHC20', 'OTHC40',
       'OTHC40HC', 'OTHC45', 'Ocean_Rates', 'OF20',
       'OF40', 'OF40HC', 'OF45',
       'Destination_Terminal_Handling', 'DTHC20', 'DTHC40',
       'DTHC40HC', 'DTHC45', 'Destination_Haulage', 'DH20',
       'DH40', 'DH40HC', 'DH45',
       'Lead_Time']


# dropping first two rows as they are wrong
previous.drop([0,1],axis=0,inplace=True)
new.drop([0,1],axis=0,inplace=True)


# setting up upper case for carriers and striping strings
new.Carrier = new.Carrier.str.upper()
previous.Carrier = previous.Carrier.str.upper()
new.Carrier = new.Carrier.str.strip()
previous.Carrier = previous.Carrier.str.strip()

# adjusting the naming of the carrier so that it represents FCL file
previous['Carrier'].replace({'SEALAND ASIA':'MCC','CMA CGM':'CMA','SEALAND EUROPE & MED':'SEAGO',
                            'HAPAGLLOYD':'HAPAG'},inplace=True)
new['Carrier'].replace({'SEALAND ASIA':'MCC','CMA CGM':'CMA','SEALAND EUROPE & MED':'SEAGO',
                       'HAPAGLLOYD':'HAPAG'},inplace=True)

# creating a laneid columns for both frames

new['LaneID'] = new['ID Number'] + new['Carrier']
previous['LaneID'] = previous['ID Number'] + previous['Carrier']

# adding column for rates presence in previous dataframe
# and creating smaller dataframe for check-up
previous['Old_lane'] = 'yes'
boss_check = previous[['LaneID','Old_lane']]

# joining new boss with small dataframe for check-up
new = new.join(boss_check.set_index('LaneID'),on='LaneID')

# leaving only values that new lanes
new = new.loc[new['Old_lane'].isna()]

# deleting some AMERICAS shit
new = new[~new['Carrier'].str.contains('AMERICAS')]

# reading file for mapping
countries =pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping.xlsx',sheet_name = 'countries')
cities = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping.xlsx',sheet_name = 'cities')
ports =pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping.xlsx',sheet_name = 'ports')

# concatenating countries, cities and port from dataframe for new lanes
new_countries = pd.concat([new['Origin_Country'],new['Destination_Country']]).drop_duplicates().to_frame('Countries').reset_index(drop=True)
new_cities = pd.concat([new['Origin_City'],new['Destination_City']]).drop_duplicates().to_frame('Cities').reset_index(drop=True)
new_ports = pd.concat([new['Origin_Port'],new['Destination_Port']]).drop_duplicates().to_frame('Ports').reset_index(drop=True)

# checking if there are some new ports, cities or countries to be added
country_frame = new_countries.join(countries.set_index('Countries'), on = 'Countries').sort_values(by =['UNLCODE'])
city_frame =   new_cities.join(cities.set_index('Cities'), on = 'Cities').sort_values(by =['UNLCODE'])
port_frame = new_ports.join(ports.set_index('Ports'), on = 'Ports').sort_values(by =['UNLCODE'])


# saving the file with tabs for each countries, cities and ports
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping_test.xlsx',
                        engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
country_frame.to_excel(writer, sheet_name='countries',index=False)
city_frame.to_excel(writer, sheet_name = 'cities',index=False)
port_frame.to_excel(writer, sheet_name = 'ports',index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['countries']

# Get the xlsxwriter workbook and worksheet objects.
workbook1  = writer.book
worksheet1 = writer.sheets['cities']

# Get the xlsxwriter workbook and worksheet objects.
workbook2  = writer.book
worksheet2 = writer.sheets['ports']



# Close the Pandas Excel writer and output the Excel file.

writer.save()

pauza = input('Verify codes for countries, cities and ports. When'
              'ready - click ENTER')
# reading files with codes again (after modification)
countries =pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping.xlsx',sheet_name = 'countries')
cities = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping.xlsx',sheet_name = 'cities')
ports =pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Mapping.xlsx',sheet_name = 'ports')


# making a vlookup for ports, cities and countries
new['Origin_Country'] = new['Origin_Country'].map(countries.set_index('Countries')['UNLCODE'].to_dict())
new['Destination_Country'] = new['Destination_Country'].map(countries.set_index('Countries')['UNLCODE'].to_dict())
new['Origin_City'] = new['Origin_City'].map(cities.set_index('Cities')['UNLCODE'].to_dict())
new['Destination_City'] =new['Destination_City'].map(cities.set_index('Cities')['UNLCODE'].to_dict())
new['Origin_Port'] = new['Origin_Port'].map(ports.set_index('Ports')['UNLCODE'].to_dict())
new['Destination_Port'] = new['Destination_Port'].map(ports.set_index('Ports')['UNLCODE'].to_dict())

# replacing nan values with 0
new.iloc[:,18:33] = new.iloc[:,18:33].replace({np.nan:0})

# creaing datafrae for each cost
leg1 = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                     'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                     'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                     'CarrierCode': [], 'Predays': [], 'Transitdays': [],
                     'Postdays': [], 'ChargeType': [], 'ChargeCurr': [],
                     'Charge20ft': [],
                     'Charge40ft': [], 'Charge40hc': [], 'Charge40ftNOR': [],
                     'Charge40hcNOR': [], 'CHARGE45HC': [], 'CHARGE53HC': [], 'CHARGE20FTNOR': []
                     })

leg2 = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                     'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                     'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                     'CarrierCode': [], 'Predays': [], 'Transitdays': [],
                     'Postdays': [], 'Free Days': [],
                     'ChargeType': [], 'ChargeCurr': [],
                     'Charge20ft': [],
                     'Charge40ft': [], 'Charge40hc': [], 'Charge40ftNOR': [],
                     'Charge40hcNOR': [], 'CHARGE45HC': [], 'CHARGE53HC': [], 'CHARGE20FTNOR': []
                     })

leg2_origin = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                            'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                            'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                            'CarrierCode': [], 'Predays': [], 'Transitdays': [],
                            'Postdays': [], 'Free Days': [],
                            'ChargeType': [], 'ChargeCurr': [],
                            'Charge20ft': [],
                            'Charge40ft': [], 'Charge40hc': [], 'Charge40ftNOR': [],
                            'Charge40hcNOR': [], 'CHARGE45HC': [], 'CHARGE53HC': [], 'CHARGE20FTNOR': []
                            })

leg2_freight = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                             'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                             'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                             'CarrierCode': [], 'Predays': [], 'Transitdays': [],
                             'Postdays': [], 'Free Days': [],
                             'ChargeType': [], 'ChargeCurr': [],
                             'Charge20ft': [],
                             'Charge40ft': [], 'Charge40hc': [], 'Charge40ftNOR': [],
                             'Charge40hcNOR': [], 'CHARGE45HC': [], 'CHARGE53HC': [], 'CHARGE20FTNOR': []
                             })

leg2_dest = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                          'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                          'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                          'CarrierCode': [], 'Predays': [], 'Transitdays': [],
                          'Postdays': [], 'Free Days': [],
                          'ChargeType': [], 'ChargeCurr': [],
                          'Charge20ft': [],
                          'Charge40ft': [], 'Charge40hc': [], 'Charge40ftNOR': [],
                          'Charge40hcNOR': [], 'CHARGE45HC': [], 'CHARGE53HC': [], 'CHARGE20FTNOR': []
                          })

leg3 = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                     'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                     'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                     'CarrierCode': [], 'Predays': [], 'Transitdays': [],
                     'Postdays': [], 'ChargeType': [], 'ChargeCurr': [],
                     'Charge20ft': [],
                     'Charge40ft': [], 'Charge40hc': [], 'Charge40ftNOR': [],
                     'Charge40hcNOR': [], 'CHARGE45HC': [], 'CHARGE53HC': [], 'CHARGE20FTNOR': []
                     })

# extratcting data for leg 1 for each column


leg1['FromCountry'] = new['Origin_Country'].str[0:2]
leg1['FromCity'] = new['Origin_City']
leg1['FromUNLOCODE'] = new['Origin_City']
leg1['ToCountry'] = new['Origin_Port'].str[0:2]
leg1['ToCity'] = new['Origin_Port']
leg1['ToUNLOCODE'] = new['Origin_Port']
leg1['TransportMode'] = 'PRE'
leg1['CarrierName'] = new['Carrier']
leg1['CarrierCode'] = ''
leg1['Predays'] = 0
leg1['Transitdays'] = 3
leg1['Postdays'] = 0
leg1['ChargeType'] = 'Origin_Haulage'
leg1['ChargeCurr'] = new['Origin_Haulage']
leg1['Charge20ft'] = new['OH20']
leg1['Charge40ft'] = new['OH40']
leg1['Charge40hc'] = new['OH40HC']
leg1['Charge40ftNOR'] = 0
leg1['Charge40hcNOR'] = 0
leg1['CHARGE45HC'] = new['OH45']
leg1['CHARGE53HC'] = 0
leg1['CHARGE20FTNOR']=0
leg1['DateEffectiveFrom'] = start_date
leg1['DateEffectiveTo'] = end_date

# replacing nan with 0s
leg1.iloc[:,16:] = leg1.iloc[:,16:].replace({np.nan:0})

# dropping rows where connection is from port and not door
leg1.dropna(subset=['FromCity'],inplace=True)

# extratcting data for leg 2 for each column


leg2_origin['FromCountry'] = new['Origin_Port'].str[0:2]
leg2_origin['FromCity'] = new['Origin_Port']
leg2_origin['FromUNLOCODE'] = new['Origin_Port']
leg2_origin['ToCountry'] = new['Destination_Port'].str[0:2]
leg2_origin['ToCity'] = new['Destination_Port']
leg2_origin['ToUNLOCODE'] = new['Destination_Port']
leg2_origin['TransportMode'] = 'FCL'
leg2_origin['CarrierName'] = new['Carrier']
leg2_origin['CarrierCode'] = ''
leg2_origin['Predays'] = 2
leg2_origin['Transitdays'] = new['Lead_Time']
leg2_origin['Postdays'] = 2
leg2_origin['Free Days'] = 0
leg2_origin['ChargeType'] = 'Origin Terminal Handling'
leg2_origin['ChargeCurr'] = new['Origin_Terminal_Handling']
leg2_origin['DateEffectiveFrom'] = start_date
leg2_origin['DateEffectiveTo'] = end_date

leg2_origin['Charge20ft'] = new['OTHC20']
leg2_origin['Charge40ft'] = new['OTHC40']
leg2_origin['Charge40hc'] = new['OTHC40HC']
leg2_origin['Charge40ftNOR'] = 0
leg2_origin['Charge40hcNOR'] = 0
leg2_origin['CHARGE45HC'] = new['OTHC45']
leg2_origin['CHARGE53HC'] = 0
leg2_origin['CHARGE20FTNOR']=0


# changing na values to 0s
leg2_origin.iloc[:,17:] = leg1.iloc[:,17:].replace({np.nan:0})

# assigning values again
leg2_origin['Charge20ft'] = new['OTHC20']
leg2_origin['Charge40ft'] = new['OTHC40']
leg2_origin['Charge40hc'] = new['OTHC40HC']
leg2_origin['Charge40ftNOR'] = 0
leg2_origin['Charge40hcNOR'] = 0
leg2_origin['CHARGE45HC'] = new['OTHC45']
leg2_origin['CHARGE53HC'] = 0
leg2_origin['CHARGE20FTNOR']=0


# extracting values for freight
leg2_freight['FromCountry'] = new['Origin_Port'].str[0:2]
leg2_freight['FromCity'] = new['Origin_Port']
leg2_freight['FromUNLOCODE'] = new['Origin_Port']
leg2_freight['ToCountry'] = new['Destination_Port'].str[0:2]
leg2_freight['ToCity'] = new['Destination_Port']
leg2_freight['ToUNLOCODE'] = new['Destination_Port']
leg2_freight['TransportMode'] = 'FCL'
leg2_freight['CarrierName'] = new['Carrier']
leg2_freight['CarrierCode'] = ''
leg2_freight['Predays'] = 2
leg2_freight['Transitdays'] = new['Lead_Time']
leg2_freight['Postdays'] = 2
leg2_freight['Free Days'] = 0
leg2_freight['ChargeType'] = 'Ocean Rates'
leg2_freight['ChargeCurr'] = new['Ocean_Rates']

leg2_freight['DateEffectiveFrom'] = start_date
leg2_freight['DateEffectiveTo'] = end_date


# replacing nan with 0s
leg2_freight.iloc[:,17:] = leg1.iloc[:,17:].replace({np.nan:0})

# assigning values again
leg2_freight['Charge20ft'] = new['OF20']
leg2_freight['Charge40ft'] = new['OF40']
leg2_freight['Charge40hc'] = new['OF40HC']
leg2_freight['Charge40ftNOR'] = 0
leg2_freight['Charge40hcNOR'] = 0
leg2_freight['CHARGE45HC'] = new['OF45']
leg2_freight['CHARGE53HC'] = 0
leg2_freight['CHARGE20FTNOR']=0

# extracting values for destination handling
leg2_dest['FromCountry'] = new['Origin_Port'].str[0:2]
leg2_dest['FromCity'] = new['Origin_Port']
leg2_dest['FromUNLOCODE'] = new['Origin_Port']
leg2_dest['ToCountry'] = new['Destination_Port'].str[0:2]
leg2_dest['ToCity'] = new['Destination_Port']
leg2_dest['ToUNLOCODE'] = new['Destination_Port']
leg2_dest['TransportMode'] = 'FCL'
leg2_dest['CarrierName'] = new['Carrier']
leg2_dest['CarrierCode'] = ''
leg2_dest['Predays'] = 2
leg2_dest['Transitdays'] = new['Lead_Time']
leg2_dest['Postdays'] = 2
leg2_dest['Free Days'] = 0
leg2_dest['ChargeType'] = 'Destination Terminal Handling'
leg2_dest['ChargeCurr'] = new['Destination_Terminal_Handling']

leg2_dest['DateEffectiveFrom'] = start_date
leg2_dest['DateEffectiveTo'] = end_date

leg2_dest['Charge20ft'] = new['DTHC20']
leg2_dest['Charge40ft'] = new['DTHC40']
leg2_dest['Charge40hc'] = new['DTHC40HC']
leg2_dest['Charge40ftNOR'] = 0
leg2_dest['Charge40hcNOR'] = 0
leg2_dest['CHARGE45HC'] = new['DTHC45']
leg2_dest['CHARGE53HC'] = 0
leg2_dest['CHARGE20FTNOR']=0


# replacing na with 0s
leg2_dest.iloc[:,17:] = leg1.iloc[:,17:].replace({np.nan:0})

# assigning values again
leg2_dest['Charge20ft'] = new['DTHC20']
leg2_dest['Charge40ft'] = new['DTHC40']
leg2_dest['Charge40hc'] = new['DTHC40HC']
leg2_dest['Charge40ftNOR'] = 0
leg2_dest['Charge40hcNOR'] = 0
leg2_dest['CHARGE45HC'] = new['DTHC45']
leg2_dest['CHARGE53HC'] = 0
leg2_dest['CHARGE20FTNOR']=0

# extratcting data for leg 3 for each column


leg3['FromCountry'] = new['Destination_Port'].str[0:2]
leg3['FromCity'] = new['Destination_Port']
leg3['FromUNLOCODE'] = new['Destination_Port']
leg3['ToCountry'] = new['Destination_City'].str[0:2]
leg3['ToCity'] = new['Destination_City']
leg3['ToUNLOCODE'] = new['Destination_City']
leg3['TransportMode'] = 'PRE'
leg3['CarrierName'] = new['Carrier']
leg3['CarrierCode'] = ''
leg3['Predays'] = 0
leg3['Transitdays'] = 3
leg3['Postdays'] = 0
leg3['ChargeType'] = 'Destination Haulage'
leg3['ChargeCurr'] = new['Destination_Haulage']
leg3['Charge20ft'] = new['DH20']
leg3['Charge40ft'] = new['DH40']
leg3['Charge40hc'] = new['DH40HC']
leg3['Charge40ftNOR'] = 0
leg3['Charge40hcNOR'] = 0
leg3['CHARGE45HC'] = new['DH45']
leg3['CHARGE53HC'] = 0
leg3['CHARGE20FTNOR']=0
leg3['DateEffectiveFrom'] = start_date
leg3['DateEffectiveTo'] = end_date

# switching values from na to 0
leg3.iloc[:,16:] = leg3.iloc[:,16:].replace({np.nan:0})

# dropping rows that indicates to port connection and not to door
leg3.dropna(subset=['ToCity'],inplace=True)

# combining leg 2 dataframes into one
leg2 = pd.concat(([leg2_origin,leg2_freight,leg2_dest]))

# creating laneid columns for each leg
leg1['LANEID'] = leg1['FromUNLOCODE']+'_'+leg1['ToUNLOCODE']+'_'+leg1['CarrierName']
leg2['LANEID'] = leg2['FromUNLOCODE']+'_'+leg2['ToUNLOCODE']+'_'+leg2['CarrierName']
leg3['LANEID'] = leg3['FromUNLOCODE']+'_'+leg3['ToUNLOCODE']+'_'+leg3['CarrierName']

# reading rates upload for each leg and uppercasing carrier names
fcl_file_leg1 = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\FCL.xlsx',sheet_name='LEG1')
fcl_file_leg2 = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\FCL.xlsx',sheet_name='LEG2')
fcl_file_leg3 = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\FCL.xlsx',sheet_name='LEG3')

fcl_file_leg1['CarrierName'] = fcl_file_leg1['CarrierName'].str.upper()
fcl_file_leg2['CarrierName'] = fcl_file_leg2['CarrierName'].str.upper()
fcl_file_leg3['CarrierName'] = fcl_file_leg3['CarrierName'].str.upper()

# creating laneid for upload values
fcl_file_leg1['LANEID'] = fcl_file_leg1['FromUNLOCODE']+'_'+fcl_file_leg1['ToUNLOCODE']+'_'+fcl_file_leg1['CarrierName']
fcl_file_leg2['LANEID'] = fcl_file_leg2['FromUNLOCODE']+'_'+fcl_file_leg2['ToUNLOCODE']+'_'+fcl_file_leg2['CarrierName']
fcl_file_leg3['LANEID'] = fcl_file_leg3['FromUNLOCODE']+'_'+fcl_file_leg3['ToUNLOCODE']+'_'+fcl_file_leg3['CarrierName']

# creating additional column showing that rates are present
fcl_file_leg1['rates_present'] = 'yes'
fcl_file_leg2['rates_present'] = 'yes'
fcl_file_leg3['rates_present'] = 'yes'

# creating small dataframes for rates check-up

fcl_file_leg1 =fcl_file_leg1[['LANEID','rates_present']]
fcl_file_leg2 =fcl_file_leg2[['LANEID','rates_present']]
fcl_file_leg3 =fcl_file_leg3[['LANEID','rates_present']]


# dropping duplicate values from fcl legs dataframes
fcl_file_leg1.drop_duplicates(subset=['LANEID'],inplace=True)
fcl_file_leg2.drop_duplicates(subset=['LANEID'],inplace=True)
fcl_file_leg3.drop_duplicates(subset=['LANEID'],inplace=True)

# joining what we extracted from the allocation with upload file to check what is missing
leg1 = leg1.join(fcl_file_leg1.set_index('LANEID'),on='LANEID')
leg2 = leg2.join(fcl_file_leg2.set_index('LANEID'),on='LANEID')
leg3 = leg3.join(fcl_file_leg3.set_index('LANEID'),on='LANEID')

# leaving only rows that are indicated as missing
leg1 = leg1[pd.isna(leg1['rates_present'])]
leg2 = leg2[pd.isna(leg2['rates_present'])]
leg3 = leg3[pd.isna(leg3['rates_present'])]

# correcting the lane id to look for duplicates
leg1['LANEID'] = leg1['LANEID'] + '_'+ leg1['ChargeType']
leg2['LANEID'] = leg2['LANEID'] + '_'+ leg2['ChargeType']
leg3['LANEID'] = leg3['LANEID'] + '_'+ leg3['ChargeType']

# dropping duplicates for costs
leg1.drop_duplicates(subset=['LANEID'],inplace=True)
leg2.drop_duplicates(subset=['LANEID'],inplace=True)
leg3.drop_duplicates(subset=['LANEID'],inplace=True)

# sorting values
leg1.sort_values(by=['FromUNLOCODE','ToUNLOCODE','ChargeType'],inplace=True)
leg2.sort_values(by=['FromUNLOCODE','ToUNLOCODE','ChargeType'],inplace=True)
leg3.sort_values(by=['FromUNLOCODE','ToUNLOCODE','ChargeType'],inplace=True)

# moving results to excel
leg3.to_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Zleg3_new.xlsx',index=False)
leg2.to_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Zleg2_new.xlsx',index=False)
leg1.to_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\Zleg1_new.xlsx',index=False)

# establishing today date
dating = datetime.datetime.today().strftime('%Y-%m-%d')

# creaing dataframes for change logs
changes_leg1= pd.DataFrame({'Date' : [],'Changed_By':[],'Carrier':[],
                     'Leg':[],'Lane':[],'Change':[],'Change_Reason':[],'Additional_Comment':[]})
changes_leg2=pd.DataFrame({'Date' : [],'Changed_By':[],'Carrier':[],
                     'Leg':[],'Lane':[],'Change':[],'Change_Reason':[],'Additional_Comment':[]})
changes_leg3=pd.DataFrame({'Date' : [],'Changed_By':[],'Carrier':[],
                     'Leg':[],'Lane':[],'Change':[],'Change_Reason':[],'Additional_Comment':[]})

# loging leg 1 changes
changes_leg1['Date'] = datetime.datetime.today().stftime('%Y-%m-%d')
changes_leg1['Changed_By'] = "Maciej Janowski"
changes_leg1['Carrier'] = leg1['CarrierName']
changes_leg1['Leg'] = 1
changes_leg1['Lane'] = leg1['FromUNLOCODE'] +"-"+leg1['ToUNLOCODE']
changes_leg1['Change']= 'added rates'
changes_leg1['Change_Reason']= 'missing rates'
changes_leg1['Additional_Comment'] = 'new allocation'

# logging leg 2 changes
changes_leg2['Date'] = datetime.datetime.today().stftime('%Y-%m-%d')
changes_leg2['Changed_By'] = "Maciej Janowski"
changes_leg2['Carrier'] = leg2['CarrierName']
changes_leg2['Leg'] = 1
changes_leg2['Lane'] = leg2['FromUNLOCODE'] +"-"+leg2['ToUNLOCODE']
changes_leg2['Change']= 'added rates'
changes_leg2['Change_Reason']= 'missing rates'
changes_leg2['Additional_Comment'] = 'new allocation'
changes_leg2['duplicates']= leg2['FromUNLOCODE'] +"-"+leg2['ToUNLOCODE'] +"-"+leg2['Carrier']

# dropping duplicates (as there are 3 costs for each lane) and droping supportive column
changes_leg2.drop_duplicates(subset=['duplicates'],inplace=True)
changes_leg2.drop(columns=['duplicates'],inplace=True)


# logging leg 3 changes
changes_leg3['Date'] = datetime.datetime.today().stftime('%Y-%m-%d')
changes_leg3['Changed_By'] = "Maciej Janowski"
changes_leg3['Carrier'] = leg3['CarrierName']
changes_leg3['Leg'] = 1
changes_leg3['Lane'] = leg3['FromUNLOCODE'] +"-"+leg3['ToUNLOCODE']
changes_leg3['Change']= 'added rates'
changes_leg3['Change_Reason']= 'missing rates'
changes_leg3['Additional_Comment'] = 'new allocation'

# combining changes and saving to excelfile
changes = pd.concat[[changes_leg1,changes_leg2,changes_leg3]]
changes.to_excel(r'C:\Users\310295192\Desktop\Python\Projects\Python_Sea\ZchangesLOG.xlsx',index=False)



