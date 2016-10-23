# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:34:32 2016
@author: Kikkawa
絶対湿度を求める。
11g/㎡3以下だとインフルエンザ感染率UP
8.5g/㎡3以下でのどの渇き(２１℃ ４５．１％、２０℃ ４８．０％、１９℃ ５１．１％、１８℃ ５４．４％）
相対湿度80%以上でカビが生える、60%以上でダニが増え始める
"""

from math import exp, log

#relative_humidity=70 #Relative humidity %
#relative_temperature=25 #Relative temperature dgrees Celsius

def get_abs_hum(relative_Humidity, relative_Temperature):
    '''
    Determined Absolute Temperature(g/m3) by calculation
    '''
    relative_humidity=float(relative_Humidity)
    absolute_temperature= float(relative_Temperature) + 273.15
    absolute_humidity= (relative_humidity/100*0.00794
    *exp(-6096.9385/absolute_temperature+21.2409642-0.02711193
    *absolute_temperature+0.00001673952*absolute_temperature**2
    +2.433502*log(absolute_temperature))/(1+0.00366*relative_Temperature))
    return absolute_humidity

print('{0:.1f}g/m3'.format(get_abs_hum(79,14.3)))