#!/usr/bin/python
# -*- coding: utf-8 -*-
from postUtils import *

url = "http://10.211.55.4:3001/api/3.0"
method = "getLatestData"
params = {"type": "hoge", "location": "fuga"}

rpc = createJsonRPC(method, params)
a = postData(rpc, url)
print a["result"]

mongo_ip = "10.211.55.4"
