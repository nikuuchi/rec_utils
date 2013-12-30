# -*- coding: utf-8 -*-
import json
import urllib2
import os
import yaml

def loadConfig():
    config = {}
    default_path = os.path.join(os.path.dirname(__file__), 'default.yaml')
    if os.path.exists(default_path):
        with open(default_path) as f:
            config.update(yaml.load(f))

    dev_path = os.path.join(os.path.dirname(__file__), 'development.yaml')
    if os.path.exists(dev_path):
        with open(dev_path) as f:
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
