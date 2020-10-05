import pandas as pd

mps = input('provide mps file: ')
report_date = input("Provide today date: ")
carriers ={}
ups = input('provide ups file date: ')
if len(ups)>3:
    carriers['ups'] = ups
expeditors = input('provide expedtiors file date: ')
if len(expeditors)>3:
    carriers['expeditors'] = expeditors
panalpina = input('provide panalpina file date: ')
if len(panalpina)>3:
    carriers['panalpina'] = panalpina
dhl = input('provide dhl file date: ')
if len(dhl)>3:
    carriers['dhl'] = dhl
db = input('provide db file date: ')
if len(db)>3:
    carriers['db'] = db

def checking(mps_file,przewoznicy,address):
    global expeditors
    global ups
    global panalpina
    global dhl
    global db
    '''function is preparing rates check-up for air carriers'''

    # left after preparation of the function
    # ups_file = r'C:\Users\310295192\Desktop\Work\Rates\Air\UPS\Upload files\2019-2020 Rates Air UPS ().xlsx'.format(ups)
    # expeditors_file = r'C:\Users\310295192\Desktop\Work\Rates\Air\Expeditors\Rates\2019-2020 Rates Expeditors AIR ().xlsx'.format(expeditors)
    # panalpina_file = r'C:\Users\310295192\Desktop\Work\Rates\Air\Panalpina\Uploads\2019-2020 Rates Air Panalpina ().xlsx'.format(panalpina)
    # dhl_file = r'C:\Users\310295192\Desktop\Work\Rates\Air\DHL\Uploads2019-2020 Rates Air DHL ().xlsx'.format(dhl)
    # db_file = r'C:\Users\310295192\Desktop\Work\Rates\Air\DB Schenker\Uploads\2019-2020 Rates Air DB Schenker ().xlsx'.format(db)


    # create data frame based on air report
    airfile = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR {} updated.xlsx'.format(address)
    air_df = pd.read_excel(airfile)
    # leave only case that are not pending or solved
    # air_clean = air_df[air_df["Pending/Solved"].isna()]
    air_clean = air_df[air_df["Leg 2, Transport Mode"].str.contains("Service", na=False)]
    # air_clean.to_excel(r'C:\Users\310295192\Desktop\checkair.xlsx')


    for car,car_file in przewoznicy.items():
        print(car,car_file)
        if car == 'ups':
            file = r'C:\Users\310295192\Desktop\Work\Rates\Air\UPS\Upload files\2019-2020 Rates Air UPS {}.xlsx'.format(ups)
            car_name = "UPS AIR (S)"
            naming_file = 'UPS'
        elif car =='expeditors':
            file  = r'C:\Users\310295192\Desktop\Work\Rates\Air\Expeditors\Rates\2019-2020 Rates Expeditors AIR {}.xlsx'.format(expeditors)
            car_name = "Expeditors Air & Sea S"
            naming_file = 'Expeditors'
        elif car=='panalpina':
            file = r'C:\Users\310295192\Desktop\Work\Rates\Air\Panalpina\Uploads\2019-2020 Rates Air Panalpina {}.xlsx'.format(panalpina)
            car_name = "Panalpina AIR S"
            naming_file = 'Panalpina'
        elif car=='dhl':
            file = r'C:\Users\310295192\Desktop\Work\Rates\Air\DHL\Uploads2019-2020 Rates Air DHL {}.xlsx'.format(dhl)
            car_name = 'DHL AIR'
            naming_file = 'DHL'
        elif car=='db':
            file = r'C:\Users\310295192\Desktop\Work\Rates\Air\DB Schenker\Uploads\2019-2020 Rates Air DB Schenker {}.xlsx'.format(db)
            car_name = 'DB Schenker AIR'
            naming_file = 'DB Schenker'


        print('here i am ')
        # if car == "expeditors":
        #     # create dataframe for air_carrier
        #     air_carrier = air_clean[(air_clean['Leg 2, Carrier Name'] == car_name) &(air_clean['Leg 2, Carrier Name'] == "Expeditors Air & Sea")]
        # else:
        air_carrier = air_clean[air_clean['Leg 2, Carrier Name'] == car_name]

        # create series for service level for air_carrier
        expeditors_series = pd.Series(air_carrier['Leg 2, Transport Mode'])
        # extract service level for shipments with air_carrier
        service_exp = expeditors_series.str.extract(r'(\d)')
        air_carrier['service_level'] = service_exp

        # create leg ids for panalpina and air_carrier based on city names
        air_carrier['LEG1ID'] = "ALL" + "-" + air_carrier['Port of loading'].astype(str).str[2:5] + '-' + air_carrier[
            'service_level']
        air_carrier['LEG2ID'] = air_carrier['Port of loading'].astype(str).str[2:5] + "-" + air_carrier[
                                                                                              'Port of discharge'].astype(
            str).str[2:5] + '-' + air_carrier['service_level']
        air_carrier['LEG3ID'] = air_carrier['Port of discharge'].astype(str).str[2:5] + "-" + 'ALL' + '-' + \
                               air_carrier['service_level']


        # create data frame for each leg for expeditors
        e_rates_l1 = pd.read_excel(file, sheet_name='PRE_leg1')
        e_rates_l2 = pd.read_excel(file, sheet_name='AIR_leg2')
        e_rates_l3 = pd.read_excel(file, sheet_name='ONC_leg3')

        # correct codes for expeditors to have it all uppercase
        e_rates_l1['FromCity'] = e_rates_l1['FromCity'].str.upper()
        e_rates_l1['FromUNLOCODE'] = e_rates_l1['FromUNLOCODE'].str.upper()
        e_rates_l1['ToCity'] = e_rates_l1['ToCity'].str.upper()
        e_rates_l1['ToUNLOCODE'] = e_rates_l1['ToUNLOCODE'].str.upper()

        e_rates_l2['FromCity'] = e_rates_l2['FromCity'].str.upper()
        e_rates_l2['FromUNLOCODE'] = e_rates_l2['FromUNLOCODE'].str.upper()
        e_rates_l2['ToCity'] = e_rates_l2['ToCity'].str.upper()
        e_rates_l2['ToUNLOCODE'] = e_rates_l2['ToUNLOCODE'].str.upper()

        e_rates_l3['FromCity'] = e_rates_l3['FromCity'].str.upper()
        e_rates_l3['FromUNLOCODE'] = e_rates_l3['FromUNLOCODE'].str.upper()
        e_rates_l3['ToCity'] = e_rates_l3['ToCity'].str.upper()
        e_rates_l3['ToUNLOCODE'] = e_rates_l3['ToUNLOCODE'].str.upper()

        # create leg ids for expeditors rates dataframes
        e_rates_l1['LEG1ID'] = e_rates_l1['FromCity'] + "-" + e_rates_l1['ToCity'] + '-' + e_rates_l1[
            'ServiceLevel'].astype(str)
        e_rates_l2['LEG2ID'] = e_rates_l2['FromCity'] + "-" + e_rates_l2['ToCity'] + '-' + e_rates_l2[
            'ServiceLevel'].astype(str)
        e_rates_l3['LEG3ID'] = e_rates_l3['FromCity'] + "-" + e_rates_l3['ToCity'] + '-' + e_rates_l3[
            'ServiceLevel'].astype(str)

        # create dataframes for panalpina and expeditors containing only leg ids

        e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])

        e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])

        e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

        # renaming columns for dataframes for panalpina and expeditors for further adding it to report

        e_drop.rename(index=str, columns={"LEG1ID": 'L1'}, inplace=True)

        e2_drop.rename(index=str, columns={"LEG2ID": 'L2'}, inplace=True)

        e3_drop.rename(index=str, columns={"LEG3ID": 'L3'}, inplace=True)

        # removing duplicate values for all dataframes with leg ids for panalpina and epxeditors

        e_drop.drop_duplicates()

        e2_drop.drop_duplicates()

        e3_drop.drop_duplicates()

        # creating columns for dataframes for panalpina and expeditors indicating presence of rates
        # setting up an index to have the possibility to join dataframes

        e_drop['Leg1RatesPresent'] = True
        e_drop.set_index('L1', inplace=True, drop=True)

        e2_drop['Leg2RatesPresent'] = True
        e2_drop.set_index('L2', inplace=True, drop=True)

        e3_drop['Leg3RatesPresent'] = True
        e3_drop.set_index('L3', inplace=True, drop=True)

        # x.join(p_drop)
        # joining each table confirming rates presence
        # methodology - each time index for leg is assigned to main dataframe
        # then main dataframe is joined with rates confirmation dataframe
        # when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
        # when new index is assigned then program joins another dataframe to verify presence of rates

        air_carrier.set_index('LEG1ID', inplace=True, drop=False)
        air_carrier = air_carrier.join(e_drop)
        air_carrier.set_index('LEG2ID', inplace=True, drop=False)
        air_carrier = air_carrier.join(e2_drop)
        air_carrier.set_index('LEG3ID', inplace=True, drop=False)
        air_carrier = air_carrier.join(e3_drop)

        air_carrier.reset_index(inplace=True, drop=True)

        air_carrier.drop_duplicates(subset='Shipment', inplace=True)

        mps = pd.read_excel(mps_file,
                            sheet_name=0,
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

        mps = mps[['Carrier', 'LaneID']]

        mps.LaneID = mps.LaneID.str[2:]

        air_carrier["LANEID"] = air_carrier['Port of loading'].str[2:] + "-" + air_carrier['Port of discharge'].str[
                                                                             2:] + '-' + air_carrier['service_level']
            air_carrier['allocation'] = air_carrier['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())
        air_carrier.drop(
            columns=['Action taken', 'Pending/Solved', 'date of email', 'E-mail subject', 'Delay in answer',
                     'Comments from carrier', 'Comments', 'Booker name (1)', 'Shipper name (1)',
                     'Original shipper name (1)'],inplace=True)

        # sending the dataframe for expeditors to excel
        air_carrier.to_excel(
            r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\{} check-up {}.xlsx'.format(naming_file,
                address),
            index=False)

        # if we have expeditors as a carrier
        if car_name == 'Expeditors Air & Sea S':
            # create data frame based on air report
            airfile = r'C:\Users\310295192\Desktop\Work\Rates\Air\reports\report AIR {} updated.xlsx'.format(address)
            air_df = pd.read_excel(airfile)
            # leave only case that are not pending or solved
            # air_clean = air_df[air_df["Pending/Solved"].isna()]
            air_clean = air_df[air_df["Leg 2, Transport Mode"].str.contains("Service", na=False)]
            # air_clean.to_excel(r'C:\Users\310295192\Desktop\checkair.xlsx')

            # dropping rows where there is no port indication
            air_clean = air_df.dropna(subset=['Port of loading', 'Port of discharge'])
            # leaving data with only expeditors
            air_carrier = air_clean[air_clean["Shipment"].str.contains("MTA", na=False)]

            # create series for service level for air_carrier
            expeditors_series = pd.Series(air_carrier['Leg 2, Transport Mode'])

            # extract service level for shipments with air_carrier
            service_exp = expeditors_series.str.extract(r'(\d)')
            air_carrier['service_level'] = service_exp

            # create leg ids for panalpina and air_carrier based on city names
            air_carrier['LEG1ID'] = "ALL" + "-" + air_carrier['Port of loading'].astype(str).str[2:5] + '-' + \
                                    air_carrier[
                                        'service_level']
            air_carrier['LEG2ID'] = air_carrier['Port of loading'].astype(str).str[2:5] + "-" + air_carrier[
                                                                                                    'Port of discharge'].astype(
                str).str[2:5] + '-' + air_carrier['service_level']
            air_carrier['LEG3ID'] = air_carrier['Port of discharge'].astype(str).str[2:5] + "-" + 'ALL' + '-' + \
                                    air_carrier['service_level']

            # create data frame for each leg for expeditors
            e_rates_l1 = pd.read_excel(file, sheet_name='PRE_leg1')
            e_rates_l2 = pd.read_excel(file, sheet_name='AIR_leg2')
            e_rates_l3 = pd.read_excel(file, sheet_name='ONC_leg3')

            # correct codes for expeditors to have it all uppercase
            e_rates_l1['FromCity'] = e_rates_l1['FromCity'].str.upper()
            e_rates_l1['FromUNLOCODE'] = e_rates_l1['FromUNLOCODE'].str.upper()
            e_rates_l1['ToCity'] = e_rates_l1['ToCity'].str.upper()
            e_rates_l1['ToUNLOCODE'] = e_rates_l1['ToUNLOCODE'].str.upper()

            e_rates_l2['FromCity'] = e_rates_l2['FromCity'].str.upper()
            e_rates_l2['FromUNLOCODE'] = e_rates_l2['FromUNLOCODE'].str.upper()
            e_rates_l2['ToCity'] = e_rates_l2['ToCity'].str.upper()
            e_rates_l2['ToUNLOCODE'] = e_rates_l2['ToUNLOCODE'].str.upper()

            e_rates_l3['FromCity'] = e_rates_l3['FromCity'].str.upper()
            e_rates_l3['FromUNLOCODE'] = e_rates_l3['FromUNLOCODE'].str.upper()
            e_rates_l3['ToCity'] = e_rates_l3['ToCity'].str.upper()
            e_rates_l3['ToUNLOCODE'] = e_rates_l3['ToUNLOCODE'].str.upper()

            # create leg ids for expeditors rates dataframes
            e_rates_l1['LEG1ID'] = e_rates_l1['FromCity'] + "-" + e_rates_l1['ToCity'] + '-' + e_rates_l1[
                'ServiceLevel'].astype(str)
            e_rates_l2['LEG2ID'] = e_rates_l2['FromCity'] + "-" + e_rates_l2['ToCity'] + '-' + e_rates_l2[
                'ServiceLevel'].astype(str)
            e_rates_l3['LEG3ID'] = e_rates_l3['FromCity'] + "-" + e_rates_l3['ToCity'] + '-' + e_rates_l3[
                'ServiceLevel'].astype(str)

            # create dataframes for panalpina and expeditors containing only leg ids

            e_drop = pd.DataFrame(e_rates_l1['LEG1ID'])

            e2_drop = pd.DataFrame(e_rates_l2['LEG2ID'])

            e3_drop = pd.DataFrame(e_rates_l3['LEG3ID'])

            # renaming columns for dataframes for panalpina and expeditors for further adding it to report

            e_drop.rename(index=str, columns={"LEG1ID": 'L1'}, inplace=True)

            e2_drop.rename(index=str, columns={"LEG2ID": 'L2'}, inplace=True)

            e3_drop.rename(index=str, columns={"LEG3ID": 'L3'}, inplace=True)

            # removing duplicate values for all dataframes with leg ids for panalpina and epxeditors

            e_drop.drop_duplicates()

            e2_drop.drop_duplicates()

            e3_drop.drop_duplicates()

            # creating columns for dataframes for panalpina and expeditors indicating presence of rates
            # setting up an index to have the possibility to join dataframes

            e_drop['Leg1RatesPresent'] = True
            e_drop.set_index('L1', inplace=True, drop=True)

            e2_drop['Leg2RatesPresent'] = True
            e2_drop.set_index('L2', inplace=True, drop=True)

            e3_drop['Leg3RatesPresent'] = True
            e3_drop.set_index('L3', inplace=True, drop=True)

            # x.join(p_drop)
            # joining each table confirming rates presence
            # methodology - each time index for leg is assigned to main dataframe
            # then main dataframe is joined with rates confirmation dataframe
            # when joinning is finished - program switches to another leg (from 1 to 2, from 2 to 3) and assignes proper index
            # when new index is assigned then program joins another dataframe to verify presence of rates

            air_carrier.set_index('LEG1ID', inplace=True, drop=False)
            air_carrier = air_carrier.join(e_drop)
            air_carrier.set_index('LEG2ID', inplace=True, drop=False)
            air_carrier = air_carrier.join(e2_drop)
            air_carrier.set_index('LEG3ID', inplace=True, drop=False)
            air_carrier = air_carrier.join(e3_drop)

            air_carrier.reset_index(inplace=True, drop=True)

            air_carrier.drop_duplicates(subset='Shipment', inplace=True)

            mps = pd.read_excel(mps_file,
                                sheet_name=0,
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

            mps = mps[['Carrier', 'LaneID']]

            mps.LaneID = mps.LaneID.str[2:]

            air_carrier["LANEID"] = air_carrier['Port of loading'].str[2:] + "-" + air_carrier['Port of discharge'].str[
                                                                                   2:] + '-' + air_carrier[
                                        'service_level']
            air_carrier['allocation'] = air_carrier['LANEID'].map(mps.set_index("LaneID")["Carrier"].to_dict())
            air_carrier.drop(
                columns=['Action taken', 'Pending/Solved', 'date of email', 'E-mail subject', 'Delay in answer',
                         'Comments from carrier', 'Comments', 'Booker name (1)', 'Shipper name (1)',
                         'Original shipper name (1)'], inplace=True)

            # sending the dataframe for expeditors to excel
            air_carrier.to_excel(
                r'C:\Users\310295192\Desktop\Work\Rates\Air\python check-up\MATC {} check-up {}.xlsx'.format(naming_file,
                                                                                                            address),
                index=False)



checking(mps,carriers,report_date)