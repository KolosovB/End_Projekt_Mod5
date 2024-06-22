def open_ini():
    """
    Offnet ini-file and erstellt eine liste aus Inhalt
    
    Gibt zuruck die liste
    """
    # Lese ini-file und einsetze erste 3 stellen als host, user und password
    with open("ini", "r") as file:
        for line in file:
            temp = line.strip().split(";")
    return temp
