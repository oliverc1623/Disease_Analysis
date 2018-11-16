"""
Disease Analysis Project
By Oliver Chang
Pomona '22
11/14/2018
"""

import matplotlib as plt
from tkinter import *
from read_data import *

df = return_data_frame()
print(df.columns)
topic_options = (return_topics(df))


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Disease Analysis Application")
        self.pack(fill=BOTH, expand=1)

        # Tkinter Variable
        self.default_option = StringVar(root)
        self.default_option.set("Cancer")  # set the default option

        # Welcome Label
        welcome_label = Label(self, text="Welcome to Disease Data Analysis. Pick a disease you'd like to see plotted.")
        welcome_label.pack()

        # Option Menu
        topic_option = OptionMenu(self, self.default_option, *topic_options)
        topic_option.place(x=0, y=20)

        # Run Button
        run_button = Button(self, text="Run", command=self.run_analysis)
        run_button.pack()

        # Quit Button
        quit_button = Button(self, text="Quit", command=self.client_exit)
        quit_button.place(x=0, y=0)

    def run_analysis(self):
        print(self.default_option.get())

    def client_exit(self):
        exit()


root = Tk()
root.geometry("600x300")
app = Window(root)
root.mainloop()
