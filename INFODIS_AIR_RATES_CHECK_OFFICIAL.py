import pandas as pd
print("type n if report is not needed")

print(r"C:\Users\310295192\Desktop")


exp_report = input("Provide path to Expeditors report: ")
rates_for_exp = input("Provide path to Expeditors rates: ")

pan_report = input("Provide path to Panalpina report: ")
rates_for_pan = input("Provide path to Panalpina rates: ")

ups_report = input("Provide path to UPS report: ")
rates_for_ups = input("Provide path to UPS rates: ")

dhl_report = input("Provide path to DHL report: ")
rates_for_dhl = input("Provide path to DHL rates: ")

mps_file = input('Provide path to MPS file: ')
address = input("Provide today date: ")


# loading of MPS data
mps = pd.read_excel(mps_file, sheet_name=0,
                    skiprows=[0], header=[0], parse_cols='A:AG',
                    names=["skip0", "DateFrom", "DateTo", "Sector", "Carrier",
                           "LaneID", "AirportID", "skip4", "skip5", "AirportFrom",
                           "FromCountry", "RegionFrom",
                           "AirportTo", "ToCountry", "RegionTo", "DD", "DP", "PD", "PP",
                           "skip1", "skip2", "skip3", "Currency", "PickUp", "CustomsOrigin",
                           "HandlingOrigin", "AirFreight",
                           "HandlingDestination", "CustomsDestination",
                           "skip5", "Delivery", "ScreeningType", "ScreeningPrice"],
                    keep_default_na=False)
# create date frame with carrie and LANE ID only
mps = mps[['Carrier', 'LaneID']]

# extract proper value for Lane ID
mps.LaneID = mps.LaneID.str[2:]




if exp_report!='n':
    air_df = pd.read_excel(exp_report)

    # leave only case that are not pending or solved
    expeditors = air_df[air_df["Leg 2, Transport Mode"].str.contains("Service")]
    expeditors = expeditors.loc[expeditors['Total costs EUR']==0]
    expeditors  = expeditors.rename(columns= {'Leg 1, Leg pickup country':'Pickup country','Leg n, Leg delivery country':"Delivery country"})

    # dropping columns
    expeditors.drop(columns=['Domain Name','Booker id','Booker_name','Pallets','Units',
                            'Total costs EUR','Leg 1, Total costs EUR','Leg 2, Total costs EUR',
                            'Leg 3, Total costs EUR','Billable Leg 1','Billable Leg 2',
                            'Billable Leg 3','Weight_shipment','Volume_shipment',
                            'Length','Width','Height','Container type','Number of packages'])

    #create series for service level for expeditors
    expeditors_series = pd.Series(expeditors['Leg 2, Transport Mode'])
    # extract service level for shipments with expeditors
    service_exp = expeditors_series.str.extract(r'(\d)')
    expeditors['service_level']=service_exp

    expeditors['LEG1ID']= "ALL" +"-"+ expeditors['Port of loading'].astype(str).str[2:5]+'-'+expeditors['service_level']
    expeditors['LEG2ID'] = expeditors['Port of loading'].astype(str).str[2:5] +"-"+ expeditors['Port of discharge'].astype(str).str[2:5]+'-'+expeditors['service_level']
    expeditors['LEG3ID']= expeditors['Port of discharge'].astype(str).str[2:5] +"-"+ 'ALL'+'-'+ expeditors['service_level']

    e_rates = rates_for_exp

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
    #p_drop = pd.DataFrame(p_rates_l1['LEG1ID'])
    e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])
    #p2_drop = pd.DataFrame(p_rates_l2['LEG2ID'])
    e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])
    #p3_drop = pd.DataFrame(p_rates_l3['LEG3ID'])
    e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'] )

    # renaming columns for dataframes for panalpina and expeditors for further adding it to report
    #p_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    e_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    #p2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    e2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    #p3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e2_drop['L2']=e2_drop['L2'].str[0:9]

    # removing duplicate values for all dataframes with leg ids for panalpina and epxeditors
    #p_drop.drop_duplicates()
    e_drop.drop_duplicates()
    #p2_drop.drop_duplicates()
    e2_drop.drop_duplicates()
    #p3_drop.drop_duplicates()
    e3_drop.drop_duplicates()

    # creating columns for dataframes for panalpina and expeditors indicating presence of rates
    # setting up an index to have the possibility to join dataframes
    #p_drop['Leg1RatesPresent']=True
    #p_drop.set_index('L1', inplace=True, drop=True)
    e_drop['Leg1RatesPresent']=True
    e_drop.set_index('L1', inplace=True, drop=True)
    #p2_drop['Leg2RatesPresent']=True
    #p2_drop.set_index('L2', inplace=True, drop=True)
    e2_drop['Leg2RatesPresent']=True
    e2_drop.set_index('L2', inplace=True, drop=True)
    #p3_drop['Leg3RatesPresent']=True
    #p3_drop.set_index('L3', inplace=True, drop=True)
    e3_drop['Leg3RatesPresent']=True
    e3_drop.set_index('L3', inplace=True, drop=True)

    # joining each table confirming rates presence
    # methodology - each time index for leg is assigned to main dataframe
    # then main dataframe is joined with rates confirmation dataframe
    # when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
    # when new index is assigned then program joins another dataframe to verify presence of rates
    #panalpina.set_index('LEG1ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p_drop)
    #panalpina.set_index('LEG2ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p2_drop)
    #panalpina.set_index('LEG3ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p3_drop)
    expeditors.set_index('LEG1ID', inplace=True, drop=False)
    expeditors = expeditors.join(e_drop)
    expeditors.set_index('LEG2ID', inplace=True, drop=False)
    expeditors = expeditors.join(e2_drop)
    expeditors.set_index('LEG3ID', inplace=True, drop=False)
    expeditors = expeditors.join(e3_drop)
    #panalpina.reset_index(inplace=True,drop = True)
    expeditors.reset_index(inplace=True,drop = True)

    expeditors.drop_duplicates(subset='Shipment',inplace=True)

    # mps = pd.read_excel(mps_file,sheet_name=0,
    #                    skiprows=[0],header=[0],parse_cols='A:AG',names=["skip0","DateFrom","DateTo","Sector","Carrier",
    #                                                                     "LaneID","AirportID","skip4","skip5","AirportFrom",
    #                                                                     "FromCountry","RegionFrom",
    #                                                                     "AirportTo","ToCountry","RegionTo","DD","DP","PD","PP",
    #                                                                     "skip1","skip2","skip3","Currency","PickUp","CustomsOrigin",
    #                                                                     "HandlingOrigin","AirFreight",
    #                                                                     "HandlingDestination","CustomsDestination",
    #                                                                     "skip5","Delivery","ScreeningType","ScreeningPrice"],
    #                                                                       keep_default_na=False)
    # # create date frame with carrie and LANE ID only
    # mps  = mps[['Carrier','LaneID']]
    #
    # # extract proper value for Lane ID
    # mps.LaneID =  mps.LaneID.str[2:]

    # create additional column with LAND ID in Expeditors data frame
    # And indicate in the report who is allocate based on MPS
    expeditors["LANEID"] = expeditors['Port of loading'].str[2:] +"-"+expeditors['Port of discharge'].str[2:] + '-'+expeditors['service_level']
    expeditors['allocation'] = expeditors['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())

    expeditors.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\Expeditors check-up {}.xlsx'.format(address),index=False)






#Panalpina
#Panalpina
#Panalpina

if pan_report!='n':
    air_df = pd.read_excel(pan_report)
    # leave only case that are not pending or solved
    panalpina = air_df[air_df["Leg 1, Transport Mode"].str.contains("Service")]
    panalpina = panalpina.loc[panalpina['Total costs EUR']==0]
    panalpina  = panalpina.rename(columns= {'Leg 1, Leg pickup country':'Pickup country','Leg n, Leg delivery country':"Delivery country"})

    # dropping columns
    panalpina.drop(columns=['Domain Name','Booker id','Booker_name','Pallets','Units',
                            'Total costs EUR','Leg 1, Total costs EUR','Leg 2, Total costs EUR',
                            'Leg 3, Total costs EUR','Billable Leg 1','Billable Leg 2',
                            'Billable Leg 3','Weight_shipment','Volume_shipment',
                            'Length','Width','Height','Container type','Number of packages'])

    #create series for service level for panalpina
    expeditors_series = pd.Series(panalpina['Leg 1, Transport Mode'])
    # extract service level for shipments with panalpina
    service_exp = expeditors_series.str.extract(r'(\d)')
    panalpina['service_level']=service_exp

    panalpina['LEG1ID']= "ALL" +"-"+ panalpina['Port of loading'].astype(str).str[2:5]+'-'+panalpina['service_level']
    panalpina['LEG2ID'] = panalpina['Port of loading'].astype(str).str[2:5] +"-"+ panalpina['Port of discharge'].astype(str).str[2:5]+'-'+panalpina['service_level']
    panalpina['LEG3ID']= panalpina['Port of discharge'].astype(str).str[2:5] +"-"+ 'ALL'+'-'+ panalpina['service_level']

    e_rates = rates_for_exp

    # create data frame for each leg for panalpina
    e_rates_l1 = pd.read_excel(e_rates,sheet_name='PRE_leg1')
    e_rates_l2 = pd.read_excel(e_rates,sheet_name='AIR_leg2')
    e_rates_l3 = pd.read_excel(e_rates,sheet_name='ONC_leg3')

    # correct codes for panalpina to have it all uppercase
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

    # create leg ids for panalpina rates dataframes
    e_rates_l1['LEG1ID']=e_rates_l1['FromCity']+"-"+e_rates_l1['ToCity']+'-'+e_rates_l1['ServiceLevel'].astype(str)
    e_rates_l2['LEG2ID']=e_rates_l2['FromCity']+"-"+e_rates_l2['ToCity']+'-'+e_rates_l2['ServiceLevel'].astype(str)
    e_rates_l3['LEG3ID']=e_rates_l3['FromCity']+"-"+e_rates_l3['ToCity']+'-'+e_rates_l3['ServiceLevel'].astype(str)


    # create dataframes for panalpina and panalpina containing only leg ids
    #p_drop = pd.DataFrame(p_rates_l1['LEG1ID'])
    e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])
    #p2_drop = pd.DataFrame(p_rates_l2['LEG2ID'])
    e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])
    #p3_drop = pd.DataFrame(p_rates_l3['LEG3ID'])
    e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

    # renaming columns for dataframes for panalpina and panalpina for further adding it to report
    #p_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    e_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    #p2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    e2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    #p3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e2_drop['L2']=e2_drop['L2'].str[0:9]

    # removing duplicate values for all dataframes with leg ids for panalpina and epxeditors
    #p_drop.drop_duplicates()
    e_drop.drop_duplicates()
    #p2_drop.drop_duplicates()
    e2_drop.drop_duplicates()
    #p3_drop.drop_duplicates()
    e3_drop.drop_duplicates()

    # creating columns for dataframes for panalpina and panalpina indicating presence of rates
    # setting up an index to have the possibility to join dataframes
    #p_drop['Leg1RatesPresent']=True
    #p_drop.set_index('L1', inplace=True, drop=True)
    e_drop['Leg1RatesPresent']=True
    e_drop.set_index('L1', inplace=True, drop=True)
    #p2_drop['Leg2RatesPresent']=True
    #p2_drop.set_index('L2', inplace=True, drop=True)
    e2_drop['Leg2RatesPresent']=True
    e2_drop.set_index('L2', inplace=True, drop=True)
    #p3_drop['Leg3RatesPresent']=True
    #p3_drop.set_index('L3', inplace=True, drop=True)
    e3_drop['Leg3RatesPresent']=True
    e3_drop.set_index('L3', inplace=True, drop=True)

    # joining each table confirming rates presence
    # methodology - each time index for leg is assigned to main dataframe
    # then main dataframe is joined with rates confirmation dataframe
    # when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
    # when new index is assigned then program joins another dataframe to verify presence of rates
    #panalpina.set_index('LEG1ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p_drop)
    #panalpina.set_index('LEG2ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p2_drop)
    #panalpina.set_index('LEG3ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p3_drop)
    panalpina.set_index('LEG1ID', inplace=True, drop=False)
    panalpina = panalpina.join(e_drop)
    panalpina.set_index('LEG2ID', inplace=True, drop=False)
    panalpina = panalpina.join(e2_drop)
    panalpina.set_index('LEG3ID', inplace=True, drop=False)
    panalpina = panalpina.join(e3_drop)
    #panalpina.reset_index(inplace=True,drop = True)
    panalpina.reset_index(inplace=True,drop = True)

    panalpina.drop_duplicates(subset='Shipment',inplace=True)

    # mps = pd.read_excel(mps_file,sheet_name=0,
    #                    skiprows=[0],header=[0],parse_cols='A:AG',names=["skip0","DateFrom","DateTo","Sector","Carrier",
    #                                                                     "LaneID","AirportID","skip4","skip5","AirportFrom",
    #                                                                     "FromCountry","RegionFrom",
    #                                                                     "AirportTo","ToCountry","RegionTo","DD","DP","PD","PP",
    #                                                                     "skip1","skip2","skip3","Currency","PickUp","CustomsOrigin",
    #                                                                     "HandlingOrigin","AirFreight",
    #                                                                     "HandlingDestination","CustomsDestination",
    #                                                                     "skip5","Delivery","ScreeningType","ScreeningPrice"],
    #                                                                       keep_default_na=False)
    # # create date frame with carrie and LANE ID only
    # mps  = mps[['Carrier','LaneID']]
    #
    # # extract proper value for Lane ID
    # mps.LaneID =  mps.LaneID.str[2:]

    # create additional column with LAND ID in Expeditors data frame
    # And indicate in the report who is allocate based on MPS
    panalpina["LANEID"] = panalpina['Port of loading'].str[2:] +"-"+panalpina['Port of discharge'].str[2:] + '-'+panalpina['service_level']
    panalpina['allocation'] = panalpina['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())


    panalpina.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\Panalpina check-up {}.xlsx'.format(address),index=False)



#UPS
#UPS
#UPS


if ups_report!='n':
    air_df = pd.read_excel(ups_report)
    # leave only case that are not pending or solved
    ups = air_df[air_df["Leg 1, Transport Mode"].str.contains("Service")]
    ups = ups.loc[ups['Total costs EUR']==0]
    ups  = ups.rename(columns= {'Leg 1, Leg pickup country':'Pickup country','Leg n, Leg delivery country':"Delivery country"})

    # dropping columns
    ups.drop(columns=['Domain Name','Booker id','Booker_name','Pallets','Units',
                            'Total costs EUR','Leg 1, Total costs EUR','Leg 2, Total costs EUR',
                            'Leg 3, Total costs EUR','Billable Leg 1','Billable Leg 2',
                            'Billable Leg 3','Weight_shipment','Volume_shipment',
                            'Length','Width','Height','Container type','Number of packages'])

    #create series for service level for ups
    expeditors_series = pd.Series(ups['Leg 1, Transport Mode'])
    # extract service level for shipments with ups
    service_exp = expeditors_series.str.extract(r'(\d)')
    ups['service_level']=service_exp

    ups['LEG1ID']= "ALL" +"-"+ ups['Port of loading'].astype(str).str[2:5]+'-'+ups['service_level']
    ups['LEG2ID'] = ups['Port of loading'].astype(str).str[2:5] +"-"+ ups['Port of discharge'].astype(str).str[2:5]+'-'+ups['service_level']
    ups['LEG3ID']= ups['Port of discharge'].astype(str).str[2:5] +"-"+ 'ALL'+'-'+ ups['service_level']

    e_rates = rates_for_exp

    # create data frame for each leg for ups
    e_rates_l1 = pd.read_excel(e_rates,sheet_name='PRE_leg1')
    e_rates_l2 = pd.read_excel(e_rates,sheet_name='AIR_leg2')
    e_rates_l3 = pd.read_excel(e_rates,sheet_name='ONC_leg3')

    # correct codes for ups to have it all uppercase
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

    # create leg ids for ups rates dataframes
    e_rates_l1['LEG1ID']=e_rates_l1['FromCity']+"-"+e_rates_l1['ToCity']+'-'+e_rates_l1['ServiceLevel'].astype(str)
    e_rates_l2['LEG2ID']=e_rates_l2['FromCity']+"-"+e_rates_l2['ToCity']+'-'+e_rates_l2['ServiceLevel'].astype(str)
    e_rates_l3['LEG3ID']=e_rates_l3['FromCity']+"-"+e_rates_l3['ToCity']+'-'+e_rates_l3['ServiceLevel'].astype(str)


    # create dataframes for panalpina and ups containing only leg ids
    #p_drop = pd.DataFrame(p_rates_l1['LEG1ID'])
    e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])
    #p2_drop = pd.DataFrame(p_rates_l2['LEG2ID'])
    e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])
    #p3_drop = pd.DataFrame(p_rates_l3['LEG3ID'])
    e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

    # renaming columns for dataframes for panalpina and ups for further adding it to report
    #p_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    e_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    #p2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    e2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    #p3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e2_drop['L2']=e2_drop['L2'].str[0:9]

    # removing duplicate values for all dataframes with leg ids for panalpina and epxeditors
    #p_drop.drop_duplicates()
    e_drop.drop_duplicates()
    #p2_drop.drop_duplicates()
    e2_drop.drop_duplicates()
    #p3_drop.drop_duplicates()
    e3_drop.drop_duplicates()

    # creating columns for dataframes for panalpina and ups indicating presence of rates
    # setting up an index to have the possibility to join dataframes
    #p_drop['Leg1RatesPresent']=True
    #p_drop.set_index('L1', inplace=True, drop=True)
    e_drop['Leg1RatesPresent']=True
    e_drop.set_index('L1', inplace=True, drop=True)
    #p2_drop['Leg2RatesPresent']=True
    #p2_drop.set_index('L2', inplace=True, drop=True)
    e2_drop['Leg2RatesPresent']=True
    e2_drop.set_index('L2', inplace=True, drop=True)
    #p3_drop['Leg3RatesPresent']=True
    #p3_drop.set_index('L3', inplace=True, drop=True)
    e3_drop['Leg3RatesPresent']=True
    e3_drop.set_index('L3', inplace=True, drop=True)

    # joining each table confirming rates presence
    # methodology - each time index for leg is assigned to main dataframe
    # then main dataframe is joined with rates confirmation dataframe
    # when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
    # when new index is assigned then program joins another dataframe to verify presence of rates
    #panalpina.set_index('LEG1ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p_drop)
    #panalpina.set_index('LEG2ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p2_drop)
    #panalpina.set_index('LEG3ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p3_drop)
    ups.set_index('LEG1ID', inplace=True, drop=False)
    ups = ups.join(e_drop)
    ups.set_index('LEG2ID', inplace=True, drop=False)
    ups = ups.join(e2_drop)
    ups.set_index('LEG3ID', inplace=True, drop=False)
    ups = ups.join(e3_drop)
    #panalpina.reset_index(inplace=True,drop = True)
    ups.reset_index(inplace=True,drop = True)

    ups.drop_duplicates(subset='Shipment',inplace=True)

    # mps = pd.read_excel(mps_file,sheet_name=0,
    #                    skiprows=[0],header=[0],parse_cols='A:AG',names=["skip0","DateFrom","DateTo","Sector","Carrier",
    #                                                                     "LaneID","AirportID","skip4","skip5","AirportFrom",
    #                                                                     "FromCountry","RegionFrom",
    #                                                                     "AirportTo","ToCountry","RegionTo","DD","DP","PD","PP",
    #                                                                     "skip1","skip2","skip3","Currency","PickUp","CustomsOrigin",
    #                                                                     "HandlingOrigin","AirFreight",
    #                                                                     "HandlingDestination","CustomsDestination",
    #                                                                     "skip5","Delivery","ScreeningType","ScreeningPrice"],
    #                                                                       keep_default_na=False)
    # # create date frame with carrie and LANE ID only
    # mps  = mps[['Carrier','LaneID']]
    #
    # # extract proper value for Lane ID
    # mps.LaneID =  mps.LaneID.str[2:]

    # create additional column with LAND ID in Expeditors data frame
    # And indicate in the report who is allocate based on MPS
    ups["LANEID"] = ups['Port of loading'].str[2:] +"-"+ups['Port of discharge'].str[2:] + '-'+ups['service_level']
    ups['allocation'] = ups['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())

    ups.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\UPS check-up {}.xlsx'.format(address),index=False)




#DHL
#DHL
#DHL

if dhl_report!="n":
    air_df = pd.read_excel(dhl_report)
    # leave only case that are not pending or solved
    dhl = air_df[air_df["Leg 1, Transport Mode"].str.contains("Service")]
    dhl = dhl.loc[dhl['Total costs EUR']==0]
    dhl  = dhl.rename(columns= {'Leg 1, Leg pickup country':'Pickup country','Leg n, Leg delivery country':"Delivery country"})

    # dropping columns
    dhl.drop(columns=['Domain Name','Booker id','Booker_name','Pallets','Units',
                            'Total costs EUR','Leg 1, Total costs EUR','Leg 2, Total costs EUR',
                            'Leg 3, Total costs EUR','Billable Leg 1','Billable Leg 2',
                            'Billable Leg 3','Weight_shipment','Volume_shipment',
                            'Length','Width','Height','Container type','Number of packages'])

    #create series for service level for dhl
    expeditors_series = pd.Series(dhl['Leg 1, Transport Mode'])
    # extract service level for shipments with dhl
    service_exp = expeditors_series.str.extract(r'(\d)')
    dhl['service_level']=service_exp

    dhl['LEG1ID']= "ALL" +"-"+ dhl['Port of loading'].astype(str).str[2:5]+'-'+dhl['service_level']
    dhl['LEG2ID'] = dhl['Port of loading'].astype(str).str[2:5] +"-"+ dhl['Port of discharge'].astype(str).str[2:5]+'-'+dhl['service_level']
    dhl['LEG3ID']= dhl['Port of discharge'].astype(str).str[2:5] +"-"+ 'ALL'+'-'+ dhl['service_level']

    e_rates = rates_for_exp

    # create data frame for each leg for dhl
    e_rates_l1 = pd.read_excel(e_rates,sheet_name='PRE_leg1')
    e_rates_l2 = pd.read_excel(e_rates,sheet_name='AIR_leg2')
    e_rates_l3 = pd.read_excel(e_rates,sheet_name='ONC_leg3')

    # correct codes for dhl to have it all uppercase
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

    # create leg ids for dhl rates dataframes
    e_rates_l1['LEG1ID']=e_rates_l1['FromCity']+"-"+e_rates_l1['ToCity']+'-'+e_rates_l1['ServiceLevel'].astype(str)
    e_rates_l2['LEG2ID']=e_rates_l2['FromCity']+"-"+e_rates_l2['ToCity']+'-'+e_rates_l2['ServiceLevel'].astype(str)
    e_rates_l3['LEG3ID']=e_rates_l3['FromCity']+"-"+e_rates_l3['ToCity']+'-'+e_rates_l3['ServiceLevel'].astype(str)


    # create dataframes for panalpina and dhl containing only leg ids
    #p_drop = pd.DataFrame(p_rates_l1['LEG1ID'])
    e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])
    #p2_drop = pd.DataFrame(p_rates_l2['LEG2ID'])
    e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])
    #p3_drop = pd.DataFrame(p_rates_l3['LEG3ID'])
    e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

    # renaming columns for dataframes for panalpina and dhl for further adding it to report
    #p_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    e_drop.rename(index=str,columns={"LEG1ID":'L1'},inplace=True)
    #p2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    e2_drop.rename(index=str,columns={"LEG2ID":'L2'},inplace=True)
    #p3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e3_drop.rename(index=str,columns={"LEG3ID":'L3'},inplace=True)
    e2_drop['L2']=e2_drop['L2'].str[0:9]

    # removing duplicate values for all dataframes with leg ids for panalpina and epxeditors
    #p_drop.drop_duplicates()
    e_drop.drop_duplicates()
    #p2_drop.drop_duplicates()
    e2_drop.drop_duplicates()
    #p3_drop.drop_duplicates()
    e3_drop.drop_duplicates()

    # creating columns for dataframes for panalpina and dhl indicating presence of rates
    # setting up an index to have the possibility to join dataframes
    #p_drop['Leg1RatesPresent']=True
    #p_drop.set_index('L1', inplace=True, drop=True)
    e_drop['Leg1RatesPresent']=True
    e_drop.set_index('L1', inplace=True, drop=True)
    #p2_drop['Leg2RatesPresent']=True
    #p2_drop.set_index('L2', inplace=True, drop=True)
    e2_drop['Leg2RatesPresent']=True
    e2_drop.set_index('L2', inplace=True, drop=True)
    #p3_drop['Leg3RatesPresent']=True
    #p3_drop.set_index('L3', inplace=True, drop=True)
    e3_drop['Leg3RatesPresent']=True
    e3_drop.set_index('L3', inplace=True, drop=True)

    # joining each table confirming rates presence
    # methodology - each time index for leg is assigned to main dataframe
    # then main dataframe is joined with rates confirmation dataframe
    # when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
    # when new index is assigned then program joins another dataframe to verify presence of rates
    #panalpina.set_index('LEG1ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p_drop)
    #panalpina.set_index('LEG2ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p2_drop)
    #panalpina.set_index('LEG3ID', inplace=True, drop=False)
    #panalpina = panalpina.join(p3_drop)
    dhl.set_index('LEG1ID', inplace=True, drop=False)
    dhl = dhl.join(e_drop)
    dhl.set_index('LEG2ID', inplace=True, drop=False)
    dhl = dhl.join(e2_drop)
    dhl.set_index('LEG3ID', inplace=True, drop=False)
    dhl = dhl.join(e3_drop)
    #panalpina.reset_index(inplace=True,drop = True)
    dhl.reset_index(inplace=True,drop = True)

    dhl.drop_duplicates(subset='Shipment',inplace=True)

    # mps = pd.read_excel(mps_file,sheet_name=0,
    #                    skiprows=[0],header=[0],parse_cols='A:AG',names=["skip0","DateFrom","DateTo","Sector","Carrier",
    #                                                                     "LaneID","AirportID","skip4","skip5","AirportFrom",
    #                                                                     "FromCountry","RegionFrom",
    #                                                                     "AirportTo","ToCountry","RegionTo","DD","DP","PD","PP",
    #                                                                     "skip1","skip2","skip3","Currency","PickUp","CustomsOrigin",
    #                                                                     "HandlingOrigin","AirFreight",
    #                                                                     "HandlingDestination","CustomsDestination",
    #                                                                     "skip5","Delivery","ScreeningType","ScreeningPrice"],
    #                                                                       keep_default_na=False)
    # # create date frame with carrie and LANE ID only
    # mps  = mps[['Carrier','LaneID']]
    #
    # # extract proper value for Lane ID
    # mps.LaneID =  mps.LaneID.str[2:]

    # create additional column with LAND ID in Expeditors data frame
    # And indicate in the report who is allocate based on MPS
    dhl["LANEID"] = dhl['Port of loading'].str[2:] +"-"+dhl['Port of discharge'].str[2:] + '-'+dhl['service_level']
    dhl['allocation'] = dhl['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())


    dhl.to_excel(r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\DHL check-up {}.xlsx'.format(address),index=False)












