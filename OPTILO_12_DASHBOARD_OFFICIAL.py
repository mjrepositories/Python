import pandas as pd
import numpy as np
import datetime
from distutils.dir_util import copy_tree
today = datetime.date.today()
two_weeks = today - datetime.timedelta(21)
import matplotlib.pyplot as plt
import shutil
import os
import time
#we are opening the file here
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# root = Tk()
# ftypes = [('All files','*.*')]
# ttl  = "Select the file"
# dir1 = r'C:\Users\310295192\Downloads'
# root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
# naming = str(root.fileName)
# root.destroy()

naming = input("Provide source file path: ")

# read optilo report
optilo = pd.read_csv(naming,delimiter=';')

# delete unnecessary columns
optilo.drop(columns=['Choose','Operational status','External number','Service type','Service level','Vehicle',
                    'Prebooked','Carrier status','Custom Exit Point','Oru Payer',
                    'PF Requested','DG indicator','Reference1','Reference2','Reference3',
                    'Reference4','Reference5','Company','Income contract','Event list id',
                    'Documents List','Order references','Carrier ref. 1','Carrier External Reference',
                    'EU-MDR','Cost contract'],inplace=True)

# change name for statuses
optilo['Cost status'] = np.select([optilo['Cost status']=='220 fully calculated (according to price list)',
                                  optilo['Cost status']=='200 not calculated (no price list)',
                                  optilo['Cost status']=='210 partially calculated (according to price list)',
                                  optilo['Cost status']=='100 assigned contract (designated codes)',
                                  optilo['Cost status']=='000 no settlements'],
                                   ['fully calculated','not calculated','partially calculated',
                                                       'assigned contract','no settlements'],default ='no settlements')
 # create dictionary with name and count for statuses
summary = optilo['Cost status'].value_counts().to_dict()

# create list for axis x and y in graph
labels = [x for x in summary.keys()]
rates = [x for x in summary.values()]

# take the value for fully calcualted shipments
calculated = summary['fully calculated']

# calculate value for rates presence in percentage
rate_status=round(calculated/sum(rates),2)*100

#read Dashboard with overall data
rating = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard\Optilo dashboard_test.xlsx',
                       sheet_name="Data")

# create new dataframe with value of current day
new_rating = pd.DataFrame([[today,rate_status,95]],columns=["Date",'Coverage','Target'])

# change the format of time for new dataframe
new_rating.Date = pd.to_datetime(new_rating.Date,dayfirst=True)

# add new data to existing one
rating = rating.append(new_rating)

# reset index
rating.reset_index(inplace=True,drop=True)


# extracting the proper dataframe from file
rating = rating[(rating['Date']<=today) & (rating['Date']>=two_weeks)]

# assigning date table for x axis
dates =[x.strftime('%Y-%m-%d') for x in rating['Date']]
# assigning table with values for y axis
values = [round(x,3) for x in rating['Coverage']]
# assigning values for target
target = [95 for x in range(len(rating['Target']))]
coloring =[]
# checking the color for bars, if good then green and if not - red
for x in values:
    if x >95:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')
# setting up figure size
plt.figure(dpi=128,figsize=(10,6))
# creating bar chart
plt.bar(dates,values,color=coloring)
# creating line chart
plt.plot(dates, target,color='#031f85',linewidth=3,linestyle='--')
# rotating ticks
plt.xticks(dates, rotation='vertical')
# adding title
plt.title('Shipments with rates in Optilo', fontsize=14)
# setting up label for y axis
plt.ylabel('%',fontsize=14,rotation='horizontal')
# setting up legend and location
plt.legend(["Target"],loc='upper center', bbox_to_anchor=(0.5, -0.25))
# "Packing" the figure
plt.tight_layout()
# setting up date for file name
x = datetime.datetime.today().strftime("%Y-%m-%d")
# creating file name
f_name = r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkoverall.png'
# saving figure
plt.savefig(f_name)

# clear figure
plt.clf()

plt.close('all')
time.sleep(4)

# read all necessary mode of transports from Optilo report
sea_rates = optilo[optilo['Transport type'] =='Sea']
air_rates = optilo[optilo['Transport type'] == 'Air']
road_rates = optilo[optilo['Transport type'] == "Road"]
parcel_rates = optilo[optilo['Transport type'] == 'Parcel']

# create dictionary for sea and respective values
summary_sea = sea_rates['Cost status'].value_counts().to_dict()

# create list for axis x and y for graphs for sea
labels_sea = [x for x in summary_sea.keys()]
rates_sea = [x for x in summary_sea.values()]

# check the presence of rates for sea
calculated_sea = summary_sea['fully calculated']

# turn value for sea in percentage
rate_status_sea=round(calculated_sea/sum(rates_sea),2)*100

# read current data for sea
rating_sea = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard\Optilo dashboard_test.xlsx',
                           sheet_name="Sea")

# create dataframe for new data for sea
new_rating_sea = pd.DataFrame([[today,rate_status_sea,95]],columns=["Date",'Coverage','Target'])

# change the format of dataframe for new value for sea
new_rating_sea.Date = pd.to_datetime(new_rating_sea.Date,dayfirst=True)

# add new data to existing values
rating_sea = rating_sea.append(new_rating_sea)

#reset index
rating_sea.reset_index(inplace=True,drop=True)

# extracting the proper dataframe from file
rating_sea = rating_sea[(rating_sea['Date']<=today) & (rating_sea['Date']>=two_weeks)]

# assigning date table for x axis
dates =[x.strftime('%Y-%m-%d') for x in rating_sea['Date']]
# assigning table with values for y axis
values = [round(x,3) for x in rating_sea['Coverage']]
# assigning values for target
target = [95 for x in range(len(rating_sea['Target']))]
coloring =[]
# checking the color for bars, if good then green and if not - red
for x in values:
    if x >95:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')
# setting up figure size
plt.figure(dpi=128,figsize=(10,6))
# creating bar chart
plt.bar(dates,values,color=coloring)
# creating line chart
plt.plot(dates, target,color='#031f85',linewidth=3,linestyle='--')
# rotating ticks
plt.xticks(dates, rotation='vertical')
# adding title
plt.title('sea shipments with rates in Optilo', fontsize=14)
# setting up label for y axis
plt.ylabel('%',fontsize=14,rotation='horizontal')
# setting up legend and location
plt.legend(["Target"],loc='upper center', bbox_to_anchor=(0.5, -0.25))
# "Packing" the figure
plt.tight_layout()
# setting up date for file name
x = datetime.datetime.today().strftime("%Y-%m-%d")
# creating file name
f_name = r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checksea.png'
# saving figure
plt.savefig(f_name)

# clear figure
plt.clf()

plt.close('all')
time.sleep(4)


# create dictionary for road
summary_road = road_rates['Cost status'].value_counts().to_dict()

# create labels for axis x and y for road graph
labels_road = [x for x in summary_road.keys()]
rates_road = [x for x in summary_road.values()]

# calculate the value for road and current status
calculated_road = summary_road['fully calculated']

# turn value for road to percentage
rate_status_road=round(calculated_road/sum(rates_road),2)*100

# read data for road
rating_road = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard\Optilo dashboard_test.xlsx',
                            sheet_name="Road")

# create dataframe for new data
new_rating_road = pd.DataFrame([[today,rate_status_road,95]],columns=["Date",'Coverage','Target'])

# turn date format for road
new_rating_road.Date = pd.to_datetime(new_rating_road.Date,dayfirst=True)

# add new dataframe to existing data
rating_road = rating_road.append(new_rating_road)

# reset index
rating_road.reset_index(inplace=True,drop=True)


# extracting the proper dataframe from file
rating_road = rating_road[(rating_road['Date']<=today) & (rating_road['Date']>=two_weeks)]

# assigning date table for x axis
dates =[x.strftime('%Y-%m-%d') for x in rating_road['Date']]
# assigning table with values for y axis
values = [round(x,3) for x in rating_road['Coverage']]
# assigning values for target
target = [95 for x in range(len(rating_road['Target']))]
coloring =[]
# checking the color for bars, if good then green and if not - red
for x in values:
    if x >95:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')
# setting up figure size
plt.figure(dpi=128,figsize=(10,6))
# creating bar chart
plt.bar(dates,values,color=coloring)
# creating line chart
plt.plot(dates, target,color='#031f85',linewidth=3,linestyle='--')
# rotating ticks
plt.xticks(dates, rotation='vertical')
# adding title
plt.title('road shipments with rates in Optilo', fontsize=14)
# setting up label for y axis
plt.ylabel('%',fontsize=14,rotation='horizontal')
# setting up legend and location
plt.legend(["Target"],loc='upper center', bbox_to_anchor=(0.5, -0.25))
# "Packing" the figure
plt.tight_layout()
# setting up date for file name
x = datetime.datetime.today().strftime("%Y-%m-%d")
# creating file name
f_name = r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkroad.png'
# saving figure
plt.savefig(f_name)


# clear figure
plt.clf()

plt.close('all')
time.sleep(4)


# dictionary with values for air
summary_air = air_rates['Cost status'].value_counts().to_dict()

# lists for axis x and y for air
labels_air = [x for x in summary_air.keys()]
rates_air = [x for x in summary_air.values()]

# calculate air rates presence
calculated_air = summary_air['fully calculated']

# turn value into percentage
rate_status_air=round(calculated_air/sum(rates_air),2)*100

# read air data
rating_air = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard\Optilo dashboard_test.xlsx',
                           sheet_name="Air")

# create dataframe
new_rating_air = pd.DataFrame([[today,rate_status_air,95]],columns=["Date",'Coverage','Target'])

# turn date format
new_rating_air.Date = pd.to_datetime(new_rating_air.Date,dayfirst=True)

# add new data to existing one
rating_air = rating_air.append(new_rating_air)

# reset index
rating_air.reset_index(inplace=True,drop=True)

# extracting the proper dataframe from file
rating_air = rating_air[(rating_air['Date']<=today) & (rating_air['Date']>=two_weeks)]

# assigning date table for x axis
dates =[x.strftime('%Y-%m-%d') for x in rating_air['Date']]
# assigning table with values for y axis
values = [round(x,3) for x in rating_air['Coverage']]
# assigning values for target
target = [95 for x in range(len(rating_air['Target']))]
coloring =[]
# checking the color for bars, if good then green and if not - red
for x in values:
    if x >95:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')
# setting up figure size
plt.figure(dpi=128,figsize=(10,6))
# creating bar chart
plt.bar(dates,values,color=coloring)
# creating line chart
plt.plot(dates, target,color='#031f85',linewidth=3,linestyle='--')
# rotating ticks
plt.xticks(dates, rotation='vertical')
# adding title
plt.title('air shipments with rates in Optilo', fontsize=14)
# setting up label for y axis
plt.ylabel('%',fontsize=14,rotation='horizontal')
# setting up legend and location
plt.legend(["Target"],loc='upper center', bbox_to_anchor=(0.5, -0.25))
# "Packing" the figure
plt.tight_layout()
# setting up date for file name
x = datetime.datetime.today().strftime("%Y-%m-%d")
# creating file name
f_name = r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkair.png'
# saving figure
plt.savefig(f_name)

# clear figure
plt.clf()

plt.close('all')
time.sleep(4)

# dictionary for parcel
summary_parcel = parcel_rates['Cost status'].value_counts().to_dict()

# list for axis x and y for parcel graph
labels_parcel = [x for x in summary_parcel.keys()]
rates_parcel = [x for x in summary_parcel.values()]

# check status of rates for parcel
calculated_parcel = summary_parcel['fully calculated']

# calculate percentage for parcel rates
rate_status_parcel=round(calculated_parcel/sum(rates_parcel),2)*100

# read parcel rates
rating_parcel = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard\Optilo dashboard_test.xlsx',
                              sheet_name="Parcel")

# create dataframe based on new data for parcel
new_rating_parcel = pd.DataFrame([[today,rate_status_parcel,95]],columns=["Date",'Coverage','Target'])

# change format for date in parcel data
new_rating_parcel.Date = pd.to_datetime(new_rating_parcel.Date,dayfirst=True)

# add new data to existing values
rating_parcel = rating_parcel.append(new_rating_parcel)

#rating_parcel.set_index('Date').plot()
# reset index
rating_parcel.reset_index(inplace=True,drop=True)

# extracting the proper dataframe from file
rating_parcel = rating_parcel[(rating_parcel['Date']<=today) & (rating_parcel['Date']>=two_weeks)]

# assigning date table for x axis
dates =[x.strftime('%Y-%m-%d') for x in rating_parcel['Date']]
# assigning table with values for y axis
values = [round(x,3) for x in rating_parcel['Coverage']]
# assigning values for target
target = [95 for x in range(len(rating_parcel['Target']))]
coloring =[]
# checking the color for bars, if good then green and if not - red
for x in values:
    if x >95:
        coloring.append('#038518')
    else:
        coloring.append('#f5424b')
# setting up figure size
plt.figure(dpi=128,figsize=(10,6))
# creating bar chart
plt.bar(dates,values,color=coloring)
# creating line chart
plt.plot(dates, target,color='#031f85',linewidth=3,linestyle='--')
# rotating ticks
plt.xticks(dates, rotation='vertical')
# adding title
plt.title('Parcel shipments with rates in Optilo', fontsize=14)
# setting up label for y axis
plt.ylabel('%',fontsize=14,rotation='horizontal')
# setting up legend and location
plt.legend(["Target"],loc='upper center', bbox_to_anchor=(0.5, -0.25))
# "Packing" the figure
plt.tight_layout()
# setting up date for file name
x = datetime.datetime.today().strftime("%Y-%m-%d")
# creating file name
f_name = r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkparcel.png'
# saving figure
plt.savefig(f_name)

# clear figure
plt.clf()

plt.close('all')
time.sleep(4)


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard\Optilo dashboard_test.xlsx',
                        engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
rating.to_excel(writer, sheet_name='Data',index=False)
rating_sea.to_excel(writer, sheet_name = 'Sea',index=False)
rating_air.to_excel(writer, sheet_name = 'Air',index=False)
rating_road.to_excel(writer, sheet_name = 'Road',index=False)
rating_parcel.to_excel(writer, sheet_name = 'Parcel',index=False)
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Data']

# Get the xlsxwriter workbook and worksheet objects.
workbook1  = writer.book
worksheet1 = writer.sheets['Sea']

# Get the xlsxwriter workbook and worksheet objects.
workbook2  = writer.book
worksheet2 = writer.sheets['Air']

# Get the xlsxwriter workbook and worksheet objects.
workbook3 = writer.book
worksheet3 = writer.sheets['Road']

# Get the xlsxwriter workbook and worksheet objects.
workbook4  = writer.book
worksheet4 = writer.sheets['Parcel']

# Insert an image.
worksheet.insert_image('G3', r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkoverall.png')
# Insert an image.
worksheet1.insert_image('G3', r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checksea.png')
# Insert an image.
worksheet2.insert_image('G3', r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkair.png')
# Insert an image.
worksheet3.insert_image('G3', r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkroad.png')
# Insert an image.
worksheet4.insert_image('G3', r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs\checkparcel.png')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

#delete the folders from place where files are managed and create them again
shutil.rmtree(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\graphs', ignore_errors=True)

# copies the corrected files to desktop (to avoid downloading from mail box)
copy_tree(r'C:\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD\dashboard', r'C:\Users\310295192\Desktop')

# check week num
week_num_opt= str(datetime.datetime.today().strftime("%V"))

# rename the file
os.rename(r'\Users\310295192\Desktop\Optilo dashboard_test.xlsx',r'\Users\310295192\Desktop\Optilo dashboard week {}.xlsx'.format(week_num_opt))

# check if folder is present
os.chdir(r'\Users\310295192\Desktop\Python\Projects\OPTILO_DASHBOARD')
# if not - created folder for graphs
if not os.path.isdir('graphs'):
    os.mkdir('graphs')

