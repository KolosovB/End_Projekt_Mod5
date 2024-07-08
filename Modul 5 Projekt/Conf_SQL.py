import sys
IOError is OSError
import pyodbc as dbcon

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

def send_an_db(): pass
    # def send_an_db():

    #     all_for_send = samle_all()
    #     check_bereitschaft = mb.askyesno(title="Bereitschaft", message="Sind Sie sicher?", parent=self)
    #     if check_bereitschaft and all_for_send:
                 
    #         # Get Last Mitarbeiter_ID
    #         get_last_ma_id = "SELECT * FROM `mitarbeiter` ORDER BY mitarbeiter.Mitarbeiter_ID DESC LIMIT 1;"
    #         mycursor.execute(get_last_ma_id)
    #         last_ma_id_old = mycursor.fetchone()
                
    #         # Send Adresse
    #         send_adress = "INSERT INTO `Adresse` (`Straﬂe`, `HausNr`, `Ort`, `PLZ`) VALUES ('" + str(all_for_send[4]) + "'," + str(all_for_send[5]) + ",'" + str(all_for_send[7]) + "','" + str(all_for_send[6]) + "');"
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
    #         send_vert = "INSERT INTO `arbeitsvertrag` (`Vertragsbeginn`, `Vertragsende`, `Besch‰ftigung_ID`, `Vertragsart_ID`, `Gehalt`) VALUES ('" + str(all_for_send[16]) + "','" + str(all_for_send[17]) + "'," + str(all_for_send[11][0]) + "," + str(all_for_send[10][0]) + "," + str(all_for_send[15]) + ");"
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