import sys
##lines = [line.rstrip('\n') for line in open('weather-data.txt')]
#lines = [line.rstrip('\n') for line in open('sample.txt')]

weather = {}

for line in sys.stdin:
	YMD = line[13:21]
	if YMD == 'YR--MODA':
		continue
	#print YMD, len(YMD)
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
	
	if YMD in weather:
		if not '*' in Speed:	
			weather[YMD]['Speed'] = Speed
		if not '*' in Gust:	
			weather[YMD]['Gust'] = Gust
		if not '*' in CloudCeiling:	
			weather[YMD]['CC'] = CloudCeiling
		if not '*' in SkyCover:	
			weather[YMD]['SkyCover'] = SkyCover
		if not '*' in LowCloudType:	
			weather[YMD]['LCT'] = LowCloudType
		if not '*' in MiddleCloudType:	
			weather[YMD]['MCT'] = MiddleCloudType
		if not '*' in HighCloudType:	
			weather[YMD]['HCT'] = HighCloudType
		if not '*' in Visibility:	
			weather[YMD]['Visib'] = Visibility
		if not '*' in Temp:	
			weather[YMD]['Temp'] = Temp
		if not '*' in Dew:	
			weather[YMD]['Dew'] = Dew
		if not '*' in MaxTemp:	
			weather[YMD]['MaxT'] = MaxTemp
		if not '*' in MinTemp:	
			weather[YMD]['MinT'] = MinTemp 
		if not '*' in Precip_01:	
			weather[YMD]['P01'] = Precip_01
		if not '*' in Precip_06:	
			weather[YMD]['P06'] = Precip_06
		if not '*' in Precip_24:	
			weather[YMD]['P24'] = Precip_24
		if not '*' in Precip_XX:	
			weather[YMD]['PXX'] = Precip_XX
		if not '*' in SnowDepth:	
			weather[YMD]['SD'] = SnowDepth
		
	else:
		weather[YMD] = {}

		#Speed_list = []
		#Gust_list = []
		#Speed_list.append(Speed)
		#Gust_list.append(Gust)
		weather[YMD]['Speed'] = Speed
		weather[YMD]['Gust'] = Gust

		#CloudCeiling_list = []
		#CloudCeiling_list.append(CloudCeiling)
		weather[YMD]['CC'] = CloudCeiling
		
		#SkyCover_list = []
		#SkyCover_list.append(SkyCover)
		weather[YMD]['SkyCover'] = SkyCover
		
		#LowCloudType_list = []
		#MiddleCloudType_list = []
		#HighCloudType_list = []
		#LowCloudType_list.append(LowCloudType)
		#MiddleCloudType_list.append(MiddleCloudType)
		#HighCloudType_list.append(HighCloudType)
		weather[YMD]['LCT']= LowCloudType
		weather[YMD]['MCT']= MiddleCloudType
		weather[YMD]['HCT']= HighCloudType

		#Visibility_list = []
		#Visibility_list.append(Visibility)
		weather[YMD]['Visib']  = Visibility

		#Temp_list = []
		#Dew_list = []
		#MaxTemp_list  = []
		#MinTemp_list  = []
		#Temp_list.append(Temp)
		#Dew_list.append(Dew)
		#MaxTemp_list.append(MaxTemp)
		#MinTemp_list.append(MinTemp)
		weather[YMD]['Temp'] = Temp
		weather[YMD]['Dew'] = Dew
		weather[YMD]['MaxT']=MaxTemp
		weather[YMD]['MinT']=MinTemp

		#Precip_01_list = []
		#Precip_06_list = []
		#Precip_24_list = []
		#Precip_XX_list = []
		#SnowDepth_list = []
		#Precip_01_list.append(Precip_01)
		#Precip_06_list.append(Precip_06)
		#Precip_24_list.append(Precip_24)
		#Precip_XX_list.append(Precip_XX)
		#SnowDepth_list.append(SnowDepth)
		weather[YMD]['P01']= Precip_01
		weather[YMD]['P06']= Precip_06
		weather[YMD]['P24']= Precip_24
		weather[YMD]['PXX']= Precip_XX
		weather[YMD]['SD'] = SnowDepth

	#print "line"	

#print weather

for key1 in weather:
	key = key1[0:4] + '-' + key1[4:6] + '-' + key1[6:8]
	dict = weather[key1]
	val = ""
	for key2 in dict:
		val = val + dict[key2] + ", "
	val = val[:-2]
	print key + ": " + val
