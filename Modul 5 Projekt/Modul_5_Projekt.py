import tkinter as tk
from tkinter import filedialog, messagebox as mb
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import mysql.connector as dbcon
#import pyodbc as dbcon

import hashlib
import datetime as dt
from datetime import datetime, timedelta
import re
from PIL import Image, ImageTk as pil
import os
import csv
from encodings import utf_8

class maingui:
    def __init__(self, root, title, geometry):

        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
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
        
        self.frame = tk.Frame(window)
        self.frame.pack()

        self.welcm_lbl = tk.Label(self.frame, text='welcome sign-up')
        self.welcm_lbl.grid(row=0, column=1)

        self.name_lbl = tk.Label(self.frame, text='name:')
        self.name_lbl.grid(row=1, column=0)

        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.sbt = tk.Button(self.frame, text='sign-up', command=self.clicked)
        self.sbt.grid(row=2, column=1)      

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(0)
        
    
def main():
    root = tk.Tk()
    maingui(root, "Rpg", "400x400")
    root.mainloop()
    
if __name__ =='__main__':
    main()