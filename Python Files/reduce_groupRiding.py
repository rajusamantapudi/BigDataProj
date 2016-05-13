#!/usr/bin/env python

import sys

current_key = None
current_weather = []
current_passenger_count = []

weather = {}
file = open('data/mapout.txt', 'r')
for line in file:
# for line in sys.stdin:

    key, value = line.split(':')
    value_split = value.split(',')
    if key == current_key:
        if len(value_split) == 2:
            current_weather.append(value_split[0])
        else:
            current_passenger_count.append(value)
    else:
        if len(current_passenger_count) > 0 and len(current_weather) > 0:
            weather_key = current_weather[0]
            #for entry in current_weather:
            #    weather_key = weather_key + int(entry)
            #weather_key = weather_key / len(current_weather)
            # weather_key_str = ''
            # weather_key_str = str(weather_key)
            if weather_key != None:
                weather[weather_key] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1%, 2%, 3%..  etc 50%  50 bins
                # for i in range(10):
                #     weather[weather_key].append(0)
                for entry in current_passenger_count:
                    if int(entry) < 10:
                        # print int(entry)
                        weather[weather_key][int(entry)] += 0.001
        current_pasenger_count = []
        current_weather = []
        current_key = key

        if len(value_split) == 2:
            current_weather.append(value_split[0])
        else:
            current_passenger_count.append(value)

for key in weather:
    tip_dist = weather[key]
    value = ''
    for tips in tip_dist:
        value = value + str(tips) + ','
    value = value[:-1]
    print key, value
