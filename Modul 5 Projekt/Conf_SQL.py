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
        if d == "0000": end_date = dt.date('1900-01-01')
        else: end_date = d
        return end_date

    get_db_ids(free_ids)
    print(free_ids)
    print(all_in_one)
    
    dates = []
    dates.append(conv_date_new(all_in_one[2]))
    dates.append(conv_date_new(all_in_one[12]))
    dates.append(conv_date_new(all_in_one[13]))
    
    send_data = ""
    
    if fa.flag == False:
        send_data = (f"INSERT INTO telefon (telefon_nr) VALUES\n"
                    f"('{all_in_one[3]}');\n"
                    f"GO\n"
                    f"INSERT INTO windows (win_nr) VALUES\n"
                    f"('{all_in_one[18]}');\n"
                    f"GO\n"
                    f"INSERT INTO msoffice (msoffice_nr) VALUES\n"
                    f"('{all_in_one[19]}');\n"
                    f"GO\n"
                    f"INSERT INTO power_bi (power_bi_nr) VALUES\n"
                    f"('{all_in_one[20]}');\n"
                    f"GO\n"
                    f"INSERT INTO software (win_nr_id, msoffice_nr_id, power_bi_id) VALUES\n"
                    f"('{free_ids[8]+1}', '{free_ids[7]+1}', '{free_ids[6]+1}');\n"
                    f"GO\n"
                    f"INSERT INTO urlaub (urlaub_wert) VALUES\n"
                    f"('{all_in_one[16]}');\n"
                    f"GO\n"
                    f"INSERT INTO gehalt (gehalt_wert) VALUES\n"
                    f"('{all_in_one[15]}');\n"
                    f"GO\n"
                    f"INSERT INTO mitarbeiter_adr (ma_ad_str, ma_ad_hnr, ma_ad_ort, ma_ad_plz) VALUES\n"
                    f"('{all_in_one[4]}', '{all_in_one[5]}', '{all_in_one[7]}', '{all_in_one[6]}');\n"
                    f"GO\n"
                    f"INSERT INTO vertrag (abteilung_id, position_id, vertragbeginn, vertragende, arbeitszeit_id, vertragsart_id, urlaub_id, gehalt_id) VALUES\n"
                    f"('{all_in_one[8]}', '{all_in_one[9]}', '{dates[1]}', '{dates[2]}', '{all_in_one[11]}', '{all_in_one[10]}', '{free_ids[4]+1}', '{free_ids[3]+1}');\n"
                    f"GO\n"
                    f"INSERT INTO mitarbeiter (vorname, nachname, geburtsdatum, ma_ad_id, telefon_id, email, soft_id, office_id, vertrag_id) VALUES\n"
                    f"('{all_in_one[0]}', '{all_in_one[1]}', '{dates[0]}', '{free_ids[2]+1}', '{free_ids[9]+1}', '{all_in_one[14]}', '{free_ids[5]+1}', '{all_in_one[17]}', '{free_ids[1]+1}');\n"
                    f"GO\n")
    else:
        send_data = (f"INSERT INTO telefon (telefon_nr_id, telefon_nr) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[3]}');\n"
                    f"GO\n"
                    f"INSERT INTO windows (win_nr_id, win_nr) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[18]}');\n"
                    f"GO\n"
                    f"INSERT INTO msoffice (msoffice_nr_id, msoffice_nr) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[19]}');\n"
                    f"GO\n"
                    f"INSERT INTO power_bi (power_bi_id, power_bi_nr) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[20]}');\n"
                    f"GO\n"
                    f"INSERT INTO software (soft_id, win_nr_id, msoffice_nr_id, power_bi_id) VALUES\n"
                    f"('{lst[0]}', '{free_ids[8]+1}', '{free_ids[7]+1}', '{free_ids[6]+1}');\n"
                    f"GO\n"
                    f"INSERT INTO urlaub (urlaub_id, urlaub_wert) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[16]}');\n"
                    f"GO\n"
                    f"INSERT INTO gehalt (gehalt_id, gehalt_wert) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[15]}');\n"
                    f"GO\n"
                    f"INSERT INTO mitarbeiter_adr (ma_ad_id, ma_ad_str, ma_ad_hnr, ma_ad_ort, ma_ad_plz) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[4]}', '{all_in_one[5]}', '{all_in_one[7]}', '{all_in_one[6]}');\n"
                    f"GO\n"
                    f"INSERT INTO vertrag (vertrag_id, abteilung_id, position_id, vertragbeginn, vertragende, arbeitszeit_id, vertragsart_id, urlaub_id, gehalt_id) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[8]}', '{all_in_one[9]}', '{dates[1]}', '{dates[2]}', '{all_in_one[11]}', '{all_in_one[10]}', '{free_ids[4]+1}', '{free_ids[3]+1}');\n"
                    f"GO\n"
                    f"INSERT INTO mitarbeiter (mitarbeiter_id, vorname, nachname, geburtsdatum, ma_ad_id, telefon_id, email, soft_id, office_id, vertrag_id) VALUES\n"
                    f"('{lst[0]}', '{all_in_one[0]}', '{all_in_one[1]}', '{dates[0]}', '{free_ids[2]+1}', '{free_ids[9]+1}', '{all_in_one[14]}', '{free_ids[5]+1}', '{all_in_one[17]}', '{free_ids[1]+1}');\n"
                    f"GO\n")
        
    print(send_data)
  
    # Send Login
    try:
        # Execute the SQL command
        mycursor = myDBcon.cursor()
        mycursor.execute(send_data)
        # Commit your changes in the database
        myDBcon.commit()
    except:
        # Roll back in case there is any error
        myDBcon.rollback()
                    
    # Get New Last Mitarbeiter_ID
    mycursor.execute(get_last_ma_id)
    last_ma_id_new = mycursor.fetchone()

    we_mad_it = free_ids[0] < last_ma_id_new[0]
    
    print(we_mad_it)
    # if we_mad_it:
    #     its_ok = mb.showinfo(title="Its OK", message="Its OK!", parent=self)
    # else: mb.showinfo(title="Trubbles", message="We Have Trubbles!", parent=self)
                
    #if we_mad_it and its_ok: self.destroy()