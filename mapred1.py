#!/usr/bin/python
import os,thread,time


def Jobtracker(jtip,nnip):
	f=open("mapred-site.xml","w+")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9002<value>\n</property>\n</configuration>'.format(jtip,nnip))
	f.close()
	f=open("core-site.xml","w+")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{1}:9001</value>\n</property>\n</configuration>'.format(jtip,nnip))
	f.close()
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no mapred-site.xml root@{0}:/etc/hadoop/mapred-site.xml'.format(jtip))
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no core-site.xml root@{0}:/etc/hadoop/core-site.xml'.format(jtip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} iptables -F".format(jtip,nnip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} setenforce 0".format(jtip,nnip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} systemctl stop firewalld".format(jtip,nnip))	
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hadoop-daemon.sh start jobtracker".format(jtip,nnip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} jps".format(jtip,nnip))
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hadoop job -list-active-tracker".format(jtip,nnip))

def Tasktracker(ttip,jtip):
	f=open("mapred-site.xml","w+")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{1}:9002<value>\n</property>\n</configuration>'.format(ttip,jtip))
	f.close()
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no mapred-site.xml root@{0}:/etc/hadoop/mapred-site.xml'.format(jtip,nnip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} iptables -F".format(ttip,jtip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} setenforce 0".format(ttip,jtip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} systemctl stop firewalld".format(ttip,jtip))
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hadoop-daemon.sh start tasktracker".format(ttip,jtip))
	

def Client(jtip):
	f=open("/etc/hadoop/mapred-site.xml","w")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>{0}:9002<value>\n</property>\n</configuration>'.format(jtip))
	f.close()

def readyMR()	:
	os.system('nmap -sP 192.168.43.10-19 | grep report |cut -d" " -f5|sort -k 1.11 >ipscaned.txt')
	fip=open("ipscaned.txt")	
	nnip=(fip.read().split("\n")[0])
	for iip in fip:
		ip=iip.split("\n")[0]
		if ip=='vishal' or ip==nnip:
			continue
		elif ip=='192.168.43.14':
			jtip=ip 
			Jobtracker(jtip,nnip)
		elif ip=='192.168.43.15': 
			client(nnip)
		else:
			Tasktracker(ip,jtip)
