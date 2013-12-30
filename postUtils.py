# -*- coding: utf-8 -*-
import json
import urllib2
import os
import yaml

def loadConfig():
    config = {}
    if os.path.exists("default.yaml"):
        with open("default.yaml") as f:
            config.update(yaml.load(f))

    if os.path.exists("development.yaml"):
        with open("development.yaml") as f:
            config.update(yaml.load(f))
    return config

def createJsonRPC(method, params):
    ret = {"method": method, "params": params, "id": 1, "jsonrpc": "2.0"}
    return json.dumps(ret)

def postData(data, url):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, data)
    return json.load(response)
