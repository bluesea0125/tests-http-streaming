#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:01:16 2018

@author: frank
"""
import json
from base_handler import BaseHandler

import decimal
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

from sql import query_all
#from constants import sql_conf
hisTable='t_objdet_camera0_his'#db_conf.get('objectdetection','camera0')
class CAMERA_ObjectDetection(BaseHandler):
    def get(self):
        try:
            query = "SELECT * FROM %s WHERE frame_id=(SELECT MAX(frame_id) FROM %s);"%(hisTable,hisTable)
            data = query_all(query)
            self.write(json.dumps(BaseHandler.success_ret_with_data(data), default=decimal_default))
        except Exception as e:
            self.write(json.dumps(BaseHandler.error_ret()))
            print("BTC_TransferFund error:%s", format(e))
