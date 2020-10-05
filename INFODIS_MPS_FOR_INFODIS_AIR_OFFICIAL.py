import pandas as pd
import numpy as np
import datetime
print(datetime.datetime.now())
# setting the date for file name
today = datetime.datetime.today().strftime("%Y-%m-%d")

# reading mps
path_to_file = input("Provide path to File: ")
df = pd.read_excel(path_to_file,sheet_name=0,
                   skiprows=[0],header=[0],parse_cols='A:AE',names=["skip0","DateFrom","DateTo","Sector","Carrier",
                                                                    "LaneID","AirportID","AirportFrom",
                                                                    "FromCountry","RegionFrom",
                                                                    "AirportTo","ToCountry","RegionTo","DD","DP","PD","PP",
                                                                    "skip1","skip2","skip3","Currency","PickUp","CustomsOrigin",
                                                                    "HandlingOrigin","AirFreight",
                                                                    "HandlingDestination","CustomsDestination",
                                                                    "skip5","Delivery","ScreeningType","ScreeningPrice"],
                                                                      keep_default_na=False)


# creating a dictionary for carriers codes
car_dict = {"CEVA":'CEVA', 'PANALPINA':'PANALPINA', 'DHL':'DHL', 'Nippon':'Nippon',
            'DBS':'DBS', 'UPS SCS':'UPS', 'Expeditors':'Expeditors'}
# DHl is with carrier name DHL AIR, DBS is with carrier name DB Schenker, /
# UPS SCS is with carrier name UPS AIRFEIGHT

# creating dataframe for each carrier and a list of carriers
ceva = df[df.Carrier=='CEVA']
dbs = df[df.Carrier=='DBS']
dhl = df[df.Carrier=='DHL']
expeditors = df[df.Carrier=='Expeditors']
nippon = df[df.Carrier=='Nippon']
panalpina = df[df.Carrier=='PANALPINA']
ups = df[df.Carrier=='UPS SCS']

car_list = [ceva,dbs,dhl,expeditors,nippon,panalpina,ups]

for car_df in car_list:
    car_name = np.select([car_df.iloc[0,4]  == 'CEVA',car_df.iloc[0,4]  =='DBS',car_df.iloc[0,4]  =='DHL',
                         car_df.iloc[0,4]  =='Expeditors',car_df.iloc[0,4]  =='Nippon',
                          car_df.iloc[0,4]  =='PANALPINA',car_df.iloc[0,4]  =='UPS SCS'],
              ['CEVA','DBS','DHL','Expeditors','Nippon','PANALPINA','UPS SCS'],
              default='Carrier')

    car_code = np.select([car_df.iloc[0,4]  == 'CEVA',car_df.iloc[0,4]  =='DBS',car_df.iloc[0,4]  =='DHL',
                         car_df.iloc[0,4]  =='Expeditors',car_df.iloc[0,4]  =='Nippon',
                          car_df.iloc[0,4]  =='PANALPINA',car_df.iloc[0,4]  =='UPS SCS'],
                                         ['CEVB2', 'SCH18','DHAIR','','NIP06','PA','UPAT1'],
                                         default='Carrier')
    # creating leg 1 template
    leg1 = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                         'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                         'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                         'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                         'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                         'ChargeCurr': [], 'minweight': [], 'maxweight': [], 'Charge': []})

    # creating leg 2 template
    leg2custo = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                              'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                              'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                              'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                              'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                              'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 2 template
    leg2custd = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                              'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                              'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                              'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                              'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                              'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 1 template
    leg2freight = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                                'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                                'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                                'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                                'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                                'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 2 template
    leg2ho = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                           'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                           'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                           'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                           'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                           'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 2 template
    leg2hd = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                           'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                           'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                           'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                           'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                           'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 2 template
    leg2screen = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                               'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                               'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                               'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                               'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                               'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 2 template
    leg2 = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                         'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                         'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                         'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                         'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                         'ChargeCurr': [], 'minweight': [], 'Charge': []})

    # creating leg 3 template
    leg3 = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                         'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                         'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                         'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                         'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                         'ChargeCurr': [], 'minweight': [], 'maxweight': [], 'Charge': []})

    # extratcting data for leg 1 for each column
    leg1['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg1['FromCity'] = 'ALL'
    leg1['FromUNLOCODE'] = leg1['FromCountry'] + leg1['FromCity']
    leg1['ToCountry'] = car_df['FromCountry'].str[0:2]
    leg1['ToCity'] = car_df['AirportFrom']
    leg1['ToUNLOCODE'] = leg1['ToCountry'] + leg1['ToCity']
    leg1['TransportMode'] = 'PRE'
    leg1['CarrierName'] = car_name
    leg1['CarrierCode'] = car_code
    leg1['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg1['Predays'] = 0
    leg1['Transitdays'] = 1
    leg1['Postdays'] = 0
    leg1['ChargeType'] = 'Pick-up from door'
    leg1['CostDriver'] = 'Chargeable weight'
    leg1['ChargeCurr'] = car_df['Currency']
    leg1['minweight'] = 30
    leg1['maxweight'] = 5000
    leg1['Charge'] = car_df['PickUp']
    leg1['DateEffectiveFrom'] = '2019-07-01'
    leg1['DateEffectiveTo'] = '2020-06-30'

    # correcting the potential issue with HKG port for leg 1
    leg1.ToCity.replace({'ToUNLOCODE': r'CNHKG'}, {'ToUNLOCODE': 'HKHKG'}, regex=True, inplace=True)
    leg1.ToCity.replace({'ToCity': r'HKG'}, {'ToCountry': 'HK'}, regex=True, inplace=True)

    # reading additional dateframe for Hong Kong
    hkg = pd.read_excel(path_to_file, sheet_name=0,
                        skiprows=[0], header=[0], parse_cols='E,F,H,I,AN',
                        names=['service_provider', 'SL', 'airportfrom', 'countryfrom',
                               'charge'],
                        keep_default_na=False)

    # creating leg 1 template
    leg1hkg = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
                            'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
                            'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
                            'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
                            'Postdays': [], 'ChargeType': [], 'CostDriver': [],
                            'ChargeCurr': [], 'minweight': [], 'maxweight': [], 'Charge': []})

    # filtering data
    hkg = hkg[hkg.airportfrom == 'HKG']
    hkg.iloc[:, 3] = "CN"

    # creating column for checking duplicates
    hkg['duplicates'] = hkg.service_provider + hkg.airportfrom + hkg.SL.str[-1:]

    # dropping duplicates
    hkg.drop_duplicates(subset=['duplicates'], inplace=True)

    # dropping column
    hkg.drop(columns=['duplicates'], axis=1, inplace=True)
    print(car_name)
    print(car_code)
    hkg= hkg[hkg.iloc[:,0] == str(car_name).strip()]
    # creating additional rates for HK
    # extracting data for leg 1 from China to Hong Kong for each column
    leg1hkg['FromCountry'] = str("CN")
    leg1hkg['FromCity'] = str("ALL")
    leg1hkg['FromUNLOCODE'] = str("CNALL")
    leg1hkg['ToCountry'] = str("HK")
    leg1hkg['ToCity'] = str("HKG")
    leg1hkg['ToUNLOCODE'] = str("HKHKG")
    leg1hkg['TransportMode'] = str("PRE")
    leg1hkg['CarrierName'] = str(car_name).strip()
    leg1hkg['CarrierCode'] = str(car_code).strip()
    leg1hkg['ServiceLevel'] = hkg['SL'].str[-1:]
    leg1hkg['Predays'] = 0
    leg1hkg['Transitdays'] = 1
    leg1hkg['Postdays'] = 0
    leg1hkg['ChargeType'] = "Pick-up from door"
    leg1hkg['CostDriver'] = "Chargeable weight"
    leg1hkg['ChargeCurr'] = "USD"
    leg1hkg['minweight'] = 30
    leg1hkg['maxweight'] = 5000
    leg1hkg['Charge'] = hkg['charge']
    leg1hkg['DateEffectiveFrom'] = "2019-07-01"
    leg1hkg['DateEffectiveTo'] = "2020-06-30"

    # # creating leg 1 template
    # leg1hkg = pd.DataFrame({'DateEffectiveFrom': [], 'DateEffectiveTo': [], 'FromCountry': [],
    #                         'FromCity': [], 'FromUNLOCODE': [], 'ToCountry': [],
    #                         'ToCity': [], 'ToUNLOCODE': [], 'TransportMode': [], 'CarrierName': [],
    #                         'CarrierCode': [], 'ServiceLevel': [], 'Predays': [], 'Transitdays': [],
    #                         'Postdays': [], 'ChargeType': [], 'CostDriver': [],
    #                         'ChargeCurr': [], 'minweight': [], 'maxweight': [], 'Charge': []})
    #
    # # creating additional rates for HK
    # extracting data for leg 1 from China to Hong Kong for each column
    leg1hkg['FromCountry'] = 'CN'
    leg1hkg['FromCity'] = 'ALL'
    leg1hkg['FromUNLOCODE'] = "CNALL"
    leg1hkg['ToCountry'] = "HK"
    leg1hkg['ToCity'] = 'HKG'
    leg1hkg['ToUNLOCODE'] = "HKHKG"
    leg1hkg['TransportMode'] = 'PRE'
    leg1hkg['CarrierName'] = car_name
    leg1hkg['CarrierCode'] = car_code
    leg1hkg['ServiceLevel'] = hkg['SL'].str[-1:]
    leg1hkg['Predays'] = 0
    leg1hkg['Transitdays'] = 1
    leg1hkg['Postdays'] = 0
    leg1hkg['ChargeType'] = 'Pick-up from door'
    leg1hkg['CostDriver'] = 'Chargeable weight'
    leg1hkg['ChargeCurr'] = 'USD'
    leg1hkg['minweight'] = 30
    leg1hkg['maxweight'] = 5000
    leg1hkg['Charge'] = hkg['charge']
    leg1hkg['DateEffectiveFrom'] = '2019-07-01'
    leg1hkg['DateEffectiveTo'] = '2020-06-30'

    # adding additional codes to official dataframe for leg1
    leg1 = pd.concat([leg1,leg1hkg])
    #leg1 = leg1.append(leg1hkg, ignore_index=True)

    #leg1hkg.to_excel(r'C:\Users\310295192\Desktop\testing MPS\testing{}.xlsx'.format(car_name))


    # extratcting data for leg 3 for each column
    leg3['FromCountry'] = car_df['ToCountry'].str[0:2]
    leg3['FromCity'] = car_df['AirportTo']
    leg3['FromUNLOCODE'] = leg3['FromCountry'] + leg3['FromCity']
    leg3['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg3['ToCity'] = 'ALL'
    leg3['ToUNLOCODE'] = leg3['ToCountry'] + leg3['ToCity']
    leg3['TransportMode'] = 'ONC'
    leg3['CarrierName'] = car_name
    leg3['CarrierCode'] = car_code
    leg3['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg3['Predays'] = 0
    leg3['Transitdays'] = 1
    leg3['Postdays'] = 0
    leg3['ChargeType'] = 'Delivery to door'
    leg3['CostDriver'] = 'Chargeable weight'
    leg3['ChargeCurr'] = car_df['Currency']
    leg3['minweight'] = 30
    leg3['maxweight'] = 5000
    leg3['Charge'] = car_df['PickUp']
    leg3['DateEffectiveFrom'] = '2019-07-01'
    leg3['DateEffectiveTo'] = '2020-06-30'

    # correcting the potential issue with HKG port for leg 2
    leg3.FromCity.replace({'FromUNLOCODE': r'CNHKG'}, {'FromUNLOCODE': 'HKHKG'}, regex=True, inplace=True)
    leg3.FromCity.replace({'FromCity': r'HKG'}, {'FromCountry': 'HK'}, regex=True, inplace=True)

    # extracting data for leg 2 for each column
    leg2custo['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg2custo['FromCity'] = car_df['AirportFrom']
    leg2custo['FromUNLOCODE'] = leg2custo['FromCountry'] + leg2custo['FromCity']
    leg2custo['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg2custo['ToCity'] = car_df['AirportTo']
    leg2custo['ToUNLOCODE'] = leg2custo['ToCountry'] + leg2custo['ToCity']
    leg2custo['TransportMode'] = 'AIR'
    leg2custo['CarrierName'] = car_name
    leg2custo['CarrierCode'] = car_code
    leg2custo['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg2custo['Predays'] = 0
    leg2custo['Transitdays'] = np.select([car_df['DD'] > 3,car_df['DD']<= 3],[car_df['DD']-3, car_df['DD']],
                                         default=car_df['DD'])
    leg2custo['Postdays'] = 0
    leg2custo['ChargeType'] = 'Customs clearance origin'
    leg2custo['CostDriver'] = 'Shipment'
    leg2custo['ChargeCurr'] = car_df['Currency']
    leg2custo['minweight'] = 30
    leg2custo['Charge'] = car_df['CustomsOrigin']
    leg2custo['DateEffectiveFrom'] = '2019-07-01'
    leg2custo['DateEffectiveTo'] = '2020-06-30'

    # extracting data for leg 2 for each column
    leg2custd['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg2custd['FromCity'] = car_df['AirportFrom']
    leg2custd['FromUNLOCODE'] = leg2custd['FromCountry'] + leg2custd['FromCity']
    leg2custd['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg2custd['ToCity'] = car_df['AirportTo']
    leg2custd['ToUNLOCODE'] = leg2custd['ToCountry'] + leg2custd['ToCity']
    leg2custd['TransportMode'] = 'AIR'
    leg2custd['CarrierName'] = car_name
    leg2custd['CarrierCode'] = car_code
    leg2custd['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg2custd['Predays'] = 0
    leg2custd['Transitdays'] = np.select([car_df['DD'] > 3,car_df['DD']<= 3],[car_df['DD']-3, car_df['DD']],
                                         default=car_df['DD'])
    leg2custd['Postdays'] = 0
    leg2custd['ChargeType'] = 'Customs clearance destination'
    leg2custd['CostDriver'] = 'Shipment'
    leg2custd['ChargeCurr'] = car_df['Currency']
    leg2custd['minweight'] = 30
    leg2custd['Charge'] = car_df['CustomsDestination']
    leg2custd['DateEffectiveFrom'] = '2019-07-01'
    leg2custd['DateEffectiveTo'] = '2020-06-30'

    # extracting data for leg 2 for each column
    leg2freight['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg2freight['FromCity'] = car_df['AirportFrom']
    leg2freight['FromUNLOCODE'] = leg2freight['FromCountry'] + leg2freight['FromCity']
    leg2freight['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg2freight['ToCity'] = car_df['AirportTo']
    leg2freight['ToUNLOCODE'] = leg2freight['ToCountry'] + leg2freight['ToCity']
    leg2freight['TransportMode'] = 'AIR'
    leg2freight['CarrierName'] = car_name
    leg2freight['CarrierCode'] = car_code
    leg2freight['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg2freight['Predays'] = 0
    leg2freight['Transitdays'] = np.select([car_df['DD'] > 3,car_df['DD']<= 3],[car_df['DD']-3, car_df['DD']],default=car_df['DD'])
    leg2freight['Postdays'] = 0
    leg2freight['ChargeType'] = 'Airfreight'
    leg2freight['CostDriver'] = 'Chargeable weight'
    leg2freight['ChargeCurr'] = car_df['Currency']
    leg2freight['minweight'] = 30
    leg2freight['Charge'] = car_df['AirFreight']
    leg2freight['DateEffectiveFrom'] = '2019-07-01'
    leg2freight['DateEffectiveTo'] = '2020-06-30'

    # extracting data for leg 2 for each column
    leg2ho['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg2ho['FromCity'] = car_df['AirportFrom']
    leg2ho['FromUNLOCODE'] = leg2ho['FromCountry'] + leg2ho['FromCity']
    leg2ho['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg2ho['ToCity'] = car_df['AirportTo']
    leg2ho['ToUNLOCODE'] = leg2ho['ToCountry'] + leg2ho['ToCity']
    leg2ho['TransportMode'] = 'AIR'
    leg2ho['CarrierName'] = car_name
    leg2ho['CarrierCode'] = car_code
    leg2ho['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg2ho['Predays'] = 0
    leg2ho['Transitdays'] = np.select([car_df['DD'] > 3,car_df['DD']<= 3],[car_df['DD']-3, car_df['DD']],default=car_df['DD'])
    leg2ho['Postdays'] = 0
    leg2ho['ChargeType'] = 'Airport terminal handling charges origin'
    leg2ho['CostDriver'] = 'Chargeable weight'
    leg2ho['ChargeCurr'] = car_df['Currency']
    leg2ho['minweight'] = 30
    leg2ho['Charge'] = car_df['HandlingOrigin']
    leg2ho['DateEffectiveFrom'] = '2019-07-01'
    leg2ho['DateEffectiveTo'] = '2020-06-30'

    # extracting data for leg 2 for each column
    leg2hd['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg2hd['FromCity'] = car_df['AirportFrom']
    leg2hd['FromUNLOCODE'] = leg2hd['FromCountry'] + leg2hd['FromCity']
    leg2hd['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg2hd['ToCity'] = car_df['AirportTo']
    leg2hd['ToUNLOCODE'] = leg2hd['ToCountry'] + leg2hd['ToCity']
    leg2hd['TransportMode'] = 'AIR'
    leg2hd['CarrierName'] = car_name
    leg2hd['CarrierCode'] = car_code
    leg2hd['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg2hd['Predays'] = 0
    leg2hd['Transitdays'] = np.select([car_df['DD'] > 3,car_df['DD']<= 3],[car_df['DD']-3, car_df['DD']],default=car_df['DD'])
    leg2hd['Postdays'] = 0
    leg2hd['ChargeType'] = 'Airport terminal handling charges destination'
    leg2hd['CostDriver'] = 'Chargeable weight'
    leg2hd['ChargeCurr'] = car_df['Currency']
    leg2hd['minweight'] = 30
    leg2hd['Charge'] = car_df['HandlingDestination']
    leg2hd['DateEffectiveFrom'] = '2019-07-01'
    leg2hd['DateEffectiveTo'] = '2020-06-30'

    # extracting data for leg 2 for each column
    leg2screen['FromCountry'] = car_df['FromCountry'].str[0:2]
    leg2screen['FromCity'] = car_df['AirportFrom']
    leg2screen['FromUNLOCODE'] = leg2screen['FromCountry'] + leg2screen['FromCity']
    leg2screen['ToCountry'] = car_df['ToCountry'].str[0:2]
    leg2screen['ToCity'] = car_df['AirportTo']
    leg2screen['ToUNLOCODE'] = leg2screen['ToCountry'] + leg2screen['ToCity']
    leg2screen['TransportMode'] = 'AIR'
    leg2screen['CarrierName'] = car_name
    leg2screen['CarrierCode'] = car_code
    leg2screen['ServiceLevel'] = car_df['LaneID'].str[-1:]
    leg2screen['Predays'] = 0
    leg2screen['Transitdays'] = np.select([car_df['DD'] > 3,car_df['DD']<= 3],[car_df['DD']-3, car_df['DD']],default=car_df['DD'])
    leg2screen['Postdays'] = 0
    leg2screen['ChargeType'] = 'Screening Fee'

    leg2screen['CostDriver'] = np.select([car_df['ScreeningType'] == 'Per Shipment',
                                          car_df['ScreeningType'] == 'Per KG'],
                                         ['Shipment', 'Chargeable weight'],
                                         default='Chargeable weight')
    leg2screen['ChargeCurr'] = car_df['Currency']
    leg2screen['minweight'] = 30
    leg2screen['Charge'] = car_df['ScreeningPrice']
    leg2screen['DateEffectiveFrom'] = '2019-07-01'
    leg2screen['DateEffectiveTo'] = '2020-06-30'



    # creating dataframe for Tokyo to copy (leg1)
    tyo1 = leg1.loc[leg1['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to IDBUr and IDBTH for leg1
    tyo1.loc[:, 'ToCity'] = "TYO"
    tyo1.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg1
    leg1 = leg1.append(tyo1, ignore_index=True)

    # creating id column
    leg1['id'] = leg1['FromUNLOCODE'] + leg1['ToUNLOCODE'] + leg1['ServiceLevel']

    # dropping duplicates and column that served as ID column
    leg1.drop_duplicates(subset=['id'], inplace=True)
    leg1.drop(columns=['id'], inplace=True)





    # creating dataframe for Tokyo to copy (leg3)
    tyo3 = leg3.loc[leg3['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to Tokyo for leg3
    tyo3.loc[:, 'FromCity'] = "TYO"
    tyo3.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg3
    leg3 = leg3.append(tyo3, ignore_index=True)
    # creating id column
    leg3['id'] = leg3['FromUNLOCODE'] + leg3['ToUNLOCODE'] + leg3['ServiceLevel']

    # dropping duplicates and dropping column that served as ID column
    leg3.drop_duplicates(subset=['id'], inplace=True)
    leg3.drop(columns=['id'], inplace=True)

    # creating dataframe for Tokyo to copy (leg2)
    tyo2custo = leg2custo.loc[leg2custo['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    tyo2custodel = leg2custo.loc[leg2custo['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to Tokyo for leg2 custom origin
    tyo2custo.loc[:, 'FromCity'] = "JPTYO"
    tyo2custo.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    tyo2custodel.loc[:, 'ToCity'] = "JPTYO"
    tyo2custodel.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg2
    leg2custo = leg2custo.append(tyo2custo, ignore_index=True)
    leg2custo = leg2custo.append(tyo2custodel, ignore_index=True)
    # resetting index
    leg2custo['id'] = leg2custo['FromUNLOCODE'] + leg2custo['ToUNLOCODE'] + leg2custo['ServiceLevel'] + leg2custo[
        'ChargeType']

    # dropping duplicates
    leg2custo.drop_duplicates(subset=['id'], inplace=True)
    leg2custo.drop(columns=['id'], inplace=True)

    # creating dataframe for Batam to copy (leg2)
    tyo2custd = leg2custd.loc[leg2custd['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    tyo2custddel = leg2custd.loc[leg2custd['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to IDBUR and IDBTH for leg2 custom origin
    tyo2custd.loc[:, 'FromCity'] = "JPTYO"
    tyo2custd.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    tyo2custddel.loc[:, 'ToCity'] = "JPTYO"
    tyo2custddel.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg2
    leg2custd = leg2custd.append(tyo2custd, ignore_index=True)
    leg2custd = leg2custd.append(tyo2custddel, ignore_index=True)
    # resetting index
    leg2custd['id'] = leg2custd['FromUNLOCODE'] + leg2custd['ToUNLOCODE'] + leg2custd['ServiceLevel'] + leg2custd[
        'ChargeType']

    # dropping duplicates
    leg2custd.drop_duplicates(subset=['id'], inplace=True)
    leg2custd.drop(columns=['id'], inplace=True)

    # creating dataframe for Batam to copy (leg2)
    tyo2freight = leg2freight.loc[leg2freight['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    tyo2freightdel = leg2freight.loc[leg2freight['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to IDBUR and IDBTH for leg2 custom origin
    tyo2freight.loc[:, 'FromCity'] = "JPTYO"
    tyo2freight.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    tyo2freightdel.loc[:, 'ToCity'] = "JPTYO"
    tyo2freightdel.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg2
    leg2freight = leg2freight.append(tyo2freight, ignore_index=True)
    leg2freight = leg2freight.append(tyo2freightdel, ignore_index=True)
    # resetting index
    leg2freight['id'] = leg2freight['FromUNLOCODE'] + leg2freight['ToUNLOCODE'] + leg2freight['ServiceLevel'] + \
                        leg2freight['ChargeType']

    # dropping duplicates
    leg2freight.drop_duplicates(subset=['id'], inplace=True)
    leg2freight.drop(columns=['id'], inplace=True)

    # creating dataframe for Batam to copy (leg2)
    tyo2ho = leg2ho.loc[leg2ho['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    tyo2hodel = leg2ho.loc[leg2ho['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to Toky for leg2 custom origin
    tyo2ho.loc[:, 'FromCity'] = "JPTYO"
    tyo2ho.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    tyo2hodel.loc[:, 'ToCity'] = "JPTYO"
    tyo2hodel.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg2
    leg2ho = leg2ho.append(tyo2ho, ignore_index=True)
    leg2ho = leg2ho.append(tyo2hodel, ignore_index=True)
    # resetting index
    leg2ho['id'] = leg2ho['FromUNLOCODE'] + leg2ho['ToUNLOCODE'] + leg2ho['ServiceLevel'] + leg2ho['ChargeType']

    # dropping duplicates
    leg2ho.drop_duplicates(subset=['id'], inplace=True)
    leg2ho.drop(columns=['id'], inplace=True)

    # creating dataframe for Batam to copy (leg2)
    tyo2hd = leg2hd.loc[leg2hd['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    tyo2hddel = leg2hd.loc[leg2hd['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to Tokyo for leg2 custom origin
    tyo2hd.loc[:, 'FromCity'] = "JPTYO"
    tyo2hd.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    tyo2hddel.loc[:, 'ToCity'] = "JPTYO"
    tyo2hddel.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg2
    leg2hd = leg2hd.append(tyo2hd, ignore_index=True)
    leg2hd = leg2hd.append(tyo2hddel, ignore_index=True)
    # resetting index
    leg2hd['id'] = leg2hd['FromUNLOCODE'] + leg2hd['ToUNLOCODE'] + leg2hd['ServiceLevel'] + leg2hd['ChargeType']

    # dropping duplicates
    leg2hd.drop_duplicates(subset=['id'], inplace=True)
    leg2hd.drop(columns=['id'], inplace=True)

    # creating dataframe for Batam to copy (leg2)
    tyo2screen = leg2screen.loc[leg2screen['FromUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    tyo2screendel = leg2screen.loc[leg2screen['ToUNLOCODE'] == "JPNRT"].reset_index(drop=True)

    # changing codes to IDBUR and IDBTH for leg2 custom origin
    tyo2screen.loc[:, 'FromCity'] = "JPTYO"
    tyo2screen.loc[:, 'FromUNLOCODE'] = 'JPTYO'

    tyo2screendel.loc[:, 'ToCity'] = "JPTYO"
    tyo2screendel.loc[:, 'ToUNLOCODE'] = 'JPTYO'

    # adding additional codes to official dataframe for leg2
    leg2screen = leg2screen.append(tyo2screen, ignore_index=True)
    leg2screen = leg2screen.append(tyo2screendel, ignore_index=True)
    # resetting index
    leg2screen['id'] = leg2screen['FromUNLOCODE'] + leg2screen['ToUNLOCODE'] + leg2screen['ServiceLevel'] + leg2screen[
        'ChargeType']

    # dropping duplicates
    leg2screen.drop_duplicates(subset=['id'], inplace=True)
    leg2screen.drop(columns=['id'], inplace=True)

    # adding all created dataframes with costs for leg 2 to one big dataframe
    leg2 = leg2.append(leg2custo, ignore_index=True)

    leg2 = leg2.append(leg2custd, ignore_index=True)

    leg2 = leg2.append(leg2ho, ignore_index=True)

    leg2 = leg2.append(leg2hd, ignore_index=True)

    leg2 = leg2.append(leg2freight, ignore_index=True)

    leg2 = leg2.append(leg2screen, ignore_index=True)

    # dropping na values from leg 1, leg 2 , leg 3
    leg2.dropna(subset=['Charge', 'FromUNLOCODE', 'ToUNLOCODE'], inplace=True)
    leg1.dropna(subset=['Charge', 'FromUNLOCODE', 'ToUNLOCODE'], inplace=True)
    leg3.dropna(subset=['Charge', 'FromUNLOCODE', 'ToUNLOCODE'], inplace=True)

    # sorting leg 2, then changing four columns to integer values
    leg2.sort_values(by=['FromUNLOCODE', 'ToUNLOCODE', 'ServiceLevel', 'ChargeType', 'Charge'], inplace=True)
    leg2['Transitdays'] = leg2['Transitdays'].astype(int)
    leg2['Predays'] = leg2['Predays'].astype(int)
    leg2['Postdays'] = leg2['Postdays'].astype(int)
    leg2['minweight'] = leg2['minweight'].astype(int)

    # sorting leg 1, then changing four columns to integer values
    leg1.sort_values(by=['FromUNLOCODE', 'ToUNLOCODE', 'ServiceLevel', 'Charge'], inplace=True)
    leg1['Transitdays'] = leg1['Transitdays'].astype(int)
    leg1['Predays'] = leg1['Predays'].astype(int)
    leg1['Postdays'] = leg1['Postdays'].astype(int)
    leg1['minweight'] = leg1['minweight'].astype(int)
    leg1['maxweight'] = leg1['maxweight'].astype(int)

    # sorting leg 3, then changing four columns to integer values
    leg3.sort_values(by=['FromUNLOCODE', 'ToUNLOCODE', 'ServiceLevel', 'Charge'], inplace=True)
    leg3['Transitdays'] = leg3['Transitdays'].astype(int)
    leg3['Predays'] = leg3['Predays'].astype(int)
    leg3['Postdays'] = leg3['Postdays'].astype(int)
    leg3['minweight'] = leg3['minweight'].astype(int)
    leg3['maxweight'] = leg3['maxweight'].astype(int)

    # creating file and saving each dataframe to separate sheet
    with pd.ExcelWriter(r'C:\Users\310295192\Desktop\2019-2020 Rates Air {} {} .xlsx'.format(car_name,today)) as writer:
        leg1.to_excel(writer, sheet_name='Pre_leg1', index=False)
        leg2.to_excel(writer, sheet_name='AIR_leg2', index=False)
        leg3.to_excel(writer, sheet_name='ONC_leg3', index=False)

        worksheet1 = writer.sheets['Pre_leg1']
        worksheet2 = writer.sheets['AIR_leg2']
        worksheet3 = writer.sheets['ONC_leg3']
        # setting up the width of the columns
        worksheet1.set_column('A:H', 16)
        worksheet1.set_column('I:Q', 20)
        worksheet2.set_column('A:H', 16)
        worksheet2.set_column('I:Q', 20)
        worksheet3.set_column('A:H', 16)
        worksheet3.set_column('I:Q', 20)


print(datetime.datetime.now())

