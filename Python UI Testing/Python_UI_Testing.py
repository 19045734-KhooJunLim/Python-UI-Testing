from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import pypyodbc
conn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=(localdb)\\ProjectsV13; DATABASE=test; Trusted_Connection=Yes')
cursor = conn.cursor();

class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.app_data = {}
        
        window = Frame(self)
        window.pack()
<<<<<<< HEAD
        window.grid_rowconfigure(0, minsize=500) #500 / 1000
        window.grid_columnconfigure(0, minsize=800) #800 / 1500
=======
        window.grid_rowconfigure(0, minsize=1000) #500 or 1000
        window.grid_columnconfigure(0, minsize=1500) #800 or 1500
>>>>>>> 11cb11b0231a6ad7b8448db03317c2286190bb9a
        self.T5 = StringVar()
        

        self.frames = {}
        for f in(firstPage, secondPage_lost, thirdPage_found, fourPage_found, fivePage_lost, iphone, tab, mac, umbrella):
            frame = f(window, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0,sticky="nsew")
        self.show_frame(firstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Lost and Application")

    

    
class firstPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        border = LabelFrame(self, text="",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150,pady=100)
        
        l1 = Label(border, text="Selection Page",font=("Arial bold",25))
        l1.place(x=120, y=50)
        
        bLost = Button(border, text="Lost an Item",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bFound = Button(border, text="Found an Item ",font=("Arial",15), command=lambda:controller.show_frame(thirdPage_found))
        bLost.place(x=160, y=100)
        bFound.place(x=150, y=150)
        
#report lost
class secondPage_lost(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        border = LabelFrame(self, text="Form",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)
        
        l1 = Label(border, text="Full name",font=("Arial",15)).place(x=20, y=15)
        T1 = Entry(border, width =30, bd=5)
        T1.place(x=200,y=15)
        l2 = Label(border, text="Contact Number",font=("Arial",15)).place(x=20, y=65)
        T2 = Entry(border, width =30, bd=5)
        data = IntVar()
        entry = Entry(textvariable = data)
        T2.place(x=200,y=65)
        l3 = Label(border, text="Item Type Lost",font=("Arial",15)).place(x=20, y=115)
        cursor.execute("SELECT DISTINCT item_type FROM item")
        testresult = cursor.fetchall()
        testvariable = StringVar()
        test = [list(i) for i in testresult]
        testvariable.set(test[3])
        T3 = OptionMenu(border, testvariable, *test)
        T3.place(x=200,y=115)
        l4 = Label(border, text="Item Description",font=("Arial",15)).place(x=20, y=165)
        T4 = Entry(border, width =30, bd=5)
        T4.place(x=200,y=165)
        l5 = Label(border, text="Where you lost it",font=("Arial",15)).place(x=20, y=215)
        T5 = Entry(border, width =30, bd=5)
        T5.place(x=200,y=215)
        l6 = Label(border, text="Item Code (if available)",font=("Arial",15)).place(x=20, y=265)
        T6 = Entry(border, width =30, bd=5).place(x=240,y=265)
        self.controller.T5.set(T5)
        
       #cursor.execute("Select item_desc, box_id FROM item Inner Join box ON item.box_id = box.box_id WHERE retrieve_code=T6")

        def entry_to_Int(value):
                a = []
                b = ''
                for i in value:
                    ii = int(i)
                    a.append(ii)
                for i in a:
                    b = b + str(i)
                    c = int(b)
                return c
            

        def verify():
            if T1.get() == '' or T2.get() == ''or T4.get() == '' or T5.get() == '':
                messagebox.showinfo("Error", "Please ensure all blanks have been filled!")
            else:
                 z = entry_to_Int(T2.get())
                 if type(z) != int:
                    messagebox.showinfo("Error", "Please only enter numbers")
                 else: 
                     z = str(z)
                     if len(z) != 8:
                        messagebox.showinfo("Error", "Please enter your 8 digit number")
                     else:
                        controller.show_frame(fivePage_lost)

        
        bHome = Button(self, text="Back",font=("Arial",15), command=lambda:controller.show_frame(firstPage)).place(x=100, y=450) #x=100, y=450 or x=200, y=900
        bNext = Button(self, text="Submit",font=("Arial",15), command=verify).place(x=600, y=450) #x = 600, y=450 or x and y =900
        b1 = Button(self, text="iPhone",font=("Arial",15), command=lambda:controller.show_frame(iphone)).place(x=200, y=450)
        b2 = Button(self, text="Galaxy Tab",font=("Arial",15), command=lambda:controller.show_frame(tab)).place(x=280, y=450)
        b3 = Button(self, text="Macbook",font=("Arial",15), command=lambda:controller.show_frame(mac)).place(x=400, y=450)
        b4 = Button(self, text="Umbrella",font=("Arial",15), command=lambda:controller.show_frame(umbrella)).place(x=500, y=450)
        
        
#claim found
class thirdPage_found(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        border = LabelFrame(self, text="Form",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)
        
        l1 = Label(border, text="Full name",font=("Arial",15)).place(x=20, y=15)
        T1 = Entry(border, width =50, bd=5)
        T1.place(x=500,y=5)
        l2 = Label(border, text="Contact Number",font=("Arial",15)).place(x=20, y=55)
        T2 = Entry(border, width =50, bd=5)
        T2.place(x=500,y=55)
        l3 = Label(border, text="Item Type Found",font=("Arial",15)).place(x=20, y=105)
        T3 = Entry(border, width =50, bd=5)
        T3.place(x=500,y=105)
        l4 = Label(border, text="Item Description",font=("Arial",15)).place(x=20, y=155)
        T4 = Entry(border, width =50, bd=5)
        T4.place(x=500,y=155)
        l5 = Label(border, text="Where did you find the item",font=("Arial",15)).place(x=20, y=205)
        T5 = Entry(border, width =50, bd=5)
        T5.place(x=500,y=205)
        l6 = Label(border, text="Date",font=("Arial",15)).place(x=20, y=255)
        T6 = Calendar(border, selectmode = 'day').place(x=500, y=255)
        l7 = Label(border, text="Height of item (If you know, else don't need)",font=("Arial",15)).place(x=20, y=445)
        T7 = Entry(border, width =50, bd=5).place(x=500,y=435)
        l8 = Label(border, text="Length of item (If you know, else don't need)",font=("Arial",15)).place(x=20, y=495)
        T8 = Entry(border, width =50, bd=5).place(x=500,y=485)
        l9 = Label(border, text="Width of item (If you know, else don't need)",font=("Arial",15)).place(x=20, y=545)
        T9 = Entry(border, width =50, bd=5).place(x=500,y=535)
        self.controller.T5.set(T5)
        
       


        def verify():
            if T1.get() == '' or T2.get() == '' or T3.get() == '' or T4.get() == '' or T5.get() == '' or T6.get() == '':
                messagebox.showinfo("Error", "Please ensure all blanks have been filled!")
            else:
                cursor.execute("INSERT INTO item({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})")
                controller.show_frame(fourPage_found)
            
        
        bHome = Button(self, text="Back",font=("Arial",15), command=lambda:controller.show_frame(firstPage)).place(x=200, y=900)
        bNext = Button(self, text="Submit",font=("Arial",15), command=verify).place(x=900, y=900)
        

#verify code check from database when user want to retr
class fourPage_found(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        border = LabelFrame(self, text="Form",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes")
        label1 = Label(border, textvariable=self.controller.T5).place(x=20, y=15)
        
    
        
#        l1=Label(self, text="four",font=("Arial bold",30))
#        l1.place(x=230, y=230)
        
        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(thirdPage_found))
        bHome.place(x=100, y=450)

#give code to user who submit the LOST item
class fivePage_lost(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        l1 = Label(self, text="fifth",font=("Arial bold",30))
        l1.place(x=230, y=230)

        

        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(firstPage))
        bHome.place(x=100, y=450)
        
        
class iphone(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Display",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)

        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            
            if row[2] == "iphone 12 red":
                l1 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=75)
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=100, y=450)


class tab(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Display",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)


        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            if row[2] == "galaxy tab s7":
                l1 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=75)
        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=100, y=450)



class mac(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Display",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)


        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            if row[2] == "macbook pro 16 in":
                l1 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=75)
        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=100, y=450)


class umbrella(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Display",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)


        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            if row[2] == "umbrella (not collapsible)":
                l1 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=75)

        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=100, y=450)

app = Application()
app.mainloop()
