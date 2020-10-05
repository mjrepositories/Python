import tkinter as tk
from tkinter import messagebox
#Tworze okno analogowe

root =tk.Tk()
# Tworze funkcję
def nk():
    pass

mejn = tk.Menu(root)
root.config(menu = mejn)

sub_1 = tk.Menu(mejn,tearoff=0)
mejn.add_cascade(label="File",menu=sub_1)
sub_1.add_command(label='New file',command=nk)
sub_1.add_separator()
sub_1.add_command(label='Save file',command=nk)
sub_1.add_command(label='Export file',command=nk)

sub_2 = tk.Menu(mejn,tearoff=0)
mejn.add_cascade(label='Code',menu=sub_2)
sub_2.add_command(label='Execute code',command=nk)
sub_2.add_command(label='Export code',command=nk)
sub_2.add_separator()
sub_2.add_command(label='Clean code',command=nk)

sub_3 = tk.Menu(mejn,tearoff=0)
mejn.add_cascade(label='Flow',menu=sub_3)
sub_3a = tk.Menu(sub_3,tearoff=0)
sub_3.add_cascade(label='Chart',menu=sub_3a)
sub_3b = tk.Menu(sub_3,tearoff=0)
sub_3.add_cascade(label="Option",menu=sub_3b)
sub_3a.add_command(label="Present chart",command=nk)
sub_3a.add_command(label='Modify chart',command=nk)
sub_3b.add_command(label="Modify settings",command=nk)
sub_3b.add_command(label='Set default',command=nk)


# setting up 4th tab
sub_4 = tk.Menu(mejn,tearoff=0)
mejn.add_cascade(label="Help",menu=sub_4)
sub_4a = tk.Menu(sub_4,tearoff=0)
sub_4.add_cascade(label='HOW',menu=sub_4a)
sub_4a.add_command(label='Request help',command=nk)
sub_4a.add_command(label='FAQ',command=nk)
sub_4a.add_command(label='Add solution',command=nk)





# # i am creating the menu here
# mejn_menu = tk.Menu(root)
# root.config(menu=mejn_menu)
#
#
# sub_1=tk.Menu(mejn_menu,tearoff=0)
# mejn_menu.add_cascade(label='File',menu=sub_1)
# sub_1.add_command(label="open file",command=nk)
# sub_1.add_command(label='save file',command=nk)
# sub_1.add_separator()
# sub_1.add_command(label='transfer file',command=nk)
#
# sub_2=tk.Menu(mejn_menu,tearoff=0)
# mejn_menu.add_cascade(label='Transfer',menu=sub_2)
# sub_2.add_command(label='Check transfer',command=nk)
# sub_2.add_separator()
# sub_2.add_command(label='Cancel transfer',command=nk)
# sub_2.add_command(label='Corrent transfer',command=nk)
#
# sub_3=tk.Menu(mejn_menu,tearoff=0)
# mejn_menu.add_cascade(label="Tools",menu=sub_3)
# sub_3first = tk.Menu(sub_3,tearoff=0)
# sub_3.add_cascade(label="Additional tools",menu=sub_3first)
# sub_3first.add_command(label="Export cutter",command=nk)
# sub_3first.add_command(label="Import cutter",command=nk)
# sub_3.add_separator()
# sub_3.add_command(label='Standard tools',command=nk)
#
# sub_4=tk.Menu(mejn_menu,tearoff=0)
# mejn_menu.add_cascade(label="help",menu=sub_4)
# sub_4.add_command(label="Open help site",command=nk)
# sub_4first = tk.Menu(sub_4,tearoff=0)
# sub_4.add_cascade(label="Tips",menu=sub_4first)
# sub_4first.add_command(label="Show tips and tricks",command=nk)
# sub_4first.add_command(label="Add tip",command=nk)
# sub_4first.add_command(label='Webpage',command=nk)
# sub_4.add_separator()
# sub_4second = tk.Menu(sub_4,tearoff=0)
# sub_4.add_cascade(label="Donation",menu=sub_4second)
# sub_4second.add_command(label="Donate to developer",command=nk)
# sub_4second.add_command(label='Donate to charity',command=nk)
# # # Creating menu
# # Najpierw tworzę ogólne menu
# selection = tk.Menu(root)
# # potem wprowadzam je jakby do programu (że zaczyna on rozumieć hej! Coś dodałeś. Wyświetlę to
# root.config(menu=selection)
#
#
# # Dalej tworzę podmenu dla głównego paska, wprowadzam informację, że należy ono do głównego menu i usuwam pierwszy dziwny wiersz
#
# sub_1=tk.Menu(selection,tearoff=0)
# # Potem muszę pokazać, że chce to wprowadzić (co i pod jaką nazwą
# selection.add_cascade(label="File",menu=sub_1)
#
# # Potem tworzę poszczególne etykiety dla rzeczy, które chciałbym robić z programem
# sub_1.add_command(label="Open file",command=nk)
# sub_1.add_command(label="Save file",command=nk)
#
# #Totaj wprowadzony jest separator, żeby nie było wszystko ciurkiem
# sub_1.add_separator()
#
# # I tutaj dodaje ostatnią etykietę
# sub_1.add_command(label="Export file",command=nk)
#
#
# #Tutaj znowu deklaruje, że chce kolejne podmenu w głównym menu
# sub_2 = tk.Menu(selection,tearoff=0)
#
# # Tu wprowadzam informację jak się to powinno nazywać w menu i co ma być dodane (wcześniej utworzony katalog)
# selection.add_cascade(label="Edit",menu=sub_2)
# # Tutaj dodaję poszczególne etykiety, jakie mają się pojawić po rozwinięciu
# sub_2.add_command(label="Edit file",command=nk)
# sub_2.add_command(label="Edit scrypt",command=nk)
# sub_2.add_command(label="Edit graph",command=nk)
#
# # Dodaję separator, żeby nie było wszystko ciurkiem
# sub_2.add_separator()
#
# # I na końcu dodaję ostatnią zakładkę
# sub_2.add_command(label="Edit screenshot",command=nk)
#
#
# # Tutaj znowu deklaruję, że chce dodać kolejne menu
# sub_3 = tk.Menu(selection, tearoff=0)
# # Tutaj wpisuję, żeby główne menu dodało ją do siebie
# selection.add_cascade(label="Window",menu=sub_3)
#
# # I tworzę dla tegu menu jedna zakładkę
# sub_3.add_command(label="Maximize",command=nk)
#
#
# # Tutaj znow deklaruję, że ma się pojawić kolejna zakładka
# sub_4 = tk.Menu(selection,tearoff=0)
# # I że ma być dodana do głównego menu
# selection.add_cascade(label='Help',menu=sub_4)
# # Po czym tworzę teraz zakładki w zakładce (podmenu)
# under_1=tk.Menu(sub_4,tearoff=0)
# # I jak zadeklakrowałem to podmenu to wstawiam jest do to pierwszego elementu kolejnej zakładki
# sub_4.add_cascade(label="Issue list",menu=under_1)
# #Tworzę pierwszą podzakładkę  zakładki
# under_1.add_command(label="Python crashes",command=nk)
# # Tworzę drugą podzakładkę zakładki
# under_1.add_command(label='Interpreter failure',command=nk)
# # Tworzę trzecią podzakładkę zakładki
# under_1.add_command(label="Files partially open",command=nk)
#
# # I tutaj tworzę drugą zakładkę w 4 zakłace z głównego menu (po zrobieniu tych podzakładek dla tej pierwszej)
# sub_4.add_command(label='FAQ',command=nk)

# root=tk.Tk()
# #Tworzę menu
# def nk():
#     pass
# selection=tk.Menu(root)
# root.config(menu=selection)
#
# submenu_1=tk.Menu(selection,tearoff=0)
# mniejsze= tk.Menu(submenu_1,tearoff=0)
# submenu_1.add_cascade(label='try',menu=mniejsze)
# mniejsze.add_command(label='success',command=nk)
# selection.add_cascade(label="File",menu=submenu_1)
# submenu_1.add_command(label="Open file",command=nk)
# submenu_1.add_command(label='Save file',command=nk)
# submenu_1.add_separator()
# submenu_1.add_command(label='Export file',command=nk)
#
# submenu_2=tk.Menu(selection,tearoff=0)
# selection.add_cascade(label='Project',menu=submenu_2)
# submenu_2.add_command(label='New project',command=nk)
# submenu_2.add_separator()
# submenu_2.add_command(label='Load Project',command=nk)
#
# #3 menu
# submenu_3=tk.Menu(selection,tearoff=0)
# selection.add_cascade(label="Toolbox",menu=submenu_3)
# submenu_3.add_command(label='Open toolbox',command=nk)
# submenu_3.add_command(label="Modify toolbox",command=nk)
# submenu_3.add_command(label="Select toolbox",command=nk)
# submenu_3.add_separator()
# submenu_3.add_command(label='Delete toolbox',command=nk)
#
#
# #4 menu
# submenu_4=tk.Menu(selection,tearoff=0)
# selection.add_cascade(label="Help",menu=submenu_4)
# submenu_4.add_command(label='Open help',command=nk)
# submenu_4.add_command(label='Export help',command=nk)
# submenu_4.add_command(label="Import help",command=nk)
# submenu_4.add_command(label="Go to website",command=nk)
# pickup = tk.Menu(root)
# root.config(menu=pickup)
#
# submenu = tk.Menu(pickup,tearoff=0)
# pickup.add_cascade(label='File',menu=submenu)
# submenu.add_command(label='Load file',command=donothing)
# submenu.add_cascade(label='Load project',command=donothing)
# submenu.add_separator()
# submenu.add_cascade(label="Load..",command=donothing)
#
#
# editmenu =tk.Menu(pickup,tearoff=0)
# pickup.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label='Edit file',command=donothing)
# editmenu.add_separator()
# editmenu.add_command(label="Edit project",command=donothing)
#
# searchmenu=tk.Menu(pickup,tearoff=0)
# pickup.add_cascade(label='search',menu=searchmenu)
# searchmenu.add_command(label="Search file",command=donothing)
# searchmenu.add_separator()
# searchmenu.add_command(label="Search project",command=donothing)
#
# toolsmenu=tk.Menu(pickup,tearoff=0)
# pickup.add_cascade(label='tools',menu=toolsmenu)
# toolsmenu.add_command(label='open toolbar',command=donothing)
# toolsmenu.add_command(label='widgets',command=donothing)
# toolsmenu.add_separator()
# toolsmenu.add_command(label="modify toolbox",command=donothing)
#
#
# helpmenu = tk.Menu(pickup,tearoff=0)
# pickup.add_cascade(label="Help",menu=helpmenu)
# helpmenu.add_command(label='Open help file',command=donothing)
# helpmenu.add_command(label="Add to help",command=donothing)
# helpmenu.add_separator()
# helpmenu.add_command(label='Ask IT',command=donothing)
#

# menuing= tk.Menu(root)
# submenu = tk.Menu(menuing,tearoff=0)
# menuing.add_cascade(label="File",menu=submenu)
# submenu.add_command(label="New project",command=donothing)
# submenu.add_command(labe='New file',command=donothing)
# submenu.add_separator()
# submenu.add_command(label='exit',command=donothing)
#
# editmenu = tk.Menu(menuing,tearoff=0)
# menuing.add_cascade(label="Edit",menu=editmenu)
# editmenu.add_command(label="Edit project",command=donothing)
# editmenu.add_command(labe='Edit file',command=donothing)
# editmenu.add_separator()
# editmenu.add_command(label='exit',command=donothing)



# label_1= tk.Label(root,text='Name')
# label_2= tk.Label(root,text='password')
#
# input_1=tk.Entry(root)
# input_2=tk.Entry(root)
# label_1.grid(row=0,column=0,sticky="E")
# label_2.grid(row=1,column=0,sticky='E')
# input_1.grid(row=0,column=1)
# input_2.grid(row=1,column=1)
# c = tk.Checkbutton(root,text='Keep me logged in')
# c.grid(columnspan=2)
# label_3=tk.Label(root,text="Maciej co robisz")
# label_3.grid()


# def print_name(event):
#     print('I am printing this sentence')
#
# but1= tk.Button(root,text='print name')
# but1.bind('<Button-1>',print_name)
# but1.pack()
#
# def leftclick(event):
#     print('left click')
#
# def rightclick(event):
#     print('right click')
#
# frame = tk.Frame(root,width=300,height=300)
# frame.bind("<Return>",leftclick)
# frame.bind("<Button-3>",rightclick)
# frame.pack()
root.mainloop()
