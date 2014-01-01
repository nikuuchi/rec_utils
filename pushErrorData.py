#!/usr/bin/python
# -*- coding: utf-8 -*-
from postUtils import *
from mongoUtils import *
import datetime
import time

def datetime2long(date):
    return long(time.mktime(date.timetuple()))

if __name__ == '__main__':
    config = loadConfig()

    url = config["rec"]["url"]
    method = "pushRawData"
    params_orig = {"location": "AppServer", "authid":"aspen"}

    end_time = datetime2long(datetime.datetime.today())
    start_time = end_time - (60 * 90) # 90 minutes

    mongo = Mongo(config["mongo"]["ip"])
    for x in config["data"]:
        count = mongo.getErrorDataCount(x, start_time, end_time)
        print count
        params = params_orig.copy()
        params["type"] = x+".count"
        params["data"] = count

        rpc = createJsonRPC(method, params)
        postData(rpc, url)
