#!/usr/bin/python
from commands import getoutput
from os import system
import time

import RamHardDisk,hdfs1,mapred1

system('./RamHardDisk.py >infoNodes.txt') 
#system('dialog --infobox "The host you are accessing will be client" 10 30')
time.sleep(3)
system('dialog --textbox infoNodes.txt 15 70')
system('dialog --inputbox "Enter ip address  for namenode" 10 5 2>/tmp/namenode.txt')
system('dialog --inputbox "Enter ip address  for resourcemanager" 10 5 2>/tmp/rmm.txt')
system('dialog --infobox "Now the rest nodes will be the datanodes and nodemanagers" 10 30')
time.sleep(2)
fh1=open('/tmp/namenode.txt')
fh2=open('/tmp/rmm.txt')
x1=fh1.read()
x2=fh2.read()
fh1.close()
fh2.close()
nip=x1.split('\n')[0]
hdfs2.Namenode(nip)
rmip=x2.split('\n')[0]
mapred2.RM(rmip)
fip=open("newiip.txt")
for iip in fip:
	ip=iip.split("\n")[0]
	if ip==nip or ip==rmip or ip=='vishal':
		continue
	else: 
		hdfs2.Datanode(ip,nip)
		mapred2.NM(ip,rmip)

fip.close()
