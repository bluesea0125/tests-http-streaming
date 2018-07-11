#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:47:10 2018

@author: frank
"""
import time 
import random

from constants import sql_conf
hisTable=sql_conf.get('objectdetection','camera0')

from sql import execute

def process_frame(frame_cnt):
    process_obj(frame_cnt)
    obj_cnt=random.randint(0,10)
    for i in range(obj_cnt):
        process_obj(frame_cnt,obj_cnt)
    
def process_obj(frame_cnt,object_cnt):
    camera_id=0
    frame_id=frame_cnt
    object_id=object_cnt
    object_class=random.randint(0,2)#0:VEHICLE,1:PEDESTRIAN,2:MOTORCYCLE
    object_type='bus'
    object_colr='green'
    vehicle_license='粤B12345'
    person_name='陈优良'
    person_gender=random.randint(0,1)#0:MALE,1:FEMALE
    person_age=random.randint(5, 70)
    left=random.randint(0,1000)
    top=random.randint(0,1000)
    width=random.randint(20,200)
    height=random.randint(20,200)
    create_time=time.time()
    status=0
    
    query = "INSERT INTO %s SET camera_id = %d, frame_id =%d, object_id =%d, " \
                              "object_class =%d, object_type ='%s', object_colr ='%s'," \
                              "vehicle_license ='%s'," \
                              "person_name ='%s', person_gender =%s,person_age =%d," \
                              "left =%d, top =%d, width =%d, height =%d," \
                              "create_time =%d, status =%s" % \
                              (hisTable, camera_id, frame_id, object_id,
                               object_class, object_type, object_colr,
                               vehicle_license,
                               left,top,width,height,
                               person_name, person_gender, person_age,
                               create_time, status)
    execute(query)

from constants import loop_time

def start_timer():
    frame_cnt=0
    while 1:
        start = int(time.time())
        process_frame(frame_cnt)
        frame_cnt +=1
        end = int(time.time())
        tmptime = abs(end-start)
        if tmptime >= loop_time:
            pass
        else:
            sleep_time = loop_time-tmptime
            time.sleep(sleep_time)

from multiprocessing import Pool    
def main():
    task_list = []
    task_list.append(start_timer)
    
    pool = Pool(processes=len(task_list))

    for task in task_list:
        pool.apply_async(task)

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
    
    
