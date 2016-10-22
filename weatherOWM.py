# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:49:39 2016

@author: toru_hp
OpenWeatherMap  のデータを読みだす
"""

import json
import sys
from urllib.request import urlopen
import pprint

try:citycode = sys.argv[1]
except:citycode = '1862415'#'{0},{1}'.format('Hiroshima-Shi','jp')
key='1c03d86d598fba73f1debc9b011e098d'
url='http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}'.format(citycode,key)

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
