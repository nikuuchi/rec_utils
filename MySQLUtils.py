import MySQLdb

class SQL:
    def __init__(self, dbName, dbUser, dbPass):
        self.conn = MySQLdb.connect(db=dbName, user=dbUser, passwd=dbPass)
        self.db = self.conn.cursor()
