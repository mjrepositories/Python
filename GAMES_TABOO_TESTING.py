import tkinter  as tk
import tkinter.messagebox as mb
import time
import pandas as pd
import random

sec= 60
mac = 0
# import taboo wordpedia
taboo = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Taboo\taboo_wordpedia.xlsx')
# set number of words
rows = taboo.shape[0]-1

team_num=0

# initiating window

root = tk.Tk()


# creating the tile of the game
root.title("Taboo game")

# setting up the size of the window
window_height = 830
window_width = 1100

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


background_image =tk.PhotoImage(file=r'C:\Users\310295192\Desktop\Taboo1.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)


tk.Label(text='Testujemy',fg='White',bg='#312587',font=('Calibri',20,'bold'),relief='raised'
          ).pack()

# mycanvas = tk.Canvas(root, width = 200, height = 25)
# mycanvas.create_rectangle(0, 0, 100, 40, fill = "green")
# mycanvas.pack(side = "top", fill = "both", expand = True)
#
# text_canvas = mycanvas.create_text(10, 10, anchor = "nw")
# mycanvas.itemconfig(text_canvas, text="Look no background! Thats new!")
# def select_new_word():
#     global word_to_guess
#     global hint_1
#     global hint_2
#     global hint_3
#     global hint_4
#     global hint_5
#     global hint_6
#     global mac
#
#
#     # list of indices that are not solved
#     for_guessing = taboo[taboo.solved.isna()].index.to_list()
#     # selecting random value from available words
#     selected = random.choice(for_guessing)
#     # assigning clues
#     guess_what = taboo.loc[selected, 'key']
#     word_1 = taboo.loc[selected, 'word_1']
#     word_2 = taboo.loc[selected, 'word_2']
#     word_3 = taboo.loc[selected, 'word_3']
#     word_4 = taboo.loc[selected, 'word_4']
#     word_5 = taboo.loc[selected, 'word_5']
#     word_6 = taboo.loc[selected, 'word_6']
#     print(mac)
#
#     if mac > 0:
#         word_to_guess.config(text=guess_what)
#         hint_1.config(text=word_1)
#         hint_2.config(text=word_2)
#         hint_3.config(text=word_3)
#         hint_4.config(text=word_4)
#         hint_5.config(text=word_5)
#         hint_6.config(text=word_6)
#
#
#
#
#     if mac == 0:
#         word_to_guess = tk.Label(text=guess_what)
#         hint_1 = tk.Label(text=word_1)
#         hint_2 = tk.Label(text=word_2)
#         hint_3 = tk.Label(text=word_3)
#         hint_4 = tk.Label(text=word_4)
#         hint_5 = tk.Label(text=word_5)
#         hint_6 = tk.Label(text=word_6)
#
#         word_to_guess.place(relx=0.85,rely=0.1)
#         hint_1.place(relx=0.85,rely=0.14)
#         hint_2.place(relx=0.85,rely=0.18)
#         hint_3.place(relx=0.85,rely=0.22)
#         hint_4.place(relx=0.85,rely=0.26)
#         hint_5.place(relx=0.85,rely=0.30)
#         hint_6.place(relx=0.85,rely=0.34)
#         mac = mac + 1
#
#         def tick():
#             global sec
#             sec -= 1
#             time['text'] = sec
#             # Take advantage of the after method of the Label
#             time.after(1000, tick)
#
#         time = tk.Label(root, fg='green')
#         time.pack()
#         button_for_clock = tk.Button(root, fg='blue', text='Start', command=tick())
#
#
#
# # Button fo ending the game
# end_game = tk.Button(text='Next word',command=select_new_word)
#
# # placing the buttons and labels
# end_game.place(relx=0.5,rely=0.1)
tk.mainloop()