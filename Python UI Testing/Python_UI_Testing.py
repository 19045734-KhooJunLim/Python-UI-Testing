import argparse
from tkinter import *
import tkinter as tk

class Helpme:
    def __init__(self, master):
        self.master = master
        master.title('UI Test')
        master.geometry('600x300')
        self.found_button = Button(master, text="Found Something", height=10, width=20, command=lambda : input("found"))
        self.retrieve_button = Button(master, text="Retrieve Something", height=10, width=20, command=lambda : input("retrieve"))

        self.found_button.grid(row=2, column=1, padx=100, pady=50)
        self.retrieve_button.grid(row=2, column=3, padx=25, pady=50)

        

    


    # Defining a function that will get the details
    # and print them on the screen
    def input(self, method):
        # Delcaring variables to store details
        fname_var = tk.StringVar() #Finder name
        fid_var = tk.IntVar() #Finder ID
        iname_var = tk.StringVar() #Item name
        itype_var = tk.StringVar() #Item type
        
        if method == "found":
            self.found_button.grid_forget()
            self.retrieve_button.grid_forget()
            self.fname_label = Label(root, text = 'Username', font=('calibre',10, 'bold'))
            self.fname_entry = Entry(root,textvariable = fname_var, font=('calibre',10,'normal'))

            self.fid_label = Label(root, text = 'ID', font=('calibre',10, 'bold'))
            self.fid_entry = Entry(root,textvariable = fid_var, font=('calibre',10,'normal'))

            self.iname_label = Label(root, text = 'Item name', font=('calibre',10, 'bold'))
            self.iname_entry = Entry(root,textvariable = iname_var, font=('calibre',10,'normal'))

            self.itype_label = Label(root, text = 'Item type', font=('calibre',10, 'bold'))
            self.itype_entry = Entry(root,textvariable = itype_var, font=('calibre',10,'normal'))


            # Creating a button using the widget
            # Button that will call the submit function
            self.sub_btn = Button(root,text = 'Submit', command=None)

            # Placing the label and entry in the required position using grid method
            self.fname_label.grid(row=0, column=0)
            self.fname_entry.grid(row=0, column=1)

            self.fid_label.grid(row=1, column=0)
            self.fid_entry.grid(row=1, column=1)

            self.iname_label.grid(row=2, column=0)
            self.iname_entry.grid(row=2, column=1)

            self.itype_label.grid(row=3, column=0)
            self.itype_entry.grid(row=3, column=1)

            # Creating a submit button
            self.sub_btn.grid(row=4, column=1)
        else:
            self.found_button.grid_forget()
            self.retrieve_button.grid_forget()
            self.fname_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
            self.fname_entry = tk.Entry(root,textvariable = fname_var, font=('calibre',10,'normal'))

            self.fid_label = tk.Label(root, text = 'ID', font=('calibre',10, 'bold'))
            self.fid_entry = tk.Entry(root,textvariable = fid_var, font=('calibre',10,'normal'))

            self.iname_label = tk.Label(root, text = 'Item name', font=('calibre',10, 'bold'))
            self.iname_entry = tk.Entry(root,textvariable = iname_var, font=('calibre',10,'normal'))

            self.itype_label = tk.Label(root, text = 'Item type', font=('calibre',10, 'bold'))
            self.itype_entry = tk.Entry(root,textvariable = itype_var, font=('calibre',10,'normal'))


            # Creating a button using the widget
            # Button that will call the submit function
            self.sub_btn = tk.Button(root,text = 'Submit', command = None)

            # Placing the label and entry in the required position using grid method
            self.fname_label.grid(row=0, column=0)
            self.fname_entry.grid(row=0, column=1)

            self.fid_label.grid(row=1, column=0)
            self.fid_entry.grid(row=1, column=1)

            self.iname_label.grid(row=2, column=0)
            self.iname_entry.grid(row=2, column=1)

            self.itype_label.grid(row=3, column=0)
            self.itype_entry.grid(row=3, column=1)

            # Creating a submit button
            self.sub_btn.grid(row=4, column=1)

    #def submit(self):
        




root = tk.Tk()
gui = Helpme(root)
root.mainloop()
