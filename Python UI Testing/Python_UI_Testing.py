import argparse
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('UI Test')
root.geometry('600x300')

b1 = Button(root, text="Found Something", height=10, width=20, command=None).place(x=100, y=50)
b2 = Button(root, text="Retrieve Something", height=10, width=20, command=None).place(x=350, y=50)

root.mainloop()
