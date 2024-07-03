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