#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:47:10 2018

@author: frank
"""

HOST='127.0.0.1'
USRNAME='root'
PASSWD='root'
DBNAME='stream'

FPS = 10
loop_time = 1000 / FPS

import os
root_path = os.path.dirname(os.path.abspath(__file__))

import ConfigParser
sql_conf = ConfigParser.ConfigParser()
sql_conf.read(os.path.join(root_path,'sql.ini'))