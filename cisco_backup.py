#!/usr/bin/python

# A script to ssh into a cisco device, set the terminal length
# such that paging is turned off, then run commands.
# the results go into 'resp', then are displayed.
# Tweak to your hearts content!

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from time import time
import threading
from threading import Thread
from queue import Queue
import paramiko
import cmd
import time
import sys
import re


my_file = open("ipler.txt", "rb")
ilk_sira = Queue()

buff = ''
resp = ''




def IPokuyan():
    while True:
		IP = ilk_sira.get()
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(IP, username='sshusername', password='sshpassword')
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		chan = ssh.invoke_shell()
		chan.settimeout(20)
		# first we enable!
		chan.send('en\n')
		#time.sleep(1)
		#resp = chan.recv(9999)
		#print resp
		
		# enablepassword!
		chan.send('ciscoenablepassword\n')
		#time.sleep(1)
		#print resp
		chan.send('copy running-config ftp://ftpusername:ftppassword@ftpserveripaddress\n')
		#time.sleep(1)
		chan.send('\r\n')
		#time.sleep(1)
		chan.send('\r\n')
		time.sleep(1)	
		buff = ''
		while buff.find('copied') < 0:
			resp = chan.recv(9999)
			buff += resp
			print resp
			print IP + " YEDEK OK"


if __name__ == "__main__":
    for i in range(2):
        t = Thread(target = IPokuyan)
        t.daemon = True
        t.start()

    for line in my_file:
		l = [i.strip() for i in line.split(' ')]
		IP = l[0]
		ilk_sira.put(IP)

    ilk_sira.join()
time.sleep(1)
my_file.close()
