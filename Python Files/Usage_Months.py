#!/usr/bin/env python
import sys
from datetime import datetime as dt

# Reducer takes the output from the LoadMap(mapper) and prints the month
# and total trips made in the week days and total trips made in the weekend
# in that particular month
# key = month
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

month = {1: 'January', 2: 'Febuary', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
         7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month_usage = {}
for key in results:
    trip_count = results[key][0]
    if trip_count != None:
        key_month = month[dt.strptime(key, '%Y-%m-%d').month]
        if dt.strptime(key, '%Y-%m-%d').weekday() > 4:
            if key_month in month_usage.keys():
                if 'Weekend' in month_usage[key_month].keys():
                    month_usage[month[dt.strptime(key, '%Y-%m-%d').month]]['Weekend'] = month_usage[month[
                        dt.strptime(key, '%Y-%m-%d').month]]['Weekend'] + trip_count
                else:
                    month_usage[month[dt.strptime(key, '%Y-%m-%d').month]]['Weekend'] = trip_count
            else:
                month_usage[month[dt.strptime(key, '%Y-%m-%d').month]] = {'Weekend':trip_count}
        else:
            if key_month in month_usage.keys():
                if 'Weekday' in month_usage[key_month].keys():
                    month_usage[month[dt.strptime(key, '%Y-%m-%d').month]]['Weekday'] = month_usage[month[
                        dt.strptime(key, '%Y-%m-%d').month]]['Weekday'] + trip_count
                else:
                    month_usage[month[dt.strptime(key, '%Y-%m-%d').month]]['Weekday'] = trip_count
            else:
                month_usage[month[dt.strptime(key, '%Y-%m-%d').month]] = {'Weekday':trip_count}
for key in month_usage:
    print key, month_usage[key]['Weekday'], month_usage[key]['Weekend']
