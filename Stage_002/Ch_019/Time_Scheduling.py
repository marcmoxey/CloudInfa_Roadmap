# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:56:26 2026

@author: moxey
"""

import time 
# print(time.time())
print(time.ctime())
this_moment = time.time()
print(time.ctime(this_moment))

# Pasuing Programs 
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)
# time.sleep(5)


# The datetime Module 
import datetime, time

print(datetime.datetime.now())
dt = datetime.datetime(2026, 10, 21, 16, 29,0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

dt = datetime.datetime.fromtimestamp(10000000)
print(dt)
dt = datetime.datetime.fromtimestamp(time.time())
print(dt)

halloween_2026 = datetime.datetime(2026, 10,31,0, 0,0)
new_years_2027 = datetime.datetime(2027, 1,1, 0,0,0)
oct_31_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)
print(halloween_2026 == oct_31_2026)
print(halloween_2026 > new_years_2027)
print(new_years_2027 > halloween_2026)
print(new_years_2027 != oct_31_2026)

# Representing Durtion 
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))

now = datetime.datetime.now()
datetime.datetime(2026,12,2,18,38,50,636181)
thousand_days = datetime.timedelta(days=1000)
result = now + thousand_days
print(result)

oct_21st = datetime.datetime(2026, 10, 21,16,29,0)
about_thirty_years = datetime.timedelta(days=365*30)
print(oct_21st)
print(oct_21st - about_thirty_years)
print(oct_21st - (2* about_thirty_years))


# Pausing Until a Specific date
# halloween_2039 = datetime.datetime(2029, 10, 31, 0,0,0 )
# while datetime.datetime.now() < halloween_2039:
#     time.sleep(1) # wait 1 second before looping to check again
    
    

# Converting datetime Objects into Strings 
oct_21st = datetime.datetime(2026, 10, 21, 16, 29, 0)
result = oct_21st.strftime('%Y/%m/%d %H:%M:%S')
print(result)
result = oct_21st.strftime('%I:%M %p')
print(result)
result = oct_21st.strftime("%B of %y")
print(result)


# Converting Strings into datetime Objects
dt = datetime.datetime.strptime('October 21, 2026', '%B %d, %Y')
print(dt)
dt = datetime.datetime.strptime('2026/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(dt)
dt = datetime.datetime.strptime('October of 26', '%B of %y')
print(dt)
dt = datetime.datetime.strptime('November of 63', '%B of %y')
print(dt)
dt = datetime.datetime.strptime('November of 73', '%B of %y')
print(dt)


# Launching other programs from python
import subprocess
subprocess.run(['C:\\Windows\\System32\\calc.exe'])
calc_proc = subprocess.Popen(['C:\\Windows\\System32\\calc.exe'])
result = calc_proc.poll() == None
print(result)
result = calc_proc.wait() # Doesn't retun untill calculator closes 
print(result)
result = calc_proc.poll()
print(result)

# import subprocess
# paint_proc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
# paint_proc.kill()


# Passing Command Line Arguments to Processes
result = subprocess.run(['C:\\Windows\\notepad.exe','C:\\Users\\moxey\\Desktop\DevSecOps_Roadmap\\Stage_002\\Ch_019\\hello.txt' ])
print(result)


# Receiving Output from launched Commands
proc = subprocess.run(['ping', '-n', '4','nostarch.com'], capture_output=True, text=True)
print(proc.stdout)


# Running Task Scheduler, launched, and cron
file_obj = open('hello2.txt', 'w') # Create hello2.txt file
file_obj.write('Hello, world!')
file_obj.close()
import subprocess
subprocess.run(['start','hello2.txt'], shell=True)