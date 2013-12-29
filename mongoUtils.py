from pymongo import MongoClient

class Mongo:
    '''
    Mongo
    '''
    def __init__(self, addr):
        self.addr = addr
        self.conn = MongoClient(self.addr)
        self.db   = self.conn.test

    def getErrorData(errorMessage):
        return errorMessage
