import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime


tuday = datetime.datetime.today().strftime("%Y-%m-%d")
# reading data from csv. Separator is ;
dash = pd.read_csv('Desktop\ddd.csv',sep = ';')

# checking the domains names
dash['Domain Name'].value_counts()

# switching names of domains to more readable format
dash['Domain Name'].replace({'Domain Philips EUR DC North':'DC North',"Domain Philips India":"India",
                    "Domain Philips EUR DC South":"DC South",'Domain Philips EUR  DC East':"DC East",
                    'Domain Philips CL':"CL","Domain Philips NAM":"NAM",
                    "Domain Philips Respironics NAM":"SRC",'Domain Philips MATC':'MATC'},inplace=True)

# columns for my reference - switching to upper case
dash['Leg 2, Transport Mode'] = dash['Leg 2, Transport Mode'].map(lambda x: x.upper() if isinstance(x,str) else x)

# setting up filter for SEA shipments. Regex allows to look for both FCL and LCL with one string and "na" allows to keep empty values as faluse
filt_sea = dash['Leg 2, Transport Mode'].str.contains('SEA FCL',regex=True,na=False)
filt_sea_sub = dash['Leg 2, Carrier Name'].str.contains('sub',regex=True,na=False)
filt_lcl= dash['Leg 2, Transport Mode'].str.contains('SEA LCL',regex=True,na=False)


# creating dataframe for sea shipments
# using first filter
dash_sea = dash[filt_sea]
# using second filter
dash_sea = dash_sea[~filt_sea_sub]

# creating filter for sea
filt_sea_bill = dash_sea['Billable Indicator Leg 2']=='Yes'
# using third filter for sea
dash_sea = dash_sea[filt_sea_bill]

# using first filter for lcl
dash_lcl =dash[filt_lcl]

# creating filter for lcl
filt_lcl_bill = dash_lcl['Billable Indicator Leg 2']=='Yes'

# using filter for lcl
dash_lcl = dash_lcl[filt_lcl_bill]

# setting up filter for AIR shipments
filt_air = dash['Leg 2, Transport Mode'].str.contains('SERVICE LEVEL',regex=True,na=False)
# creating dataframe for air shipments
dash_air = dash[filt_air]

# creating second filter for air
filt_air_bill =dash_air['Billable Indicator Leg 2']=='Yes'

# using second filter for air
dash_air = dash_air[filt_air_bill]

# setting up a filter for ROAD shipments
filt_road = dash['Leg 2, Transport Mode'].str.contains('FCL|LCL|LEVEL',regex=True,na=False)

# creating dataframe for raod shipments
dash_road = dash[~filt_road]

# name rows with total cost and billable indicator as rated
ship_rated = [(dash_road['Total costs (sales) EUR']>0)]
dash_road['Rated']= np.select(ship_rated,['Rated'],default = 'Not Rated')

# setting up a group for domains
domains_road = dash_road.groupby('Domain Name')

# creating data frame for road
roading = pd.DataFrame(domains_road['Rated'].value_counts(normalize=True))

# renaming the column
roading.columns = ['situation']

# resetting the index
roading.reset_index(inplace=True)

# creating data frame with only rated shipments
roading_adjusted = roading[['Domain Name','situation']][roading['Rated']=='Rated']

# setting the index
roading_adjusted.set_index('Domain Name',drop=True,inplace=True)

# assigning the colors for results
coloring=[]
for x in roading_adjusted['situation'].to_list():
    if x >0.99:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')


# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(roading_adjusted.index.to_list(),roading_adjusted['situation'].to_list(),color=coloring)
plt.ylim([0.6,1])

f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\road {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)

# name rows with total cost and billable indicator as rated
ship_rated_sea = [(dash_sea['Total costs (sales) EUR']>0)&(dash_sea['Billable Indicator Leg 2']=='Yes')]
dash_sea['Rated']= np.select(ship_rated_sea,['Rated'],default = 'Not Rated')


# setting up a group for domains
domains_sea = dash_sea.groupby('Domain Name')

# created data frame for sea based on grouping
seaing = pd.DataFrame(domains_sea['Rated'].value_counts(normalize=True))

# changing the name of column and setting up index
seaing.columns = ['situation']
seaing.reset_index(inplace=True)

# creating data frame with only rated shipments for domains
seaing_adjusted = seaing[['Domain Name','situation']][seaing['Rated']=='Rated']

# setting up index
seaing_adjusted.set_index('Domain Name',drop=True,inplace=True)

# creating list for coloring
coloring=[]
for x in seaing_adjusted['situation'].to_list():
    if x >0.99:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')

# creating plot
# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(seaing_adjusted.index.to_list(),seaing_adjusted['situation'].to_list(),color=coloring,align='center', width=0.3)
plt.ylim([0.6,1])
plt.tight_layout()

# saving graph
f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\sea {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)

# name rows with total cost and billable indicator as rated
ship_rated_lcl = [(dash_lcl['Total costs (sales) EUR']>0)&(dash_lcl['Billable Indicator Leg 2']=='Yes')]
dash_lcl['Rated']= np.select(ship_rated_lcl,['Rated'],default = 'Not Rated')

# setting up a group for domains
domains_lcl = dash_lcl.groupby('Domain Name')

# created data frame for sea based on grouping
lcling = pd.DataFrame(domains_lcl['Rated'].value_counts(normalize=True))

# changing the name of column and setting up index
lcling.columns = ['situation']
lcling.reset_index(inplace=True)

#  creating data frame with only rated shipments for domains
lcling_adjusted = lcling[['Domain Name','situation']][lcling['Rated']=='Rated']

# setting up index

lcling_adjusted.set_index('Domain Name',drop=True,inplace=True)

# coloring for results
coloring=[]
for x in lcling_adjusted['situation'].to_list():
    if x >0.99:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')

# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(lcling_adjusted.index.to_list(),lcling_adjusted['situation'].to_list(),color=coloring,align='center', width=0.3)
plt.ylim([0.6,1])
plt.tight_layout()

# saving graph
f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\lcl {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)

# name rows with total cost and billable indicator as rated
ship_rated_air = [(dash_air['Total costs (sales) EUR']>0)&(dash_air['Billable Indicator Leg 2']=='Yes')]
dash_air['Rated']= np.select(ship_rated_air,['Rated'],default = 'Not Rated')


# setting up a group for domains
domains_air = dash_air.groupby('Domain Name')

# creating dataframe with results
airing = pd.DataFrame(domains_air['Rated'].value_counts(normalize=True))

# changing column name and setting up index
airing.columns = ['situation']
airing.reset_index(inplace=True)

# creating dataframe with only rated shipments
airing_adjusted = airing[['Domain Name','situation']][airing['Rated']=='Rated']

# setting up index
airing_adjusted.set_index('Domain Name',drop=True,inplace=True)

# arranging colors for results
coloring=[]
for x in airing_adjusted['situation'].to_list():
    if x >0.99:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')


# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(airing_adjusted.index.to_list(),airing_adjusted['situation'].to_list(),color=coloring,align='center', width=0.3)
plt.ylim([0.6,1])
plt.tight_layout()

# saving graph
f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\air {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)

# grouping data for sea on carriers
overview_sea = dash_sea.groupby('Leg 2, Carrier Name')

# creating data frame based on grouping
overview_sea_adjusted =pd.DataFrame(overview_sea['Rated'].value_counts())


# changing the name for column and reseting
overview_sea_adjusted.columns = ['situation']
overview_sea_adjusted.reset_index(inplace=True)

# creating overview only with rated situation
seaing_adjusted = overview_sea_adjusted[['Leg 2, Carrier Name','situation']][overview_sea_adjusted['Rated']=='Not Rated']

# sorting values
seaing_adjusted.sort_values(by=['situation'],ascending=False,inplace=True)

# setting up index for graph
seaing_adjusted.set_index('Leg 2, Carrier Name',drop=True,inplace=True)

# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(seaing_adjusted.index.to_list(),seaing_adjusted['situation'].to_list(),color=coloring,align='center', width=0.3)
plt.xticks(rotation=90)
plt.tight_layout()

# saving graph
f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\sea per carrier {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)

# grouping data for sea on carriers
overview_air = dash_air.groupby('Leg 2, Carrier Name')

# creating data frame based on grouping
overview_air_adjusted =pd.DataFrame(overview_air['Rated'].value_counts())

# changing the name for column and reseting
overview_air_adjusted.columns = ['situation']
overview_air_adjusted.reset_index(inplace=True)

# creating overview only with rated situation
airing_adjusted = overview_air_adjusted[['Leg 2, Carrier Name','situation']][overview_air_adjusted['Rated']=='Not Rated']

# sorting values
airing_adjusted.sort_values(by=['situation'],ascending=False,inplace=True)


# setting up index

airing_adjusted.set_index('Leg 2, Carrier Name',drop=True,inplace=True)

# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(airing_adjusted.index.to_list(),airing_adjusted['situation'].to_list(),color=coloring,align='center', width=0.3)
plt.xticks(rotation=90)
plt.tight_layout()


# saving graph
f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\air per carrier {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)


# grouping the data for carriers
overview_road = dash_road.groupby('Leg 2, Carrier Name')

# creating dataframe
overview_road_adjusted =pd.DataFrame(overview_road['Rated'].value_counts())


# chaning the column name
overview_road_adjusted.columns = ['situation']

# resetting index
overview_road_adjusted.reset_index(inplace=True)

# createing data frame only for rated shipemnts
roading_adjusted = overview_road_adjusted[['Leg 2, Carrier Name','situation']][overview_road_adjusted['Rated']=='Not Rated']

# sorting values
roading_adjusted.sort_values(by=['situation'],ascending=False,inplace=True)

# resetting values
roading_adjusted.set_index('Leg 2, Carrier Name',drop=True,inplace=True)

# setting up figure size
plt.figure(dpi=128,figsize=(20,10))

plt.rcParams.update({'font.size': 22})

# creating bar chart
plt.bar(roading_adjusted.index.to_list(),roading_adjusted['situation'].to_list(),color=coloring,align='center', width=0.3)
plt.xticks(rotation=90)
plt.tight_layout()

# saving graph
f_name = r'C:\Users\310295192\Desktop\Python\Projects\infodis_DASHBOARD\road per carrier {}.png'.format(tuday)
# saving figure
plt.savefig(f_name)