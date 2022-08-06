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

#creates the main class
class app_interface():

    #takes in root_window to use(from outside class)
    def __init__(self, root_window):
        #defines some windows needed within entire class
        self.registration_window = ''
        self.catalog_window = ''
        self.root = root_window
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

        some_label = ttk.Label(ttt_window, text = 'You are in tic tac toe window')
        some_label.pack(pady = 25)

        #if the user tries to X out of cur window, exits the program entirely
        ttt_window.protocol("WM_DELETE_WINDOW", lambda: self.root.destroy())

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