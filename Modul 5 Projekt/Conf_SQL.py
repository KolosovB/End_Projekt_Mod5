import sys
IOError is OSError

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
        file.write("server=''\n")
        file.write("database=''\n")
        file.write("username=''\n")
        file.write("password=''\n")
        file.write("driver='{ODBC Driver 18 for SQL Server}'\n")

def write_conf_file(send_info):
    with open(conf_name, "r", encoding="UTF-8") as file:
        temp = []
        for line in file:
            temp.append(line.strip().split(" = "))

        print(temp)
        
    with open(conf_name, "w") as file:
        for i in range(len(send_info)):
                file.write(temp[i][0] + " = " + send_info[i] + "\n")
        file.write("driver = {ODBC Driver 18 for SQL Server}\n")

def open_conf_file():

    with open(conf_name, "r", encoding="UTF-8") as file:
        temp = []
        for line in file:
            temp.append(line.strip().split(" = "))
        
        print(temp)
    return temp

# with open("Dateiname", "r") as file:
#     while line := file.readline():
#         print(line.rstrip())