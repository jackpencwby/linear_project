import tkinter as tk
from tkinter import ttk
from processing.vector import Vector

port = []
showlist = []
boollist = []
vectorlist = []

class Menu:
    def __init__(self, parent):
        self.frame = tk.Frame(parent,bg='#e9eaed')
        self.index = None
        self.pfmyear = 1
        self.addlist = []

        #inside frame
        self.lbframe = tk.LabelFrame(self.frame, text="Stock Properties", width=500, height=200,bd=5)
        self.lbframe.pack(fill="both", padx=25, pady=10)

        self.lbframe2 = tk.LabelFrame(self.frame, text="Result", width=500, height=200,bd=5)
        self.lbframe2.pack(fill="both", padx=25, pady=10)

        #inside labelframe stock properties
        #indexes
        self.indexlabel = tk.Label(self.lbframe, text="              Indexes :")
        self.indexlabel.grid(row=1, column=1, pady=10,sticky='w')
        index = [
            "All Indexes", 
            "Dow Jones", 
            "S&P500", 
            "Nasdaq", 
        ]

        string = tk.StringVar()
        string.set("Select Index")
        self.optionmenu1 = tk.OptionMenu(self.lbframe, string, *index, command=self.updateIndex)
        self.optionmenu1.grid(row=1, column=2,padx=8, pady=10)

        self.pelabel = tk.Label(self.lbframe, text="              P/E Ratio")
        self.pelabel.grid(row=2, column=1, pady=5,sticky='w')

        self.entry1 = tk.Entry(self.lbframe, width=25)
        self.entry1.grid(row=2, column=2,padx=8, pady=5)

        self.epslabel = tk.Label(self.lbframe, text="              EPS Growth (%)")
        self.epslabel.grid(row=3, column=1, pady=5,sticky='w')

        self.entry2 = tk.Entry(self.lbframe, width=25)
        self.entry2.grid(row=3, column=2, pady=5)

        self.roelabel = tk.Label(self.lbframe, text="              ROE (%)")
        self.roelabel.grid(row=4, column=1, pady=5,sticky='w')

        self.entry3 = tk.Entry(self.lbframe, width=25)
        self.entry3.grid(row=4, column=2,padx=8, pady=5)

        self.epslabel = tk.Label(self.lbframe, text="              Divident Yield (%)")
        self.epslabel.grid(row=5, column=1, pady=5,sticky='w')

        self.entry4 = tk.Entry(self.lbframe, width=25)
        self.entry4.grid(row=5, column=2,padx=8, pady=5)

        self.pfmlabel = tk.Label(self.lbframe, text="              Performance Year")
        self.pfmlabel.grid(row=6, column=1, pady=5,sticky='w')
        year = [
            "1 Year", 
            "2 Years", 
            "5 Years"
        ]

        string = tk.StringVar()
        string.set("Select Year")
        self.optionmenu2 = tk.OptionMenu(self.lbframe, string, *year, command=self.updatePfmyear)
        self.optionmenu2.grid(row=6, column=2,padx=8, pady=10)

        self.epslabel = tk.Label(self.lbframe, text="              Performance (%)")
        self.epslabel.grid(row=7, column=1, pady=5,sticky='w')

        self.entry5 = tk.Entry(self.lbframe, width=25)
        self.entry5.grid(row=7, column=2,padx=8, pady=5)

        #submit button
        self.button = tk.Button(self.lbframe, text="Search" ,width=8, command=self.handleSubmit, bg="#80E12A")
        self.button.grid(row=8, column=1,padx=(30,0), pady=(10,15))

        self.warnlabel = tk.Label(self.lbframe, text="")

        #inside labelframe result
        for i in range(10):
            showlist.append(tk.Button(self.lbframe2, width=40, anchor="nw"))
            boollist.append(False)
            self.addlist.append(tk.Button(self.lbframe2, width=5, anchor="nw", text="Add", bg="orange"))
        for i in range(10):
            showlist[i].grid(row=i+1, column=1, padx=(10, 0), pady=5)
            self.addlist[i].grid(row=i+1, column=2, padx=(0, 10), pady=5)


    def updateIndex(self, selection):
        self.index = selection

    def updatePfmyear(self, selection):
        if selection == "1 Year":
            self.pfmyear = 1
        elif selection == "2 Years":
            self.pfmyear = 2
        elif selection == "5 Years":
            self.pfmyear = 5

    def handleSubmit(self):
        varlist = []

        if self.index == "All Indexes":
            self.index = "All Indexes"
        elif self.index == "Dow Jones":
            self.index = "DJIA"
        elif self.index == "Nasdaq":
            self.index = "NASDAQ"

        try:
            varlist.append(self.index)
            varlist.append(None if self.entry1.get() == "" else float(self.entry1.get()))
            varlist.append(None if self.entry2.get() == "" else float(self.entry2.get()))
            varlist.append(None if self.entry3.get() == "" else float(self.entry3.get()))
            varlist.append(None if self.entry4.get() == "" else float(self.entry4.get()))
            varlist.append(self.pfmyear)
            varlist.append(None if self.entry5.get() == "" else float(self.entry5.get()))
        except:
            self.warnlabel.config(text="Please enter numerical information", fg="red")
            self.warnlabel.grid(row=8, column=2, pady=10)
            return 0

        isNone = False
        for ele in varlist:
            if ele == None:
                isNone = True
                break

        if isNone:
            self.warnlabel.config(text="Not enough input", fg="red")
            self.warnlabel.grid(row=8, column=2, pady=10)
            return 0
        elif self.index == None:
            self.warnlabel.config(text="Please input index", fg="red")
            self.warnlabel.grid(row=8, column=2, pady=10)
            return 0 
        else:
            self.warnlabel.config(text="Input Completed!", fg="green")
            self.warnlabel.grid(row=8, column=2, pady=10)
                
        v = Vector(varlist[0], varlist[1], varlist[2], varlist[3], varlist[4], varlist[5], varlist[6])
        if len(vectorlist) > 0:
            vectorlist.clear()
        vectorlist.extend(v.filter_stocks())

        #inside labelframe result
        for i in range(10):
            showlist[i].config(text="{:.6f}".format(vectorlist[i][7]) + "       " + vectorlist[i][0])
            showlist[i].configure(command=lambda index=i: self.handleClickshow(index, showlist[index]))
            self.addlist[i].configure(command=lambda index=i: self.handleClickadd(index, showlist[index]))

    def handleClickshow(self, index, button):
        if boollist[index] == False:
            button.config(justify="left", text= vectorlist[index][1] + " (" + vectorlist[index][0] + ")" + "\n-----------------------------\n" + "P/E Ratio : " + "{:.2f}".format(vectorlist[index][2], 2) + "     " + "EPS Growth : " + "{:.2f}".format(vectorlist[index][3], 2) + " %\n" + "Return On Equity : " + "{:.2f}".format(vectorlist[index][4], 2) + " %     " + "Dividend Yield : " + "{:.2f}".format(vectorlist[index][5], 2) + " %\n" + "Performance " + str(self.pfmyear) + " Year(s) : " + "{:.2f}".format(vectorlist[index][6], 2) + '%   ' + vectorlist[index][14])
            boollist[index] = True
        elif boollist[index] == True:
            button.config(text="{:.6f}".format(vectorlist[index][7]) + "       " + vectorlist[index][0])
            boollist[index] = False

    def handleClickadd(self, index, showbutton):
        if len(port) >= 0 and len(port) < 10:
            print(index,vectorlist)
            showbutton.config(text="Added " + vectorlist[index][0] + " to your Portfolio")
            self.checkport(port, vectorlist[index])
            print(boollist)
        else:
            showbutton.config(text="Your Portfolio limit exceeded")
        print("from menu", len(port))

    def checkport(self, list, object):
        isdup = False
        if len(list) < 10:
            for i in range(len(list)):
                if list[i][0] == object[0]:
                    isdup = True
        if not isdup:
            list.append(object)

        





