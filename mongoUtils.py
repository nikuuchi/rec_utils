from pymongo import MongoClient

class Mongo:
    '''
    Mongo
    '''
    def __init__(self, addr):
        self.addr = addr
        self.conn = MongoClient(self.addr)
        self.db   = self.conn.test

    def getErrorDataCount(self, errorMessage, start_time, end_time):
        ret = self.db.compile_message.find({"hoge" :errorMessage})
        #TODO
        return ret