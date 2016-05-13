#!/usr/bin/env python

import sys
import os

# input comes from STDIN (stream data that goes to the program)
# file = open('data/weather-data.txt', 'r')
# for line in file:
for line in sys.stdin:
    if len(line.split(',')) == 19:
        val = line.split(',')
        key = val[1].split()[0]
        if key == 'tpep_pickup_datetime':
            continue
        passenger_count = val[3]
        print str(key) + ':' + str(passenger_count)
    else:
        weather = {}
        YMD = line[13:21]
        if YMD == 'YR--MODA':
            continue
        # print YMD, len(YMD)
        Speed = line[30:33].strip(' ')
        Gust = line[34:37].strip(' ')
        CloudCeiling = line[38:41].strip(' ')
        SkyCover = line[42:45].strip(' ')
        LowCloudType = line[46:47].strip(' ')
        MiddleCloudType = line[48:49].strip(' ')
        HighCloudType = line[50:51].strip(' ')
        Visibility = line[52:56].strip(' ')
        Temp = line[83:87].strip(' ')
        Dew = line[88:92].strip(' ')
        MaxTemp = line[113:116].strip(' ')
        MinTemp = line[117:120].strip(' ')
        Precip_01 = line[121:126].strip(' ')
        Precip_06 = line[127:132].strip(' ')
        Precip_24 = line[133:138].strip(' ')
        Precip_XX = line[139:144].strip(' ')
        SnowDepth = line[145:147].strip(' ')
        key = YMD[0:4] + '-' + YMD[4:6] + '-' + YMD[6:8]
        # print str(key)+':'+str(Speed)+','+str(Gust)+','+str(CloudCeiling)+','+str(SkyCover)+','+str(LowCloudType)+','+str(MiddleCloudType)+','+str(HighCloudType)+','+str(Visibility)+','+str(Temp)+','+str(Dew)+','+str(MaxTemp)+','+str(MinTemp)+','+str(Precip_01)+','+str(Precip_06)+','+str(Precip_24)+','+str(Precip_XX)+','+str(SnowDepth)
        if not ('*' in Temp):
            print str(key) + ':' + str(Temp) + ',w'
