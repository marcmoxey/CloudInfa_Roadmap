# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:37:05 2026

@author: moxey
"""

import time, subprocess

time_left = 60
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left = time_left - 1
    
#TODO: At the end of the countdown, play a sound file
subprocess.run(['start', "C:/Users/moxey/Desktop/DevSecOps_Roadmap/Stage_002/Ch_019/alarm.wav"], shell=True)