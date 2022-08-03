import tkinter as tk
from tkinter import ttk

class Converter():
    def __init__(self):
        master_window = tk.Tk()
        master_window.title('Feet to Meters Converter')
        master_window.geometry('275x125')

        self.feet = tk.StringVar()
        self.meters = tk.StringVar()

        feet_input = ttk.Entry(master_window, textvariable = self.feet)
        feet_input.grid(column = 1, row = 0)
        #feet_input.place(x=140, y=70, width = 120, height = 30)

        feet_label = ttk.Label(master_window, text = 'Input feet: ')
        #feet_label.place(x=70, y = 65, height = 40)
        feet_label.grid(column = 0, row = 0)

        self.meters_output_label = ttk.Label(master_window, textvariable = self.meters)

        meters_label = ttk.Label(master_window, text = 'Meters Equivalent: ')
        meters_label.grid(column = 0, row = 2)
        #meters_label.place(x=40, y = 125)

        convert_button = ttk.Button(master_window, text = 'Convert', command = self.convert_MTF)
        convert_button.grid(column = 1, row = 4)
        #convert_button.place(x=150,y = 175, width = 75)

        #some spacing labels
        spacing_label1 = ttk.Label(master_window, text = ' ')
        spacing_label1.grid(column = 0, row = 1)

        spacing_label2 = ttk.Label(master_window, text = ' ')
        spacing_label2.grid(column = 1, row = 1)

        spacing_label3 = ttk.Label(master_window, text = ' ')
        spacing_label3.grid(column = 1, row = 3)
        master_window.bind('<Return>', self.convert_MTF)

        feet_input.focus()

        master_window.mainloop()

    def convert_MTF(self, *args):
        try:
            foot_value = float(self.feet.get())
            self.meters.set(int(foot_value * 3048) / 10000)
            #self.meters_output_label.place(x=165, y=115, width = 100, height = 40)
            self.meters_output_label.grid(column = 1, row = 2)
        except ValueError:
            pass
        except TypeError:
            pass
        return 0

converter_obj = Converter()