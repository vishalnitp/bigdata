#!/usr/bin/python
from os import system
from commands import getoutput

#system('nmap -sP 192.168.43.10-200 | grep report |cut -d" " -f5  >newiip.txt') 

d={}
d[1]="ip\t\t","Free ram\t","Hard Disk\t","CPU"
print d[1][0],d[1][1],d[1][2],d[1][3]

x1='echo $(free -m | cut -d":" -f2 |head -2|tail -1) | cut -d" " -f1'
x2='lscpu | grep "CPU MHz:" | cut -d" " -f17'
x3='echo $(df -hT | grep ext4) | cut -d" " -f5' 

fip=open("newiip.txt")
c=1
for iip in fip:
	c+=1
	ip=iip.split("\n")[0]
	if ip=='192.168.43.1' or ip=='192.168.43.152' or ip=='vishal':
		continue
	else: 
		t=getoutput("sshpass -p redhat@134 ssh -o StrictHostKeyChecking=no root@{0} {1}; {3}; {2}".format(ip,x1,x2,x3))
		x=t.split('\n')
                fram=x[0]
		fhd= x[1]
		fcp= x[2]
		d[c]=ip,fram,fhd,fcp
		print  d[c][0]," ",d[c][1],"\t\t",d[c][2],"\t\t",d[c][3]
