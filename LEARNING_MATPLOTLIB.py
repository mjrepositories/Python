# from matplotlib import pyplot as plt
# # import random
# # print(plt.style.available)
# # ages_x = [x for x in range(25,36)]
# #
# # dev_y = [38496, 42000, 46752, 49320, 53200,
# #          56000, 62316, 64928, 67317, 68748, 73752]
# #
# # plt.xkcd()
# # # Median Python Developer Salaries by Age
# # py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# # py_dev_y = [45372, 48876, 53850, 57287, 63016,
# #             65998, 70003, 70000, 71496, 75370, 83640]
# #
# #
# # # Median JavaScript Developer Salaries by Age
# # js_dev_y = [37810, 43515, 46823, 49293, 53437,
# #             56373, 62375, 66674, 68745, 68746, 74583]
# #
# # # Ages 18 to 55
# # ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
# #           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
# #
# # py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
# #             84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
# #
# # js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
# #             78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
# #
# # dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
# #          78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
# #
# # plt.plot(ages_x,dev_y,color='#444444',linestyle='--',label='All Developers')
# # plt.xlabel('Ages')
# # plt.ylabel("Salary")
# # plt.title('Median salary by age')
# #
# #
# #
# # plt.plot(ages_x,py_dev_y,label='Python')
# # plt.plot(ages_x,js_dev_y,label='JS')
# # plt.legend()
# # plt.tight_layout()
# # plt.grid(True)
# # plt.savefig(r'C:\Users\310295192\Desktop\graphmpl.png')
# # plt.show()
# # import numpy as np
# # plt.style.use('fivethirtyeight')
# # age = [1,2,3,4,5,6,7,8,9,10]
# # x_indexes = np.arange(len(age))
# # width = 0.25
# # print(x_indexes-width)
# # weight=[30,30,30,30,30,30,30,30,30,30]
# # avg_weight_england =[10,11,15,20,26,31,34,39,40,49]
# # avg_weight_poland = [10,13,15,17,20,24,26,40,38,59]
# # avg_weight_world = [13,16,18,26,29,30,36,40,49,50]
# # plt.style.use('ggplot')
# # coloring = []
# # plt.bar(x_indexes-width,avg_weight_england,width=width,color='Green')
# # plt.bar(x_indexes,avg_weight_poland,width=width, color='Blue')
# # plt.bar(x_indexes+width,avg_weight_world,width=width, color = 'Yellow')
# # #plt.plot(age,weight,color='Blue',linestyle='-',linewidth=3,label='Target')
# # plt.xlabel('Wiek')
# # plt.ylabel("Waga")
# # plt.legend(['England','Poland','World'])
# # plt.xticks(ticks=x_indexes,labels=age)
# # plt.tight_layout()
# # plt.grid(True)
#
# #plt.show()
# # plt.style.available shows what styles of plots are available
# # plt.style.use() enables me to type in the proper value as for style and then transfer that to graph
# # as for feautres of the graph we have linestyle, linewidth,marker,color,label
# # we can either input label or type in labels as list in plt.legend()
# # plt.xkcd() will generate comics graph
# # plt.tight_layout() will...tight the layout
# # we can also add grid to our graph so that it is possible to change the view of the graph
# # after all is added we just generate graph by typing in plt.show()
# # or we can move with the graph to the file by typing plt.savefig()and declaring the location of the file
#
# # plt.style.available shows all available styles that we have in matplotlib
# # plt.style.use() is a method that enables user to input the style we want to use to change the style of the graph
# # as for the features that can be used for graphs we can indcate:
# # linestyle, linewidth, marker, color, label
# # # we have to options as for putting label of the line/bar created
# # # we can either use label property while plotting the graph or put the label in plt.legend() method
# # # plt.xkcd() is a method that turns graph into comic style
# # # plt.tight_layout() is a method that packs the graph more neatly in the square for graph
# # # we can also add grid by adding plt.grid(True) which will show the graph with grip for better visualization of graph
# # # after all needed data/methods/features are added we can use plt.plot() method
# # # then we can either do plt.show() to present the graph or plot.savefig() to save the figure into specific location
# #
# # # import os
# # # import csv
# # # from collections import Counter
# # # csvdata = os.environ['HOMEPATH']+'\Desktop\data.csv'
# # # print(csvdata)
# # # plt.style.use('fivethirtyeight')
# # # with open(csvdata) as csv_file:
# # #
# # #     csv_reader = csv.DictReader(csv_file)
# # #     lang_counter = Counter()
# # #     for row in csv_reader:
# # #         lang_counter.update(row['LanguagesWorkedWith'].split(';'))
# # #         languages,popularity = map(list,zip(*lang_counter.most_common(15)))
# # #     # languages =[]
# # #     # popularity =[]
# # #     #
# # #     # for item in lang_counter.most_common(15):
# # #     #     languages.append(item[0])
# # #     #     popularity.append(item[1])
# # #
# # # languages.reverse()
# # # popularity.reverse()
# # #
# # # plt.barh(languages,popularity)
# # #
# # # plt.title("Most popular langauages")
# # # plt.xlabel("Median Salary (USD)")
# # # plt.tight_layout()
# # # plt.show()
# #
# #
# # import os
# # import csv
# # import pandas as pd
# # from collections import Counter
# # # #
# # # csvdata = os.environ['HOMEPATH']+'\Desktop\data.csv'
# # # print(csvdata)
# # # print(csvdata)
# # # plt.style.use('fivethirtyeight')
# # # data = pd.read_csv(csvdata)
# # # ids = data['Responder_id']
# # # lang_responses = data['LanguagesWorkedWith']
# # #
# # # lang_counter = Counter()
# # # for response in lang_responses:
# # #     lang_counter.update(response.split(';'))
# # #
# # # languages,popularity = map(list,zip(*lang_counter.most_common(15)))
# # # # languages =[]
# # # # popularity =[]
# # # #
# # # # for item in lang_counter.most_common(15):
# # # #     languages.append(item[0])
# # # #     popularity.append(item[1])
# # #
# # # languages.reverse()
# # # popularity.reverse()
# # #
# # # plt.barh(languages,popularity)
# # #
# # # plt.title("Most popular langauages")
# # # plt.xlabel("Median Salary (USD)")
# # # plt.tight_layout()
# # # plt.show()
# #
# # # To create a bar chart with bars next to themselves we have to create a numpy array
# # # by typing in np.arange(len(listforx))
# # # then we have to input that as x data for every plot and move it to the side by the width of the column
# # # Could be width = 0,25 then we move one chart -0,25, second one is the same, and thirt one is +0,25
# # # then in xticks we specify ticks as this array, so(xticks = x_tick) and we add labels as (labels=age)
# #
# #
# #
# # #
# # # csvdata = os.environ["HOMEPATH"] + "\Desktop\Data.csv"
# # #
# # # # Language Popularity
# # # slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# # # labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# # #
# # # explode = [0, 0, 0, 0.2, 0]
# # # colors =['#008fd5','#fc4f30','#e5ae37','#6d904f','#f23456','#f4324v4']
# # # plt.pie(slices[0:5],labels=labels[0:5],colors =colors,wedgeprops={'edgecolor':'black'},shadow =True,startangle=90,
# # #         autopct='%1.1f%%',
# # #         explode=explode)
# # # plt.style.use('fivethirtyeight')
# # # plt.title("MyAwesomeChart")
# # # plt.tight_layout()
# # # plt.show()
# #
# #
# # # to create pie chart we simple input plt.pie and then we specify the values we want to show
# # # as labels we input the labels for the data we wanted to put into the chart
# # # we can color our slices by adding the parameter "colors"
# # # we can also add wedgeprops where we have to specify in the dictionary what we want to present
# # # as an example it could be edgecolor that will change the color of eages for every piece of the caek
# # # so wedgeprops= {'edgecolor':'black'}
# # # we can add shadow to our graph by writing shadow=True,
# # # we can rotate our chart by saying startangle=and here we are specifying how we would like to rotate the chart
# # # chart is read counter clockwise
# # # we can put separately some piece of the cake by saying explode = and passing the list of values for each piece of cake
# # # typing in 0.1 will mean that 0.1 of the radius is the separation for the pie part to go from the center
# # # autopct= means that we can specify the format for the ticks in the pie chart,
# # # inputting '%1.1%% will mena that we can end up with values formatted like 25.5 %
# # #
# # # # o create a pie chart you simple put plt.pie() and inside this method you pass value you would like o share so i.e.
# # # hours = [50,12,6]
# # #
# # # # then you have to specify labels
# # # users = ['Maciej','Karol','Monika']
# # #
# # # # you can indicate the values that will "explode" from the graph which means they will be separated from the circle
# # # # by a part of the radius you indicate
# # # explosion =[0.2,0,0]
# # # # you can specify colors for each part of he graph in hex values
# # # hexagon =['#008fd5','#fc4f30','#e5ae37']
# # #
# # # # and now we can plot the chart having all necessary values so...
# # # # autopct is a property that allows to specify how we would like to present the value on pie chart (ticks)
# # # plt.pie(hours,labels=users,explode=explosion,colors=hexagon,autopct='%1.2f',shadow = True,startangle=90,
# # #         )
# # # plt.style.use('ggplot')
# # # plt.title("Hours spent on facebook by each worker")
# # # plt.tight_layout()
# # # plt.show()
# #
# #
# # # # Language Popularity
# # # slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# # # labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# # #
# # # plt.style.use('fivethirtyeight')
# # # explode =[0,0,0,0.2,0]
# # #
# # # plt.pie(slices[0:5], labels=labels[0:5], wedgeprops={'edgecolor':'black'},explode=explode,shadow=True,startangle=90,
# # #         autopct="%1.2f%%")
# # # plt.title('My awesome pie')
# # # plt.tight_layout()
# # # plt.show()
# # # import numpy as np
# # # import random
# # # x = [random.randint(1,100) for x in range(6)]
# # # y = [10,12,14,16,18,20]
# # # y2 = [15,20,25,30,35,40]
# # # y3 = [10,20,30,40,50,60]
# # # x_indexes = np.arange(len(x))
# # # width = 0.25
# # # plt.style.use("seaborn-dark")
# # # plt.bar(x_indexes - 0.25,y,width=width,label='Rise by 2',color='#444444')
# # # plt.bar(x_indexes,y2,width=width, label='Rise by 5')
# # # plt.bar(x_indexes + 0.25,y3,width=width,label= 'Rise by 10')
# # # plt.xticks(x_indexes,x)
# # # plt.legend()
# # # plt.tight_layout()
# #
# # # so i can either put labels in plot method to have legend
# # # or i can declare legend in .legend() by sending there list of values for legend
# #
# # # to check the available styles i have to write plt.style.available
# # # to save figure to file i should write. plt.savefig() and in parenthesis i should input directory
# #
# #
# # # plt.show()
# #
# # # import csv
# # # import os
# # # import numpy as np
# # # from collections import Counter
# # #
# # # filename = os.environ['HOMEPATH'] + r'\Desktop\data.csv'
# # # print(filename)
# # #
# # # with open(filename) as csv_file:
# # #     lang = Counter()
# # #     csv_reader = csv.DictReader(csv_file)
# # #     for x in csv_reader:
# # #         lang.update(x['LanguagesWorkedWith'].split(';'))
# # # language, popularity = map(list,zip(*lang.most_common(10)))
# # # print(lang.most_common(10))
# # # print(language)
# # # print(popularity)
# # #
# # # language.reverse()
# # # popularity.reverse()
# # # k = np.asarray(popularity)
# # # condition = [k<20000,k>20000]
# # # choices = ['Blue','Green']
# # #
# # # x = np.select(condition,choices)
# # # x  =list(x)
# # # plt.barh(language,popularity,color=x)
# # # plt.xlabel('Number of users knowing language')
# # # plt.title('Division for language knowledge')
# # # plt.tight_layout()
# # # plt.show()
# #
# # #
# # # slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# # # labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# # # explode =[0,0,0.3,0,0]
# # # plt.style.use('ggplot'
# # # )
# # # plt.pie(slices[0:5],labels=labels[0:5],wedgeprops={'edgecolor':'black'},explode=explode,shadow=True,
# # #         startangle=90,autopct='%1.1f%%')
# # # plt.title('Awesome chart')
# # # plt.tight_layout()
# # # plt.show()
# #
# #
# # import os
# # import pandas as pd
# #
# # filename = os.environ['HOMEPATH'] + r'\Desktop\newdata.csv'
# #
# # # data = pd.read_csv(filename)
# # #
# # # age = data['Age']
# # # dev_salaries = data['All_Devs']
# # # py_salaries = data['Python']
# # # js_salaries = data['JavaScript']
# #
# # # overall_median = 54000
# # # plt.plot(age,dev_salaries,color='#444444',linestyle='--',label='All-Devs')
# # # plt.plot(age,py_salaries,label='Python')
# # #
# # # plt.fill_between(age,py_salaries,dev_salaries,
# # #                  where=(py_salaries>dev_salaries),
# # #                  interpolate=True,color='blue', alpha=0.3,label='Python salary bigger than all developers')
# # #
# # # plt.fill_between(age,py_salaries,dev_salaries,
# # #                  where=(py_salaries<=dev_salaries),
# # #                  interpolate=True,color='red', alpha=0.3,label= 'Phon salary lower han all developers')
# # #
# # #
# # #
# # # plt.legend()
# # # plt.title('Salaries by Age')
# # # plt.xlabel('Ages')
# # # plt.ylabel('Median Salaries in USD')
# # # plt.tight_layout()
# # # plt.show()
# #
# # filename = os.environ['HOMEPATH'] + r'\Desktop\responder.csv'
# #
# # # data = pd.read_csv(filename)
# # # m_age = 29
# # # color = 'green'
# # # ids = data['Responder_id']
# # # ages = data['Age']
# # # plt.style.use('fivethirtyeight')
# # # # ages = [18,19,21,25,26,26,30,32,38,45,55]
# # # bins=[10,20,30,40,50,60,70,80,90,100]
# # # plt.hist(ages,bins=bins,edgecolor='black',log=True)
# # #
# # # plt.axvline(m_age,color=color, label='age median')
# # # plt.title('Age of respondents')
# # # plt.xlabel('Ages')
# # # # plt.ylabel('Total respondents')
# # # #
# # # # plt.tight_layout()
# # # # plt.show()
# # #
# # # plt.style.use('seaborn')
# # #
# # # x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# # # y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# # #
# # #
# # # # colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# # #
# # # # sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
# # # #          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
# # #
# # # # data = pd.read_csv('2019-05-31-data.csv')
# # # # view_count = data['view_count']
# # # # likes = data['likes']
# # # # ratio = data['ratio']
# # #
# # # # plt.title('Trending YouTube Videos')
# # # # plt.xlabel('View Count')
# # # # plt.ylabel('Total Likes')
# # #
# # # plt.tight_layout()
# # #
# # # plt.show()
# #
# # #
# # # import pandas as pd
# # # from matplotlib import pyplot as plt
# # # import os
# # #
# # #
# # # plt.style.use('seaborn')
# # # file_naming = os.environ['HOMEPATH'] + r"\Desktop\viewers.csv"
# # # print(file_naming)
# # # data = pd.read_csv(file_naming)
# # #
# # # print(data.head())
# # # view_count = data['view_count']
# # # likes = data['likes']
# # # ratio = data['ratio']
# # #
# # #
# # # x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# # # y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# # #
# # # colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# # #
# # # sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
# # #          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
# # #
# # # # data = pd.read_csv('2019-05-31-data.csv')
# # # # view_count = data['view_count']
# # # # likes = data['likes']
# # # # ratio = data['ratio']
# # #
# # # # plt.title('Trending YouTube Videos')
# # # # plt.xlabel('View Count')
# # # # plt.ylabel('Total Likes')
# # #
# # # plt.scatter(view_count, likes,c =ratio,cmap='summer', edgecolor='black',
# # #             linewidth=1)
# # #
# # # cbar = plt.colorbar()
# # #
# # # cbar.set_label('Like/Dislike ratio')
# # #
# # # plt.xscale('log')
# # # plt.yscale('log')
# # # # plt.tight_layout()
# # # #
# # # # plt.show()
# # #
# # #
# # #
# # # import pandas as pd
# # # from datetime import datetime,timedelta
# # # from matplotlib import pyplot as plt
# # # from matplotlib import dates as mpl_dates
# # import os
# #
# # f_name = os.environ['HOMEPATH'] + r'\Desktop\generator.csv'
# # #
# # #
# # # data = pd.read_csv(f_name)
# # #
# # # price_date = data['Date']
# # # data['Date']=pd.to_datetime(data['Date'])
# # # data.sort("Date",inplace=True)
# # # price_close = data['Close']
# # #
# # # plt.plot_date(price_date,price_close,linestyle='solid')
# # #
# # # plt.gcf().autofmt_xdate()
# # # plt.title('Bitcoin Prices')
# # # plt.xlabel('Dates')
# # # plt.ylabel('Closing price')
# # #
# # # plt.style.use('seaborn')
# # #
# # #
# # # plt.tight_layout()
# # # plt.show()
# # #
# # #
# # # import random
# # # from itertools import count
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # from matplotlib.animation import FuncAnimation
# # #
# # # plt.style.use('fivethirtyeight')
# # #
# # # x_values = []
# # # y_values = []
# # #
# # # index = count()
# # #
# # #
# # # def animate(i):
# # #     '''function that will animate the graph'''
# # #     x_values.append(next(index))
# # #     y_values.append(random.randint(0,5))
# # #
# # # ani = FuncAnimation()
# # #
# # #
# # #
# # #
# # #
# # # plt.tight_layout()
# # # plt.show()
# #
# # # import csv
# # # import random
# # # import time
# # #
# # # x_value =0
# # # total_1= 1000
# # # total_2 = 1000
# # #
# # # fieldnames = ['x_value','total_1','total_2']
# # #
# # # with open(f_name,'w') as csv_file:
# # #     csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
# # #     csv_writer.writeheader()
# # #
# # # while True:
# # #
# # #     with open(f_name,'a') as csv_file:
# # #         csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
# # #         info ={'x_value':x_value,
# # #                'total_1':total_1,
# # #                'total_2':total_2}
# # #
# # #         csv_writer.writerow(info)
# # #
# # #         x_value+=1
# # #         total_1 = total_1 + random.randint(0,5)
# # #         total_2 = total_2 + random.randint(0,5)
# # #
# # #     time.sleep(1)
# # #
# # import pandas as pd
# # from matplotlib import pyplot as plt
# # import os
# #
# # naming_file = os.environ['HOMEPATH']+r'\Desktop\data.csv'
# #
# # plt.style.use('seaborn')
# #
# # data = pd.read_csv(naming_file)
# # age = data['Age']
# # dev_salaries = data['All_Devs']
# # p_salaries =data['Python']
# # js_salaries= data['JavaScript']
# #
# # fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)
# # ax2.plot(age,p_salaries,label='Python')
# # ax2.plot(age,js_salaries,label='Java Script')
# # ax1.plot(age,dev_salaries,color='#444444',
# #          linestyle="--",
# #          label='All Devs')
# #
# #
# # ax1.legend()
# # ax1.set_title('Median salary for devs in USD by age')
# #
# # ax1.set_ylabel("Median salary ini USD")
# #
# #
# # ax2.legend()
# # ax2.set_xlabel('Ages')
# # ax2.set_ylabel("Median salary ini USD")
# # plt.tight_layout()
# # plt.show()
# # importing matplotlib
# from matplotlib import pyplot as plt
# import numpy as np
# #setting up the values for graph
# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# y2 = [2,3,4,5,6]
# y3 = [1,2,3,2,1]
#
# # # plotting graph
# # # we can add markers to that, linestyle or color
# # plt.plot(x,y, color='Blue',linestyle='--',marker='o',linewidth=4)
# #
# # # adding labels and title
# # plt.title('Progress in python')
# # plt.xlabel("Months")
# # plt.ylabel("Numbmer of achievements")
# #
# # # we can put in a tight way the graph into window by
# # plt.tight_layout()
# #
# # # we can add grid if we would like to see the values more precisely
# # plt.grid()
# #
# # print(plt.style.available)
# #
# # # showing graph in separate window
# # plt.show()
# # width = 0.25
# # indexing = np.arange(len(x))
# # plt.bar(indexing - width,y,width=width)
# # plt.bar(indexing,y2,width=width)
# # plt.bar(indexing +width,y3,width=width)
# #
# # ticking = ['Maciej','Karol','Monika','Zygmunt','Pawel']
# #
# # plt.xticks(ticks=indexing,labels=ticking)
# #
# # plt.show()
#
# # yy1 = [12,10,14,15,20]
# # yy2 = [12,23,12,14,16]
# # yy3 = [11,12,22,18,19]
# #
# # users = ['Maciej','Karol','Monika','Kamil','Zygmunt']
# # width = 0.25
# #
# # indexing = np.arange(len(x))
# # plt.bar(indexing-width,yy1, width=width)
# # plt.bar(indexing,yy2,width=width)
# # plt.bar(indexing+width,yy3,width=width)
# #
# # plt.xticks(np.arange(min(x), max(x)+1, 0.5))
# #
# # plt.show()
#
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# childs = [20,20,24,25,26]
#
# x = np.arange(len(labels))  # the label locations
# width = 0.25  # the width of the bars
#
# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width, men_means, width, label='Men')
# rects2 = ax.bar(x, women_means, width, label='Women')
# rects3 = ax.bar(x + width, childs, width, label='childs')
#
# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()
#
#
# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#
#
# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
#
# fig.tight_layout()
#
# plt.show()

from matplotlib import pyplot as plt

# creating pie chart

x  = [10,20,30,40,50]
explosion = [0,0,0,0,0.3]


# adding labels
# i also added edge colors and linewidth for the line
#plt.pie(x,labels=['Inactive','Active'],wedgeprops={'edgecolor':'pink','linewidth':5})
# i can also pass colors to pie chart
# so pie is charting its plot at 3 but when we pass startangle 90 it will start at 12
# we can also add precentage to the labels
#plt.pie(x,explode = explosion,startangle=90,autopct='%1.1f%%')
# plt.show()

t1 = [1,2,3,4,5]
t2  = [2,3,4,5,6]
t3 = [3,4,5,6,7]

plt.stackplot(x,t1,t2,t3)

# legand has to arguments - list of labels and location
# passing a list will enable us to assign proper labels
# loc is allowng us to send the location of the legend
plt.legend(['t1','t2','t3'],loc='upper left')


plt.show()
