import mysql.connector

class DBConnection:
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME):
        self.host = DB_HOST
        self.port = DB_PORT
        self.name = DB_NAME
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.conn = None

    def get_conn(self):
        if self.conn is None:
            self.conn = mysql.connector.connect(host = self.host,
                                    port = self.port,
                                    db = self.name,
                                    user = self.user,
                                    passwd = self.password)
        return self.conn

    #untuk mengoneksikan database ke python
        
