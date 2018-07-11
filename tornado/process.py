#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:47:10 2018

@author: frank
"""
import time 
import random

from sql import update  
from constants import loop_time

class ObjectDetection(object):
    def __init__(self):
        self.frame_cnt = 0
        self._hisTable = 't_objdet_camera0_his'
        
    def __process_frame(self,frame_cnt):
        print('processing frame...')
        obj_cnt=random.randint(0,4)
        print('object count : %d'%obj_cnt)
        for i in range(obj_cnt):
            self.__process_obj(frame_cnt,obj_cnt)
        print('frame processed')
            
    def __process_obj(self,frame_cnt,object_cnt):
        print('processing object...')
        camera_id=0
        frame_id=frame_cnt
        object_id=object_cnt
        object_class=random.randint(0,2)#0:VEHICLE,1:PEDESTRIAN,2:MOTORCYCLE
        object_type='bus'
        object_colr='green'
        vehicle_license='B12345'
        person_name='jack'
        person_gender=random.randint(0,1)#0:MALE,1:FEMALE
        person_age=random.randint(5, 70)
        left=random.randint(0,1000)
        top=random.randint(0,1000)
        width=random.randint(20,200)
        height=random.randint(20,200)
        create_time=int(time.time())
        status=random.randint(0,3)
        
        query="INSERT INTO `t_objdet_camera0_his`"\
                          "(`camera_id`, `frame_id`, `object_id`, "\
                          "`object_class`, `object_type`, `object_colr`, "\
                          "`vehicle_license`,"\
                          "`person_name`, `person_gender`, `person_age`, "\
                          "`left`, `top`, `width`, `height`, "\
                          "`create_time`, `status`) "\
                          "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                          
        params = [camera_id, frame_id, object_id,\
                  object_class, object_type, object_colr,\
                  vehicle_license,\
                  person_name, person_gender, person_age,\
                  left,top,width,height,\
                  create_time, status]
        update(query,tuple(params))
        time.sleep(0.01)
        print('object processed')
        
    def run_task(self):
        while True:
            start = int(time.time())
            self.__process_frame(self.frame_cnt)
            self.frame_cnt+=1
            end = int(time.time())
            tmptime = abs(end-start)
            if tmptime >= loop_time:
                print('%d elapsed'%tmptime)
            else:
                sleep_time = loop_time-tmptime
                print('%d elapsed'%sleep_time)
                time.sleep(sleep_time)

def start_timer():
    task = ObjectDetection()
    task.run_task()

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
    
    
