#!/usr/bin/python
# -*- coding: utf-8 -*-
from postUtils import *
from mongoUtils import *

url = "http://live.assure-it.org/rec3/api/3.0/"
method = "getLatestData"
#method = "pushRawData"
params = {"type": "hoge", "location": "fuga", "authid":"auth", "data":3}

rpc = createJsonRPC(method, params)
a = postData(rpc, url)
print a["result"]

mongo_ip = "10.211.55.4"
m = Mongo(mongo_ip)
count = m.getErrorDataCount("struct")
for x in count:
    print x
