#!/usr/bin/python2

import  os
import commands
import sys
import time
import hdfs1,mapred1,subNrun1,subNrun2


os.system('dialog   --infobox   "All the Basic softwares has been installed"         10    30')
time.sleep(2)

os.system('dialog   --menu  "Select The Hadoop Version you want to deploy"  15   35   2    1  "To Deploy Hadoop Version 1"   2  "To Deploy Hadoop Version 2"  2>/tmp/ch.txt')

f1=open('/tmp/ch.txt')
choice=f1.read()
f1.close()

if   choice.split('\n')[0] ==  '1':
	os.system('dialog   --infobox   "configuring hadoop version 1.........."         10    30')
	time.sleep(2)
	os.system('dialog   --menu  "Select the method"  15   35   2    1  "Manual"   2  "Automatic"  2>/tmp/ch1.txt')
	f1=open('/tmp/ch1.txt')
	choice=f1.read()
	f1.close()
	if choice.split('\n')[0] ==  '1':
		execfile('manual.py')
		subNrun1.yesno()
	else:
		thread.start_new_thread(hdfs1.readyH,())
		#thread.start_new_thread(mapred1.readyMR,())
		mapred1.readyMR()
		time.sleep(2)
		subNrun1.yesno()
		
		
elif choice.split('\n')[0] ==  '2':
	os.system('dialog   --infobox   "configuring hadoop version 2.........."         10    30')
	time.sleep(2)
	os.system('dialog   --menu  "Select the method"  15   35   2    1  "Manual"   2  "Automatic"  2>/tmp/ch1.txt')
	f1=open('/tmp/ch1.txt')
	choice=f1.read()
	f1.close()
	if choice.split('\n')[0] ==  '1':
		execfile('manual2.py')
		subNrun2.yesno()
	else:
		thread.start_new_thread(hdfs2.readyH,())
		#thread.start_new_thread(mapred2.readyMR(),)
		mapred2.readyMR()
		time.sleep(2)
		subNrun2.yesno()
 	
	
else : 
 	os.system('dialog   --infobox   "Wrong Choice.......\nPress E for exit or Any other to try again"         10    30')
	time.sleep(3)
	ch =raw_input()
	if ch=='e'or ch =="E":
		exit()
	else:
		execfile('menu.py')


