import argparse
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('UI Test')
root.geometry('600x300')

b1 = Button(root, text="Found Something", height=10, width=20, command=None).place(x=100, y=50)
b2 = Button(root, text="Retrieve Something", height=10, width=20, command=None).place(x=350, y=50)


# Delcaring variables to store details
fname_var = tk.StringVar() #Finder name
fid_var = tk.StringVar() #Finder ID
iname_var = tk.StringVar() #Item name
itype_var = tk.StringVar() #Item type

# How should I store the date?


# Defining a function that will get the details
# and print them on the screen
def submit():

    fname = fname_var.get()
    fid = fid_var.get()
    iname = iname_var.get()
    itype = itype_var.get()

    print ("Your name is: " + fname)
    print ("Your ID is: " + fid)
    print ("The item's name is: " + iname)
    print ("The item type is : " + itype)

    fname_var.set("")
    fid_var.set("")
    iname_var.set("")
    itype_var.set("")


    fname_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    fname_entry = tk.Entry(root,textvariable = fname_var, font=('calibre',10,'normal'))

    fid_label = tk.Label(root, text = 'ID', font=('calibre',10, 'bold'))
    fid_entry = tk.Entry(root,textvariable = fid_var, font=('calibre',10,'normal'))

    iname_label = tk.Label(root, text = 'Item name', font=('calibre',10, 'bold'))
    iname_entry = tk.Entry(root,textvariable = iname_var, font=('calibre',10,'normal'))

    itype_label = tk.Label(root, text = 'Item type', font=('calibre',10, 'bold'))
    itype_entry = tk.Entry(root,textvariable = itype_var, font=('calibre',10,'normal'))


    # Creating a button using the widget
    # Button that will call the submit function
    sub_btn = tk.Button(root,text = 'Submit', command = submit)

    # Placing the label and entry in the required position using grid method
    fname_label.grid(row=0, column=0)
    fname_entry.grid(row=0, column=1)

    fid_label.grid(row=1, column=0)
    fid_entry.grid(row=1, column=1)

    iname_label.grid(row=2, column=0)
    iname_entry.grid(row=2, column=1)

    itype_label.grid(row=3, column=0)
    itype_entry.grid(row=3, column=1)

    # Creating a submit button
    sub_btn.grid(row=4, column=1)

root.mainloop()
