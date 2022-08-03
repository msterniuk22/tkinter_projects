#import tkinter and ttk, along with password gen
from custom_password_generator import create_password
import tkinter as tk
from tkinter import ttk

#creates a tk window
root_window = tk.Tk()
root_window.geometry('325x225')
root_window.title('Login screen')

#creates a stringvar to hold the password
custom_passcode = tk.StringVar(root_window)
#binds the label display with stringvar defined above
custom_password_label = ttk.Label(root_window, textvariable = custom_passcode)
instruction_label = ttk.Label(root_window, text = 'Click to copy!---->', font = 'Times 10')

#creates a function that will get the value of the stringvar above
#using .get(), a nice method of StringVar class
#and then appends that to the users clipboard to allow Ctrl + V
def get_custom_passcode(event):
    passcode = custom_passcode.get()
    root_window.clipboard_append(passcode)

#binds the left mouse button to calling get_custom_passcode func
custom_password_label.bind('<Button-1>', get_custom_passcode)

#creates a function that will display the password
#and then call the password generator
#while setting the custom_passcode var above to the newly gen password
def display_password():
    custom_password_label.place(x=122, y = 175)
    instruction_label.place(x=10, y=175)
    new_password = create_password()
    custom_passcode.set(new_password)
    return 0

#creates and places the new button that when will call the display_password func
get_custom_password = ttk.Button(root_window, text = 'Get a Custom Password', command = display_password)
get_custom_password.place(x=95, y=140)

#using tk vars since they are instances of StringVar()
#and hence have some nice methods like .get() and .set()
#plus they are easy to bind with textvar and update in all places at once
user_name = tk.StringVar(root_window)
password = tk.StringVar(root_window)

#just a label
login_label = ttk.Label(root_window, text = 'Login: ')
login_label.place(x=50, y=20)

#gets the value of the two instances of stringvar above
#and prints them out
def get_user_information():
    print(user_name.get())
    print(password.get())
    return 0

#binds whatever is entered into this Entry to user_name string var
login_input = ttk.Entry(root_window, textvariable = user_name)
login_input.place(x=100, y=20)

#label to mark where password box is
password_label = ttk.Label(root_window, text = 'Password:')
password_label.place(x=30, y = 60)

#binds whatever is entered as a password to password stringvar
#and also creates a password Entry field and places it
password_input = ttk.Entry(root_window, textvariable = password)
password_input.place(x=100, y = 60)

#creates/places button that will call get_user_info when pressed, printing the entry input fields
login_button = ttk.Button(root_window, text = 'Complete Login', command = get_user_information )
login_button.place(x = 110, y = 100)

#begins the program with cursor within login_input Entry field
login_input.focus()

#runs the tkinter event loop to allow users to interact, events to happen, etc.
root_window.mainloop()
