from tkinter import *


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo,PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
            
            self.show_frame(StartPage)
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()
            
            

#start page coding
class StartPage(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text="Lost and Found")
        label.pack(padx=10, pady=10)
        
        
        button1 = Button(self, text="Lost",width=50, height=5,border=1, command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2= Button(self, text ="Found", width=50, height=5,border=1, command=lambda:controller.show_frame(PageTwo))
        button2.pack()
#Page 1
class PageOne(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text="Page one")
        label.pack(padx=10, pady=10)
        OPTIONS = [
            "select Option",
            "Phone",
            "Key",
            "Wallet",
            "Card",
            
                ]
        master = self
        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value

        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()
        page_four= Button(self, text ="enter", command=lambda:controller.show_frame(PageFour))
        Start_page= Button(self, text ="HomePage", command=lambda:controller.show_frame(StartPage))
        page_four.pack()
        Start_page.pack(side=BOTTOM)
        Start_page.pack(side=RIGHT)
         

class PageTwo(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text="Found Item")
        label.pack(padx=10, pady=10)
        
        place = Label(self,text="Place found")
        place.pack(side=LEFT)
        place_e = Entry(self)
        place_e.pack(side=LEFT)
        
        item = Label(self,text="Item")
        item.pack(side=LEFT)
        item_e = Entry(self)
        item_e.pack(side=LEFT)
        
        L1 = Label(self,text="Alalalalala")
        L1.pack(side=LEFT)
        E1 = Entry(self)
        E1.pack(side=LEFT)

        Start_page= Button(self, text ="HomePage", command=lambda:controller.show_frame(StartPage))
        Start_page.pack(side=BOTTOM)
        #Start_page.pack(side=RIGHT)

class PageFour(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text="Page 4")
        label.pack(padx=10, pady=10)
        alist = ["00000001","00000002", "00000003"]
        blist = ["Samsung S10", "Apple X", "Huawei Nova 7i"]
        total = len(alist)
        i = 0
        listbox1 = Listbox(self)
        listbox2 = Listbox(self)
        scrollbar1 = Scrollbar(self)
        scrollbar2 = Scrollbar(self)
        scrollbar1.pack(side= LEFT, fill = BOTH)
        scrollbar2.pack(side= RIGHT, fill = BOTH)
        listbox1.pack(side = LEFT)
        listbox2.pack (side = RIGHT)
        for i in range(total):
            listbox1.insert(END, alist[i])
            listbox2.insert(END, blist[i])
            i = i+1
        listbox1.config(yscrollcommand = scrollbar1.set)
        listbox2.config(yscrollcommand = scrollbar2.set)
        
        scrollbar1.config(command = listbox1.yview)
        scrollbar2.config(command = listbox2.yview)
        button1= Button(self, text ="HomePage", command=lambda:controller.show_frame(StartPage))
        button1.pack(side=BOTTOM)

       

app = App()

app.mainloop()
        
        
