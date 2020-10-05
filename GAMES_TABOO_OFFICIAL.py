import tkinter  as tk
import tkinter.messagebox as mb
import time
import pandas as pd
import string
import random
sec= 60
mac= 0

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

# # creating frame for widgets
# frame = tk.Frame(root,bg='blue')
# frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

def help_window():
   mb.showinfo('Pomoc', "Taboo to gra polegajaca na odgadywania opisywanych slow\n\n"
                        "1. Maksymalnie grac moga 4 druzyny\n\n"
                      "2. Gra wybiera losowo druzyne zgadujaca i opisujaca\n\n"
                       "3. Kazda runda trwa 60 sekund\n\n"
                        "4. Druzyna opisujaca przedstawia kazde slow\n"
                        "nie korzystajac ze slow wyswietlanych na ekranie\n\n"
                        'Zadaniem druzyny przeciwnej jest odgadniecie\n'
                        'jak najwiekszej liczby slow przedstawianych\n\n'
                       "5. Po kazdej rundzie pokazywany jest aktualny ranking\n\n"
                       "6. Dryzyny maja 10 sekund po kliknieciu 'Nastepna runda'\n\n"
                        "7. Gre mozna zakonczyc w kazdym momencie\n\n"
                        "8. Wygrywa ta druzyna, ktora odganie najwiecej slow")


def on_button_declare():
    # declaring global variables
    global team_num
    global closing_game
    global sec_for_round
    global describing
    global guessing
    global already_guessed

    # checking the number of teams declared by user
    team_num = int(declaration.get())
    print(int(team_num))

    # if the value is above 0 - then all widgets are gone
    if team_num>0:
        declaration.destroy()
        welcoming.destroy()
        declaration.destroy()
        helping.destroy()
        accepteam.destroy()

    # creating list of teams
    list_of_teams = list(string.ascii_uppercase)[:team_num]



    # new widgets are placed
    team_which_guess.place(relx=0.05,rely=0.1)
    team_which_describe.place(relx=0.85,rely=0.1)
    time_to_play.place(relx=0.4,rely=0.95)

    # function to start counting down till start of the game
    def tick_round():
        # declaring global variable for couting down
        global sec_for_round
        global mac
        # each time counting down by one
        sec_for_round -= 1
        # updating the widget with value that was decreased by couting down
        time_for_round['text'] = sec_for_round
        # Take advantage of the after method of the Label
        time_for_round.after(1000, tick_round)
        time_till_round = int(time_for_round.cget("text"))
        if time_till_round < 0:
            team_which_guess.destroy()
            team_which_describe.destroy()
            time_to_play.destroy()
            time_for_round.destroy()

            # list of indices that are not solved
            for_guessing = taboo[taboo.solved.isna()].index.to_list()
            # selecting random value from available words
            selected = random.choice(for_guessing)
            # assigning clues
            guess_what = taboo.loc[selected, 'key']
            word_1 = taboo.loc[selected, 'word_1']
            word_2 = taboo.loc[selected, 'word_2']
            word_3 = taboo.loc[selected, 'word_3']
            word_4 = taboo.loc[selected, 'word_4']
            word_5 = taboo.loc[selected, 'word_5']
            word_6 = taboo.loc[selected, 'word_6']

            word_to_guess = tk.Label(text=guess_what)
            hint_1 = tk.Label(text=word_1)
            hint_2 = tk.Label(text=word_2)
            hint_3 = tk.Label(text=word_3)
            hint_4 = tk.Label(text=word_4)
            hint_5 = tk.Label(text=word_5)
            hint_6 = tk.Label(text=word_6)

            word_to_guess.place(relx=0.85, rely=0.1)
            hint_1.place(relx=0.85, rely=0.14)
            hint_2.place(relx=0.85, rely=0.18)
            hint_3.place(relx=0.85, rely=0.22)
            hint_4.place(relx=0.85, rely=0.26)
            hint_5.place(relx=0.85, rely=0.30)
            hint_6.place(relx=0.85, rely=0.34)
            mac = mac + 1



            def select_new_word():
                global word_to_guess
                global hint_1
                global hint_2
                global hint_3
                global hint_4
                global hint_5
                global hint_6
                global mac

                # list of indices that are not solved
                for_guessing = taboo[taboo.solved.isna()].index.to_list()
                # selecting random value from available words
                selected = random.choice(for_guessing)
                # assigning clues
                guess_what = taboo.loc[selected, 'key']
                word_1 = taboo.loc[selected, 'word_1']
                word_2 = taboo.loc[selected, 'word_2']
                word_3 = taboo.loc[selected, 'word_3']
                word_4 = taboo.loc[selected, 'word_4']
                word_5 = taboo.loc[selected, 'word_5']
                word_6 = taboo.loc[selected, 'word_6']
                print(mac)
                print('tu jestem')
                print(guess_what)
                if mac > 0:


                    word_to_guess = tk.Label(text=guess_what)
                    hint_1 = tk.Label(text=word_1)
                    hint_2 = tk.Label(text=word_2)
                    hint_3 = tk.Label(text=word_3)
                    hint_4 = tk.Label(text=word_4)
                    hint_5 = tk.Label(text=word_5)
                    hint_6 = tk.Label(text=word_6)

                    word_to_guess.config(text=guess_what)
                    hint_1.config(text=word_1)
                    hint_2.config(text=word_2)
                    hint_3.config(text=word_3)
                    hint_4.config(text=word_4)
                    hint_5.config(text=word_5)
                    hint_6.config(text=word_6)
                    mac = mac + 1

                    word_to_guess.place(relx=0.85, rely=0.1)
                    hint_1.place(relx=0.85, rely=0.14)
                    hint_2.place(relx=0.85, rely=0.18)
                    hint_3.place(relx=0.85, rely=0.22)
                    hint_4.place(relx=0.85, rely=0.26)
                    hint_5.place(relx=0.85, rely=0.30)
                    hint_6.place(relx=0.85, rely=0.34)




                if mac == 0:
                    word_to_guess = tk.Label(text=guess_what)
                    hint_1 = tk.Label(text=word_1)
                    hint_2 = tk.Label(text=word_2)
                    hint_3 = tk.Label(text=word_3)
                    hint_4 = tk.Label(text=word_4)
                    hint_5 = tk.Label(text=word_5)
                    hint_6 = tk.Label(text=word_6)

                    word_to_guess.place(relx=0.85, rely=0.1)
                    hint_1.place(relx=0.85, rely=0.14)
                    hint_2.place(relx=0.85, rely=0.18)
                    hint_3.place(relx=0.85, rely=0.22)
                    hint_4.place(relx=0.85, rely=0.26)
                    hint_5.place(relx=0.85, rely=0.30)
                    hint_6.place(relx=0.85, rely=0.34)
                    mac = mac + 1

            def tick():
                global sec
                sec -= 1
                time['text'] = sec
                # Take advantage of the after method of the Label
                time.after(1000, tick)

            time = tk.Label(root, fg='green')
            time.pack()
            button_for_clock = tk.Button(root, fg='blue', text='Start', command=tick())

            # Button for next word
            next_word = tk.Button(text='Nastepne', command=select_new_word)

            # placing the buttons and labels
            next_word.place(relx=0.5, rely=0.1)

    # set up the time that we have for the round
    sec_for_round=10

    # declaring the label for counting down
    time_for_round = tk.Label(root, fg='green')
    # locating the counter
    time_for_round.place(relx=0.5,rely=0.95)
    # creating the trigger for counter
    tk.Button(root, fg='blue', text='Start', command=tick_round())






    # time_till_round = int(time_for_round.cget("text"))
    # print(int(time_till_round))
    # if time_till_round<=0:
    #     team_which_guess.place_forget()
    #     team_which_describe.place_forget()
    #     time_to_play.place_forget()
    #     time_for_round.place_forget()



# welcome label
welcoming = tk.Label(text="Podaj liczbe druzyn:")

# button for declaring participating teams
accepteam = tk.Button(text='Start!',command=on_button_declare)

# help button to show info on game
helping = tk.Button(text='Pomoc',command=help_window)


# entry teams field
declaration = tk.Entry(root,width=2)

# team that guesses label
team_which_guess = tk.Label(text="Zgaduje druzyna A")

# team that describes label

team_which_describe = tk.Label(text="Opisuje druyna B")

# Info about remaining time

time_to_play = tk.Label(text='Start za: ')



# Button for confirming right answer
right_answer = tk.Button(text='Dobrze')

# Label for time that left

time_for_next_round = tk.Label(text='Pozostaly czas: ')

# Button fo ending the game
end_game = tk.Button(text='Zakoncze gre')




# placing the buttons and labels
welcoming.place(relx=0.05,rely=0.45)

declaration.place(relx=0.185,rely=0.45)

accepteam.place(relx=0.05, rely=0.51)

helping.place(relx=0.9,rely=0.9)


#assigning time for round aka countdown

# sec = 60
#
# def tick():
#     global sec
#     sec -= 1
#     time['text'] = sec
#     # Take advantage of the after method of the Label
#     time.after(1000, tick)
#
# time = tk.Label(root, fg='green')
# time.pack()
# tk.Button(root, fg='blue', text='Start', command=tick())







# creating an infinate loop

root.mainloop()
