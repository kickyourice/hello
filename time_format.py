from datetime import datetime, timedelta
from interval import Interval
import sys

d_time1 = datetime.strptime(str(datetime.now().date() - timedelta(days=1)) + ' 05:00', '%Y-%m-%d %H:%M')
d_time2 =  datetime.strptime(str(datetime.now().date()) + ' 05:00', '%Y-%m-%d %H:%M')

def func(received_time):
    return datetime.strptime(received_time, '%Y%m%d%H%M%S') in Interval(d_time1, d_time2)
print(sys.getfilesystemencoding())
print(mystr.decode( 'utf-8' ).encode( type ))