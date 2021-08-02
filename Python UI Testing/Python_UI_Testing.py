from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from importlib import reload
from datetime import *
import pypyodbc

conn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=(localdb)\\ProjectsV13; DATABASE=test; Trusted_Connection=Yes')
cursor = conn.cursor();

class Application(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.page5_label = StringVar()
        self.shared_data = {
                "fn":StringVar()
            }
        
        window = Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500) #500 / 1000
        window.grid_columnconfigure(0, minsize=800) #800 / 1500

        window.grid_rowconfigure(0, minsize=1000) #500 or 1000
        window.grid_columnconfigure(0, minsize=1500) #800 or 1500

        self.T5 = StringVar()
        

        self.frames = {}
        for f in(firstPage, secondPage_lost, thirdPage_found, fourPage_found, fivePage_lost, iphone, tablet, laptop, umbrella):
            frame = f(window, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0,sticky="nsew")
        self.show_frame(firstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Lost and Found Application")

    

    
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
        self.T2 = Entry(border, width =30, bd=5, textvariable= self.controller.shared_data["fn"])
        data = IntVar()
        entry = Entry(textvariable = data)
        self.T2.place(x=200,y=65)
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
        self.controller.T5.set(T5)

       
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
            if T1.get() == '' or self.T2.get() ==''or T4.get() == '' or T5.get() == '':
                messagebox.showinfo("Error", "Please ensure all blanks have been filled!")
            else:
                 z = entry_to_Int(self.T2.get())
                 if type(z) != int:
                    messagebox.showinfo("Error", "Please only enter numbers")
                 else: 
                     z = str(z)
                     if len(z) != 8:
                        messagebox.showinfo("Error", "Please enter your 8 digit number")
                     else:
                        #Compare SQL Statement
                        sql_query ="select * from item"
                        cursor.execute(sql_query)
                        details = cursor.fetchall()


                        if T4.get() in details[0][2] and T5.get() in details[0][7]:
                            controller.show_frame(iphone)
                        elif T4.get() in details[1][2] and T5.get() in details[1][7]:
                            controller.show_frame(tablet)
                        elif T4.get() in details[2][2] and T5.get() in details[2][7]:
                            controller.show_frame(laptop)
                        elif T4.get() in details[3][2] and T5.get() in details[3][7]:
                            controller.show_frame(umbrella)

                        else:
                            controller.show_frame(fivePage_lost)     
                            

            #insertv = self.controller.shared_data(["fn"]).set(self.T2.get())
            #self.controller.page5_label.set(self.T2.get())
            #print(self.controller.page5_label.get())
            #self.controller.lbl.config(text=T2.get())
        
        bHome = Button(self, text="Back",font=("Arial",15), command=lambda:controller.show_frame(firstPage)).place(x=200, y=750) #x=100, y=450 or x=200, y=900
        bNext = Button(self, text="Submit",font=("Arial",15), command=verify).place(x=900, y=750) #x = 600, y=450 or x and y =900        

   
        

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
        T6 = DateEntry(border, selectmode = 'day').place(x=500, y=255)
        l7 = Label(border, text="Height of item (If you know, else don't need)",font=("Arial",15)).place(x=20, y=445)
        T7 = Entry(border, width =50, bd=5).place(x=500,y=435)
        l8 = Label(border, text="Length of item (If you know, else don't need)",font=("Arial",15)).place(x=20, y=495)
        T8 = Entry(border, width =50, bd=5).place(x=500,y=485)
        l9 = Label(border, text="Width of item (If you know, else don't need)",font=("Arial",15)).place(x=20, y=545)
        T9 = Entry(border, width =50, bd=5).place(x=500,y=535)
        self.controller.T5.set(T5)
        
       


        def verify():
            if T1.get() == '' or T2.get() == '' or T3.get() == '' or T4.get() == '' or T5.get() == '':
                messagebox.showinfo("Error", "Please ensure all blanks have been filled!")
            else:
                item_query ="select * from item"
                cursor.execute(item_query)
                itemlist = cursor.fetchall()

                box_query ="select * from box"
                cursor.execute(box_query) 
                boxlist = cursor.fetchall()
                
                itemIDlist = []
                boxIDlist = []
                i = 0;

                while i < len(itemlist):

                    if itemlist[i][8] != 0:
                        itemIDlist.append(itemlist[i][8]);
                        i = i + 1;

                    else:
                        i = i + 1
                    #it works!!


                i = 0;
                while i < len(boxlist):

                    boxIDlist.append(boxlist[i][0]);
                    i = i +1;
                    #it works here too!!



                checklist = []

                listOne = set(itemIDlist)
                listTwo = set(boxIDlist)
                    
                checklist = list(listTwo-listOne)
                today = date.today()
                print(type(today))
                print(today)
                today = str(today)
                
                rightNow = datetime.now()
                correctDay = rightNow.strftime("%d/%m/%Y")
                print(correctDay)
                
                count = 0;
                itemKeylist = []

                while count < len(itemlist):
                    itemKeylist.append(itemlist[count][0])
                    count = count + 1

                biggest = 0;

                for checkbig in itemKeylist:
                    if checkbig > biggest:
                        biggest = checkbig;
                    else:
                        break;

                id = biggest + 1;
                id = str(id);
                
                for check in checklist:


                    if T3.get() == "phone":
                        if check == 1:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc,  Date, found_item_location, box_id) VALUES" 
                                   + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                   + T5.get() + " + " + check
                                   )
                        elif check == 2:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                   + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                   + T5.get() + " + " + check
                                   )
                        else:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + "00"
                                            )


                    elif T3.get() == "tablet":
                        if check == 3:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + check
                                            )
                        elif check == 4:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + check
                                            )
                        else:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + "00"
                                            )
                    elif T3.get() == "laptop":
                        if check == 5:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + check
                                            )
                        elif check == 6:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + check
                                            )
                        else:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, item_height, item_length, item_width, Date, found_item_location, box_id) VALUES" 
                                            + T3.get() + " + " + T4.get() + " + " + T7.get() + " + " + T8.get() + " + " + T9.get() + " + " + T6.get_date() + " + " 
                                            + T5.get() + " + " + "00"
                                            )
                    else:
                            cursor.execute("Insert Into item(item_id, item_type, item_desc, Date, found_item_location, box_id) VALUES ( '" 
                                            + id + "' , '"+ T3.get() + "' , '" + T4.get() + "' , '" + correctDay + "' , '" 
                                            + T5.get() + "' , " + "00)"
                                            )
                
                fourPage_found.reload();
                controller.show_frame(fourPage_found)
            
        
        bHome = Button(self, text="Back",font=("Arial",15), command=lambda:controller.show_frame(firstPage)).place(x=200, y=750) #x=200. y=900
        bNext = Button(self, text="Submit",font=("Arial",15), command=verify).place(x=900, y=750) #x=200, y=900
        

#verify code check from database when user want to retr
class fourPage_found(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        border = LabelFrame(self, text="Dipslay",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes")
        label1 = Label(border, textvariable=self.controller.T5).place(x=20, y=15)
        
        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()
        last = len(details) - 1

        boxid = "Box " + str(details[last][8]);
        
#        l1 = Label(border, text=boxid,font=("Arial",15)).place(x=50, y=25)
#        l2 = Label(border, text=details[last][1],font=("Arial",15)).place(x=50, y=50)
#        l3 = Label(border, text=details[last][2],font=("Arial",15)).place(x=50, y=75)
#        l4 = Label(border, text=details[last][3],font=("Arial",15)).place(x=50, y=100)
#        l5 = Label(border, text=details[last][4],font=("Arial",15)).place(x=50, y=125)
#        l6 = Label(border, text=details[last][5],font=("Arial",15)).place(x=50, y=150)
#        l7 = Label(border, text=details[last][6],font=("Arial",15)).place(x=50, y=175)
#        l8 = Label(border, text=details[last][7],font=("Arial",15)).place(x=50, y=200)

        
#        l1=Label(self, text="four",font=("Arial bold",30))
#        l1.place(x=230, y=230)
        
        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(thirdPage_found))
        bHome.place(x=100, y=450)


#give code to user who submit the LOST item
class fivePage_lost(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.lbl = Label(self, text="Your Item has not been found yet.",font=("Arial bold",30))
        self.lbl.place(x=300, y=230)


        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(firstPage))
        bHome.place(x=200, y=750) #x=100, y =450
        
        
class iphone(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Your item has been found!",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)

        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            
            if row[2] == "iphone 12 red":
                box = "Box " + str(row[8]);
                l1 = Label(border, text=box,font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=75)
                l4 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=100)
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=200, y=750)


class tablet(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Your item has been found!",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)


        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            if row[2] == "galaxy tab s7":
                box = "Box " + str(row[8]);
                l1 = Label(border, text=box,font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=75)
                l4 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=100)
        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=200, y=750)



class laptop(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Your item has been found!",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)


        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            if row[2] == "macbook pro 16 in":
                box = "Box " + str(row[8]);
                l1 = Label(border, text=box,font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=75)
                l4 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=100)
        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=200, y=750)


class umbrella(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        border = LabelFrame(self, text="Your item has been found!",bg="ivory",bd=10, font=("Arial",20))
        border.pack(fill="both", expand="yes",padx=150, pady=100)


        sql_query ="select * from item"
        cursor.execute(sql_query)
        details = cursor.fetchall()

        for row in details:
            if row[2] == "umbrella (not collapsible)":
                box = "Box " + str(row[8]);
                l1 = Label(border, text=box,font=("Arial",15)).place(x=50, y=25)
                l2 = Label(border, text=row[1],font=("Arial",15)).place(x=50, y=50)
                l3 = Label(border, text=row[2],font=("Arial",15)).place(x=50, y=75)
                l4 = Label(border, text=row[7],font=("Arial",15)).place(x=50, y=100)

        
        
        
        bHome = Button(self, text="previous",font=("Arial",15), command=lambda:controller.show_frame(secondPage_lost))
        bHome.place(x=200, y=750)

app = Application()
app.mainloop()
