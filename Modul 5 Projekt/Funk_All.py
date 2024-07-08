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
                    user.extend(gw.lists[10][x])
                    user.extend(gw.lists[2][x])
                    user.extend(gw.lists[11][x])
                    user.extend(gw.lists[6][(gw.lists[3][x][8])-1])
                    user.extend(gw.lists[14][(gw.lists[9][x][1])-1])
                    user.extend(gw.lists[5][(gw.lists[9][x][2])-1])
                    if gw.lists[9][x][3] != None:
                        user.extend(gw.lists[8][(gw.lists[9][x][3])-1])
                    else: 
                        user.append("-")
                        user.append("-")
                    
                    print(user)
        else:
            for x in range(41): 
                if x == 16: user.append(1)
                elif x == 17: user.append(1)
                elif x == 20: user.append(1)
                elif x == 21: user.append(1)
                elif x == 30: user.append(1)
                else:
                    user.append("None")

        
        def somewehere(x):
             some = []
             for line in gw.lists[x]:
                 some.append(line[1])
             return some
        
        def abteilung_ausgeben(event):
            global abteilung
            abteilung = ein_09.get()
            return abteilung
    
        def position_ausgeben(event):
            global position
            position = ein_10.get()
            return position

        def vertrag_ausgeben(event):
            global vertrag
            vertrag = ein_11.get()
            return vertrag
    
        def beschaf_ausgeben(event):
            global beschaf
            beschaf = ein_12.get()
            return beschaf
    
        def office_ausgeben(event):
            global office
            office = ein_18.get()
            return office
            
        def email_value(event):
            global ein_15
            if ein_01.get() != None and ein_02.get() != None:
                fname = ein_01.get()
                sname = ein_02.get()
                global email
                email = fname.lower() + "." + sname.lower() + "@finck-maier-consulting.de"
                ein_15 = gw.WPEntry(self, email)
                ein_15.place(x = 430, y = 280, width=340)
                return email
            
        def condate(test):
             """
             Konvertiere Date in DB Format
             """
             import datetime

             def conv_date(test, x):
                 test = test.split(x)
                 date = datetime.datetime(int(test[2]), int(test[1]), int(test[0]))
                 return date

             if type(test) is not datetime.date:
                 if len(test.split(",")) > 2 : d = conv_date(test, ",")
                 elif len(test.split(".")) > 2: d = conv_date(test, ".")
                 elif len(test.split("/")) > 2: d = conv_date(test, "/")
                 else: d = None
             else: d = None
             
             if flag == True and d == None:
                 d = test
             elif flag == False and d == None:
                 d = "-"

             return d
        
        # def conv_date_new():
        #     if v_lst[1][0] == "0000": end_date = "- kein -"
        #     else: end_date = dt.date(int(v_lst[1][0]), int(v_lst[1][1]), int(v_lst[1][2]))
        #     return end_date  
    
        def samle_all():

             """
             all_in_one :
             #vorname = [0]
             #nachname = [1]
             #geburt = [2]
             #telefon = [3]
             #strasse = [4]
             #hausnr = [5]
             #plz = [6]
             #ort = [7]
             #abteilung_id = [8]
             #position_id = [9]
             #vertrag_id = [10]
             #beschaf_id = [11]
             #rolle_id = [12]
             #email = [13]
             #passwort = [14]
             #gehalt = [15]
             #vertragsbeginn = [16]
             #vertragsende = [17]
             """
             pass
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
        vertrag_liste = somewehere(13)

        beschaf_liste = []
        beschaf_liste = somewehere(1)
        
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
        fields = ["Vorname:", "Nachname:", "Geburtstag:", "Telefonnummer:", "Straße:", "Hausnummer:", "PLZ:", "Ort:", "Abteilung:", "Position:", "Vertragsart:", "Arbeitszeit:", "Vertragsbeginn:", "Vertragsende:", "Email:", "Gehalt:", "Urlaub:", "Office", "Windows", "MS Office", "Power BI"]

        label_01 = ttk.Label(self, text=fields[0], font = "Verdana 8 bold")
        label_02 = ttk.Label(self, text=fields[1], font = "Verdana 8 bold")
        label_03 = ttk.Label(self, text=fields[2], font = "Verdana 8 bold")
        label_04 = ttk.Label(self, text=fields[3], font = "Verdana 8 bold")
        label_05 = ttk.Label(self, text=fields[4], font = "Verdana 8 bold")
        label_06 = ttk.Label(self, text=fields[5], font = "Verdana 8 bold")
        label_07 = ttk.Label(self, text=fields[6], font = "Verdana 8 bold")
        label_08 = ttk.Label(self, text=fields[7], font = "Verdana 8 bold")
        label_09 = ttk.Label(self, text=fields[8], font = "Verdana 8 bold")
        label_10 = ttk.Label(self, text=fields[9], font = "Verdana 8 bold")
        label_11 = ttk.Label(self, text=fields[10], font = "Verdana 8 bold")
        label_12 = ttk.Label(self, text=fields[11], font = "Verdana 8 bold")
        label_13 = ttk.Label(self, text=fields[12], font = "Verdana 8 bold")
        label_14 = ttk.Label(self, text=fields[13], font = "Verdana 8 bold")
        label_15 = ttk.Label(self, text=fields[14], font = "Verdana 8 bold")
        label_16 = ttk.Label(self, text=fields[15], font = "Verdana 8 bold")
        label_17 = ttk.Label(self, text=fields[16], font = "Verdana 8 bold")
        label_18 = ttk.Label(self, text=fields[17], font = "Verdana 8 bold")
        label_19 = ttk.Label(self, text=fields[18], font = "Verdana 8 bold")
        label_20 = ttk.Label(self, text=fields[19], font = "Verdana 8 bold")
        label_21 = ttk.Label(self, text=fields[20], font = "Verdana 8 bold")
        
        ### 50, 120, 190, 260, 330, 400, 470, 540

        label_01.place(x = 30, y = 50)
        label_02.place(x = 230, y = 50)
        label_03.place(x = 430, y = 50)
        label_04.place(x = 630, y = 50)
        label_05.place(x = 30, y = 120)
        label_06.place(x = 230, y = 120)
        label_07.place(x = 430, y = 120)
        label_08.place(x = 630, y = 120)
        label_09.place(x = 30, y = 190)
        label_10.place(x = 230, y = 190)
        label_11.place(x = 430, y = 190)
        label_12.place(x = 630, y = 190)
        label_13.place(x = 30, y = 260)
        label_14.place(x = 230, y = 260)
        label_15.place(x = 430, y = 260)
        label_16.place(x = 30, y = 330)
        label_17.place(x = 230, y = 330)
        label_18.place(x = 430, y = 330)
        label_19.place(x = 30, y = 400)
        label_20.place(x = 30, y = 470)
        label_21.place(x = 30, y = 540)

        ein_01 = gw.WPEntry(self, user[1])
        ein_02 = gw.WPEntry(self, user[2])
        ein_03 = gw.WPEntry(self, user[3])
        ein_04 = gw.WPEntry(self, user[25])
        ein_05 = gw.WPEntry(self, user[11])
        ein_06 = gw.WPEntry(self, user[12])
        ein_07 = gw.WPEntry(self, user[14])
        ein_08 = gw.WPEntry(self, user[13])

        ein_09 = ttk.Combobox(self, value = abteilung_liste)
        ein_09.current(user[16]-1)
        ein_09.config(state="readonly")
        ein_09.bind("<<ComboboxSelected>>", abteilung_ausgeben)

        ein_10 = ttk.Combobox(self, value = position_liste)
        ein_10.current(user[17]-1)
        ein_10.config(state="readonly")
        ein_10.bind("<<ComboboxSelected>>", position_ausgeben)

        ein_11 = ttk.Combobox(self, value = vertrag_liste)
        ein_11.current(user[21]-1)
        ein_11.config(state="readonly")
        ein_11.bind("<<ComboboxSelected>>", vertrag_ausgeben)

        ein_12 = ttk.Combobox(self, value = beschaf_liste)
        ein_12.current(user[20]-1)
        ein_12.config(state="readonly")
        ein_12.bind("<<ComboboxSelected>>", beschaf_ausgeben)

        ein_13 = gw.WPEntry(self, user[18])
        end_date = condate(user[19])
        ein_14 = gw.WPEntry(self, end_date)

        global ein_15
        ein_15 = gw.WPEntry(self, user[6])
        ein_16 = gw.WPEntry(self, user[27])
        ein_17 = gw.WPEntry(self, user[29])
        
        ein_18 = ttk.Combobox(self, value = office_liste)
        ein_18.current(user[30]-1)
        ein_18.config(state="readonly")
        ein_18.bind("<<ComboboxSelected>>", office_ausgeben)

        ein_19 = gw.WPEntry(self, user[36])
        ein_20 = gw.WPEntry(self, user[38])
        ein_21 = gw.WPEntry(self, user[40])

        ### 70, 140, 210, 280, 350

        ein_01.place(x = 30, y = 70)
        ein_02.place(x = 230, y = 70)
        ein_03.place(x = 430, y = 70)
        ein_04.place(x = 630, y = 70)
        ein_05.place(x = 30, y = 140)
        ein_06.place(x = 230, y = 140)
        ein_07.place(x = 430, y = 140)
        ein_08.place(x = 630, y = 140)
        ein_09.place(x = 30, y = 210)
        ein_10.place(x = 230, y = 210)
        ein_11.place(x = 430, y = 210)
        ein_12.place(x = 630, y = 210)
        ein_13.place(x = 30, y = 280)
        ein_14.place(x = 230, y = 280)
        ein_15.place(x = 430, y = 280, width=340)
        ein_16.place(x = 30, y = 350)
        ein_17.place(x = 230, y = 350)
        ein_18.place(x = 430, y = 350, width=340)
        ein_19.place(x = 30, y = 420, width=340)
        ein_20.place(x = 30, y = 490, width=340)
        ein_21.place(x = 30, y = 560, width=340)
        
        lb_lk = ttk.Label(self, text = "")
        lb_lk.place(x = 30, y = 470)
        ein_02.bind('<Return>', email_value)
        
        but_send = ttk.Button(self, text = "Anlegen", command=fcon.send_an_db)
        but_send.place(x = 30, y = 610, width=120, height=40)
        


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