# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:46:32 2016

@author: toru_hp
Yahooの天気予報
"""

import sys
import json
from urllib import request

try:citycode = sys.argv[1]
except: citycode = '340010'
url='http://weather.livedoor.com/forecast/webservice/json/v1?city={}'.format(citycode)
resp = request.urlopen(url).read()
resp=resp.decode('utf-8')
resp= json.loads(resp)
print(resp['title'])
print(resp['description']['text'])

for forecast in resp['forecasts']:
    print('*'*20)
    print(forecast['dateLabel'] + forecast['date'])
    print(forecast['telop'])
    if forecast['temperature']['max'] == None: continue
    print('最高気温:{}度,最低気温:{}度'.format(forecast['temperature']['max']['celsius'],
          forecast['temperature']['min']['celsius']))
