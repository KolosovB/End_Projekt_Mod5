import tkinter as tk
from tkinter import filedialog, messagebox as mb
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyodbc as dbcon

import hashlib
import datetime as dt
from datetime import datetime, timedelta
import re
from PIL import Image, ImageTk as pil
import os
import csv
from encodings import utf_8
import Gui_Windows as win

    
def main():
    root = tk.Tk()
    win.maingui(root, "Mitarbeiterverwaltung")
    root.focus()

    root.mainloop()
    
if __name__ =='__main__':
    main()