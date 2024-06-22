import tkinter as tk
from tkinter import filedialog, messagebox as mb
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class maingui:
    
    def __init__(self, root, title):
        
        self.root = root
        self.root.title(title)
        
        d_width = self.root.winfo_screenwidth()
        d_height = self.root.winfo_screenheight()
        
        self.root.geometry("%dx%d+%d+%d" % (d_width, d_height, 0, 0))
        self.pageshow = Login_Page(self, self.root)
      
    def changepage(self, page):
        self.page = page
        
        if self.page == 0:
            #del self.pageshow
            self.pageshow = Login_Page(self, self.root)

        if self.page == 1:
            #del self.pageshow
            self.pageshow = Sign_Page(self, self.root)


class Login_Page:
    def __init__(self, parent, window):
        
        self.parent = parent
        
        self.frame = ttk.Frame(window)
        self.frame.pack()

        self.welcm_lbl = ttk.Label(self.frame, text='welcome')
        self.welcm_lbl.grid(row=0, column=1)

        self.name_lbl = ttk.Label(self.frame, text='name:')
        self.name_lbl.grid(row=1, column=0)

        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.sbt = ttk.Button(self.frame, text='login', command=self.clicked)
        self.sbt.grid(row=2, column=1)

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(1)
        

class Sign_Page():
    def __init__(self, parent, window):

        self.parent = parent
        
        self.frame = ttk.Frame(window)
        self.frame.pack()

        self.welcm_lbl = ttk.Label(self.frame, text='welcome sign-up')
        self.welcm_lbl.grid(row=0, column=1)

        self.name_lbl = ttk.Label(self.frame, text='name:')
        self.name_lbl.grid(row=1, column=0)

        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.sbt = ttk.Button(self.frame, text='sign-up', command=self.clicked)
        self.sbt.grid(row=2, column=1)      

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(0)
