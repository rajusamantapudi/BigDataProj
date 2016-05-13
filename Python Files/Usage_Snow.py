#!/usr/bin/env python

import sys

# Reducer takes the output from the LoadMap(mapper) and joins the weather and taxi data
# to print the total trips made with respect to the snow conditions.
# key = Snow conditions
# value = total trips

results = {}
trips_count = 0
for line in sys.stdin:
    weather = {}
    val = line.split(':')
    key = val[0]
    value = val[1].split(',')
    if key in results.keys():
        [trip_count, weather] = results[key]
        if len(value) == 4:
            if trip_count is not None:
                trip_count = trip_count + 1
            else:
                trip_count = 1
        if len(value) == 17:
            if weather is not None:
                for i in range(len(value)):
                    val = value[i].strip()
                    if '*' not in val:
                        weather[i] = val
            else:
                weather = value
        results[key] = [trip_count, weather]
    else:
        if len(value) == 4:
            results[key] = [1, None]
        if len(value) == 17:
            results[key] = [None, value]
snow_usage = {}
for key in results:
    weather = results[key][1]
    trip_count = results[key][0]
    if trip_count != None:
        if weather[16].isdigit():
            if int(weather[16]) < 1:
                if 'No Snow' in snow_usage.keys():
                    snow_usage['No Snow'] = snow_usage['No Snow'] + int(trip_count)
                else:
                    snow_usage['No Snow'] = int(trip_count)
            elif int(weather[16]) > 1 and int(weather[16]) < 2.5:
                if 'Notable' in snow_usage.keys():
                    snow_usage['Notable'] = snow_usage['Notable'] + int(trip_count)
                else:
                    snow_usage['Notable'] = int(trip_count)
            elif int(weather[16]) >= 2.5 and int(weather[16]) < 4:
                if 'Significant' in snow_usage.keys():
                    snow_usage['Significant'] = snow_usage['Significant'] + int(trip_count)
                else:
                    snow_usage['Significant'] = int(trip_count)
            elif int(weather[16]) >= 4 and int(weather[16]) < 6:
                if 'Major' in snow_usage.keys():
                    snow_usage['Major'] = snow_usage['Major'] + int(trip_count)
                else:
                    snow_usage['Major'] = int(trip_count)
            elif int(weather[16]) >= 6 and int(weather[16]) < 10:
                if 'Crippling' in snow_usage.keys():
                    snow_usage['Crippling'] = snow_usage['Crippling'] + int(trip_count)
                else:
                    snow_usage['Crippling'] = int(trip_count)
            else:
                if 'Extreme' in snow_usage.keys():
                    snow_usage['Extreme'] = snow_usage['Extreme'] + int(trip_count)
                else:
                    snow_usage['Extreme'] = int(trip_count)
        else:
            if 'No Snow' in snow_usage.keys():
                snow_usage['No Snow'] = snow_usage['No Snow'] + int(trip_count)
            else:
                snow_usage['No Snow'] = int(trip_count)

for key in snow_usage:
		print key, snow_usage[key]
