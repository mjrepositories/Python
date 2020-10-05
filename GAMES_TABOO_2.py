import tkinter  as tk
import tkinter.messagebox as mb
import time
import pandas as pd
import string
import random
sec= 10
mac= 0
sec_for_round = 5
selected = 0
list_of_teams = []
describing = []
guessing = []
already_guessed = []
describe_it = ""
guess_it = ""
ranking = {}


# import taboo wordpedia
taboo = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Taboo\taboo_wordpedia.xlsx',
                      usecols='A:H')
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


background_image =tk.PhotoImage(file=r'C:\Users\310295192\Desktop\Python\Projects\Taboo\Taboo1.png')
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
    global word_to_guess
    global hint_1
    global hint_2
    global hint_3
    global hint_4
    global hint_5
    global hint_6
    global list_of_teams
    global describing
    global guessing
    global already_guessed
    global describe_it
    global guess_it
    global ranking



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

    # assigning dictionary to keep up the track on results
    ranking = {x:0 for x in list_of_teams}

    print(list_of_teams)

    describing = list_of_teams.copy()
    guessing = list_of_teams.copy()
    already_guessed = []

    # if describing list is empty
    print("ROUND")
    if describing == []:
        # populate describing, guessing and already guessed
        describing = list_of_teams.copy()
    # select which team is describing
    describe_it = random.choice(describing)
    # delete team from describing
    describing.remove(describe_it)
    # print describing team and all available teams now
    print(describe_it)
    print(describing)
    # if we have teams for guessing
    if (len(guessing) != 0) and (describe_it in guessing):
        # remove describing team for guessing
        guessing.remove(describe_it)

    if len(guessing) == 0:
        guessing = list_of_teams.copy()
        already_guessed = []
    # select guessing team
    guess_it = random.choice(guessing)
    # enter team that already guessed
    already_guessed.append(guess_it)
    # create list of guessing teams
    guessing = [x for x in list_of_teams if x not in already_guessed]
    print("guessing team " + str(guessing))
    print(guess_it)
    print(guessing)
    print('Team describing is ' + describe_it + " and team guessing is " + guess_it)



    # ABOVE METHODOLOG IS WORKING PROPERLY
    # # describing is empty
    # if describing == []:
    #     # take the whole list of teams
    #     describing = list_of_teams.copy()
    #     guessing = list_of_teams.copy()
    #     # already guessed take as empty
    #     already_guessed = []
    # # pick describing team
    # describe_it = random.choice(describing)
    # # delete describing team from the list
    # describing.remove(describe_it)
    # print(describe_it)
    # print(describing)
    # # if guessing list have value
    # if guessing is True:
    #     # delete entry of describing team from guessing team
    #     guessing.remove(describe_it)
    # # select guessing team
    # guess_it = random.choice(guessing)
    # # add team that is guessing to team that already made it
    # already_guessed.append(guess_it)
    # # filter guessing team - only the ones that were not guessing
    # guessing = [x for x in list_of_teams if x not in already_guessed]
    # print(guess_it)
    # print(guessing)
    # print('Team describing is ' + describe_it + " and team guessing is " + guess_it)








    # new widgets are placed
    team_which_guess.config(text="Zgaduje druzyna " + guess_it)
    team_which_describe.config(text='Opisuje druzyna ' + describe_it)
    team_which_guess.place(relx=0.05,rely=0.1)
    team_which_describe.place(relx=0.75,rely=0.1)
    time_to_play.place(relx=0.4,rely=0.95)

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

    # creating the labels for first time
    word_to_guess = tk.Label(text=guess_what,fg='White',bg='#527a7a',font=('Calibri',20,'bold'))
    hint_1 = tk.Label(text=word_1,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_2 = tk.Label(text=word_2,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_3 = tk.Label(text=word_3,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_4 = tk.Label(text=word_4,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_5 = tk.Label(text=word_5,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_6 = tk.Label(text=word_6,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))


def next_round():
    '''function enables to move to the next round'''
    # declaring global variables
    global team_num
    global word_to_guess
    global hint_1
    global hint_2
    global hint_3
    global hint_4
    global hint_5
    global hint_6
    global list_of_teams
    global describing
    global guessing
    global already_guessed
    global describe_it
    global guess_it
    global ranking
    global sec
    global sec_for_round
    global time_for_round
    global time
    global clicking_next_round
    global time_to_play
    global team_which_guess
    global team_which_describe
    sec = 10
    sec_for_round = 5
    # creating list of teams
    list_of_teams = list(string.ascii_uppercase)[:team_num]


    if describing ==[]:
        # populate describing, guessing and already guessed
        describing = list_of_teams.copy()
    # select which team is describing
    describe_it = random.choice(describing)
    # delete team from describing
    describing.remove(describe_it)
    # print describing team and all available teams now
    print(describe_it)
    print(describing)
    # if we have teams for guessing
    if (len(guessing) != 0) and (describe_it in guessing):
        # remove describing team for guessing
        guessing.remove(describe_it)

    if len(guessing) == 0:
        guessing = list_of_teams.copy()
        already_guessed = []
    # select guessing team
    guess_it = random.choice(guessing)
    # enter team that already guessed
    already_guessed.append(guess_it)
    # create list of guessing teams
    guessing = [x for x in list_of_teams if x not in already_guessed]
    print("guessing team " + str(guessing))
    print(guess_it)
    print(guessing)
    print('Team describing is ' + describe_it + " and team guessing is " + guess_it)










    # ABOVE METHODOLOGY IS WORKING PROPERLY





    # # describing is empty
    # if describing == []:
    #     # take the whole list of teams
    #     describing = list_of_teams.copy()
    #     guessing = list_of_teams.copy()
    #     # already guessed take as empty
    #     already_guessed = []
    # # pick describing team
    # describe_it = random.choice(describing)
    # # delete describing team from the list
    # describing.remove(describe_it)
    # print(describe_it)
    # print(describing)
    # # if guessing list have value
    # if guessing is True:
    #     # delete entry of describing team from guessing team
    #     guessing.remove(describe_it)
    # # select guessing team
    # guess_it = random.choice(guessing)
    # # add team that is guessing to team that already made it
    # already_guessed.append(guess_it)
    # # filter guessing team - only the ones that were not guessing
    # guessing = [x for x in list_of_teams if x not in already_guessed]
    # print(guess_it)
    # print(guessing)
    # print('Team describing is ' + describe_it + " and team guessing is " + guess_it)

    # team that guesses label
    team_which_guess = tk.Label(text=guess_it,fg='White',bg='#312587',font=('Calibri',20,'bold'))

    # team that describes label

    team_which_describe = tk.Label(text=describe_it,fg='White',bg='#312587',font=('Calibri',20,'bold'))

    # Info about remaining time

    time_to_play = tk.Label(text='Start za: ',fg='White',bg='#312587',font=('Calibri',20,'bold'))

    # new widgets are placed
    team_which_guess.config(text="Zgaduje druzyna " + guess_it)
    team_which_describe.config(text='Opisuje druzyna ' + describe_it)
    team_which_guess.place(relx=0.05, rely=0.1)
    team_which_describe.place(relx=0.75, rely=0.1)
    time_to_play.place(relx=0.4, rely=0.95)

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

    # creating the labels for first time
    word_to_guess = tk.Label(text=guess_what,fg='White',bg='#527a7a',font=('Calibri',20,'bold'))
    hint_1 = tk.Label(text=word_1,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_2 = tk.Label(text=word_2,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_3 = tk.Label(text=word_3,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_4 = tk.Label(text=word_4,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_5 = tk.Label(text=word_5,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
    hint_6 = tk.Label(text=word_6,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))

    # declaring the label for counting down
    time_for_round = tk.Label(root,fg='White',bg='#312587',font=('Calibri',20,'bold'))

    # creating a label for ticking down the round
    time = tk.Label(root,fg='White',bg='#312587',font=('Calibri',20,'bold'))

    clicking_next_round.destroy()
    tk.Button(command=tick_round())






# function to start counting down till start of the game
def tick_round():
    # declaring global variable for couting down
    global sec_for_round
    global mac
    global time_till_round
    global button_for_clock
    global next_word
    global dont_know
    global team_which_guess
    global team_which_describe
    global time_to_play
    # each time counting down by one
    sec_for_round -= 1
    # updating the widget with value that was decreased by couting down
    time_for_round['text'] = sec_for_round
    # Take advantage of the after method of the Label
    time_for_round.after(1000, tick_round)
    time_till_round = int(time_for_round.cget("text"))

    # locating the counter
    time_for_round.place(relx=0.5, rely=0.95)

    # if waiting time is over
    if time_till_round < 0:
        # destroy all visible widgets
        team_which_guess.destroy()
        team_which_describe.destroy()
        time_to_play.destroy()
        time_for_round.destroy()

        #pack time counter
        time.pack()
        button_for_clock = tk.Button(root, fg='blue', text='Start', command=tick())

        # Button for next word
        next_word = tk.Button(text='Odgadniete', command=select_new_word,
                              fg='White',bg='Green',font=('Calibri',15,'bold'))

        # Button for going to next word
        dont_know = tk.Button(text='Nastepne', command=move_to_next_word,
                              fg='White',bg='Red',font=('Calibri',15,'bold'))

        # placing the buttons and labels
        next_word.place(relx=0.86, rely=0.6)

        dont_know.place(relx=0.76, rely=0.6)


        # placing labels with words
        word_to_guess.place(relx=0.75, rely=0.1)
        hint_1.place(relx=0.75, rely=0.16)
        hint_2.place(relx=0.75, rely=0.22)
        hint_3.place(relx=0.75, rely=0.28)
        hint_4.place(relx=0.75, rely=0.34)
        hint_5.place(relx=0.75, rely=0.40)
        hint_6.place(relx=0.75, rely=0.46)
        mac = mac + 1

        end_game.place(relx=0.85,rely=0.9)

def declare_and_counter():
    '''function is at one time declaring teams playing the game as well as starting the clock for round'''
    on_button_declare()
    tick_round()


def reset_timing():
    '''functions is resetting the values for time till round and time for the whole round'''
    global sec
    global sec_for_round
    sec = 10
    sec_for_round = 5


def team_selection_and_new_round():
    '''function will select again team for guessing and describing as well as start the clock till next round'''
    pass

def select_new_word():
    '''somebody guessed the world properly and button is clicked'''
    global word_to_guess
    global hint_1
    global hint_2
    global hint_3
    global hint_4
    global hint_5
    global hint_6
    global mac
    global selected
    global ranking

    ranking[guess_it] = ranking[guess_it] + 1
    print('points of team guessing: ' + str(ranking[guess_it]))
    print('word selected is from row ' + str(selected))
    # word that is present on screen is checked in dataframe as solved
    taboo.iloc[selected,7]='y'
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
        # configuring the values for new words after positive guess
        word_to_guess.config(text=guess_what)
        hint_1.config(text=word_1)
        hint_2.config(text=word_2)
        hint_3.config(text=word_3)
        hint_4.config(text=word_4)
        hint_5.config(text=word_5)
        hint_6.config(text=word_6)
        mac = mac + 1

        # placing the word in root
        word_to_guess.place(relx=0.75, rely=0.1)
        hint_1.place(relx=0.75, rely=0.16)
        hint_2.place(relx=0.75, rely=0.22)
        hint_3.place(relx=0.75, rely=0.28)
        hint_4.place(relx=0.75, rely=0.34)
        hint_5.place(relx=0.75, rely=0.40)
        hint_6.place(relx=0.75, rely=0.46)

    if mac == 0:
        word_to_guess = tk.Label(text=guess_what,fg='White',bg='#527a7a',font=('Calibri',20,'bold'))
        hint_1 = tk.Label(text=word_1,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_2 = tk.Label(text=word_2,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_3 = tk.Label(text=word_3,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_4 = tk.Label(text=word_4,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_5 = tk.Label(text=word_5,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_6 = tk.Label(text=word_6,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))

        word_to_guess.place(relx=0.75, rely=0.1)
        hint_1.place(relx=0.75, rely=0.16)
        hint_2.place(relx=0.75, rely=0.22)
        hint_3.place(relx=0.75, rely=0.28)
        hint_4.place(relx=0.75, rely=0.34)
        hint_5.place(relx=0.75, rely=0.40)
        hint_6.place(relx=0.75, rely=0.46)
        mac = mac + 1


def move_to_next_word():
    '''if button is clicked it means that somebody was not able to guess the word'''
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
        # configuring labels for words
        word_to_guess.config(text=guess_what)
        hint_1.config(text=word_1)
        hint_2.config(text=word_2)
        hint_3.config(text=word_3)
        hint_4.config(text=word_4)
        hint_5.config(text=word_5)
        hint_6.config(text=word_6)
        mac = mac + 1

        # placing the words on in the root
        word_to_guess.place(relx=0.75, rely=0.1)
        hint_1.place(relx=0.75, rely=0.16)
        hint_2.place(relx=0.75, rely=0.22)
        hint_3.place(relx=0.75, rely=0.28)
        hint_4.place(relx=0.75, rely=0.34)
        hint_5.place(relx=0.75, rely=0.40)
        hint_6.place(relx=0.75, rely=0.46)

    if mac == 0:
        # creating labels
        word_to_guess = tk.Label(text=guess_what,fg='White',bg='#527a7a',font=('Calibri',20,'bold'))
        hint_1 = tk.Label(text=word_1,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_2 = tk.Label(text=word_2,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_3 = tk.Label(text=word_3,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_4 = tk.Label(text=word_4,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_5 = tk.Label(text=word_5,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))
        hint_6 = tk.Label(text=word_6,fg='White',bg='#0000e6',font=('Calibri',20,'bold'))

        # placing labes
        word_to_guess.place(relx=0.75, rely=0.1)
        hint_1.place(relx=0.75, rely=0.16)
        hint_2.place(relx=0.75, rely=0.22)
        hint_3.place(relx=0.75, rely=0.28)
        hint_4.place(relx=0.75, rely=0.34)
        hint_5.place(relx=0.75, rely=0.40)
        hint_6.place(relx=0.75, rely=0.46)
        mac = mac + 1



def tick():
    global sec
    global clicking_next_round
    sec -= 1
    time['text'] = sec
    # Take advantage of the after method of the Label
    time.after(1000, tick)
    if sec <0:
        time.destroy()
        word_to_guess.destroy()
        hint_1.destroy()
        hint_2.destroy()
        hint_3.destroy()
        hint_4.destroy()
        hint_5.destroy()
        hint_6.destroy()
        next_word.destroy()
        dont_know.destroy()

        # button for next round
        clicking_next_round = tk.Button(text="Kolejna runda",command=next_round,
                                        fg='White',bg='Blue',font=('Calibri',15,'bold'))

        clicking_next_round.place(relx= 0.85,rely=0.8)




# creating a button for start of the round
time = tk.Label(root,fg='White',bg='#312587',font=('Calibri',20,'bold'))


def show_results():
    '''function is printing the results of the competition'''
    global ranking
    global team
    global score
    global team_which_guess
    global team_which_describe
    global end_game
    global clicking_next_round

    # destroying all the entries
    word_to_guess.destroy()
    hint_1.destroy()
    hint_2.destroy()
    hint_3.destroy()
    hint_4.destroy()
    hint_5.destroy()
    hint_6.destroy()
    next_word.destroy()
    dont_know.destroy()

    # destroying end game button
    end_game.destroy()

    # destroying next round button
    clicking_next_round.destroy()

   # destroying team labels
    team_which_guess.destroy()
    team_which_describe.destroy()

    # destroying count down
    time_to_play.destroy()


    # saving results to excel
    # taboo.to_excel(r'C:\Users\310295192\Desktop\answertaboo.xlsx')

    # Creating label for ranking
    lets_show_results = tk.Label(text="Wynik Gry",fg='White',bg='#312587',font=('Calibri',20,'bold'))
    lets_show_results.place(relx=0.025,rely=0.1)

    # counter for moving the label
    counter = 0

    # sorting dictionary to show which team won
    ranking = {k: v for k, v in sorted(ranking.items(),reverse=True, key=lambda item: item[1])}
    # looping through the whole dictionary of teams and results
    for team,score in ranking.items():
        tk.Label(text=f"Zespol {team} zdobyl punktow {score}",fg='White',bg='#312587',font=('Calibri',20,'bold'))\
            .place(relx=0.025,rely=0.2+counter)
        counter +=0.05



    #


# declaring the label for counting down
time_for_round = tk.Label(root,fg='White',bg='#312587',font=('Calibri',20,'bold'))

# # Button for next word
# next_word = tk.Button(text='Nastepne', command=select_new_word)

# welcome label
welcoming = tk.Label(text="Podaj liczbe druzyn:",fg='White',bg='#312587',font=('Calibri',15,'bold'))

# button for declaring participating teams
accepteam = tk.Button(text='Start!',command=declare_and_counter,fg='White',bg='Black',font=('Calibri',15,'bold'))

# help button to show info on game
helping = tk.Button(text='Pomoc',command=help_window,fg='White',bg='Black',font=('Calibri',15,'bold'))


# entry teams field
declaration = tk.Entry(root,width=2)

# team that guesses label
team_which_guess = tk.Label(text=guess_it,fg='White',bg='#312587',font=('Calibri',20,'bold'))

# team that describes label

team_which_describe = tk.Label(text=describe_it,fg='White',bg='#312587',font=('Calibri',20,'bold'))

# Info about remaining time

time_to_play = tk.Label(text='Start za: ',fg='White',bg='#312587',font=('Calibri',20,'bold'))



# # Button for going to next word
# dont_know = tk.Button(text='Nie wiem',command = move_to_next_word)

# Label for time that left

time_for_next_round = tk.Label(text='Pozostaly czas: ',fg='White',bg='#312587',font=('Calibri',20,'bold'))

# Button fo ending the game
end_game = tk.Button(text='Zakoncze gre',command=show_results,fg='White',bg='Black',font=('Calibri',15,'bold'))




# placing the buttons and labels
welcoming.place(relx=0.05,rely=0.45)

declaration.place(relx=0.22,rely=0.455)

accepteam.place(relx=0.05, rely=0.51)

helping.place(relx=0.87,rely=0.87)


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
