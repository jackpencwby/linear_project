import tkinter as tk
import customtkinter as custk

class Guide:
    def __init__(self,parent):
        self.frame = tk.Frame(parent,bg='#e9eaed')

        #inside frame
        self.lbframe = tk.LabelFrame(self.frame,text="Properties Range",width=500,height=200,bd=5)
        self.lbframe.pack(fill="both",padx=25,pady=10)

        self.lbframe2 = tk.LabelFrame(self.frame,text="Portfolio Risk Range",width=500,height=200,bd=5)
        self.lbframe2.pack(fill="both",padx=25,pady=10)

        buttonwidth = 35

        #inside labelframe properties range
        self.pelabel = tk.Label(self.lbframe,text="P/E Ratio ")
        self.pelabel.grid(row=1,column=1,pady=5)

        self.button = tk.Button(self.lbframe,width=buttonwidth,text="5 - 200")
        self.button.grid(row=1,column=2,pady=5)

        self.epslabel = tk.Label(self.lbframe,text="EPS Growth (%) ")
        self.epslabel.grid(row=2,column=1,pady=5)

        self.button = tk.Button(self.lbframe,width=buttonwidth,text="10% - 110%")
        self.button.grid(row=2,column=2,pady=5)

        self.roelabel = tk.Label(self.lbframe,text="ROE (%) ")
        self.roelabel.grid(row=3,column=1,pady=5)

        self.button = tk.Button(self.lbframe,width=buttonwidth,text="0% - 500%")
        self.button.grid(row=3,column=2,pady=5)

        self.epslabel = tk.Label(self.lbframe,text="Divident Yield (%)")
        self.epslabel.grid(row=4,column=1,pady=5)

        self.button = tk.Button(self.lbframe,width=buttonwidth,text="0% - 6%")
        self.button.grid(row=4,column=2,pady=5)

        self.pfmlabel = tk.Label(self.lbframe,text="Performance Year")
        self.pfmlabel.grid(row=5,column=1,pady=5)

        self.button = tk.Button(self.lbframe,width=buttonwidth,text="1, 2, 5")
        self.button.grid(row=5,column=2,pady=5)
    
        self.epslabel = tk.Label(self.lbframe,text="Performance (%)")
        self.epslabel.grid(row=6,column=1,pady=5)

        self.button = tk.Button(self.lbframe,width=buttonwidth,text="-50% - 2000%")
        self.button.grid(row=6,column=2,pady=5)

        self.warnlabel = tk.Label(self.lbframe,text="Guide Message : ")
        self.warnlabel.grid(row=7,column=1,pady=5)

        self.warnlabel2 = tk.Label(self.lbframe,text="Always input Indexes / Input every properties")
        self.warnlabel2.grid(row=7,column=2,pady=5)
        
        #inside labelframe portfolio risk range
        self.riskbar = custk.CTkProgressBar(self.lbframe2,width=350,height=10,border_width=0.5,orientation="horizontal",progress_color="#32CD32",fg_color="#d9d9d9")
        self.riskbar.grid(row=1,columnspan=3,padx=(10,0),pady=(5,0))
        self.riskbar.set(0)

        self.label = tk.Label(self.lbframe2,text="   0")
        self.label.grid(row=2,column=0,sticky="w")

        self.label2 = tk.Label(self.lbframe2,text="10")
        self.label2.grid(row=2,column=2,sticky="e")

        self.pelabel = tk.Label(self.lbframe2,text="0-3 : ")
        self.pelabel.grid(row=3,column=0,pady=5)

        self.button = tk.Button(self.lbframe2,width=buttonwidth,text="Diversified Portfolio")
        self.button.grid(row=3,column=1,pady=5,sticky='w')

        self.epslabel = tk.Label(self.lbframe2,text="3-5 : ")
        self.epslabel.grid(row=4,column=0,pady=5)

        self.button = tk.Button(self.lbframe2,width=buttonwidth,text="Balanced Portfolio")
        self.button.grid(row=4,column=1,pady=5,sticky='w')

        self.roelabel = tk.Label(self.lbframe2,text="5-8 : ")
        self.roelabel.grid(row=5,column=0,pady=5)

        self.button = tk.Button(self.lbframe2,width=buttonwidth,text="Proactived Portfolio")
        self.button.grid(row=5,column=1,pady=5,sticky='w')

        self.epslabel = tk.Label(self.lbframe2,text="8-10 : ")
        self.epslabel.grid(row=6,column=0,pady=5)

        self.button = tk.Button(self.lbframe2,width=buttonwidth,text="Specialized Portfolio")
        self.button.grid(row=6,column=1,pady=5,sticky='w')

        self.warnlabel = tk.Label(self.lbframe2,text="Guide Message : ")
        self.warnlabel.grid(row=7,column=0,pady=5)

        self.warnlabel2 = tk.Label(self.lbframe2,text="Add 3-10 Stocks from menu / Use Heatmap")
        self.warnlabel2.grid(row=7,column=1,pady=5)


