#!/usr/bin/python

import sys
current_key = None
current_weather = []
current_passenger_count = []

weather = {}

for line in sys.stdin:

        key, value = line.split(':')
	value_split = value.split(',')
        if key == current_key:
                if len(value_split)==2:
                        current_weather.append(value_split[0])
                else:
                        current_passenger_count.append(value)
        else:
		if len(current_passenger_count)>0:
			weather_key = 0
			for entry in current_weather:
				weather_key = weather_key + int(entry)
			weather_key = weather_key/len(current_weather)
			weather_key_str= ''
			weather_key_str = str(weather_key)
			if weather_key_str != '':
				weather[weather_key_str] = [] # 1%, 2%, 3%..  etc 50%  50 bins
                	        for i in range(10):
					weather[weather_key_str].append(0)
				for entry in current_passenger_count:
					if int(entry) 	< 10:	
						#print int(entry)
						weather[weather_key_str][int(entry)]+=1
        	current_pasenger_count = []
                current_weather = []
                current_key = key

                if len(value_split)==2:
                	current_weather.append(value_split[0])
                else:
                        current_passenger_count.append(value) 

print "-----"
for key in weather:
	tip_dist = weather[key]
        value = ''
	for tips in tip_dist:
		value = value + str(tips) + ','
	value = value[:-1]
	print key, value
