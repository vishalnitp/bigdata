#!/usr/bin/python
import os,thread,time

def RM(rmip):
	f=open("yarn-site.xml","w+")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n <configuration>\n<property>\n<name>yarn.resourcemanager.resource-tracker.address</name>\n<value>{0}:8025</value>\n</property>\n\n<property>\n<name>yarn.resourcemanager.scheduler.address</name>\n<value>{0}:8030</value>\n</property>\n</configuration>'.format(rmip))
	f.close()
	os.system("sshpass -p redhat@134 scp -o StrictHostKeyChecking=no yarn-site.xml root@{0}:/hadoop2/etc/hadoop/yarn-site.xml".format(rmip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} iptables -F".format(rmip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} setenforce 0".format(rmip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} systemctl stop firewalld".format(rmip))
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} yarn-daemon.sh start resourcemanager".format(rmip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} jps".format(rmip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} yarn node -list-all".format(rmip))
	

def NM(ip,rmip):
	f=open("yarn-site.xml","w+")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n <configuration>\n<property>\n<name>yarn.resourcemanager.resource-tracker.address</name>\n<value>{1}:8025</value>\n</property>\n\n<property>\n<name>yarn.nodemanage.aux-services</name>\n<value>mapreduse_shuffle</value>\n</property>\n</configuration>'.format(ip,rmip))
	f.close()	
	os.system("sshpass -p redhat@134 scp -o StrictHostKeyChecking=no yarn-site.xml root@{0}:/hadoop2/etc/hadoop/yarn-site.xml".format(ip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} iptables -F".format(ip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} setenforce 0".format(ip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} systemctl stop firewalld".format(ip))
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} yarn-daemon.sh start nodemanager".format(ip))
	

def Client(rmip):
	f=open("/hadoop2/etc/hadoop/yarn-site.xml","w+")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n <configuration>\n<property>\n<name>yarn.resourcemanager.resource-tracker.address</name>\n<value>{0}:8025</value>\n</property>\n\n<property>\n<name>yarn.resourcemanager.scheduler.address</name>\n<value>{0}:8030</value>\n</property>\n\n<property>\n<name>yarn.resourcemanager.address</name>\n<value>{0}:8032</value>\n</property>\n</configuration>'.format(rmip))
	f.close()	
	f=open("/hadoop2/etc/hadoop/mapred-site.xml","w")
	f.write('<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n <configuration>\n<property>\n<name>mapreduce.framework.name</name>\n<value>yarn</value>\n</property>\n</configuration>')
	f.close()

def readyMR():	
	os.system('nmap -sP 192.168.43.20-29 | grep report |cut -d" " -f5|sort -k 1.11 >ipscaned.txt')
	fip=open("ipscaned.txt")
	nnip=(fip.read().split("\n")[0])
	for iip in fip:
		ip=iip.split("\n")[0]
		if ip=='vishal' or ip==nnip:
			continue
		elif ip=='192.168.43.24':
			rmip=ip 
			RM(rmip)
		elif ip=='192.168.43.15': 
			client(rmip)
		else:
			NM(ip,jtip)	
