import tkinter as tk
import customtkinter as custk
from frames.menu import port , showlist , boollist , vectorlist
from processing.matrix import Matrix

class Port:
    def __init__(self, parent):
        self.frame = tk.Frame(parent,bg='#e9eaed')
        self.showlist = []

        #inside frame
        self.lbframe = tk.LabelFrame(self.frame, text="Your Portfolio", width=500, height=200,bd=5)
        self.lbframe.pack(fill="both", padx=25, pady=10)

        self.lbframe2 = tk.LabelFrame(self.frame, text="Risk", width=500, height=200,bd=5)
        self.lbframe2.pack(fill="both", padx=25, pady=10)

        self.lbframe3 = tk.LabelFrame(self.frame, text="Heatmap", width=500, height=200,bd=5)
        self.lbframe3.pack(fill="both", padx=25, pady=10)

        #inside labelframe your portfolio
        for i in range(10):
            self.showlist.append(tk.Button(self.lbframe, width=50, anchor="nw"))
        for i in range(10):
            self.showlist[i].grid(row=i+1, column=1, columnspan=3, padx=10, pady=5)

        self.button = tk.Button(self.lbframe, text="Show", width=10, command=self.handleShow, bg="#80E12A")
        self.button.grid(row=11, column=1, pady=5)

        self.button = tk.Button(self.lbframe, text="Calculate", width=10, command=self.handleSubmit, bg="orange")
        self.button.grid(row=11, column=2, pady=5)

        self.button = tk.Button(self.lbframe, text="Clear", width=10, command=self.handleClear, bg="red")
        self.button.grid(row=11, column=3, pady=5)

        #inside labelframe result
        self.riskbar = custk.CTkProgressBar(self.lbframe2, width=350, height=10, border_width=0.5, orientation="horizontal", progress_color="#32CD32", fg_color="#d9d9d9")
        self.riskbar.grid(row=1, columnspan=3, padx=(10, 0), pady=(5, 0))
        self.riskbar.set(0)

        self.label = tk.Label(self.lbframe2, text="   0")
        self.label.grid(row=2, column=0, pady=(0, 15), sticky="w")

        self.label2 = tk.Label(self.lbframe2, text="")
        self.label2.grid(row=2, column=1, pady=(5, 15))

        self.label3 = tk.Label(self.lbframe2, text="10")
        self.label3.grid(row=2, column=2, pady=(0, 15), sticky="e")

        #inside labelframe heatmap
        self.button = tk.Button(self.lbframe3, text="Show Correlation Heatmap", bg="cyan")
        self.button.pack(pady=20)


    def updateIndex(self, selection):
        self.index = selection

    def updatePfmyear(self, selection):
        if selection == "1 Year":
            self.pfmyear = 1
        elif selection == "2 Years":
            self.pfmyear = 2
        elif selection == "5 Years":
            self.pfmyear = 5

    def riskTobar(self, risk):
        riskstr = "Low-Risk"
        self.riskbar.set(risk/10)
        if risk >= 0 and risk <= 3: 
            self.riskbar.configure(progress_color="green")
            riskstr = "Low-Risk"
        elif risk > 3 and risk <= 6:
            self.riskbar.configure(progress_color="yellow")
            riskstr = "Medium-Risk"
        elif risk > 6 and risk <= 8:
            self.riskbar.configure(progress_color="orange")
            riskstr = "High-Risk"
        elif risk > 8 and risk <= 10:
            self.riskbar.configure(progress_color="red")
            self.label2.config(fg="red")
            riskstr = "Extreme-Risk"

        return riskstr


    def handleSubmit(self):
        m = Matrix()
        if len(port) > 0 and len(port) != 1:
            m.add_port(port)
            m.find_matrix_correlation()
            risk = m.risk_value
            self.label2.config(text="Your Portfolio Risk : " + "{:.6f}".format(m.risk_value) + " ({str})".format(str=self.riskTobar(risk)), fg="black")
            self.button.config(state="active", command=m.show_heatmap)
        elif len(port) == 1:
            risk = 10
            self.label2.config(text="Your Portfolio Risk : 10" + " ({str})".format(str=self.riskTobar(risk)), fg="red")
            self.button.config(state="active", command=m.show_heatmap)
        else:
            risk = 0
            self.riskTobar(risk)
            self.button.config(state="disabled")
            self.label2.config(text="Your Portfolio is Empty", fg="red")

    def handleShow(self):
        print("from port", len(port))
        for i in range(len(port)):
            self.showlist[i].config(text=port[i][0])

    def handleClear(self):
        for i in range(len(port)):
            self.showlist[i].config(text="")
        port.clear()

        print(boollist)

        for i in range(len(showlist)):
            showlist[i].config(text="{:.6f}".format(vectorlist[i][7]) + "       " + vectorlist[i][0])

        risk = 0
        self.riskTobar(risk)
        self.button.config(state="disabled")
        self.label2.config(text="Your Portfolio is Empty", fg="red")

    def handleClickshow(self, index, button):
        if self.boollist[index] == False:
            button.config(justify="left", text= self.vectorlist[index][1] + " (" + self.vectorlist[index][0] + ")" + "\n-----------------------------\n" + "P/E : " + "{:.2f}".format(self.vectorlist[index][2], 2) + "     " + "EPS Growth : " + "{:.2f}".format(self.vectorlist[index][3], 2) + " %\n" + "Return On Equity : " + "{:.2f}".format(self.vectorlist[index][4], 2) + " %     " + "Dividend Yield : " + "{:.2f}".format(self.vectorlist[index][5], 2) + " %\n" + "Performance " + str(self.pfmyear) + "Year(s) : " + "{:.2f}".format(self.vectorlist[index][6], 2))
            self.boollist[index] = True
        elif self.boollist[index] == True:
            button.config(text="{:.2f}".format(self.vectorlist[index][-1]*100, 2) + " %" + "       " + self.vectorlist[index][0])
            self.boollist[index] = False

    def handleClickadd(self, index, addbutton, showbutton):
        showbutton.config(text="Added " + self.vectorlist[index][0] + " to your Portfolio")
        





