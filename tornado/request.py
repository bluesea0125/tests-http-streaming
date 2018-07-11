#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:47:10 2018

@author: frank
"""

import requests
from constants import HTTP_IP_ADDR,HTTP_PORT

def post(fname='/0/objdet',params={}):
    url = 'http://%s:%d%s'%(HTTP_IP_ADDR,HTTP_PORT,fname)
    res =  requests.get(url,params)
    return res

import json
def str2dict(string):
    json_acceptable_string = string.replace("'", "\"")
    return json.loads(json_acceptable_string)

def object_detect(camera_id=0):
    fname = '/%d/objdet'%camera_id
    res = post(fname)
    if res.status_code != 200:
        return []
    res_dict = str2dict(res.text)
    if res_dict['success'] == 'false' or \
       'data' not in res_dict.keys():
        return None
    return res_dict['data']

import time
def main():
    while True:
        data = object_detect()
        print(data)
        time.sleep(0.05)

if __name__ == "__main__":
    main()