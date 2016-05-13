#!/usr/bin/env python

import sys

current_key = None
current_weather = []
current_tip_percentages = []

weather = {}

for line in sys.stdin:

    key, value = line.split(':')
    value_split = value.split(',')
    if key == current_key:
        if len(value_split) == 2:
            current_weather.append(value_split[0])
        else:
            current_tip_percentages.append(value)
    else:
        if len(current_tip_percentages) > 0:
            weather_key = 0
            for entry in current_weather:
                weather_key = weather_key + int(entry)
            weather_key = weather_key / len(current_weather)
            weather_key_str = ''
            weather_key_str = str(weather_key)
            if weather_key_str != '':
                weather[weather_key_str] = []  # 1%, 2%, 3%..  etc 50%  50 bins
                for i in range(50):
                    weather[weather_key_str].append(0)
                for entry in current_tip_percentages:
                    if int(entry) < 50:
                        # print int(entry)
                        weather[weather_key_str][int(entry)] += 1
        current_tip_percentages = []
        current_weather = []
        current_key = key

        if len(value_split) == 2:
            current_weather.append(value_split[0])
        else:
            current_tip_percentages.append(value)

for key in weather:
    tip_dist = weather[key]
    value = ''
    for tips in tip_dist:
        value = value + str(tips) + ','
    value = value[:-1]
    print key, value
