import tkinter as tk
from tkinter import filedialog, messagebox as mb
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import Conf_SQL as fcon
import Gui_Windows as gw

class add_user_gui(ttk.Toplevel):

    
    """
    Subclass von Toplevel - Neu Mitarbeiter Hinzufügen
    Erstellt ein Fenster mit eingaben möglichkeiten
    """
 
    def __init__(self, master):

        # def way_to_somewehere(tab):
        #     way_to_temp = "SELECT * FROM " + str(tab)
        #     mycursor.execute(way_to_temp)
        #     some = []
        #     for line in mycursor:
        #         some.append(line[1])
        #     return some
        
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
    
        def rolle_ausgeben(event):
            global rolle
            rolle = ein_she.get()
            return rolle
            
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

        # def send_an_db():

        #     all_for_send = samle_all()
        #     check_bereitschaft = mb.askyesno(title="Bereitschaft", message="Sind Sie sicher?", parent=self)
        #     if check_bereitschaft and all_for_send:
                 
        #         # Get Last Mitarbeiter_ID
        #         get_last_ma_id = "SELECT * FROM `mitarbeiter` ORDER BY mitarbeiter.Mitarbeiter_ID DESC LIMIT 1;"
        #         mycursor.execute(get_last_ma_id)
        #         last_ma_id_old = mycursor.fetchone()
                
        #         # Send Adresse
        #         send_adress = "INSERT INTO `Adresse` (`Straße`, `HausNr`, `Ort`, `PLZ`) VALUES ('" + str(all_for_send[4]) + "'," + str(all_for_send[5]) + ",'" + str(all_for_send[7]) + "','" + str(all_for_send[6]) + "');"
        #         try:
        #             # Execute the SQL command
        #             mycursor.execute(send_adress)
        #             # Commit your changes in the database
        #             myDB.commit()
        #         except:
        #             # Roll back in case there is any error
        #             myDB.rollback()
        #         # Get Last Adresse_ID
        #         get_last_id = "SELECT * FROM adresse ORDER BY `Adresse_ID` DESC LIMIT 1;"
        #         mycursor.execute(get_last_id)
        #         adress_id = mycursor.fetchone()
                
        #         # Send Arbeitsvertrag
        #         send_vert = "INSERT INTO `arbeitsvertrag` (`Vertragsbeginn`, `Vertragsende`, `Beschäftigung_ID`, `Vertragsart_ID`, `Gehalt`) VALUES ('" + str(all_for_send[16]) + "','" + str(all_for_send[17]) + "'," + str(all_for_send[11][0]) + "," + str(all_for_send[10][0]) + "," + str(all_for_send[15]) + ");"
        #         try:
        #             # Execute the SQL command
        #             mycursor.execute(send_vert)
        #             # Commit your changes in the database
        #             myDB.commit()
        #         except:
        #             # Roll back in case there is any error
        #             myDB.rollback()
        #         # Get Last Arbeitsvertrag_ID
        #         get_last_id = "SELECT * FROM arbeitsvertrag ORDER BY `Arbeitsvertrag_ID` DESC LIMIT 1;"
        #         mycursor.execute(get_last_id)
        #         vertrag_id = mycursor.fetchone()
                
        #         # Send Login
        #         send_log = "INSERT INTO `login`(`E_Mail`, `Password`) VALUES ('" + str(all_for_send[13]) + "','" + str(all_for_send[14]) + "');"
        #         try:
        #             # Execute the SQL command
        #             mycursor.execute(send_log)
        #             # Commit your changes in the database
        #             myDB.commit()
        #         except:
        #             # Roll back in case there is any error
        #             myDB.rollback()
        #         # Get Last Arbeitsvertrag_ID
        #         get_last_id = "SELECT * FROM login ORDER BY `Login_ID` DESC LIMIT 1;"
        #         mycursor.execute(get_last_id)
        #         log_id = mycursor.fetchone()
                
        #         # Send Login
        #         send_mit = "INSERT INTO `mitarbeiter`(`Vorname`, `Nachname`, `Geburtsdatum`, `Telefonnummer`, `Adresse_ID`, `Login_ID`, `Kontotype_ID`, `Abteilung_ID`, `Position_ID`, `Arbeitsvertrag_ID`) VALUES ('" + str(all_for_send[0]) + "','" + str(all_for_send[1]) + "','" + str(all_for_send[2]) + "'," + str(all_for_send[3]) + "," + str(adress_id[0]) + "," + str(log_id[0]) + "," + str(all_for_send[12][0]) + "," + str(all_for_send[8][0]) + "," + str(all_for_send[9][0]) + "," + str(vertrag_id[0]) + ");"
        #         try:
        #             # Execute the SQL command
        #             mycursor.execute(send_mit)
        #             # Commit your changes in the database
        #             myDB.commit()
        #         except:
        #             # Roll back in case there is any error
        #             myDB.rollback()
                    
        #         # Get New Last Mitarbeiter_ID
        #         mycursor.execute(get_last_ma_id)
        #         last_ma_id_new = mycursor.fetchone()

        #         we_mad_it = last_ma_id_old[0] < last_ma_id_new[0]
                
        #         if we_mad_it:
        #             its_ok = mb.showinfo(title="Its OK", message="Its OK!", parent=self)
        #         else: mb.showinfo(title="Trubbles", message="We Have Trubbles!", parent=self)
                
        #         if we_mad_it and its_ok: self.destroy()


        new_lists = []
        new_lists = gw.lists
        print(new_lists)

        # rollen_liste = []
        # rollen_liste = way_to_somewehere("kontotype")
            
        # vertrag_liste = []
        # vertrag_liste = way_to_somewehere("vertragsart")

        # beschaf_liste = []
        # beschaf_liste = way_to_somewehere("beschäftigung")
        
        # abteilung_liste = []
        # abteilung_liste = way_to_somewehere("abteilung")
        
        # position_liste = []
        # position_liste = way_to_somewehere("position")

        self = ttk.Toplevel()
        self.title("Add New User")
        self.attributes("-topmost", "True")
        self.geometry(f"1400x780")

        # Erstellen des Label für die Überschrift
        title_label = ttk.Label(self, text="Neuer Mitarbeiter Information", font=("Verdana", 10, "bold"))
        title_label.place(x = 30, y = 20)

        # Erstellen der Labels für die Mitarbeiterinformationen
        fields = ["Vorname:", "Nachname:", "Geburtstag:", "Telefonnummer:", "Straße:", "Hausnummer:", "PLZ:", "Ort:", "Abteilung:", "Position:", "Vertragsart:", "Beschäftigung:", "Vertragsbeginn:", "Vertragsende:", "Kontotyp:", "Email:", "Passwort:", "Gehalt:"]

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

        ein_uno = ttk.Entry(self)
        ein_duo = ttk.Entry(self)
        ein_tre = ttk.Entry(self)
        ein_qwa = ttk.Entry(self)
        ein_qwi = ttk.Entry(self)
        ein_sex = ttk.Entry(self)
        ein_che = ttk.Entry(self)
        ein_nen = ttk.Entry(self)

        ein_ten = ttk.Combobox(self, value = abteilung_liste)
        ein_ten.current(0)
        ein_ten.config(state="readonly")
        ein_ten.bind("<<ComboboxSelected>>", abteilung_ausgeben)

        ein_elf = ttk.Combobox(self, value = position_liste)
        ein_elf.current(0)
        ein_elf.config(state="readonly")
        ein_elf.bind("<<ComboboxSelected>>", position_ausgeben)

        ein_zwo = ttk.Combobox(self, value = vertrag_liste)
        ein_zwo.current(0)
        ein_zwo.config(state="readonly")
        ein_zwo.bind("<<ComboboxSelected>>", vertrag_ausgeben)

        ein_dre = ttk.Combobox(self, value = beschaf_liste)
        ein_dre.current(0)
        ein_dre.config(state="readonly")
        ein_dre.bind("<<ComboboxSelected>>", beschaf_ausgeben)

        ein_vie = ttk.Entry(self)
        ein_fun = ttk.Entry(self)

        ein_she = ttk.Combobox(self, value = rollen_liste)
        ein_she.current(0)
        ein_she.config(state="readonly")
        ein_she.bind("<<ComboboxSelected>>", rolle_ausgeben)

        ein_akt = ttk.Entry(self)
        ein_non = ttk.Entry(self)

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
        ein_akt.bind('<Return>', pass_check)
        
        but_send = ttk.Button(self, text = "Anlegen", command=send_an_db)
        but_send.place(x = 30, y = 650)
        


def del_user(x):
    """
    Funktion Mitarbeiter Löschen
    """
    
    if fcon.myDBcon:
        mycursor = fcon.myDBcon.cursor()

        target = x
        
        mitarbeiter_id = gw.lists[3][target-1][0]
        adresse_id = gw.lists[3][target-1][4]
        arbeits_vertrag_id = gw.lists[3][target-1][9]
        del_adresse = "DELETE FROM mitarbeiter_adr WHERE Adresse_ID = " + str(adresse_id)
        del_vertrag = "DELETE FROM Arbeitsvertrag WHERE Arbeitsvertrag_ID = " + str(arbeits_vertrag_id)
        del_mitarbeiter = "DELETE FROM Mitarbeiter WHERE Mitarbeiter_ID = " + str(mitarbeiter_id)
        # # # Delete Record aus Mitarbeiter Tabelle
        try:
            # Execute the SQL command
            mycursor.execute(del_mitarbeiter)
            # Commit your changes in the database
            fcon.myDBcon.commit()
        except:
            # Roll back in case there is any error
            fcon.myDBcon.rollback()
            # Delete Record aus Adresse Tabelle
        try:
            # Execute the SQL command
            mycursor.execute(del_adresse)
            # Commit your changes in the database
            fcon.myDBcon.commit()
        except:
            # Roll back in case there is any error
            fcon.myDBcon.rollback()
            # Delete Record aus Login Tabelle
        try:
            # Execute the SQL command
            mycursor.execute(del_vertrag)
            # Commit your changes in the database
            fcon.myDBcon.commit()
        except:
            # Roll back in case there is any error
            fcon.myDBcon.rollback()

    else: print("Kann nicht ohne DB Konnektion.")