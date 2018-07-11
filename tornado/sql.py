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
    
def update(query,values):
    conn = open_db()
    cursor = conn.cursor()
    cursor.execute(query,values)
    conn.commit()
###############################################################################

from constants import sql_conf
from argparse import ArgumentParser
def main():
    parser  = ArgumentParser(description='Customized Handling.')
    parser.add_argument("-m", "--mode", default= "prt", help="prt-print all tables in the database")
    args = parser.parse_args()
    if args.mode == 'prt':
        print('printing tables...')
        print(query_all(query='show tables;'))
    if args.mode == 'shw':
        print('showing table...')
        print(query_all(query='select * from t_objdet_camera0_his;'))
    elif args.mode == 'crt':
        execute(sql_conf.get('objectdetection','camera0'))
    elif args.mode == 'add':
        query="INSERT INTO `t_objdet_camera0_his`"\
              "(`camera_id`, `frame_id`, `object_id`, "\
              "`object_class`, `object_type`, `object_colr`, "\
              "`vehicle_license`,"\
              "`person_name`, `person_gender`, `person_age`, "\
              "`left`, `top`, `width`, `height`, "\
              "`create_time`, `status`) "\
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params=[0,1,4,2,'bus','green','B12345','jack',0,41,610,555,69,112,1531280759,2]
        print(query,tuple(params))
        update(query,tuple(params))

if __name__ == "__main__":
    main()
    
    
