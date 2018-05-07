#!/usr/bin/env python
from socket import *
from netaddr import *
from datetime import datetime

startTime = datetime.now()
print 'start time = ',startTime

#hanyang_ip = IPNetwork('166.104.0.0/16') HW2-2
#hanyang_ip = IPNetwork('166.104.177.0/24') #testing
hanyang_ip = IPNetwork('166.104.128.0/18') #bigger testing

webservers = []

def scanPort(ip,port):
	socketObject = socket(AF_INET,SOCK_STREAM)
	socketObject.settimeout(1)
	try:
		socketObject.connect((ip,port))
		addr = ip+':'+str(port)
		host = getHost(ip)
		webservers.append([addr,host])
		socketObject.close()

	except error as e:
		pass
	except timeout as e:
		print e
		pass

def getHost(ip):
	socketObject = socket(AF_INET,SOCK_STREAM)
	try:
		result = gethostbyaddr(ip)
		return result[0]
	except error as e:
		print e
		pass

for ip in hanyang_ip:
	#print '%s' % ip
	scanPort(str(ip),80)
 	scanPort(str(ip),8080)

endTime = datetime.now()

print 'Network = ',str(hanyang_ip)
print 'Time needed = ', endTime - startTime
print 'Total open webserver = ',len(webservers)

for webserver in webservers:
	print webserver[0], ' is open [',webserver[1],']'

raw_input()