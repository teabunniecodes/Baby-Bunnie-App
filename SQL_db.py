import sqlite3

class User_Info():
    def connect_db(self):
        self.conn_db = sqlite3.connect("DB/database.db")
        self.db = self.conn_db.cursor()

    def create_table(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS user_info
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        Created DATETIME, Username TEXT, Email TEXT, Password TEXT)""")

    def insert_data(self, date, username, email, password):
        sql = """INSERT INTO user_info(Created, Username, Email, Password)
                    VALUES (?, ?, ?, ?)"""
        self.db.execute(sql, [date, username, email, password])

    def access_email(self, email):
        self.db.execute("SELECT email FROM user_info WHERE email = ?", [email])
        if self.db.fetchone() != None:
            return True

    def access_username(self, username):
        self.db.execute("SELECT username FROM user_info WHERE username = ?", [username])
        if self.db.fetchone() != None:
            return True

    def access_password(self, password):
        self.db.execute("SELECT password FROM user_info WHERE password = ?", [password])
        if self.db.fetchone() != None:
            return True

    def access_user(self, username, password):
        self.db.execute("SELECT * FROM user_info WHERE username = ? and password = ?", [username, password])
        user = self.db.fetchone()
        if user is None:
            print("Boo!")
        else:
            return user

    def commit_db(self):
        self.conn_db.commit()
    
    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

class Tummy_Time():
    def connect_db(self):
        self.conn_db = sqlite3.connect("DB/database.db")
        self.db = self.conn_db.cursor()

    def create_table(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS tummy_time 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        Date DATETIME, Start DATETIME, End DATETIME, Number INT, Other TEXT)""")

    def start_data(self, date, start, number):
        sql = """INSERT INTO tummy_time(Date, Start, Number)
                VALUES (?, ?, ?)"""
        self.db.execute(sql, [date, start, number])
        self.conn_db.commit()

    def end_data(self, date, start, end, number, notes):
        self.db.execute("UPDATE tummy_time set End = ?,  Number = ?, Other = ? WHERE Date = ? Start = ?", [end, number, notes, date, start])

    def clear_table(self):
        self.db.execute("DROP TABLE tummy_time")