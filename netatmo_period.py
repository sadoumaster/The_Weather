# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:08:12 2016

@author: user1
mtype:Humidity, Temperature, CO2, Noise, Pressure
"""

import time, datetime, pprint
import lnetatmo
authorization = lnetatmo.ClientAuth()
devList = lnetatmo.DeviceList(authorization)
start= datetime.datetime(2016, 10, 1, 0, 0, 0)
start= int(time.mktime(start.timetuple()))
end= datetime.datetime(2016, 10, 3, 23, 59, 59)
end= int(time.mktime(end.timetuple()))
module='02:00:00:03:df:2e'#outdoor
#module='70:ee:50:03:d7:40'#indoor

measure_dict=devList.getMeasure( device_id='70:ee:50:03:d7:40',                             # Replace with your values
                       module_id='70:ee:50:03:d7:40',                             #    "      "    "    "
                       scale="30min",
                       mtype="Temperature,Humidity",
                       date_begin=start,
                       date_end=end)

measure_times_list = [i for i in measure_dict["body"]]
measure_times_list.sort()

for i in measure_times_list:
    print('{}:{}'.format(datetime.datetime.fromtimestamp(int(i)), 
          measure_dict['body'][i]))

time_temp_dict= {int(i):measure_dict['body'][i][0] 
                for i in measure_times_list} #timestamp:temperature
print (time_temp_dict)
