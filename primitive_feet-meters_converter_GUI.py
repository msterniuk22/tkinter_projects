import tkinter as tk
from tkinter import ttk

root_window = tk.Tk()
root_window.title('Feet to Meters Converter - Free')
root_window.geometry('400x400')

def convert_feet_to_meters():
    try:
        #tries to get value from a tkinter var stored as inputted_feet
        foot_value = float(inputted_feet.get())
        #does some math to find meters, rounds it out by *  and / by 10
        converted_meters.set(int(foot_value * 3.048) / 10)
        #makes the answer visible
        meters_output_label.place(x=170, y = 130, height = 30)
    except:
        #if we get an exception(usually non-num input), we don't calculate
        #and wait for program termination or new input
        pass

#creates two tkinter String variables with root_window as the master
converted_meters = tk.StringVar(root_window)
inputted_feet = tk.StringVar(root_window)

#creates an entry field whose input is bound(via textvariable) to inputted feet, a tk variable
#any time textvariable/inputted_feet(they are bound) changes, so will inputted feet and vice versa
foot_input = ttk.Entry(root_window,  font = 'Times 15', textvariable = inputted_feet)
foot_input.place(x=160, y=80, width = 100, height = 30)

#creates a label with some text and font specif. and then places it using .place()
foot_label = ttk.Label(root_window, text = 'Input feet here:', font = 'Times 12')
foot_label.place(x=60, y=80, height = 30)

#another label, places it
meters_label = ttk.Label(root_window, text = 'is equal to: ', font = 'Times 12')
meters_label.place(x=85, y=130, height = 30)
#creates the output label where the answer will show up. ties the output of this via textvar
#to tk variable(str type)converted meters,so that when converted meters changes in one spot, it will change in all spots
meters_output_label = ttk.Label(root_window, textvariable = converted_meters, font = 'Times 12')

#creates a label using ttk library, in root_window
meters_label2 = ttk.Label(root_window, text = 'meters', font = 'Times 12')
meters_label2.place(x=275, y=130, height = 30)

#creates a button that when presses executes command to call convert_feet_to_meters. then places the button
convert_button = ttk.Button(root_window, text = 'Convert', command = convert_feet_to_meters)
convert_button.place(x=160, y = 200, height = 30, width = 100)

#simple command that places cursor within foot_input when program boots up
foot_input.focus()

#runs the main event loop so that tkinter can listen for events, manage geometry etc.
root_window.mainloop()