import tkinter as tk
from tkinter import ttk
import frames.menu as menuframe
import frames.port as portframe
import frames.guide as guideframe
import frames.credit as creditframe

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Screener with Linear Algebra")
        self.root.geometry("600x800")

        self.notebook = ttk.Notebook(self.root)
        
        self.menu = menuframe.Menu(self.notebook)
        self.port = portframe.Port(self.notebook)
        self.guide = guideframe.Guide(self.notebook)
        self.credit = creditframe.Credit(self.notebook)

        self.notebook.add(self.menu.frame, text="Menu")
        self.notebook.add(self.port.frame, text="Portfolio")
        self.notebook.add(self.guide.frame, text="Guide")
        self.notebook.add(self.credit.frame, text="Credits")

        self.notebook.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()