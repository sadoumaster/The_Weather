# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:49:39 2016

@author: toru_hp
OpenWeatherMap  のデータを読みだす
0 dgrees celcius = absolute temperature 273.15 degrees celcius
#16days=====
resp['list'][num][keys]
keys=['clouds', 'deg', 'dt', 'humidity', 'pressure', 'speed', 'temp', 'weather']
temp_keys=['day', 'eve', 'max', 'min, 'morn', 'night']
weather_keys=['description', 'icon', 'id', 'main']
=====

#current weather=====
keys=['name', 'cod', 'coord', 'sys', 'wind', 'weather', 'main', 'clouds', 'base',
 'dt', 'id'] 
main_keys=['humidity', 'temp', 'temp_min', 'sea_level', 'temp_max',
'grnd_level', 'pressure']
weather_keys=same 16days
=====

#5days=====
resp['list'][num][keys]
keys=['sys', 'wind', 'weather', 'main', 'clouds', 'dt', 'dt_txt']
main_keys=['temp_min', 'temp', 'humidity', 'grnd_level', 'sea_level',
'temp_kf', 'pressure', 'temp_max']
['weather'][0]_keys=['description', icon', 'id', 'main']
=====
"""

import json
import sys
from urllib.request import urlopen
import pprint

try:citycode = sys.argv[1]
except:citycode = '1862415'#'{0},{1}'.format('Hiroshima-Shi','jp')
key='1c03d86d598fba73f1debc9b011e098d'
http='api.openweathermap.org/data/2.5/forecast?' #5days/3hour forecast
#http='api.openweathermap.org/data/2.5/weather?' #current weather
#http='api.openweathermap.org/data/2.5/forecast/daily?' #16day/daily forcast
if 'daily' in http : url='http://{}id={}&cnt=16&APPID={}'.format(http, citycode, key)
else : url='http://{}id={}&APPID={}'.format(http, citycode, key)

    
resp = urlopen(url).read()
resp= json.loads(resp.decode('utf-8'))
pprint.pprint(resp)
"""
print(resp['title'])
print(resp['description']['text'])

for forecast in resp['forecasts']:
    print('*'*20)
    print(forecast['dateLabel'] + forecast['date'])
    print(forecast['telop'])
    if forecast['temperature']['max'] == None: continue
    print('最高気温:{}度,最低気温:{}度'.format(forecast['temperature']['max']['celsius'],
          forecast['temperature']['min']['celsius']))
"""
