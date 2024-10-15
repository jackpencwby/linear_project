import tkinter as tk

class Credit:
    def __init__(self,parent):
        self.frame = tk.Frame(parent,bg='#e9eaed')

        #inside frame
        self.lbframe = tk.LabelFrame(self.frame,text="Creators",width=500,height=200,bd=5)
        self.lbframe.pack(fill="both",padx=25,pady=10)

        self.lbframe2 = tk.LabelFrame(self.frame,text="About Project",width=500,height=200,bd=5)
        self.lbframe2.pack(fill="both",padx=25,pady=10)

        buttonwidth = 35

        #inside labelframe creators
        self.label = tk.Label(self.lbframe,text="66010023 ")
        self.label.grid(row=1,column=1,padx=(5,0),pady=5)

        self.button = tk.Button(self.lbframe,anchor="w",width=buttonwidth,text="Krittapas Theerasatayapipat")
        self.button.grid(row=1,column=2,pady=5)

        self.label = tk.Label(self.lbframe,text="66010089 ")
        self.label.grid(row=2,column=1,padx=(5,0),pady=5)

        self.button = tk.Button(self.lbframe,anchor="w",width=buttonwidth,text="Kajonyod Juleart")
        self.button.grid(row=2,column=2,pady=5)

        self.label = tk.Label(self.lbframe,text="66010270 ")
        self.label.grid(row=3,column=1,padx=(5,0),pady=5)

        self.button = tk.Button(self.lbframe,anchor="w",width=buttonwidth,text="Nattawut Masang")
        self.button.grid(row=3,column=2,pady=5)

        self.label = tk.Label(self.lbframe,text="66010358 ")
        self.label.grid(row=4,column=1,padx=(5,0),pady=5)

        self.button = tk.Button(self.lbframe,anchor="w",width=buttonwidth,text="Thammatorn Tanasamanchoke")
        self.button.grid(row=4,column=2,pady=5)

        
        #inside labelframe about project
        self.label = tk.Label(self.lbframe2,text="This Project was made as a part of Subject 01076032")
        self.label.grid(row=1,column=1,padx=(5,0),pady=(5,0.25))
        self.label = tk.Label(self.lbframe2,text="ELEMENTARY DIFFERENTIAL EQUATIONS AND LINEAR ALGEBRA")
        self.label.grid(row=2,column=1,padx=(5,0),pady=(0,15))
        self.label = tk.Label(self.lbframe2,text="Engineering Faculty, Computer Engineering Branch")
        self.label.grid(row=3,column=1,padx=(5,0),pady=0.25)
        self.label = tk.Label(self.lbframe2,text="Undergratuated Bachelor Year 2, Semester 1 College Year 2567")
        self.label.grid(row=4,column=1,padx=(5,0),pady=0.25)
        self.label = tk.Label(self.lbframe2,text="King Mongkut\'s Institute of Technology Ladkrabang")
        self.label.grid(row=5,column=1,padx=(5,0),pady=0.25)

        self.label = tk.Label(self.lbframe2,text="© Copyright 2024 For Educational Purpose Only")
        self.label.grid(row=6,column=1,padx=(5,0),pady=15)


