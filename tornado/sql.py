#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:47:10 2018

@author: frank
"""

from constants import HOST,USRNAME,PASSWD,DBNAME

import pymysql
def open_db(host=HOST,usr=USRNAME,pw=PASSWD,db_name=DBNAME):
    conn = pymysql.connect(host=host,
                           user=usr,
                           password=pw,
                           db=db_name,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

def close_db(conn):
    conn.close()

###############################################################################    
def query_all(query):
    conn = open_db()
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    close_db(conn)
    return result

def query_one(query):
    conn = open_db()
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchone()
    close_db(conn)
    return result

def execute(query):
    conn = open_db()
    cur = conn.cursor()
    cur.execute(query)
    close_db(conn)
###############################################################################
from constants import sql_conf

from argparse import ArgumentParser
def main():
    parser  = ArgumentParser(description='Customized Handling.')
    parser.add_argument("-m", "--mode", default= "pr", help="pr-show all")
    args = parser.parse_args()
    if args.mode == 'pr':
        query_all(query='show tables;')
    elif args.mode == 'ct':
        execute(sql_conf.get('objectdetection','camera0'))
    elif args.mode == 'ct':
        execute(sql_conf.get('objectdetection','camera0'))    

if __name__ == "__main__":
    main()
    
    
