from datetime import *

today = datetime.today()
print 'Today is:', today

for attr in \
    ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print attr, getattr(today, attr)

print 'Time:', today.hour, ':', today.minute
day = today.strftime('%A')
month = today.strftime('%B')
print 'Date:', day, month, today.day

today = today.replace(year=2015)
print today

# timer
from time import  *
start_timer = time()
struct = localtime(start_timer)
print '\nStarting Countdown at:', strftime('%X', struct)
i = 10
while i > -1:
    print i
    i -= 1
    sleep(1)
end_timer = time()
difference = round(end_timer - start_timer)
print 'Run time:', difference, 'seconds'