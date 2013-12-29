# -*- coding: utf-8 -*-
import json
import urllib2

def createJsonRPC(method, params):
    ret = {"method": method, "params": params, "id": 1, "jsonrpc": "2.0"}
    return json.dumps(ret)

def postData(data, url):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, data)
    return json.load(response)
