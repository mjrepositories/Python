import tkinter  as tk
import tkinter.messagebox as mb
import random
import pandas as pd
sec = 5
player_names =[]
player_guessing = []
player_guessed = []
guessing = ''
selected = 0

ranking = {}
# initiating window

root = tk.Tk()

# import taboo wordpedia
charades = pd.read_excel(r'C:\Users\310295192\Desktop\Python\Projects\Charades\charades.xlsx',
                      usecols='A:C')

# creating the tile of the game
root.title("Charades game")

# setting up the size of the window
window_height = 900
window_width = 925

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

# set up the backgroup image
background_image =tk.PhotoImage(file=r'C:\Users\310295192\Desktop\Python\Projects\Charades\charades_open_logo1.png')

# declare background label
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

def entry_window():
    # take variables as global so that they can be changed after clicking a button
    global background_label
    global start_button
    global background_image
    global declaration
    global start_charades
    global add_player
    global helping
    global player_label
    global start_charades
    global timing
    # destroy currently set up background
    start_button.destroy()
    background_label.destroy()

    # set up the backgroup image
    background_image =tk.PhotoImage(file=r'C:\Users\310295192\Desktop\Python\Projects\Charades\charades_clean1.png')

    # declare background label
    background_label = tk.Label(root,image=background_image)
    background_label.place(relwidth=1,relheight=1)

    # creating a label for timer
    timing = tk.Label(root,fg='White', bg='#5ac7fa', font=('Calibri', 40, 'bold'))

    # help button to show info on game
    helping = tk.Button(text='Pomoc', command=help_window, fg='White', bg='Black', font=('Calibri', 15, 'bold'))
    # placing help button
    helping.place(relx=0.7,rely=0.5)

    # creating entry for players
    declaration = tk.Entry(root, width=10)
    # placing the declaration field
    declaration.place(relx=0.5,rely=0.21)

    # adding player button

    add_player = tk.Button(text='Dodaj gracza', command=add_players_for_game, fg='White', bg='Black',
                          font=('Calibri', 15, 'bold'))

    # placing add player button
    add_player.place(relx=0.7,rely=0.2)

    # creating label for player name

    player_label = tk.Label(text="Imie gracza", fg='White', bg='#5ac7fa', font=('Calibri', 15, 'bold'))

    # placing label for player name
    player_label.place(relx=0.36,rely=0.205)

    # creating button for starting the game

    start_charades = tk.Button(text='Start', command=who_is_selected, fg='White', bg='Blue',
                           font=('Calibri', 15, 'bold'))

    start_charades.config(height =2,width =20)
    # placing add player button
    start_charades.place(relx=0.4, rely=0.5)


def help_window():
   mb.showinfo('Pomoc', "Kalambury to gra na odgadywanie slow lub fraz\n\n"
                        "1. Nie ma ustalonego maksimum grajacych osob\n\n"
                      "2. Gra wybiera losowo osobe, ktore odgaduje\n\n"
                       "3. Kazda runda trwa 90 sekund\n\n"
                        "4. Osoba odgadujaca musi odgadnac prezentowane slow/fraze\n"
                        'Zadaniem pozostalych jest opis tego, co widza,\n'
                        'aby osoba wylosowana mogla odgadnac slowo\n\n'
                       "5. Za kazda fraze otrzymuje sie jeden punkt\n\n"
                       "6. Dryzyny maja 10 sekund po kliknieciu 'Nastepna runda'\n\n"
                        "7. Gre mozna zakonczyc w kazdym momencie\n\n"
                        "8. Wygrywa ta osoba, ktora odganie najwiecej slow")


def add_players_for_game():
    '''function is adding players to the list of players'''

    # getting the value of entry
    new_player = declaration.get()

    # adding the entry to list
    player_names.append(new_player)

    # clearing the entry
    declaration.delete(0, 'end')

    # printing participants names
    print(player_names)

# button for starting a game
start_button = tk.Button(text='Gramy!',command=entry_window,fg='White',bg='Black',font=('Calibri',15,'bold'))
start_button.place(relx=0.47,rely=0.5)

def who_is_selected():
    '''function is deleting all entries after initial window
    and is showing the person that will be going first'''
    global player_guessed
    global player_guessing
    global who_plays_name
    global start_round
    global ranking
    global guessing
    # deleting all widgets from opening window
    add_player.destroy()
    declaration.destroy()
    player_label.destroy()
    start_charades.destroy()
    helping.destroy()


    # after names are provided we create a copy of the list
    player_guessing = player_names.copy()


    # guessing person is selected
    guessing = random.choice(player_names)
    # player guessing is removed from the list of potention "guessers"
    player_guessing.remove(guessing)
    # player selected is add to list of player guessed
    player_guessed.append(guessing)
    # if all players guessed
    if player_guessed == player_names:
        # we empty out the list for players that guessed
        player_guessed =[]
        # and we initiate the guessing list again
        player_guessing = player_names.copy()


    # adding label with the name of the player
    who_plays_name = tk.Label(text=guessing + " zgaduje", fg='White', bg='#5ac7fa', font=('Calibri', 30, 'bold'))
    # placing label with the name of the player
    who_plays_name.place(relx=0.35, rely=0.2)
    # adding button for starting first round
    start_round = tk.Button(text='Rozpocznij runde', command=first_round, fg='White', bg='Black', font=('Calibri', 30, 'bold'))
    # placing button for starting first round
    start_round.place(relx=0.32,rely=0.4)

    # creating ranking for players declared
    ranking = {x:0 for x in player_names}
    print(ranking)


def first_round():
    '''fuction is initialazing the first round of the game'''
    global word_to_guess
    global button_for_clock
    global word_to_guess
    global next_word_right
    global next_word_give_up
    global end_game
    # destroy label for player and start game button
    who_plays_name.destroy()
    start_round.destroy()


    # list of indices that are not solved
    for_guessing = charades[charades.solved.isna()].index.to_list()
    # selecting random value from available words
    selected = random.choice(for_guessing)
    # assigning phrase/word
    guess_what = charades.loc[selected, 'phrase']

    # creating the labels for first time
    word_to_guess = tk.Label(text=guess_what, fg='White', bg='#5ac7fa', font=('Calibri', 20, 'bold'))
    word_to_guess.place(relx=0.35,rely=0.3)

    # button for starting the first round
    button_for_clock = tk.Button(root, fg='blue', text='Start', command=tick())

    # next phrase button when guessed
    next_word_right = tk.Button(root, fg='White', bg='Green', text='Odgadniete', command=next_word_correct,
                                font=('Calibri', 15, 'bold'))
    # place next phrase button
    next_word_right.place(relx=0.2,rely=0.5)


    #next phrase button when gave up
    next_word_give_up = tk.Button(root, fg='White', bg='Red', text='Nastepne', command=next_word_skipped,
                                  font=('Calibri', 15, 'bold'))

    # place next phrase "give-up" botton
    next_word_give_up.place(relx=0.35, rely=0.5)

    # Button fo ending the game
    end_game = tk.Button(text='Zakoncze gre', command=show_results, fg='White', bg='Black',
                         font=('Calibri', 15, 'bold'))
    # placing end game button
    end_game.place(relx=0.7, rely=0.5)

def tick():
    global sec
    global clicking_next_round
    sec -= 1
    timing['text'] = sec
    # Take advantage of the after method of the Label
    timing.after(1000, tick)

    timing.place(relx=0.45,rely=0.1)
    if sec < 0:
        word_to_guess.destroy()
        timing.destroy()
        next_word_right.destroy()
        next_word_give_up.destroy()

        # button for next round
        clicking_next_round = tk.Button(text="Kolejna runda", command=go_to_next_round,
                                        fg='White', bg='Blue', font=('Calibri', 15, 'bold'))

        clicking_next_round.place(relx=0.3, rely=0.5)


def next_word_correct():
    ''' function allows to select next word after
    right guessing'''
    global word_to_guess
    global selected
    global ranking
    global charades

    # assigning point for guessed word
    ranking[guessing] = ranking[guessing] + 1

    # word that is present on screen is checked in dataframe as solved
    charades.iloc[selected, 2] = 'y'


    # list of indices that are not solved
    for_guessing = charades[charades.solved.isna()].index.to_list()
    # selecting random value from available words
    selected = random.choice(for_guessing)
    # assigning phrase/word
    guess_what = charades.loc[selected, 'phrase']

    # changing the presented word
    word_to_guess.config(text=guess_what)


def next_word_skipped():
    '''function allows to select next word
    when person is not able to guess'''
    global word_to_guess

    # list of indices that are not solved
    for_guessing = charades[charades.solved.isna()].index.to_list()
    # selecting random value from available words
    selected = random.choice(for_guessing)
    # assigning phrase/word
    guess_what = charades.loc[selected, 'phrase']

    # changing the presented word
    word_to_guess.config(text=guess_what)



def go_to_next_round():
    '''function enables to move to the next round'''
    global sec
    global word_to_guess
    global button_for_clock
    global word_to_guess
    global next_word_right
    global next_word_give_up
    global player_guessed
    global player_guessing
    global start_round
    global who_plays_name
    global guessing
    sec = 5

    print("players guessed")
    print(player_guessed)


    # if all players guessed
    if set(player_guessed) == set(player_names):
        # we empty out the list for players that guessed
        player_guessed =[]
        # and we initiate the guessing list again
        player_guessing = player_names.copy()
    # destroying next round button
    clicking_next_round.destroy()
    # guessing person is selected
    guessing = random.choice(player_guessing)
    # player guessing is removed from the list of potention "guessers"
    player_guessing.remove(guessing)
    # player selected is add to list of player guessed
    player_guessed.append(guessing)



    # adding label with the name of the player
    who_plays_name = tk.Label(text=guessing + " zgaduje", fg='White', bg='#5ac7fa', font=('Calibri', 30, 'bold'))
    # placing label with the name of the player
    who_plays_name.place(relx=0.35, rely=0.2)
    # adding button for starting first round
    start_round = tk.Button(text='Rozpocznij runde', command=next_round, fg='White', bg='Black', font=('Calibri', 30, 'bold'))
    # placing button for starting first round
    start_round.place(relx=0.32,rely=0.4)

def next_round():
    ''' function that enables next round phrases selection'''
    global button_for_clock
    global sec
    global timing
    global next_word_right
    global next_word_give_up
    global word_to_guess

    # destroying who guesses label
    who_plays_name.destroy()
    # destroying start round button
    start_round.destroy()
    # list of indices that are not solved
    for_guessing = charades[charades.solved.isna()].index.to_list()
    # selecting random value from available words
    selected = random.choice(for_guessing)
    # assigning phrase/word
    guess_what = charades.loc[selected, 'phrase']

    # creating the labels for first time
    word_to_guess = tk.Label(text=guess_what, fg='White', bg='#5ac7fa', font=('Calibri', 20, 'bold'))
    word_to_guess.place(relx=0.35, rely=0.3)

    # creating a label for timer
    timing = tk.Label(root, fg='White', bg='#5ac7fa', font=('Calibri', 40, 'bold'))

    sec = 5
    # button for starting the first round
    button_for_clock = tk.Button(root, fg='blue', text='Start', command=tick())

    # next phrase button when guessed
    next_word_right = tk.Button(root, fg='White', bg='Green', text='Odgadniete', command=next_word_correct,
                                font=('Calibri', 15, 'bold'))
    # place next phrase button
    next_word_right.place(relx=0.2,rely=0.5)


    #next phrase button when gave up
    next_word_give_up = tk.Button(root, fg='White', bg='Red', text='Nastepne', command=next_word_skipped,
                                  font=('Calibri', 15, 'bold'))

    # place next phrase "give-up" botton
    next_word_give_up.place(relx=0.35, rely=0.5)



def show_results():
    '''function to show final result of the game'''
    # destroying all buttons and labels we have
    global ranking
    end_game.destroy()
    next_word_right.destroy()
    next_word_give_up.destroy()
    word_to_guess.destroy()
    timing.destroy()
    clicking_next_round.destroy()
    try:
        start_round.destroy()
    except:
        print("no start next round button")

    try:
        who_plays_name.destroy()
    except:
        print('no player name')

    # Creating label for ranking
    lets_show_results = tk.Label(text="Wynik Gry", fg='White', bg='#5ac7fa', font=('Calibri', 20, 'bold'))
    lets_show_results.place(relx=0.4, rely=0.1)

    # counter for moving the label
    counter = 0

    # sorting dictionary to show which person won
    ranking = {k: v for k, v in sorted(ranking.items(), reverse=True, key=lambda item: item[1])}
    # looping through the whole dictionary of teams and results
    for person, score in ranking.items():
        tk.Label(text=f"{person} zdobyl/a punktow {score}", fg='White', bg='#5ac7fa', font=('Calibri', 20, 'bold')) \
            .place(relx=0.4, rely=0.2 + counter)
        counter += 0.05



root.mainloop()



# player_guessed = []
#
# player_names=['Maciej','Michał','Bartek']
# # after names are provided we create a copy of the list
# player_guessing = player_names.copy()
#
#
# # guessing person is selected
# guessing = random.choice(player_names)
# # player guessing is removed from the list of potention "guessers"
# player_guessing.remove(guessing)
# # player selected is add to list of player guessed
# player_guessed.append(guessing)
# # if all players guessed
# if player_guessed = player_names:
#     # we empty out the list for players that guessed
#     player_guessed =[]
#     # and we initiate the guessing list again
#     player_guessing = player_names.copy()