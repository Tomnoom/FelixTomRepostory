import sqlite3

class Autos:
    def __init__(self, Marke, Baujahr, Kilometerstand, PS, Marktgängig):
        self.Marke = Marke
        self.Baujahr = Baujahr
        self.Kilometerstand = Kilometerstand
        self.PS = PS
        self.Marktgängig = Marktgängig

    def to_db(self):
        connection = sqlite3.connect("database.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"INSERT INTO autos(Marke, Baujahr, Kilometerstand, PS, Marktgängig) VALUES ('{self.Marke}', '{self.Baujahr}', '{self.Kilometerstand}', '{self.PS}', '{self.Marktgängig}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @classmethod
    def from_db(cls, Auto_ID):
        connection = sqlite3.connect("database.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"SELECT Auto_ID FROM users WHERE Auto_ID = {Auto_ID}"
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return (row[0], row[1], row[2], row[3], row[4], row[5])

#auto3 = Autos("Fiat", 2009, 130000, 80, "ja")
#auto3.to_db()

class Kunden:
    def __init__(self, username, firstname, lastname):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def to_db(self):
        connection = sqlite3.connect("database.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"INSERT INTO Kunden(username, firstname, lastname) VALUES ('{self.username}', '{self.firstname}', '{self.lastname}')"
        cursor.execute(sql)
        connection.commit()
        connection.close()

    @classmethod
    def from_db(cls, username):
        connection = sqlite3.connect("database.db") # Muss vorher angelegt werden.
        cursor = connection.cursor()
        sql = f"SELECT username FROM Kunden WHERE username = {username}"
        cursor.execute(sql)
        row = cursor.fetchone()
        connection.close()
        return Kunden(row[0], row[1], row[2])

    