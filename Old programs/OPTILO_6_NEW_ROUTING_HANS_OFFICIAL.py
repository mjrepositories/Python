import pandas as pd
import datetime
import os

print(datetime.datetime.now())
# reading file with new users
naming = input('What is the folder and file for forecast. Indicate "\Folder\File_Name.xlsx": ')
df = pd.read_excel(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Routings\Routings.xlsm')

# dropping irrelevant columns
df.drop(df.columns[[0,1,2,3,4,5,6,7]],axis=1, inplace=True)

# creating dataframe for existing routing
routing = df

# reading file with forecast
forecast = pd.read_excel(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Forecasts AIR\Best{}'.format(naming),sheet_name=0,header=[1])

# dropping firts column
forecast.drop(forecast.columns[[0]],axis=1, inplace=True)

# leaving routing and type of transport
hans = forecast[['Route','Item Status']]

# dropping duplicates values
hans.drop_duplicates(subset = 'Route',inplace=True)

# resetting index
hans.reset_index(inplace=True,drop=True)

# extracting the data present in parenthases
hans['cor_routing']=hans['Route'].str.extract(r'\((.*?)\)')

# selecting only rows that have air mode of transport present
hans = hans[(hans['Item Status'] == 'Air Direct Delivery') | (hans['Item Status'] =='Air General Cargo')]

# resetting index
hans.reset_index(inplace=True,drop=True)

# merging two columns to have the visibility what is present and what is missing
new_lanes = pd.merge(routing,hans,left_on='Lookup for routing',right_on='cor_routing',how='outer')

#indicating only values that are without indicating POD in routing file
missing = new_lanes[new_lanes['POD'].isna()]

# dropping irrelevant columns
missing.drop(missing.columns[[0,1,2,3]],axis=1, inplace=True)

# saving file to excel on desktop
missing.to_excel(r'C:\Users\310295192\Desktop\missingrouting.xlsx', index=False)

print(datetime.datetime.now())

os.startfile(r'C:\Users\310295192\Desktop\Work\Optilo\Forecasting\Routings')
