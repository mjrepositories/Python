import pandas as pd
import datetime
import numpy as np

# reading all order report
optilo = pd.read_csv('Desktop\grass\AllOrderReport.csv',delimiter=';')

# leaving only necessary colummns
optilo = optilo[['Transport order creation date','Real pickup date',
            'Pickup country','Pickup city','Customer address','Destination country',
             'MOT','Service lvl','Start port','Final port','Carrier 1leg','Carrier 2leg',
             'Ref. number 1leg','Ref. number 2leg']]

# getting only sea transports
optilo_sea = optilo[optilo['MOT']=='Sea']

# getting only air transports
optilo_air = optilo[optilo['MOT']=='Air']

# checking today date and setting up period of 90 days
today = datetime.datetime.today()
three_months = (today -datetime.timedelta(90)).strftime("%Y-%m-%d")

# filtering shipments onny for last 3 months
optilo_air = optilo_air[optilo_air['Transport order creation date']>three_months]
optilo_sea = optilo_sea[optilo_sea['Transport order creation date']>three_months]

# reading csv from system with MJBS
optilo_mjb = pd.read_csv('Desktop\grass\JOB_RATED.csv',delimiter=';')

# joining tables to have one source of data

optilo_air = optilo_mjb.join(optilo.set_index('Ref. number 1leg'),on = 'Number').dropna(subset=['Transport order creation date'])
optilo_sea = optilo_mjb.join(optilo.set_index('Ref. number 1leg'),on = 'Number').dropna(subset=['Transport order creation date'])

optilo_air = optilo_air[optilo_air['MOT'] =='Air']
optilo_sea = optilo_sea[optilo_sea['MOT'] =='Sea']

# reading MPS
mps = pd.read_excel('Desktop\grass\MPS.xlsx',sheet_name=0, skiprows=0,header =1, usecols=list(range(3,13)))


# reading rates for FCL
boss_leg2 = pd.read_excel('Desktop\\grass\\2020 FCL.xlsx',sheet_name=1)

# replacing the carriers with proper naming
optilo_air.replace({'EXP-WG-AIR':'EXPEDITORS','PAN-AIR-GL':'PANALPINA',
                   'DHL-AIR-GL':'DHL','UPS-AIR-GL':'UPS','EXP-AIR-GL':'EXPEDITORS',
                   'CEV-AIR-GL':'CEVA','NIP-AIR-GL':'NIPPON','DBS-AIR-GL':'DBS'},inplace=True)

# dropping unnecassary carriers
optilo_air.drop(optilo_air[(optilo_air['Carrier 1leg']=='MWD-LMP-EU')|((optilo_air['Carrier 1leg']=='FED-EXP-GL'))|
          (optilo_air['Carrier 1leg']=='DHL-EXP-GL')|(optilo_air['Carrier 1leg']=='EXP-WG-EU')].index,inplace=True)

# dropping unnecessary columns
optilo_air.drop(columns=['Carrier 2leg','Ref. number 2leg'],inplace=True)

# creating a laneID
optilo_air['LaneID'] = optilo_air['Carrier 1leg']+ "-A-" + optilo_air['Start port'] + "-"+optilo_air['Final port']+ '-' + optilo_air['Service lvl'].str[-1:]

# creating a laneID in MPS
mps['LANEID']=mps['TSP - Transport Service Provider'].str.upper() + "-"+ mps['Lane ID code']

# setting up only LaneID series
mps = mps['LANEID']

# switching to DataFrame for series created
mps = pd.DataFrame(mps)

# adding additional column indicating that rate is present for further merging
mps['present'] = 'yes'

# joining dataframes
optilo_air = optilo_air.join(mps.set_index('LANEID'),on='LaneID')

# adjusting the cost status for MJBs
optilo_air['Cost status'] = np.select([optilo_air['Cost status']=='210 partially calculated (according to price list)',
                                     optilo_air['Cost status']=='200 not calculated (no price list)',
                                     optilo_air['Cost status']=='220 fully calculated (according to price list)',
                                     optilo_air['Cost status']=='100 assigned contract (designated codes)'],['Partially',
                                        'Not calculated','Fully','Assigned'],default = 'No info')

# dropping missing laneIDs
optilo_air.dropna(subset=['LaneID'],inplace=True)

# leaving everything in DataFrame aside from 'assigned' indication
optilo_air=optilo_air[~(optilo_air['Cost status'] == 'Assigned')]

# creating a methodology behind reasons for lack of rates for AIR

# creating a dictionary for results
dict_air = optilo_air['pareto'].value_counts().to_dict()

# adding additional key/value pair
dict_air['Rated'] = dict_air['nan']

# getting rid of unused data
dict_air.pop('nan')

# creating a descending dataframe
air_pareto = pd.Series(dict_air).to_frame('Count').sort_values(by='Count',ascending=False)

# creating a series for graph
air_pareto_series = air_pareto['Count']

# creating a graph with reasons
fig = air_pareto.iloc[1:].plot(figsize=(20,10),kind='bar',color='red',rot=0, fontsize=16)

# setting up title
fig.set_title('Reason for lack of AIR rates for last 3 months',fontsize=16)
#fig.set_xlabel("Reasons",fontsize=16)

# setting up y label
fig.set_ylabel("Number of shipments without rates",fontsize=16)

# getting the xticks text
for x,y in enumerate(air_pareto_series.iloc[1:].iteritems(),0):
    fig.text(x-0.025,y[1]+5,y[1],weight='bold',fontsize=14)

# saving the figure to file
fig.get_figure().savefig(r'C:\Users\310295192\Desktop\Pareto_AIR.png')


# NOW IT IS TIME FOR SEA


# taking necessary columns from infodis upload
allocation_fcl = boss_leg2[['FromUNLOCODE','ToUNLOCODE','CarrierName']]

# switching to uppercase letters for carriers names
allocation_fcl['CarrierName'] = allocation_fcl['CarrierName'].str.upper()

# creating an LaneID for checking
allocation_fcl['LANEID'] = allocation_fcl['FromUNLOCODE'] + "-" + allocation_fcl['ToUNLOCODE'] + "-" + allocation_fcl['CarrierName']

# deleting duplicate values
allocation_fcl.drop_duplicates(subset = ['LANEID'],inplace=True)

# creating column for presence of rates and dropping to unnecessary columns
allocation_fcl['present'] = 'yes'
allocation_fcl.drop(columns=['FromUNLOCODE','ToUNLOCODE','CarrierName'],inplace=True)

# adjusting the cost status
optilo_sea['Cost status'] = np.select([optilo_sea['Cost status']=='210 partially calculated (according to price list)',
                                     optilo_sea['Cost status']=='200 not calculated (no price list)',
                                     optilo_sea['Cost status']=='220 fully calculated (according to price list)',
                                     optilo_sea['Cost status']=='100 assigned contract (designated codes)'],['Partially',
                                        'Not calculated','Fully','Assigned'],default = 'No info')

# adjusting names of carriers
optilo_sea.replace({'MAE-SEA-GL':'MAERSK','HAL-SEA-GL':'HAPAG',
                   'ONE-SEA-GL':'ONE','ANL-SEA-GL':'ANL','ZIM-SEA-GL':'ZIM',
                   'HYU-SEA-GL':'HYUNDAI','COS-SEA-GL':'COSCO','ICL-SEA-GL':'ICL',
                   'HAS-SEA-GL':'HAMBURGSUD','APL-SEA-GL':'APL','OOC-SEA-GL':'OOCL',
                   'MCC-SEA-GL':'MCC'},inplace=True)

# creating laneID
optilo_sea['LaneID'] = optilo_sea['Start port'] + '-' + optilo_sea['Final port'] + "-" + optilo_sea['Carrier 1leg']

# joining two dataframes
optilo_sea = optilo_sea.join(allocation_fcl.set_index('LANEID'),on='LaneID')

# deleting "assigned" values
optilo_sea=optilo_sea[~(optilo_sea['Cost status'] == 'Assigned')]

# pareto analysis column
optilo_sea['pareto'] = np.select(
[(optilo_sea['Cost status']=='Partially')&(optilo_sea['present'] == 'yes'),
(optilo_sea['Cost status']=='Not calculated')&(optilo_sea['present'] == 'yes'),
(optilo_sea['Cost status']=='Not calculated')&(pd.isnull(optilo_sea['present']))],
['Technical issue','Pending upload','Spot quote'],
    default = np.nan)

# creating dictionary with reasons and counter
dict_sea = optilo_sea['pareto'].value_counts().to_dict()

# adjusting dictionary
dict_sea['Rated'] = dict_sea['nan']
dict_sea.pop('nan')

# creating a dataframe
sea_pareto = pd.Series(dict_sea).to_frame('Count').sort_values(by='Count',ascending=False)

# creaing  series for further iteration and assigning labels for x axis
sea_pareto['Count'].to_list()
sea_pareto_series = sea_pareto['Count']

# creating graph
fig = sea_pareto.iloc[1:].plot(figsize=(20,10),kind='bar',color='red',rot=0, fontsize=16)
fig.set_title('Reason for lack of sea rates for last 3 months',fontsize=16)
#fig.set_xlabel("Reasons",fontsize=16)
fig.set_ylabel("Number of shipments without rates",fontsize=16)
for x,y in enumerate(sea_pareto_series.iloc[1:].iteritems(),0):
    fig.text(x,y[1]+0.5,y[1],weight='bold',fontsize=14)

# saving the figure to file
fig.get_figure().savefig(r'C:\Users\310295192\Desktop\Pareto_SEA.png')

