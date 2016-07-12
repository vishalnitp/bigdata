#!/usr/bin/python
from os import system

def Checkfs():
	print "All present files in hdfs--" 
	#system('hdfs fs -lsr /')
	system('hdfs dfs -mkdir /input')
	system('hdfs dfs -ls /input')
	
def upload(ufile):
	system("hdfs dfs -put {0} /input".format(ufile))

def runjob(operation,inpfile):
	system('dialog   --menu  "Do you want to upload a file and run job....."  15   35   2    1  "YES"   2  "NO"  2>yesno.txt')
	system("yarn jar /usr/share/hdfs/hdfs-examples-1.2.1.jar {0} {1} /output".format(operation,inpfile))
	system("hdfs dfs -cat /output/part-r-00000")
	
def yesno():
	system('dialog   --menu  "Do you want to upload a file and run job....."  15   35   2    1  "YES"   2  "NO"  2>yesno.txt')
	f1=open('yesno.txt')
	ch=f1.read()
	f1.close()
	if ch.split('\n')[0] ==  '1':
		infile=raw_input("Enter file name from current location ")
		upload(infile)
		operation=raw_input("Enter operation u want to perform")
		runjob(operation,infile)
	else :
		exit()

