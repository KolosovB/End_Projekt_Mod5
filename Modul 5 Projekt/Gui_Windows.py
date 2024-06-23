import tkinter as tk
from tkinter import filedialog, messagebox as mb
from turtle import color
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import Conf_SQL as fcon
from PIL import Image, ImageTk as itk

class maingui:
    
    def __init__(self, root, title):
        
        self.root = root
        self.root.title(title)
        
        d_width = self.root.winfo_screenwidth()
        d_height = self.root.winfo_screenheight()
        
        self.root.geometry("%dx%d+%d+%d" % (d_width, d_height, 0, 0))
        self.pageshow = Start_Page(self, self.root)
      
    def changepage(self, page):
        self.page = page
        
        if self.page == 0:
            #del self.pageshow
            self.pageshow = Start_Page(self, self.root)

        if self.page == 1:
            #del self.pageshow
            self.pageshow = Sign_Page(self, self.root)


class Start_Page:
    
    def __init__(self, parent, window):
        
        global points
        points = []
        
        date_lst = []
        self.sql_check(date_lst)
        
        self.parent = parent
        
        points = self.take_the_middle(self.parent, points)

        self.frame = ttk.Frame(window)
        self.frame.pack(fill="both", expand=True)
        
        self.img = Image.open("fmc_logo.png")
        width, height = self.img.size
        self.img_new_size = self.img.resize((int(width/8), int(height/8)))
        self.tkimage = itk.PhotoImage(image = self.img_new_size)
        self.label_img = ttk.Label(self.frame, image=self.tkimage)
        self.label_img.place(x = ((points[2]-int(width/8))/2), y = ((points[1]-int(height/8))/2))
        
        self.welcm_lbl = ttk.Label(self.frame, text='DB Connection')
        self.welcm_lbl.place(x = points[4], y = (((points[1]-int(height/8))/2) + 0))

        self.serv_lbl = ttk.Label(self.frame, text='Server:')
        self.serv_lbl.place(x = points[4], y = (((points[1]-int(height/8))/2) + 26))

        self.serv_entr = WPEntry(self.frame, date_lst[0][1])
        self.serv_entr.place(x = points[4], y = (((points[1]-int(height/8))/2) + 46))
        
        self.db_lbl = ttk.Label(self.frame, text='Database:')
        self.db_lbl.place(x = points[4], y = (((points[1]-int(height/8))/2) + 76))

        self.db_entr = WPEntry(self.frame, date_lst[1][1])
        self.db_entr.place(x = points[4], y = (((points[1]-int(height/8))/2) + 96))
        
        self.user_lbl = ttk.Label(self.frame, text='Username:')
        self.user_lbl.place(x = points[4], y = (((points[1]-int(height/8))/2) + 126))

        self.user_entr = WPEntry(self.frame, date_lst[2][1])
        self.user_entr.place(x = points[4], y = (((points[1]-int(height/8))/2) + 146))
        
        self.pass_lbl = ttk.Label(self.frame, text='Password:')
        self.pass_lbl.place(x = points[4], y = (((points[1]-int(height/8))/2) + 176))

        self.pass_entr = WPEntry(self.frame, date_lst[3][1])
        self.pass_entr.place(x = points[4], y = (((points[1]-int(height/8))/2) + 196))
        
        global check_save
        check_save = ttk.IntVar()
        self.checkbox = ttk.Checkbutton(self.frame, text="Speichern Einstellungen", variable=check_save)
        self.checkbox.place(x = points[4], y = (((points[1]-int(height/8))/2) + 236))

        self.sbt = ttk.Button(self.frame, text='Login', command=self.clicked)
        self.sbt.place(x = points[4], y = (((points[1]-int(height/8))/2) + 260))
        
        
    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(1)
        
    def sql_check(self, lst):
        
        fcon.check_conf_file()
        fcon.read_conf_file(lst)

        return lst

    def sql_conf():
        pass
        
    def take_the_middle(self, par, lis):
        d_width = par.root.winfo_screenwidth()
        lis.append(d_width) # 0
        d_height = par.root.winfo_screenheight()
        lis.append(d_height) # 1
        mid_w = d_width / 2
        lis.append(int(mid_w)) # 2
        mid_h = d_height / 2
        lis.append(int(mid_h)) # 3
        mid_w_r_half = (mid_w / 3) + mid_w
        lis.append(int(mid_w_r_half)) # 4

        return lis

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

class WPEntry(ttk.Entry):
        
        def __init__(self, master=None, placeholder="PLACEHOLDER"):
            
            super().__init__(master)

            self.placeholder = placeholder

            self.bind("<FocusIn>")
            self.bind("<FocusOut>")

            self.put_placeholder()

        def put_placeholder(self):
            
            self.insert(0, self.placeholder)
            
