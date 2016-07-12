#!/usr/bin/python
from os import system


def Checkfs():
	print "All present files in hdfs--" 
	#system('hadoop fs -lsr /')
	system('hadoop fs -mkdir /input')
	system('hadoop fs -ls /input')
	
def upload(ufile):
	system("hadoop fs -put {0} /input".format(ufile))

def runjob(operation,inpfile):
	system('dialog   --menu  "Do you want to upload a file and run job....."  15   35   2    1  "YES"   2  "NO"  2>yesno.txt')
	system("hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar {0} {1} /output".format(operation,inpfile))
	system("hadoop fs -cat /output/part-r-00000")
	
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

