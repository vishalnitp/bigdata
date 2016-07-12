#!/usr/bin/python2

#!/usr/bin/python
import  os,commands,time,sys,socket

print "print executing login.."
os.system('dialog   --infobox   " WELCOME TO HADOOP CLUSTER "         10    30')

time.sleep(2)

os.system('dialog   --msgbox  "Click OK to GO "         10   30')
os.system('dialog   --inputbox  "Enter your UserName: " 10 30     2>/tmp/user.txt')
os.system('dialog  --insecure  --passwordbox  "Password:"  10 30   2>/tmp/pass.txt')


f1=open('/tmp/user.txt')
user=f1.read()
f1.close()

f2=open('/tmp/pass.txt')
password=f2.read()
print password
f2.close()

if   user == "vishal"   and  password  == "hadoopv" :
	print "Executing menu...."
	execfile('menu.py')
	
else :
	os.system('dialog   --infobox   "Wrong Password"         10    30')
	time.sleep(3)
	exit()	



