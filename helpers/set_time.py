import sys
from _datetime import datetime, timedelta
import time 


def _win_set_time(offset):
    import win32api
    time = calculate_time(offset)
    win32api.SetSystemTime(*time)

def calculate_time(offset):
    time = datetime.now()
    td = timedelta(seconds=offset)
    wantedTime = time + td
    dayOfWeek = wantedTime.isocalendar()[2]
    wantedTup = wantedTime.timetuple()
    return  wantedTup[:2] + (dayOfWeek,) + wantedTup[2:6] + (0,)
    
