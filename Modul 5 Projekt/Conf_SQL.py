import sys
IOError is OSError
import pyodbc as dbcon
import Funk_All as fa
import Gui_Windows as gw
import tkinter as tk
from tkinter import filedialog, messagebox as mb
import datetime as dt
from datetime import datetime, timedelta

global conf_name
conf_name = "conf.ini"

def check_conf_file():
    
    try:
        f = open(conf_name, 'rb')
    except FileNotFoundError:
        create_conf_file()
    except OSError:
        print(f"OS error occurred trying to open {conf_name}")
        sys.exit()
    except Exception as err:
        print(f"Unexpected error opening {conf_name} is",repr(err))
        sys.exit()

def create_conf_file():
    
    with open(conf_name, "w") as file:
        file.write("server = ''\n")
        file.write("database = ''\n")
        file.write("username = ''\n")
        file.write("password = ''\n")
        file.write("driver = {ODBC Driver 18 for SQL Server}\n")

def write_conf_file(send_info):
    with open(conf_name, "r", encoding="UTF-8") as file:
        temp = []
        for line in file:
            temp.append(line.strip().split(" = "))
        
    with open(conf_name, "w") as file:
        for i in range(len(send_info)):
                file.write(temp[i][0] + " = " + send_info[i] + "\n")
        file.write("driver = {ODBC Driver 18 for SQL Server}")

def read_conf_file(temp):

    with open(conf_name, "r", encoding="UTF-8") as file:
        for line in file:
            temp.append(line.strip().split(" = "))

    return temp

def connect_to_datebank():
    
    global myDBcon
    
    temp = []
    read_conf_file(temp)

    try:
        myDBcon = dbcon.connect('DRIVER='+temp[4][1]+';SERVER='+temp[0][1]+';DATABASE='+temp[1][1]+';UID='+temp[2][1]+';PWD='+temp[3][1]+';')
    except dbcon.Error as err:
        print("Something went wrong: {}".format(err))
        try:
            print("MySQL Error [%d]: %s" % (err.args[0], err.args[1]))
            return None
        except IndexError:
            print ("MySQL Error: %s" % str(err))
            return None
    except TypeError:
        print(err)
        return None
    except ValueError:
        print(err)
        return None

    return myDBcon

def send_an_db(all_in_one, lst):

    free_ids = []

    def get_db_ids(free_ids):
        #Get Last Mitarbeiter_ID
        global get_last_ma_id
        get_last_ma_id = "SELECT TOP 1 * FROM mitarbeiter ORDER BY mitarbeiter_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_ma_id)
        last_ma_id = mycursor.fetchone()
        free_ids.append(last_ma_id[0])

        #Get Last Vertrag_ID
        get_last_vert_id = "SELECT TOP 1 * FROM vertrag ORDER BY vertrag_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_vert_id)
        last_vert_id = mycursor.fetchone()
        free_ids.append(last_vert_id[0])

        #Get Last MAAdresse_ID
        get_last_maa_id = "SELECT TOP 1 * FROM mitarbeiter_adr ORDER BY ma_ad_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_maa_id)
        last_maa_id = mycursor.fetchone()
        free_ids.append(last_maa_id[0])

        #Get Last Gehalt_ID
        get_last_g_id = "SELECT TOP 1 * FROM gehalt ORDER BY gehalt_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_g_id)
        last_g_id = mycursor.fetchone()
        free_ids.append(last_g_id[0])

        #Get Last Urlaub_ID
        get_last_u_id = "SELECT TOP 1 * FROM urlaub ORDER BY urlaub_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_u_id)
        last_u_id = mycursor.fetchone()
        free_ids.append(last_u_id[0])

        #Get Last Soft_ID
        get_last_s_id = "SELECT TOP 1 * FROM software ORDER BY soft_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_s_id)
        last_s_id = mycursor.fetchone()
        free_ids.append(last_s_id[0])
    
        #Get Last Power_BI_ID
        get_last_pbi_id = "SELECT TOP 1 * FROM power_bi ORDER BY power_bi_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_pbi_id)
        last_pbi_id = mycursor.fetchone()
        free_ids.append(last_pbi_id[0])

        #Get Last MSOffice_ID
        get_last_mso_id = "SELECT TOP 1 * FROM msoffice ORDER BY msoffice_nr_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_mso_id)
        last_mso_id = mycursor.fetchone()
        free_ids.append(last_mso_id[0])

        #Get Last Windows_ID
        get_last_w_id = "SELECT TOP 1 * FROM windows ORDER BY win_nr_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_w_id)
        last_w_id = mycursor.fetchone()
        free_ids.append(last_w_id[0])
    
        #Get Last Telefon_ID
        get_last_t_id = "SELECT TOP 1 * FROM telefon ORDER BY telefon_nr_id DESC"
        mycursor = myDBcon.cursor()
        mycursor.execute(get_last_t_id)
        last_t_id = mycursor.fetchone()
        free_ids.append(last_t_id[0])
        
        return free_ids

    def conv_date_new(d):
        if d == '0000': end_date = '1900-01-01'
        else: end_date = d
        return end_date

    get_db_ids(free_ids)

    dates = []
    dates.append(conv_date_new(all_in_one[2]))
    dates.append(conv_date_new(all_in_one[12]))
    dates.append(conv_date_new(all_in_one[13]))
    s_data = []
 
    if fa.flag == False:
        
        s_data.append([f"INSERT INTO telefon (telefon_nr) VALUES ('{all_in_one[3]}');"])
        s_data.append([f"INSERT INTO windows (win_nr) VALUES ('{all_in_one[18]}');"])
        s_data.append([f"INSERT INTO msoffice (msoffice_nr) VALUES ('{all_in_one[19]}');"])
        s_data.append([f"INSERT INTO power_bi (power_bi_nr) VALUES ('{all_in_one[20]}');"])
        s_data.append([f"INSERT INTO software (win_nr_id, msoffice_nr_id, power_bi_id) VALUES ('{gw.lists[9][lst[0]][1]}', '{gw.lists[9][lst[0]][2]}', '{gw.lists[9][lst[0]][3]}');"])
        s_data.append([f"INSERT INTO urlaub (urlaub_wert) VALUES ('{all_in_one[16]}');"])
        s_data.append([f"INSERT INTO gehalt (gehalt_wert) VALUES ('{all_in_one[15]}');"])
        s_data.append([f"INSERT INTO mitarbeiter_adr (ma_ad_str, ma_ad_hnr, ma_ad_ort, ma_ad_plz) VALUES ('{all_in_one[4]}', '{all_in_one[5]}', '{all_in_one[7]}', '{all_in_one[6]}');"])
        s_data.append([f"INSERT INTO vertrag (abteilung_id, position_id, vertragbeginn, vertragende, arbeitszeit_id, vertragsart_id, urlaub_id, gehalt_id) VALUES ('{all_in_one[8]}', '{all_in_one[9]}', '{dates[1]}', '{dates[2]}', '{all_in_one[11]}', '{all_in_one[10]}', '{gw.lists[12][lst[0]][7]}', '{gw.lists[12][lst[0]][8]}');"])
        s_data.append([f"INSERT INTO mitarbeiter (vorname, nachname, geburtsdatum, ma_ad_id, telefon_id, email, soft_id, office_id, vertrag_id) VALUES ('{all_in_one[0]}', '{all_in_one[1]}', '{dates[0]}', '{gw.lists[3][lst[0]][4]}', '{gw.lists[3][lst[0]][5]}', '{all_in_one[14]}', '{gw.lists[3][lst[0]][7]}', '{gw.lists[3][lst[0]][8]}', '{gw.lists[3][lst[0]][7]}');"])

    else:
        
        s_data.append([f"UPDATE telefon SET telefon.telefon_nr = '{all_in_one[3]}' WHERE telefon_nr_id = {lst[0]};"])
        s_data.append([f"UPDATE windows SET windows.win_nr = '{all_in_one[18]}' WHERE win_nr_id = {lst[0]};"])
        s_data.append([f"UPDATE msoffice SET msoffice.msoffice_nr = '{all_in_one[19]}' WHERE msoffice_nr_id = {lst[0]};"])
        s_data.append([f"UPDATE power_bi SET power_bi.power_bi_nr = '{all_in_one[20]}' WHERE power_bi_id = {lst[0]};"])
        s_data.append([f"UPDATE software SET software.win_nr_id = '{gw.lists[9][lst[0]][1]}' WHERE soft_id = {lst[0]};"])
        s_data.append([f"UPDATE software SET software.msoffice_nr_id = '{gw.lists[9][lst[0]][2]}' WHERE soft_id = {lst[0]};"])         
        s_data.append([f"UPDATE software SET software.power_bi_id = '{gw.lists[9][lst[0]][3]}' WHERE soft_id = {lst[0]};"]) 
        s_data.append([f"UPDATE urlaub SET urlaub.urlaub_wert = '{all_in_one[16]}' WHERE urlaub_id = {lst[0]};"])
        s_data.append([f"UPDATE gehalt SET gehalt.gehalt_wert = '{all_in_one[15]}' WHERE gehalt_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter_adr SET mitarbeiter_adr.ma_ad_str = '{all_in_one[4]}' WHERE ma_ad_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter_adr SET mitarbeiter_adr.ma_ad_hnr = '{all_in_one[5]}' WHERE ma_ad_id = {lst[0]};"]) 
        s_data.append([f"UPDATE mitarbeiter_adr SET mitarbeiter_adr.ma_ad_ort = '{all_in_one[7]}' WHERE ma_ad_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter_adr SET mitarbeiter_adr.ma_ad_plz = '{all_in_one[6]}' WHERE ma_ad_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.abteilung_id = '{all_in_one[8]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.position_id = '{all_in_one[9]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.vertragbeginn = '{dates[1]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.vertragende = '{dates[2]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.arbeitszeit_id = '{all_in_one[11]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.vertragsart_id = '{all_in_one[10]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.urlaub_id = '{gw.lists[12][lst[0]][7]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE vertrag SET vertrag.gehalt_id = '{gw.lists[12][lst[0]][8]}' WHERE vertrag_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.vorname = '{all_in_one[0]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.nachname = '{all_in_one[1]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.geburtsdatum = '{dates[0]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.ma_ad_id = '{gw.lists[3][lst[0]][4]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.telefon_id = '{gw.lists[3][lst[0]][5]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.email = '{all_in_one[14]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.soft_id = '{gw.lists[3][lst[0]][7]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.office_id = '{gw.lists[3][lst[0]][8]}' WHERE mitarbeiter_id = {lst[0]};"])
        s_data.append([f"UPDATE mitarbeiter SET mitarbeiter.vertrag_id = '{gw.lists[3][lst[0]][9]}' WHERE mitarbeiter_id = {lst[0]};"])
  
    # Send Data
    
    for x in range(len(s_data)):  
        try:
            # Execute the SQL command
            mycursor = myDBcon.cursor()
            print(s_data[x][0])
            mycursor.execute(s_data[x][0])
            # Commit your changes in the database
            myDBcon.commit()
        except:
            # Roll back in case there is any error
            print("Rollback")
            myDBcon.rollback()
                    
    gw.tab_frame.forget()
        
    gw.buttonselect.forget()
    gw.buttondeselect.forget()
    gw.buttonaddma.forget()
    gw.buttondelete.forget()
    gw.buttontops.forget()

    gw.create_table()
    gw.load_buttons()