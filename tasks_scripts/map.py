#!/usr/bin/python

import sys
import os

for line in sys.stdin:
		
	for i in range(20):
		line = line.replace("     ",",")
	for i in range(20):
		line = line.replace("    ",",")
	for i in range(20):
		line = line.replace("   ",",")
	for i in range(20):
		line = line.replace("  ",",")
	for i in range(20):
		line = line.replace(" ",",")
	if line[0]==',':
		line = line[1:]
	splits1 = line.split(",")
	splits2 = line.split(",")
	#print len(splits1)
	#print len(splits2)	
	
	
	if len(splits2) >= 34 and len(splits2) <= 34: # weather data
		
		key1 = splits2[2][0:8]
		key1 = key1[0:4]+'-'+key1[4:6]+'-'+key1[6:8]
		keyAttributes = (key1)
		other1 = ",".join(splits2[0:2])
		other2 = ",".join(splits2[3:])
		otherAttributes = other1 + "," + other2
		
		valuePair = ("weather", otherAttributes) 
		
		if key1 != 'YR--MO-DA': 
			print "%s\t%s" % (keyAttributes, valuePair) 
		else:
			pass		

	elif len(splits1) >= 21 and len(splits1) <= 21:  # taxi data
		
		key1 = splits1[1]
		keyAttributes = (key1)
		other1 = ",".join(splits1[0:1])
		other2 = ",".join(splits1[5:])
		otherAttributes = other1 + "," + other2
		valuePair = ("taxi", otherAttributes) 	
		
		if key1 != 'tpep_pickup_datetime':
			print "%s\t%s" % (keyAttributes, valuePair)
		else:
			pass

	else:
		pass

