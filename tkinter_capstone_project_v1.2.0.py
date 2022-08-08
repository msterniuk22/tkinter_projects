"""
This is a multi-window interface written completely in tkinter
without any tutorials. The idea is to combine several previous ideas
and unify them with an interface in tkinter. It will feature a login
page where you register or log in to an existing account, a page to 'sample'
the various options and choose one, and then you can use whatever option you
chose. As of now, I plan to have a up-to-date weather app and interactive
tic-tac-toe.
"""

import tkinter as tk
from tkinter import ttk
import time
#for pop ups
from tkinter import messagebox
#dealing with importing .jpeg's
from PIL import ImageTk, Image
import random

image = Image.open("tic_tac_toe_O.jpeg")
image2 = Image.open("tic_tac_toe_X.png")

#creates the main class
class app_interface():

    #takes in root_window to use(from outside class)
    def __init__(self, root_window):
        #defines some windows needed within entire class
        self.registration_window = ''
        self.catalog_window = ''
        self.root = root_window
        self.ttt_user_moves = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.ttt_comp_moves = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.O_photo = ImageTk.PhotoImage(image.resize((40, 40), Image.ANTIALIAS))
        self.X_photo = ImageTk.PhotoImage(image2.resize((40, 40), Image.ANTIALIAS))
        login_page_frame = ttk.Frame(self.root, width = 150, height = 100)

        #all the labels
        title_label = ttk.Label(login_page_frame, text = 'Login Page', font = 'Times 20')
        username_label = ttk.Label(login_page_frame, text = 'Username: ')
        password_label = ttk.Label(login_page_frame, text = 'Password: ')

        #creates stringvars to track user entries. then creates user entries
        username_tracker = tk.StringVar(login_page_frame)
        password_tracker = tk.StringVar(login_page_frame)
        username_entry = ttk.Entry(login_page_frame, textvariable = username_tracker)
        password_entry = ttk.Entry(login_page_frame, textvariable = password_tracker)

        #does the buttons
        login_button = ttk.Button(text = 'Log In', command = self.init_login)
        register_button = ttk.Button(text = 'Register', command = self.init_registration)

        #gridding everything in column/row form. added some padding
        login_page_frame.grid(column = 0, row = 0)
        title_label.grid(column = 1, row = 0)
        username_label.grid(column = 0, row = 1)
        password_label.grid(column = 0, row = 2)
        login_button.grid(column = 0, row = 3, sticky = 'w', pady = 15)
        username_entry.grid(column = 1, row = 1)
        password_entry.grid(column = 1, row = 2)
        register_button.grid(column = 2, row = 3, pady = 15, padx = 5)

        #iterates through each child of login_page_frame and adds padding
        #basically, adds padding to each widget within the frame
        for child in login_page_frame.winfo_children():
            child.grid_configure(padx=5, pady = 10)

    #processes any login details, validates them
    #if they are valid, calls processing_login and withdraws the root window
    def init_login(self):
        messagebox.showinfo('LOGIN COMPLETE', 'Routing to the next page...')
        self.root.withdraw()
        self.processing_login()

    #creates the registration page to take new account details from user
    #much of this is a replica of the original log in page
    def init_registration(self):
        messagebox.showinfo('REGISTRATION REQUESTED', 'Routing you to the next page...')
        #creates a new window and 'withdraws' root window
        self.registration_window = tk.Toplevel(self.root)
        self.root.withdraw()

        regis_frame = ttk.Frame(self.registration_window, width=150, height=100)

        #does all the labels
        title_label = ttk.Label(regis_frame, text='Register Account', font='Times 20')
        username_label = ttk.Label(regis_frame, text='New Username: ')
        password_label = ttk.Label(regis_frame, text='New Password: ')

        #creates stringvars to track user entries, then instantiates the user entries
        regis_username_tracker = tk.StringVar(regis_frame)
        regis_password_tracker = tk.StringVar(regis_frame)
        regis_username_entry = ttk.Entry(regis_frame, textvariable=regis_username_tracker)
        regis_password_entry = ttk.Entry(regis_frame, textvariable=regis_password_tracker)

        #adds a button to call next step in process
        complete_regis_button = ttk.Button(regis_frame, text='Register', command = self.processing_registration)

        #gridding everything
        regis_frame.grid(column=0, row=0)
        title_label.grid(column=1, row=0)
        username_label.grid(column=0, row=1)
        password_label.grid(column=0, row=2)
        regis_username_entry.grid(column=1, row=1)
        regis_password_entry.grid(column=1, row=2)
        complete_regis_button.grid(column=1, row=3, pady=15, padx=5)

        #placeholder labels for aesthetics
        PH1 = ttk.Label(regis_frame, text = '                              ')
        PH1.grid(column = 2, row = 1)

        #iterates through all the widgets in this frame and adds padding too
        for child in regis_frame.winfo_children():
            child.grid_configure(padx=5, pady=10)

        #if the user tries to X out of the registration window, it destroys all windows
        #and ends the program. data is not saved as user account
        self.registration_window.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())

    #this is where login details will be checked prior to access to apps
    def processing_login(self):
        #if validation is good, calls the options window
        self.options_window()

    #this window checks the user details and then creates a new account. after acc is
    #created, gives access to options window and closes registration window
    def processing_registration(self):
        #create the new account and verify it
        messagebox.showinfo('REGISTRATION COMPLETE', 'Congratulations on your new account. Enjoy!')
        self.options_window()
        self.registration_window.withdraw()

    #this is the window where the user can look at the possible apps
    def options_window(self):
        #creates a new window and nests a notebook widget within it
        self.catalog_window = tk.Toplevel(self.root)
        option_notebook = ttk.Notebook(self.catalog_window, )

        #creates a frame for each of the options and then adds those to the notebook
        tic_tac_toe_frame = ttk.Frame(option_notebook, width = 400, height = 200)
        weather_app_frame = ttk.Frame(option_notebook, width = 400, height = 200)

        option_notebook.add(tic_tac_toe_frame, text = 'Tic-Tac-Toe')
        option_notebook.add(weather_app_frame, text = 'Weather App')

        #creates a header, the textbox to store info and a button to move to app
        ttt_header = ttk.Label(tic_tac_toe_frame, text = 'Tic-Tac-Toe', font = 'Times 20')
        ttt_textbox = tk.Text(tic_tac_toe_frame, width = 40, height = 10, state = 'normal', wrap = 'word')
        ttt_button = ttk.Button(tic_tac_toe_frame, text = 'Continue to Tic-Tac-Toe', command = self.tic_tac_toe)

        #adds a description to the textbox
        textbox_message = 'This is the classic Tic-Tac-Toe game. Play this fun little ' \
                          'game against the computer and challenge your skills!'
        ttt_textbox.insert('0.0', textbox_message)

        #in the future there will be an app in the format below added
        #ttt_image = ImageTk.PhotoImage(Image.open("tic_tac_toe_stock_image.jpeg"))
        #ttt_textbox.image_create('0.0', image = ttt_image)

        #grids everything
        ttt_header.grid(row = 0, column = 0, padx = 200, pady = 10, sticky = 'ew', columnspan = 3)
        ttt_textbox.grid(row = 1, column = 0, padx = 50, pady = 10, sticky = 'ew', columnspan = 3)
        ttt_button.grid(row = 2, column = 0, padx = 200, pady = 10, sticky = 'ew', columnspan = 1)

        #-----------------------------------------------------------------------------
        #creates a header, textbox and button to proceed to weather app
        weather_app_header = ttk.Label(weather_app_frame, text='Weather App', font='Times 20')
        weather_textbox = tk.Text(weather_app_frame, width=40, height=10, state='normal', wrap='word')
        weather_app_button = ttk.Button(weather_app_frame, text='Continue to the Weather App', command = self.weather_app)

        #inserts a description to weather textbox
        weather_textbox_msg = 'Welcome to the Weather App, where you can get up to date ' \
                              "weather information and statistics. Click below to see today's " \
                              "forecast and more!"
        weather_textbox.insert('0.0', weather_textbox_msg)

        #grids it all
        weather_app_header.grid(row=0, column=0, padx=200, pady=10, sticky='ew', columnspan=3)
        weather_textbox.grid(row=1, column=0, padx=50, pady=10, sticky='ew', columnspan=3)
        weather_app_button.grid(row=2, column=0, padx=200, pady=10, sticky='ew', columnspan=1)
        option_notebook.grid()

    #will deal with the tic tac toe window and playing the game
    def tic_tac_toe(self):
        #creates a new window and withdraws options window
        ttt_window = tk.Toplevel(self.root)
        self.catalog_window.withdraw()
        ttt_window.geometry("+500-350")
        master_frame = ttk.Frame(ttt_window, width=500, height=500, relief='sunken', borderwidth=10)

        # creating the 9 squares to play on
        frame_0 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_1 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_2 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_3 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_4 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_5 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_6 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_7 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)
        frame_8 = ttk.Frame(master_frame, relief='sunken', borderwidth=5, width=52, height=52)

        aval_moves = [i for i in range(9)]

        label0 = ttk.Label(frame_0, image = self.X_photo)
        label1 = ttk.Label(frame_1, image = self.X_photo)
        label2 = ttk.Label(frame_2, image = self.X_photo)
        label3 = ttk.Label(frame_3, image = self.X_photo)
        label4 = ttk.Label(frame_4, image = self.X_photo)
        label5 = ttk.Label(frame_5, image = self.X_photo)
        label6 = ttk.Label(frame_6, image = self.X_photo)
        label7 = ttk.Label(frame_7, image = self.X_photo)
        label8 = ttk.Label(frame_8, image = self.X_photo)

        frame_0.grid(column=0, row=0, padx=5, pady=5, sticky='w')
        frame_1.grid(column=1, row=0, padx=5, pady=5, sticky='n')
        frame_2.grid(column=2, row=0, padx=5, pady=5, sticky='e')
        frame_3.grid(column=0, row=1, padx=5, pady=5, sticky='w')
        frame_4.grid(column=1, row=1, padx=5, pady=5, sticky='nsew')
        frame_5.grid(column=2, row=1, padx=5, pady=5, sticky='e')
        frame_6.grid(column=0, row=2, padx=5, pady=5, sticky='w')
        frame_7.grid(column=1, row=2, padx=5, pady=5, sticky='s')
        frame_8.grid(column=2, row=2, padx=5, pady=5, sticky='e')
        master_frame.grid(column=0, row=0)

        #preventing frames from changing dimensions
        frame_0.grid_propagate('False')
        frame_1.grid_propagate('False')
        frame_2.grid_propagate('False')
        frame_3.grid_propagate('False')
        frame_4.grid_propagate('False')
        frame_5.grid_propagate('False')
        frame_6.grid_propagate('False')
        frame_7.grid_propagate('False')
        frame_8.grid_propagate('False')

        def insert_new_move(move, player):
            #take the move and the place it came from
            #insert that into respective list
            if player == 'Computer':
                iter_lst = []
                for lists in self.ttt_comp_moves:
                    for ele in lists:
                        iter_lst.append(ele)
                iter_lst[move] = move
                self.ttt_comp_moves.clear()
                self.ttt_comp_moves.append(iter_lst[0:3])
                self.ttt_comp_moves.append(iter_lst[3:6])
                self.ttt_comp_moves.append(iter_lst[6:9])

            elif player == 'User':
                iter_lst = []
                for lists in self.ttt_user_moves:
                    for ele in lists:
                        iter_lst.append(ele)
                iter_lst[move] = move
                self.ttt_user_moves.clear()
                self.ttt_user_moves.append(iter_lst[0:3])
                self.ttt_user_moves.append(iter_lst[3:6])
                self.ttt_user_moves.append(iter_lst[6:9])


        def determine_winner():
            #determine horizontals first
            #checking the users side
            int_count = 0
            for lsts in self.ttt_user_moves:
                for ele in lsts:
                    if type(ele) == int:
                        int_count += 1
                if int_count == 3:
                    messagebox.showinfo('USER WINS','read title, u moron')
                    return 0
                int_count = 0

            #checking the computers side
            int_count = 0
            for lsts in self.ttt_comp_moves:
                for ele in lsts:
                    if type(ele) == int:
                        int_count += 1
                if int_count == 3:
                    messagebox.showinfo('COMPUTER WINS','read title, u moron')
                    return 0
                int_count = 0

            #checking vertical winners
            #checking users side
            checker_list = []
            given_index = 0
            iter_progress = 0
            flattened_list = []
            for lists in self.ttt_user_moves:
                for ele in lists:
                    flattened_list.append(ele)

            for _ in range(3):
                given_index = iter_progress
                for _ in range(3):
                    checker_list.append(flattened_list[given_index])
                    given_index += 3
                iter_progress += 1
                int_count = 0
                for ele in checker_list:
                    if type(ele) == int:
                        int_count += 1
                if int_count == 3:
                    messagebox.showinfo('USER WINS', 'read da title')
                checker_list.clear()

            #checking computer side
            checker_list = []
            given_index = 0
            iter_progress = 0
            flattened_list = []
            for lists in self.ttt_comp_moves:
                for ele in lists:
                    flattened_list.append(ele)

            for _ in range(3):
                given_index = iter_progress
                for _ in range(3):
                    checker_list.append(flattened_list[given_index])
                    given_index += 3
                iter_progress += 1
                int_count = 0
                for ele in checker_list:
                    if type(ele) == int:
                        int_count += 1
                if int_count == 3:
                    messagebox.showinfo('Computer WINS', 'read da title')
                checker_list.clear()

            #dealing with diagonals
            #user first
            flat_list = []
            checker_list = []
            for lists in self.ttt_user_moves:
                for ele in lists:
                    flat_list.append(ele)


            checker_list.append(flat_list[0])
            checker_list.append(flat_list[4])
            checker_list.append(flat_list[8])

            for x in range(2):
                int_count = 0
                for ele in checker_list:
                    if type(ele) == int:
                        int_count += 1
                if int_count == 3:
                    messagebox.showinfo('USER WINS', 'User won on a diagonal')

                checker_list.clear()
                checker_list.append(flat_list[2])
                checker_list.append(flat_list[4])
                checker_list.append(flat_list[6])

            #computer side
            flat_list = []
            checker_list = []
            for lists in self.ttt_comp_moves:
                for ele in lists:
                    flat_list.append(ele)

            checker_list.append(flat_list[0])
            checker_list.append(flat_list[4])
            checker_list.append(flat_list[8])

            for x in range(2):
                int_count = 0
                for ele in checker_list:
                    if type(ele) == int:
                        int_count += 1
                if int_count == 3:
                    messagebox.showinfo('COMPUTER WINS', 'Computer won on a diagonal')

                checker_list.clear()
                checker_list.append(flat_list[2])
                checker_list.append(flat_list[4])
                checker_list.append(flat_list[6])



        def user_move():
            def f0(*args):
                try:
                    aval_moves.remove(0)
                    label0.grid()
                    insert_new_move(0, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f1(*args):
                try:
                    aval_moves.remove(1)
                    label1.grid()
                    insert_new_move(1, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f2(*args):
                try:
                    aval_moves.remove(2)
                    label2.grid()
                    insert_new_move(2, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f3(*args):
                try:
                    aval_moves.remove(3)
                    label3.grid()
                    insert_new_move(3, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f4(*args):
                try:
                    aval_moves.remove(4)
                    label4.grid()
                    insert_new_move(4, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f5(*args):
                try:
                    aval_moves.remove(5)
                    label5.grid()
                    insert_new_move(5, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')
            def f6(*args):
                try:
                    aval_moves.remove(6)
                    label6.grid()
                    insert_new_move(6, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f7(*args):
                try:
                    aval_moves.remove(7)
                    label7.grid()
                    frame_7.propagate(0)
                    insert_new_move(7, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')

            def f8(*args):
                try:
                    aval_moves.remove(8)
                    label8.grid()
                    insert_new_move(8, 'User')
                    determine_winner()
                    computer_move()
                except ValueError:
                    print('That spot is taken. Try somewhere else')


            # making them all reponsive to the touch
            frame_0.bind('<Button-1>', f0)
            frame_1.bind('<Button-1>', f1)
            frame_2.bind('<Button-1>', f2)
            frame_3.bind('<Button-1>', f3)
            frame_4.bind('<Button-1>', f4)
            frame_5.bind('<Button-1>', f5)
            frame_6.bind('<Button-1>', f6)
            frame_7.bind('<Button-1>', f7)
            frame_8.bind('<Button-1>', f8)

        def computer_move():
            #allowing the computer to choose something if len(aval_moves) > 0
            if len(aval_moves) > 0:
                comp_move = random.sample(aval_moves, 1)
            else:
                messagebox.showinfo('DRAW', "All moves are taken. It's a draw!")
                comp_move = [None]

            frame_to_spot = {frame_0 : 0, frame_1 : 1, frame_2 : 2,
                             frame_3:3, frame_4 : 4, frame_5 : 5,
                             frame_6 : 6, frame_7 : 7, frame_8 : 8}

            def get_key(val):
                for key, value in frame_to_spot.items():
                    if val == value:
                        return key

                return "key doesn't exist"

            insert_frame = get_key(comp_move[0])

            #had to create photo as a obj attr(self.O_photo)
            #because tkinter garbage collects images nested with a function
            display_label = ttk.Label(insert_frame, image = self.O_photo)
            display_label.grid()
            insert_frame.grid_propagate('False')
            aval_moves.remove(comp_move[0])
            insert_new_move(comp_move[0], 'Computer')
            determine_winner()

        #if the user tries to X out of cur window, exits the program entirely
        ttt_window.protocol("WM_DELETE_WINDOW", lambda: destroy_root())

        def destroy_root():
            self.root.destroy()

        user_move()

    #will deal with the weather app window and displaying API data
    def weather_app(self):
        #creates a new window and withdraws options window
        weather_window = tk.Toplevel(self.root)
        self.catalog_window.withdraw()

        some_label = ttk.Label(weather_window, text = 'You are in weather App window')
        some_label.pack(pady = 25)

        weather_window.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())

#creates a root window, passes it in to the main class and then runs tkinter event loop
root = tk.Tk()
obj = app_interface(root)
root.mainloop()