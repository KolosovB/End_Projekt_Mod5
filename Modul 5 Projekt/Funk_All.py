import tkinter as tk
from tkinter import filedialog, messagebox as mb
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import Conf_SQL as fcon
import Gui_Windows as gw
import datetime as dt
from datetime import datetime, timedelta

class add_user_gui(ttk.Toplevel):
    """
    Subclass von Toplevel - Neu Mitarbeiter Hinzufügen oder Alte Editieren
    Erstellt ein Fenster mit eingaben möglichkeiten
    """
    global flag, user
    flag = False

    def __init__(self, lst):
        
        self.lst = lst
        
        global flag, user
        
        user = []
        
        if len(self.lst) > 0:
            flag = True
            
            for x in range(len(gw.lists[3])):
                if lst[0] == gw.lists[3][x][0]: 
                    user.extend(gw.lists[3][x])
                    user.extend(gw.lists[4][x])
                    user.extend(gw.lists[12][x])
                    print(user)
        else:
            for x in range(25): user.append("None")

        
        def somewehere(x):
             some = []
             for line in gw.lists[x]:
                 some.append(line[1])
             return some
        
        def abteilung_ausgeben(event):
            global abteilung
            abteilung = ein_ten.get()
            return abteilung
    
        def position_ausgeben(event):
            global position
            position = ein_elf.get()
            return position

        def vertrag_ausgeben(event):
            global vertrag
            vertrag = ein_zwo.get()
            return vertrag
    
        def beschaf_ausgeben(event):
            global beschaf
            beschaf = ein_dre.get()
            return beschaf
    
        def office_ausgeben(event):
            global office
            office = ein_she.get()
            return office
            
        def email_value(event):
            if ein_uno.get() != "" and ein_duo.get() != "":
                fname = ein_uno.get()
                sname = ein_duo.get()
                global email
                email = fname.lower() + "." + sname.lower() + "@finck-maier-consulting.de"
                lb_lk.config(text = email)
                return email
            
        # def condate(test):
        #     """
        #     Konvertiere Date in DB Format
        #     """
        #     import datetime

        #     def conv_date(test, x):
        #         test = test.split(x)
        #         date = datetime.datetime(int(test[2]), int(test[1]), int(test[0]))
        #         return date

        #     if len(test.split(",")) > 2 : d = conv_date(test, ",")
        #     elif len(test.split(".")) > 2: d = conv_date(test, ".")
        #     elif len(test.split("/")) > 2: d = conv_date(test, "/")
        #     else: d = None

        #     return d
            
        # def samle_all():
        #     """
        #     all_in_one :
        #     #vorname = [0]
        #     #nachname = [1]
        #     #geburt = [2]
        #     #telefon = [3]
        #     #strasse = [4]
        #     #hausnr = [5]
        #     #plz = [6]
        #     #ort = [7]
        #     #abteilung_id = [8]
        #     #position_id = [9]
        #     #vertrag_id = [10]
        #     #beschaf_id = [11]
        #     #rolle_id = [12]
        #     #email = [13]
        #     #passwort = [14]
        #     #gehalt = [15]
        #     #vertragsbeginn = [16]
        #     #vertragsende = [17]
        #     """
        #     all_in_one = []
        #     all_in_one.append(ein_uno.get())
        #     all_in_one.append(ein_duo.get())
            
        #     # Umwandle Datum
        #     test = ein_tre.get()
        #     bdate = condate(test)
        #     all_in_one.append(bdate)
            
        #     #all_in_one.append()
        #     all_in_one.append(ein_qwa.get())
            
        #     all_in_one.append(ein_qwi.get())
        #     all_in_one.append(ein_sex.get())
        #     all_in_one.append(ein_che.get())
        #     all_in_one.append(ein_nen.get())

        #     # Get Abteilung_ID
        #     get_abt = "SELECT Abteilung_ID FROM abteilung WHERE Abteilung_name = '" + abteilung + "';"
        #     mycursor.execute(get_abt)
        #     abteilung_id = mycursor.fetchone()
        #     all_in_one.append(abteilung_id)
            
        #     # Get Position_ID
        #     get_pos = "SELECT `Position_ID` FROM `position` WHERE `Position_name` = '" + position + "';"
        #     mycursor.execute(get_pos)
        #     position_id = mycursor.fetchone()
        #     all_in_one.append(position_id)
            
        #     # Get Vertrag_ID
        #     get_ver = "SELECT `Vertragsart_ID` FROM `vertragsart` WHERE `Vertragsart_name` = '" + vertrag + "';"
        #     mycursor.execute(get_ver)
        #     vertrag_id = mycursor.fetchone()
        #     all_in_one.append(vertrag_id)
            
        #     # Get Beschäftigung_ID
        #     get_bes = "SELECT `Beschäftigung_ID` FROM `beschäftigung` WHERE `Beschäftigung_name` = '" + beschaf + "';"
        #     mycursor.execute(get_bes)
        #     beschaf_id = mycursor.fetchone()
        #     all_in_one.append(beschaf_id)
            
        #     # Get Rolle
        #     get_roll = "SELECT `Kontotype_ID` FROM `kontotype` WHERE `Kontotype_name` = '" + rolle + "';"
        #     mycursor.execute(get_roll)
        #     rolle_id = mycursor.fetchone()
        #     all_in_one.append(rolle_id)
            
        #     all_in_one.append(email)
        #     all_in_one.append(new_pass)

        #     all_in_one.append(ein_non.get())
            
        #     test2 = ein_vie.get()
        #     vdate = condate(test2)
        #     all_in_one.append(vdate)
        #     test3 = ein_fun.get()
        #     edate = condate(test3)
        #     all_in_one.append(edate)

        #     return all_in_one

        # new_lists = []
        # new_lists = gw.lists
        # print(new_lists)

        office_liste = []
        office_liste = somewehere(6)
            
        vertrag_liste = []
        vertrag_liste = somewehere(1)

        beschaf_liste = []
        beschaf_liste = somewehere(13)
        
        abteilung_liste = []
        abteilung_liste = somewehere(0)
        
        position_liste = []
        position_liste = somewehere(7)

        self = ttk.Toplevel()
        self.title("Add New User")
        self.attributes("-topmost", "True")
        self.geometry(f"800x680")

        # Erstellen des Label für die Überschrift
        title_label = ttk.Label(self, text="Neuer Mitarbeiter Information", font=("Verdana", 10, "bold"))
        title_label.place(x = 30, y = 20)

        # Erstellen der Labels für die Mitarbeiterinformationen
        fields = ["Vorname:", "Nachname:", "Geburtstag:", "Telefonnummer:", "Straße:", "Hausnummer:", "PLZ:", "Ort:", "Abteilung:", "Position:", "Vertragsart:", "Beschäftigung:", "Vertragsbeginn:", "Vertragsende:", "Email:", "Gehalt:", "Urlaub:", "Office"]

        label_uno = ttk.Label(self, text=fields[0], font = "Verdana 8 bold")
        label_duo = ttk.Label(self, text=fields[1], font = "Verdana 8 bold")
        label_tre = ttk.Label(self, text=fields[2], font = "Verdana 8 bold")
        label_qwa = ttk.Label(self, text=fields[3], font = "Verdana 8 bold")
        label_qwi = ttk.Label(self, text=fields[4], font = "Verdana 8 bold")
        label_sex = ttk.Label(self, text=fields[5], font = "Verdana 8 bold")
        label_che = ttk.Label(self, text=fields[6], font = "Verdana 8 bold")
        label_nen = ttk.Label(self, text=fields[7], font = "Verdana 8 bold")
        label_ten = ttk.Label(self, text=fields[8], font = "Verdana 8 bold")
        label_elf = ttk.Label(self, text=fields[9], font = "Verdana 8 bold")
        label_zwo = ttk.Label(self, text=fields[10], font = "Verdana 8 bold")
        label_dre = ttk.Label(self, text=fields[11], font = "Verdana 8 bold")
        label_vie = ttk.Label(self, text=fields[12], font = "Verdana 8 bold")
        label_fun = ttk.Label(self, text=fields[13], font = "Verdana 8 bold")
        label_she = ttk.Label(self, text=fields[14], font = "Verdana 8 bold")
        label_sib = ttk.Label(self, text=fields[15], font = "Verdana 8 bold")
        label_akt = ttk.Label(self, text=fields[16], font = "Verdana 8 bold")
        label_non = ttk.Label(self, text=fields[17], font = "Verdana 8 bold")
        
        label_uno.place(x = 30, y = 50)
        label_duo.place(x = 250, y = 50)
        label_tre.place(x = 30, y = 100)
        label_qwa.place(x = 250, y = 100)
        label_qwi.place(x = 30, y = 150)
        label_sex.place(x = 250, y = 150)
        label_che.place(x = 30, y = 200)
        label_nen.place(x = 250, y = 200)
        label_ten.place(x = 30, y = 250)
        label_elf.place(x = 250, y = 250)
        label_zwo.place(x = 30, y = 300)
        label_dre.place(x = 250, y = 300)
        label_vie.place(x = 30, y = 350)
        label_fun.place(x = 250, y = 350)
        label_she.place(x = 30, y = 400)
        label_sib.place(x = 30, y = 450)
        label_akt.place(x = 30, y = 500)
        label_non.place(x = 30, y = 550)

        ein_uno = gw.WPEntry(self, user[1])
        ein_duo = gw.WPEntry(self, user[2])
        ein_tre = gw.WPEntry(self, user[3])
        ein_qwa = gw.WPEntry(self, user[4])
        ein_qwi = gw.WPEntry(self, user[5])
        ein_sex = gw.WPEntry(self, user[6])
        ein_che = gw.WPEntry(self, user[1])
        ein_nen = gw.WPEntry(self, user[2])

        ein_ten = ttk.Combobox(self, value = abteilung_liste)
        ein_ten.current(user[3])
        ein_ten.config(state="readonly")
        ein_ten.bind("<<ComboboxSelected>>", abteilung_ausgeben)

        ein_elf = ttk.Combobox(self, value = position_liste)
        ein_elf.current(user[4])
        ein_elf.config(state="readonly")
        ein_elf.bind("<<ComboboxSelected>>", position_ausgeben)

        ein_zwo = ttk.Combobox(self, value = vertrag_liste)
        ein_zwo.current(user[5])
        ein_zwo.config(state="readonly")
        ein_zwo.bind("<<ComboboxSelected>>", vertrag_ausgeben)

        ein_dre = ttk.Combobox(self, value = beschaf_liste)
        ein_dre.current(user[6])
        ein_dre.config(state="readonly")
        ein_dre.bind("<<ComboboxSelected>>", beschaf_ausgeben)

        ein_vie = gw.WPEntry(self, dt.date(int(user[1]), int(user[1]), int(user[1])))
        end_date = (user[6])
        ein_fun = gw.WPEntry(self, end_date)

        # Tashemto Email?
        ein_she = ttk.Combobox(self, value = office_liste)
        ein_she.current(0)
        ein_she.config(state="readonly")
        ein_she.bind("<<ComboboxSelected>>", office_ausgeben)

        ein_akt = ttk.Entry(self)
        ein_non = gw.WPEntry(self, user[6])

        ein_uno.place(x = 30, y = 70)
        ein_duo.place(x = 250, y = 70)
        ein_tre.place(x = 30, y = 120)
        ein_qwa.place(x = 250, y = 120)
        ein_qwi.place(x = 30, y = 170)
        ein_sex.place(x = 250, y = 170)
        ein_che.place(x = 30, y = 220)
        ein_nen.place(x = 250, y = 220)
        ein_ten.place(x = 30, y = 270)
        ein_elf.place(x = 250, y = 270)
        ein_zwo.place(x = 30, y = 320)
        ein_dre.place(x = 250, y = 320)
        ein_vie.place(x = 30, y = 370)
        ein_fun.place(x = 250, y = 370)
        ein_she.place(x = 30, y = 420)
        ein_akt.place(x = 30, y = 520)
        ein_non.place(x = 30, y = 570)
        
        lb_lk = ttk.Label(self, text = "")
        lb_lk.place(x = 30, y = 470)
        ein_duo.bind('<Return>', email_value)
        #ein_akt.bind('<Return>', pass_check)
        
        but_send = ttk.Button(self, text = "Anlegen", command=fcon.send_an_db)
        but_send.place(x = 30, y = 650, width=120, height=40)
        


def del_user(lst):
    """
    Funktion Mitarbeiter Löschen
    """
    
    l = lst

    for x in l:
        print(gw.lists[3])
        print(l)
        for y in range(len(gw.lists[3])):
            if x == gw.lists[3][y][0]: 
                print("x = " + str(x))
                mitarbeiter_id = gw.lists[3][y][0]
                print("MaID = " + str(mitarbeiter_id))
                adresse_id = (gw.lists[3][mitarbeiter_id][4])-1
                vertrag_id = (gw.lists[3][mitarbeiter_id][9])-1

                if fcon.myDBcon:
                    mycursor = fcon.myDBcon.cursor()

                    del_adresse = "DELETE FROM mitarbeiter_adr WHERE ma_ad_id = " + str(adresse_id)
                    print(del_adresse)
                    del_vertrag = "DELETE FROM vertrag WHERE vertrag_id = " + str(vertrag_id)
                    print(del_vertrag)
                    del_mitarbeiter = "DELETE FROM Mitarbeiter WHERE mitarbeiter_id = " + str(mitarbeiter_id)
                    print(del_mitarbeiter)
                
                    # # # Delete Record aus Mitarbeiter Tabelle
                    try:
                        # Execute the SQL command
                        mycursor.execute(del_mitarbeiter)
                        # Commit your changes in the database
                        fcon.myDBcon.commit()
                    except:
                        # Roll back in case there is any error
                        fcon.myDBcon.rollback()
                    
                    try:
                        # Execute the SQL command
                        mycursor.execute(del_adresse)
                        # Commit your changes in the database
                        fcon.myDBcon.commit()
                    except:
                        # Roll back in case there is any error
                        fcon.myDBcon.rollback()
                        
                    try:
                        # Execute the SQL command
                        mycursor.execute(del_vertrag)
                        # Commit your changes in the database
                        fcon.myDBcon.commit()
                    except:
                        # Roll back in case there is any error
                        fcon.myDBcon.rollback()

                else: print("Kann nicht ohne DB Konnektion.")
    
    gw.tab_frame.forget()
        
    gw.buttonselect.forget()
    gw.buttondeselect.forget()
    gw.buttonaddma.forget()
    gw.buttondelete.forget()
    gw.buttontops.forget()

    gw.create_table()
    gw.load_buttons()