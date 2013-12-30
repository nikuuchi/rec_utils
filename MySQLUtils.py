import MySQLdb
import MySQLdb.cursors

class SQL:
    def __init__(self, dbName, dbUser, dbPass):
        self.conn = MySQLdb.connect(db=dbName, user=dbUser, passwd=dbPass, cursorclass=MySQLdb.cursors.DictCursor)
        #self.db.execute("select * from users;")

    def select_ping(self, itemid):
        self.db = self.conn.cursor()
        self.db.execute("""
            select from_unixtime(clock) as time, value
            from history_uint
            where itemid=%s
            order by clock desc limit 3
            """, itemid)
        l = self.db.fetchall()
        ret = 1
        for x in l:
            if x['value'] == 0:
                ret = 0
        self.db.close()
        return ret

    def close(self):
        self.conn.close()