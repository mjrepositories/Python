import pandas as pd
# address = input("Provide date for report in 'rrrr-mm-dd' format: ")
address = input("provide today date")

mps = input('provide mps file')

exp_file = input("Porvide date for expeditors file")
# create data frame based on air report
airfile = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR {} updated.xlsx'.format(address)
air_df = pd.read_excel(airfile)

# leave only case that are not pending or solved
#air_clean = air_df[air_df["Pending/Solved"].isna()]
air_clean = air_df[air_df["Leg 2, Transport Mode"].str.contains("Service",na=False)]

# create dataframe for expeditors
expeditors = air_clean[air_clean['Leg 2, Carrier Name']=='Expeditors Air & Sea S']

#create series for service level for expeditors
expeditors_series = pd.Series(expeditors['Leg 2, Transport Mode'])
# extract service level for shipments with expeditors
service_exp = expeditors_series.str.extract(r'(\d)')
expeditors['service_level']=service_exp

# create leg ids for panalpina and expeditors based on city names
expeditors['LEG1ID']= "ALL" +"-"+ expeditors['Port of loading'].astype(str).str[2:5]+'-'+expeditors['service_level']
expeditors['LEG2ID'] = expeditors['Port of loading'].astype(str).str[2:5] +"-"+ expeditors['Port of discharge'].astype(str).str[2:5]+'-'+expeditors['service_level']
expeditors['LEG3ID']= expeditors['Port of discharge'].astype(str).str[2:5] +"-"+ 'ALL'+'-'+ expeditors['service_level']


e_rates = r'C:\Users\310295192\Desktop\Work\Rates\Air\Expeditors\Rates\2019-2020 Rates Expeditors AIR {}.xlsx'.format(exp_file)

# create data frame for each leg for expeditors
e_rates_l1 = pd.read_excel(e_rates,sheet_name='PRE_leg1')
e_rates_l2 = pd.read_excel(e_rates,sheet_name='AIR_leg2')
e_rates_l3 = pd.read_excel(e_rates,sheet_name='ONC_leg3')

# correct codes for expeditors to have it all uppercase
e_rates_l1['FromCity']=e_rates_l1['FromCity'].str.upper()
e_rates_l1['FromUNLOCODE']=e_rates_l1['FromUNLOCODE'].str.upper()
e_rates_l1['ToCity']=e_rates_l1['ToCity'].str.upper()
e_rates_l1['ToUNLOCODE']=e_rates_l1['ToUNLOCODE'].str.upper()

e_rates_l2['FromCity']=e_rates_l2['FromCity'].str.upper()
e_rates_l2['FromUNLOCODE']=e_rates_l2['FromUNLOCODE'].str.upper()
e_rates_l2['ToCity']=e_rates_l2['ToCity'].str.upper()
e_rates_l2['ToUNLOCODE']=e_rates_l2['ToUNLOCODE'].str.upper()

e_rates_l3['FromCity']=e_rates_l3['FromCity'].str.upper()
e_rates_l3['FromUNLOCODE']=e_rates_l3['FromUNLOCODE'].str.upper()
e_rates_l3['ToCity']=e_rates_l3['ToCity'].str.upper()
e_rates_l3['ToUNLOCODE']=e_rates_l3['ToUNLOCODE'].str.upper()


# create leg ids for expeditors rates dataframes
e_rates_l1['LEG1ID']=e_rates_l1['FromCity']+"-"+e_rates_l1['ToCity']+'-'+e_rates_l1['ServiceLevel'].astype(str)
e_rates_l2['LEG2ID']=e_rates_l2['FromCity']+"-"+e_rates_l2['ToCity']+'-'+e_rates_l2['ServiceLevel'].astype(str)
e_rates_l3['LEG3ID']=e_rates_l3['FromCity']+"-"+e_rates_l3['ToCity']+'-'+e_rates_l3['ServiceLevel'].astype(str)

# create dataframes for panalpina and expeditors containing only leg ids

e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])

e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])

e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

# renaming columns for dataframes for panalpina and expeditors for further adding it to report

e_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)

e2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)

e3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)

# removing duplicate values for all dataframes with leg ids for panalpina and epxeditors

e_drop.drop_duplicates()

e2_drop.drop_duplicates()

e3_drop.drop_duplicates()

# creating columns for dataframes for panalpina and expeditors indicating presence of rates
# setting up an index to have the possibility to join dataframes

e_drop['Leg1RatesPresent']=True
e_drop.set_index('L1', inplace=True, drop=True)

e2_drop['Leg2RatesPresent']=True
e2_drop.set_index('L2', inplace=True, drop=True)

e3_drop['Leg3RatesPresent']=True
e3_drop.set_index('L3', inplace=True, drop=True)

# x.join(p_drop)
# joining each table confirming rates presence
# methodology - each time index for leg is assigned to main dataframe
# then main dataframe is joined with rates confirmation dataframe
# when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
# when new index is assigned then program joins another dataframe to verify presence of rates

expeditors.set_index('LEG1ID', inplace=True, drop=False)
expeditors = expeditors.join(e_drop)
expeditors.set_index('LEG2ID', inplace=True, drop=False)
expeditors = expeditors.join(e2_drop)
expeditors.set_index('LEG3ID', inplace=True, drop=False)
expeditors = expeditors.join(e3_drop)

expeditors.reset_index(inplace=True,drop = True)

expeditors.drop_duplicates(subset='Shipment',inplace=True)

mps = pd.read_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\MPS\MPS Air Freight 2019 December.xlsx',sheet_name=0,
                   skiprows=[0],header=[0],parse_cols='A:AG',names=["skip0","DateFrom","DateTo","Sector","Carrier",
                                                                    "LaneID","AirportID","skip4","skip5","AirportFrom",
                                                                    "FromCountry","RegionFrom",
                                                                    "AirportTo","ToCountry","RegionTo","DD","DP","PD","PP",
                                                                    "skip1","skip2","skip3","Currency","PickUp","CustomsOrigin",
                                                                    "HandlingOrigin","AirFreight",
                                                                    "HandlingDestination","CustomsDestination",
                                                                    "skip5","Delivery","ScreeningType","ScreeningPrice"],
                                                                      keep_default_na=False)
# selecting only two columns
mps  = mps[['Carrier','LaneID']]

mps.LaneID =  mps.LaneID.str[2:]

expeditors["LANEID"] = expeditors['Port of loading'].str[2:] +"-"+expeditors['Port of discharge'].str[2:] + '-'+expeditors['service_level']
expeditors['allocation'] = expeditors['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())
expeditors.drop(columns=['Action taken','Pending/Solved','date of email','E-mail subject','Delay in answer',
                        'Comments from carrier','Comments','Booker name (1)','Shipper name (1)',
                        'Original shipper name (1)'])


# sending the dataframe for expeditors to excel
expeditors.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\Expeditors check-up {}.xlsx'.format(address),
                   index=False)