import sys
from _datetime import datetime, timedelta
import time 


def _win_set_time(offset):
    import win32api
    time = calculate_time(offset)
    year = int(time.year)
    month = int(time.month)
    # Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    dayOfWeek = int(time.weekday())
    day = int(time.day)
    hour = int(time.hour)
    minute = int(time.minute)
    second = int(time.second)
    millseconds = int((time.microsecond)/1000)

    win32api.SetSystemTime(year,month,dayOfWeek,day,hour,minute,second,millseconds)

def calculate_time(offset):
    time = datetime.utcnow()
    return time + timedelta(seconds=offset)
 
    # dayOfWeek = wantedTime.isocalendar()[2]
    # wantedTup = wantedTime.timetuple()
    # return  wantedTup[:2] + (dayOfWeek,) + wantedTup[2:6] + (0,)
    
