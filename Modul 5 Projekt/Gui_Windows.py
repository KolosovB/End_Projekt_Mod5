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

        if check_save.get() == 1:
            
            temp = []
            
            try:
                temp.append(self.serv_entr.get())
            except (AttributeError, TypeError, NameError):
                temp.append(None)
                
            try:
                temp.append(self.db_entr.get())
            except (AttributeError, TypeError, NameError):
                temp.append(None)
                
            try:
                temp.append(self.user_entr.get())
            except (AttributeError, TypeError, NameError):
                temp.append(None)
                
            try:
                temp.append(self.pass_entr.get())
            except (AttributeError, TypeError, NameError):
                temp.append(None)
            
            fcon.write_conf_file(temp)
            
        self.frame.destroy()
        self.parent.changepage(1)
        
        
    def sql_check(self, lst):
        fcon.check_conf_file()
        fcon.read_conf_file(lst)
        return lst
        
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
        
        fcon.connect_to_datebank()

        self.frame = ttk.Frame(window)
        self.frame.pack()

        create_table(self.frame)
         

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
            
def create_table(main):
    global abteilung, arbeitszeit, mitarbeiter, mitarbeiter_adr, office_adr, position, vertrag, vertragsart
    dbnames = ("abteilung", "arbeitszeit", "mitarbeiter", "mitarbeiter_adr", "office_adr", "position", "vertrag", "vertragsart")

    abteilung = []
    arbeitszeit = []
    mitarbeiter = []
    mitarbeiter_adr = []
    office_adr = []
    position = []
    vertrag = []
    vertragsart = []
    
    lists = []
    
    def get_all_data():
        
        myDBcon = fcon.connect_to_datebank()
        
        for dbn in dbnames:
            mycursor = myDBcon.cursor()
            get_data = "SELECT * FROM " + dbn + ";"
            mycursor.execute(get_data)
            getta = mycursor.fetchall()
            lists.append(getta)
    
    def sort_all_data():
        for i in range(len(lists)):
            for e in range(len(lists[i])):
                if i == 0: abteilung.append(lists[i][e])
                elif i == 1: arbeitszeit.append(lists[i][e])
                elif i == 2: mitarbeiter.append(lists[i][e])
                elif i == 3: mitarbeiter_adr.append(lists[i][e])
                elif i == 4: office_adr.append(lists[i][e])
                elif i == 5: position.append(lists[i][e])
                elif i == 6: vertrag.append(lists[i][e])
                elif i == 7: vertragsart.append(lists[i][e])
                else: break

        for n in range(len(mitarbeiter)):
            data = []

            for i in range(14):
                if i == 0: data.append(mitarbeiter[n][0])
                elif i == 1: 
                    s = mitarbeiter[n][7]
                    f = vertrag[s-1][2]
                    data.append(abteilung[int(f)-1][1])
                elif i == 2:
                    s = mitarbeiter[n][7]
                    f = vertrag[s-1][3]
                    data.append(position[int(f)-1][1])
                elif i == 3: 
                    vorname = mitarbeiter[n][1]
                    nachname = mitarbeiter[n][2]
                    name = vorname + " " + nachname
                    data.append(name)
                elif i == 4:
                    s = mitarbeiter[n][4]
                    strasse = mitarbeiter_adr[s-1][1]
                    haus =  mitarbeiter_adr[s-1][2]
                    plz =  mitarbeiter_adr[s-1][4]
                    ort =  mitarbeiter_adr[s-1][3]
                    adresse = strasse + " " + haus + ", " + plz + " " + ort
                    data.append(adresse)
                elif i == 5: data.append(mitarbeiter[n][5])
                elif i == 6: data.append(mitarbeiter[n][6])
                elif i == 7:
                    gb = str(mitarbeiter[n][3]).split("-")
                    gbg = gb[2] + "." + gb[1] + "." + gb[0]
                    data.append(gbg)
                elif i == 8: 
                    av = str(vertrag[(mitarbeiter[n][7]) - 1][4]).split("-")
                    ava = av[2] + "." + av[1] + "." + av[0]
                    data.append(ava)
                elif i == 9:
                    av = str(vertrag[(mitarbeiter[n][7]) - 1][5]).split("-")
                    if av[0] == "1900": ava = "-"
                    else: ava = av[2] + "." + av[1] + "." + av[0]
                    data.append(ava)
                elif i == 10:
                    s = mitarbeiter[n][7]
                    f = vertrag[s-1][7]
                    data.append(vertragsart[int(f)-1][1])
                elif i == 11: 
                    s = mitarbeiter[n][7]
                    f = vertrag[s-1][6]
                    data.append(arbeitszeit[int(f)-1][1])
                elif i == 12:
                    s = mitarbeiter[n][7]
                    data.append(vertrag[s-1][8])
                elif i == 13:
                    s = mitarbeiter[n][7]
                    data.append(vertrag[s-1][9])    
                else: break

            tab.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13]))
        
    global tab_frame
    tab_frame = ttk.Frame(main, relief= "flat", width= 1450)
    tab_frame.pack()
    global vsb
    vsb = ttk.Scrollbar(tab_frame, orient="vertical")
    vsb.pack(side="right", anchor = "e", fill="y", expand=True)
    global hsb
    hsb = ttk.Scrollbar(tab_frame, orient="horizontal")
    hsb.pack(side="bottom", anchor = "s", fill="x", expand=True)
    global tab
    tab = ttk.Treeview(tab_frame, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14), height=34, show="headings", yscrollcommand= vsb.set, xscrollcommand= hsb.set)
    
    tab.column(1, width=30, stretch= True)
    tab.column(2, width=120, stretch= True)
    tab.column(3, width=170, stretch= True)
    tab.column(4, width=140, stretch= True)
    tab.column(5, width=230, stretch= True)
    tab.column(6, width=90, stretch= True)
    tab.column(7, width=260, stretch= True)
    tab.column(8, width=100, stretch= True)
    tab.column(9, width=100, stretch= True)
    tab.column(10, width=90, stretch= True)
    tab.column(11, width=90, stretch= True)
    tab.column(12, width=90, stretch= True)
    tab.column(13, width=70, stretch= True)
    tab.column(14, width=90, stretch= True)

    tab.heading(1, text = "ID")
    tab.heading(2, text = "Abteilung")
    tab.heading(3, text = "Position")
    tab.heading(4, text = "Name")
    tab.heading(5, text = "Adresse")
    tab.heading(6, text = "Telefon")
    tab.heading(7, text = "E-Mail")
    tab.heading(8, text = "Geburtsdatum")
    tab.heading(9, text = "Vertragbeginn")
    tab.heading(10, text = "Vertragsend")
    tab.heading(11, text = "Vertragsart")
    tab.heading(12, text = "Arbeitszeit")
    tab.heading(13, text = "Urlaub")
    tab.heading(14, text = "Gehalt")
    
    get_all_data()
    sort_all_data()
    
    tab.pack()
    tab.bind("<Button-1>", onselect)
    tab.bind("<Key> <Button-1>", pressed)
    
    vsb.configure(command=tab.yview)
    hsb.configure(command=tab.xview)