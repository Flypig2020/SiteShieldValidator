#! /usr/bin/env python2
from socket import *
import sys, time
from datetime import datetime
import os
import csv

scriptDir = sys.path[0]
hostfilepath = os.path.join(scriptDir, 'hosts.txt')
hostFile = open(hostfilepath, "r")
hosts = hostFile.readlines()

def scan_host(host, port):
	
	s = socket(AF_INET, SOCK_STREAM)
	try:
		con=s.connect((host, port))
		print (con)
		return True
	except:
		print("scan_host exception catched")
		return False

with open('result.csv', 'w') as csvfile:
	fieldnames = ['Hostanme', 'IP', 'Port', 'Status']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for host in hosts:

		try:
			host = host.strip()
			hostip = gethostbyname(host)
			for port in (80,443):
				try:
					print  ("\n[*] Host: %s IP: %s" % (host, hostip))
					if scan_host(hostip,port):
						writer.writerow({'Hostanme': host, 'IP': hostip, 'Port': port, 'Status': "open" })
					else:
						writer.writerow({'Hostanme': host, 'IP': hostip, 'Port': port, 'Status': "close" })
				except Exception, e :
					pass
		except Exception, e:
			writer.writerow({'Hostanme': host, 'IP': "N/A", 'Port': "N/A", 'Status': "can not resolve" })
			print("\n[*] can not resolve Host: %s " % (host))
			pass

hostFile.close()


