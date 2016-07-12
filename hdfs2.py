#!/usr/bin/python
import os,thread,time

def Namenode(nip):
	f=open("hdfs-site.xml","w+")
	f.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>file:/metadata</value>\n</property>\n</configuration')
	f.close()
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no hdfs-site.xml root@{0}:/hadoop2/etc/hadoop/hdfs-site.xml'.format(nip))
	f=open("core-site.xml","w+")
	f.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:9001</value>\n</property>\n</configuration>'.format(nip))
	f.close()
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no core-site.xml root@{0}:/hadoop2/etc/hadoop/core-site.xml'.format(nip))
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no core-site.xml root @{0}:/etc/hadoop/core-site.xml'.format(nip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} iptables -F".format(nip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} setenforce 0".format(nip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} systemctl stop firewalld".format(nip))	
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hdfs namenode -formate".format(ip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hadoop-daemon.sh start namenode".format(ip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} jps".format(nip))
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hdfs dfsadmin -report".format(nip))
	
def Datanode(dnip,nip):
	f=open("hdfs-site.xml","w+")
	f.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/datadwnld</value>\n</property>\n</configuration>')
	f.close()
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no hdfs-site.xml root@{0}:/hadoop2/etc/hadoop/hdfs-site.xml'.format(nip))
	f=open("core-site.xml","w+")
	f.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{0}:9001</value>\n</property>\n</configuration>'.format(nip))
	f.close()
	os.system('sshpass -p redhat@134 scp -o StrictHostKeyChecking=no core-site.xml root@{0}:/hadoop2/etc/hadoop/core-site.xml'.format(dnip))
	
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} iptables -F".format(dnip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} setenforce 0".format(dnip))
	os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} systemctl stop firewalld".format(dnip))	
        os.system("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} hadoop-daemon.sh start datanode".format(dnip,nip))

def client(nip):
	f=open("core-site.xml","w+")
	f.write('<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://h2nn:9001</value>\n</property>\n</configuration>'.format(nip))
	f.close()

def readyH():
	print "scanning all active ips..."
	os.system('nmap -sP 192.168.43.20-29 | grep report |cut -d" " -f5|sort -k 1.11 >ipscaned.txt')
	fip=open("ipscaned.txt")
	nip=(fip.read().split("\n")[0])
	Namenode(nip)
	for iip in fip:
		ip=iip.split("\n")[0]
		if ip=='vishal' or ip==nip or ip=='192.168.43.24':
			continue
		elif ip=='192.168.43.25': 
			client(nip)
		else:
			Datanode(ip,nip)
