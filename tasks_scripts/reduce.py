#!/usr/bin/python

import sys

current_key = None
current_weather = []
current_taxis = []

for line in sys.stdin:

        key, value = line.split('\t')
        value = eval(value)

        tableName = value[0]

        tempAttributes = value[1]
        tableAttributes = tempAttributes.split(",")

        if key == current_key:
	
                if tableName == 'weather':
                        current_weather = tableAttributes
                else:
                        current_taxis = tableAttributes
        else:  
 			 
               	allAttributes = []
                allAttributes.extend(current_taxis)
                allAttributes.extend(current_weather)
		
		if len(allAttributes) == 17:  #make sure each key appears in both
                	
			entry1 = str(current_key)
			 
			entry2 = str(allAttributes)
        		entry2 = entry2.replace('[','')
        		entry2 = entry2.replace(']','')
        		for i in range(30):
        		        entry2 = entry2.replace("'",'')
        		        	
			print "%s\t%s" % (entry1, entry2) 

			current_taxis = [] 
			current_weather = [] 	
			current_key = key
	
			if tableName == 'weather':
        	               	current_weather = tableAttributes
               		else:
                       		current_taxis = tableAttributes
		else: 
			current_trips = []
                        current_fares = []
                        current_key = key

                        if tableName == 'weather':
                                current_weather = tableAttributes
                        else:
                                current_taxis = tableAttributes
			
if current_key == key: 
	allAttributes = []
        allAttributes.extend(current_taxis)
        allAttributes.extend(current_weather)
	
	entry1 = str(current_key)
        entry1 = entry1.replace('(','')
        entry1 = entry1.replace(')','')
        for i in range(30):
                entry1 = entry1.replace("'",'')
	 
	entry2 = str(allAttributes)
        entry2 = entry2.replace('[','')
        entry2 = entry2.replace(']','')
        for i in range(30):
                entry2 = entry2.replace("'",'')
                	
	print "%s\t%s" % (entry1, entry2) 

