global conf_name
conf_name = "config.ini"

def check_conf_file():
    pass

def write_conf_file():
    pass

def open_conf_file():

    with open("ini", "r") as file:
        for line in file:
            temp = line.strip().split(";")
    return temp
