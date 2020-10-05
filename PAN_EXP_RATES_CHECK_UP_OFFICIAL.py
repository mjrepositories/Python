import pandas as pd

# asking for details regarding files (dates to be more specific). For report and for uploads
address = input("Provide date for report in 'rrrr-mm-dd' format: ")
pan_file = input("Provide the date for Panalpina upload in 'rrrr-mm-dd' format: ")
exp_file = input("Provide the date for Expedtiors upload in 'rrrr-mm-dd' format: ")

# create data frame based on air report
airfile = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR {}.xlsx'.format(address)
air_df = pd.read_excel(airfile)

# leave only case that are not pending or solved
air_clean = air_df[air_df["Pending/Solved"].isna()]

# restrict number of columns
air_clean = air_clean.iloc[0:,:-9]

# create dataframe for expeditors
expeditors = air_clean[air_clean['Leg 2, Carrier Name']=='Expeditors Air & Sea S']
# create dateframe for panalpina
panalpina = air_clean[air_clean['Leg 2, Carrier Name']=='Panalpina AIR S']


# assign columns to be deleted
c = ['Bill of lading','Bookingnumber','GTNexus Id','Shipment modifier/canceller','Leg 2, Transport confirmation',
    'Confirmation status','Status Extended','Booker Group','Shipment Bill Of Lading (BOL) attached by',
     'Shipment Bill Of Lading (HBL) attached by','Invoice number','BL attached date', 'HBL attached date',
       'Leg 2, Total costs (purchase) EUR', 'Billable Indicator Leg 1',
       'Billable Indicator Leg 2', 'Billable Indicator Leg 3','Del terms','Container type(s)','Leg 3, Delivery Planned',
    'Leg 3, Delivery Actual','Booker id','Shipper id',"Original shipper name (1)",'Container number']
# drop columns from expeditors dataframe
expeditors.drop(columns=c,inplace=True)
# drop columns from panalpina dataframe
panalpina.drop(columns=c,inplace=True)
# reset index for panalpina dataframe
panalpina.reset_index(inplace=True,drop = True)
#reset index for expeditors dataframe
expeditors.reset_index(inplace=True,drop=True)

# create series for service level for panalpina
panalpina_series = pd.Series(panalpina['Leg 2, Transport Mode'])

# extract service level for shipmentp with panalpina
service = panalpina_series.str.extract(r'(\d)')
panalpina['service_level']=service

#create series for service level for expeditors
expeditors_series = pd.Series(expeditors['Leg 2, Transport Mode'])

# extract service level for shipments with expeditors
service_exp = expeditors_series.str.extract(r'(\d)')
expeditors['service_level']=service_exp

# create leg ids for panalpina and expeditors based on city names
panalpina['LEG1ID']='ALL'+"-"+ panalpina['Port of loading'].astype(str).str[2:5]+'-'+panalpina['service_level']
panalpina['LEG2ID'] = panalpina['Port of loading'].astype(str).str[2:5]+"-"+ panalpina['Port of discharge'].astype(str).str[2:5]+'-'+panalpina['service_level']
panalpina['LEG3ID'] =panalpina['Port of discharge'].astype(str).str[2:5]+"-"+ 'ALL'+'-'+panalpina['service_level']
expeditors['LEG1ID']= "ALL" +"-"+ expeditors['Port of loading'].astype(str).str[2:5]+'-'+expeditors['service_level']
expeditors['LEG2ID'] = expeditors['Port of loading'].astype(str).str[2:5] +"-"+ expeditors['Port of discharge'].astype(str).str[2:5]+'-'+expeditors['service_level']
expeditors['LEG3ID']= expeditors['Port of discharge'].astype(str).str[2:5] +"-"+ 'ALL'+'-'+ expeditors['service_level']

# creates the naming of the files for opening by pandas
p_rates = r'C:\Users\310295192\Desktop\Work\Rates\Air\Panalpina\Uploads\2019-2020 Rates Air Panalpina {}.xlsx'.format(pan_file)
e_rates = r'C:\Users\310295192\Desktop\Work\Rates\Air\Expeditors\Rates\2019-2020 Rates Expeditors AIR {}.xlsx'.format(exp_file)


# create data frame for each leg for panalpina
p_rates_l1 = pd.read_excel(p_rates,sheet_name='PRE_leg1')
p_rates_l2 = pd.read_excel(p_rates,sheet_name='AIR_leg2')
p_rates_l3 = pd.read_excel(p_rates,sheet_name='ONC_leg3')
# create data frame for each leg for expeditors
e_rates_l1 = pd.read_excel(e_rates,sheet_name='PRE_leg1')
e_rates_l2 = pd.read_excel(e_rates,sheet_name='AIR_leg2')
e_rates_l3 = pd.read_excel(e_rates,sheet_name='ONC_leg3')

# correct codes for expeditors to have it all uppercase
e_rates_l1['FromCity']=e_rates_l1['FromCity'].str.upper()
e_rates_l1['FromUNLOCODE']=e_rates_l1['FromUNLOCODE'].str.upper()
e_rates_l3['ToCity']=e_rates_l3['ToCity'].str.upper()
e_rates_l3['ToUNLOCODE']=e_rates_l3['ToUNLOCODE'].str.upper()

# create leg ids for panalpina rates dataframes
p_rates_l1['LEG1ID']=p_rates_l1['FromCity']+"-"+p_rates_l1['ToCity']+'-'+p_rates_l1['ServiceLevel'].astype(str)
p_rates_l2['LEG2ID']=p_rates_l2['FromCity']+"-"+p_rates_l2['ToCity']+'-'+p_rates_l2['ServiceLevel'].astype(str)
p_rates_l3['LEG3ID']=p_rates_l3['FromCity']+"-"+p_rates_l3['ToCity']+'-'+p_rates_l3['ServiceLevel'].astype(str)
# create leg ids for expeditors rates dataframes
e_rates_l1['LEG1ID']=e_rates_l1['FromCity']+"-"+e_rates_l1['ToCity']+'-'+e_rates_l1['ServiceLevel'].astype(str)
e_rates_l2['LEG2ID']=e_rates_l2['FromCity']+"-"+e_rates_l2['ToCity']+'-'+e_rates_l2['ServiceLevel'].astype(str)
e_rates_l3['LEG3ID']=e_rates_l3['FromCity']+"-"+e_rates_l3['ToCity']+'-'+e_rates_l3['ServiceLevel'].astype(str)

# create dataframes for panalpina and expeditors containing only leg ids
p_drop = pd.DataFrame(p_rates_l1['LEG1ID'])
e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])
p2_drop = pd.DataFrame(p_rates_l2['LEG2ID'])
e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])
p3_drop = pd.DataFrame(p_rates_l3['LEG3ID'])
e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

# renaming columns for dataframes for panalpina and expeditors for further adding it to report
p_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
e_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
p2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
e2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
p3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
e3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)

# removing duplicate values for all dataframes with leg ids for panalpina and epxeditors
p_drop.drop_duplicates()
e_drop.drop_duplicates()
p2_drop.drop_duplicates()
e2_drop.drop_duplicates()
p3_drop.drop_duplicates()
e3_drop.drop_duplicates()

# creating columns for dataframes for panalpina and expeditors indicating presence of rates
# setting up an index to have the possibility to join dataframes
p_drop['Leg1RatesPresent']=True
p_drop.set_index('L1', inplace=True, drop=True)
e_drop['Leg1RatesPresent']=True
e_drop.set_index('L1', inplace=True, drop=True)
p2_drop['Leg2RatesPresent']=True
p2_drop.set_index('L2', inplace=True, drop=True)
e2_drop['Leg2RatesPresent']=True
e2_drop.set_index('L2', inplace=True, drop=True)
p3_drop['Leg3RatesPresent']=True
p3_drop.set_index('L3', inplace=True, drop=True)
e3_drop['Leg3RatesPresent']=True
e3_drop.set_index('L3', inplace=True, drop=True)

# x.join(p_drop)
# joining each table confirming rates presence
# methodology - each time index for leg is assigned to main dataframe
# then main dataframe is joined with rates confirmation dataframe
# when joining is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assigns proper index
# when new index is assigned then program joins another dataframe to verify presence of rates
panalpina.set_index('LEG1ID', inplace=True, drop=False)
panalpina = panalpina.join(p_drop)
panalpina.set_index('LEG2ID', inplace=True, drop=False)
panalpina = panalpina.join(p2_drop)
panalpina.set_index('LEG3ID', inplace=True, drop=False)
panalpina = panalpina.join(p3_drop)
expeditors.set_index('LEG1ID', inplace=True, drop=False)
expeditors = expeditors.join(e_drop)
expeditors.set_index('LEG2ID', inplace=True, drop=False)
expeditors = expeditors.join(e2_drop)
expeditors.set_index('LEG3ID', inplace=True, drop=False)
expeditors = expeditors.join(e3_drop)
panalpina.reset_index(inplace=True,drop = True)
expeditors.reset_index(inplace=True,drop = True)

# sending the dataframe for panalpina to excel
panalpina.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\Panalpina check-up {}.xlsx').format(address)
# sending the dataframe for expeditors to excel
expeditors.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\Expeditors check-up {}.xlsx').format(address)
