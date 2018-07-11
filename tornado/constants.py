#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:47:10 2018

@author: frank
"""

# Host
HTTP_IP_ADDR='127.0.0.1'
HTTP_PORT=9092

# MySQL
HOST='localhost'
USRNAME='root'
PASSWD='root'
DBNAME='stream'

# Timer
FPS = 10
loop_time = 1.0 / FPS

# SQL
import os
root_path = os.path.dirname(os.path.abspath(__file__))

import ConfigParser
sql_conf = ConfigParser.ConfigParser()
sql_conf.read(os.path.join(root_path,'sql.ini'))