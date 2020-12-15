import tkinter  as tk
import os
import datetime



tod_ay = datetime.datetime.today().strftime('%Y-%m-%d')
print(tod_ay)
# initiating window

root = tk.Tk()

# setting up the size of the window
window_height = 730
window_width = 1200

# getting data on size of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# creating x and y cordinates
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

# locating the window on the screen with proper size
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

print(screen_height)
print(screen_width)


background_image =tk.PhotoImage(file=r"C:\Users\Maciek\Downloads\bat.png")
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


# Placing labels for each mode of transport
tk.Label(text='LCL',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.05,rely=0.05)
tk.Label(text='FCL',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.20,rely=0.05)
tk.Label(text='AIR',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.35,rely=0.05)
tk.Label(text='US ROAD',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.45,rely=0.05)
tk.Label(text='EU ROAD',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.6,rely=0.05)
tk.Label(text='SRC',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.75,rely=0.05)
tk.Label(text='MATC',fg='White',bg='Black',font=('Calibri',20,'bold')).place(relx=0.85,rely=0.05)

def infodis():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates')

def lcl_rates_func():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\LCL\DB Schenker\upload files')

def lcl_request():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\LCL\DB Schenker\LCL new lane request\LCL new rate request.xlsx')

def fcl_rates_func():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Sea\FCL upload files')

def alloction_fcl():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Sea\allocation file')

def air_rates_func():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Air')

def mps():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Air\MPS')

def dbs():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Air\DB Schenker\Uploads')

def expeditors():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Air\Expeditors\Rates')


def src_folder():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\SRC')

def matc_folder():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\MATC')


def road_folder_func():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Road\US')

def road_folder_eu_func():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Road')

def tracking():
    os.startfile(r'C:\Users\310295192\Desktop\VBA projects\Action Tracker v.4.xlsm')

def contact_person():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Contact lists  (infodis)\key_users_overview_file.xlsx')

def open_dashboard_func():
    os.startfile(r'C:\Users\310295192\Desktop\Work\Rates\Dashboard\rates dashboard {}.xlsx'.format(tod_ay))

def closing():
    root.destroy()

# creating the tile of the game
root.title("Infodis Rates Manager")

# LCL
lcl_rates = tk.Button(text='LCL rates',command=lcl_rates_func,fg='White',bg='Black',font=('Calibri',12,'bold'))
lcl_rates_request = tk.Button(text='LCL rates request',command=lcl_request,fg='White',bg='Black',font=('Calibri',12,'bold'))


# FCL
fcl_rates = tk.Button(text='FCL rates',command=fcl_rates_func,fg='White',bg='Black',font=('Calibri',12,'bold'))


fcl_allocation = tk.Button(text='BOSS FCL',command=alloction_fcl,fg='White',bg='Black',font=('Calibri',12,'bold'))


# AIR
air_rates = tk.Button(text='AIR rates',command=air_rates_func,fg='White',bg='Black',font=('Calibri',12,'bold'))

mps_file =  tk.Button(text='MPS',command=mps,fg='White',bg='Black',font=('Calibri',12,'bold'))

exp_rates =  tk.Button(text='Expeditors',command=expeditors,fg='White',bg='Black',font=('Calibri',12,'bold'))

db_rates =  tk.Button(text='DB Schenker',command=dbs,fg='White',bg='Black',font=('Calibri',12,'bold'))

# SRC

src_rates = tk.Button(text='SRC Folder',command=src_folder,fg='White',bg='Black',font=('Calibri',12,'bold'))


#MATC

matc_rates = tk.Button(text='MATC Folder',command=matc_folder,fg='White',bg='Black',font=('Calibri',12,'bold'))


# ROAD
road_folder = tk.Button(text='US Road Folder',command=road_folder_func,fg='White',bg='Black',font=('Calibri',12,'bold'))

road_folder_eu = tk.Button(text='EU Road Folder',command=road_folder_func,fg='White',bg='Black',font=('Calibri',12,'bold'))


# FUNCTIONAL BUTTONS

# tracker
tracker  = tk.Button(text='Open Tracker',command=tracking,fg='White',bg='Black',font=('Calibri',20,'bold'))


# dashboard
open_dashboard = tk.Button(text='Open Dashboard',command=open_dashboard_func,fg='White',bg='Black',font=('Calibri',18,'bold'))

# contact people

contact_people = tk.Button(text='Key Users Address Book',command=contact_person,fg='White',bg='Black',font=('Calibri',14,'bold'))

# infodis folder
infodis_folder = tk.Button(text='Infodis Rates',command=infodis,fg='White',bg='Black',font=('Calibri',14,'bold'))


# closing manager
closing_manager = tk.Button(text='Close Manager',command=closing,fg='White',bg='Black',font=('Calibri',20,'bold'))


lcl_rates.place(relx=0.05,rely=0.15)
lcl_rates_request.place(relx=0.05,rely=0.25)


fcl_rates.place(relx=0.2,rely=0.15)
fcl_allocation.place(relx=0.2,rely=0.25)


air_rates.place(relx=0.35,rely=0.15)
mps_file.place(relx=0.35,rely=0.25)
exp_rates.place(relx=0.35,rely=0.35)
db_rates.place(relx=0.35,rely=0.45)

road_folder.place(relx=0.45,rely=0.15)
road_folder_eu.place(relx=0.6,rely=0.15)

src_rates.place(relx=0.75,rely=0.15)

matc_rates.place(relx=0.85,rely=0.15)


open_dashboard.place(relx=0.42,rely=0.80)

contact_people.place(relx=0.415,rely=0.90)

closing_manager.place(relx=0.8,rely=0.85)

infodis_folder.place(relx=0.45,rely=0.73)

tracker.place(relx=0.05,rely=0.85)


# creating an infinate loop

root.mainloop()

