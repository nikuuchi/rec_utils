from pymongo import MongoClient
import re

class Mongo:
    '''
    Mongo
    '''
    def __init__(self, addr):
        self.addr = addr
        self.conn = MongoClient(self.addr)
        self.db   = self.conn.test

    def getErrorDataCount(self, errorMessage, start_time, end_time):
        r = re.compile(errorMessage)
        ret = self.db.compile_message.find({"message" : r, "unixtime" : {"$gte" : start_time, "$lte": end_time}}).count()
        return ret