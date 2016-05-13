#!/usr/bin/python

import sys

# Reducer takes the output from the LoadMap(mapper) and prints the date and total trips
# key = date
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
                    if '*' not in value[i]:
                        weather[i] = value[i]
            else:
                weather = value
        results[key] = [trip_count, weather]
    else:
        if len(value) == 4:
            results[key] = [1, None]
        if len(value) == 17:
            results[key] = [None, value]

for key in results:
    weather = results[key][1]
    trip_count = results[key][0]
    print key, str(trip_count)