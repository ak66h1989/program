get_option("display.max_rows")
get_option("display.max_columns")
set_option("display.max_rows", 100)
set_option("display.max_columns", 100)
set_option('display.expand_frame_repr', False)
set_option('display.unicode.east_asian_width', True)

import time
import datetime

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except :
       # Handle the Ctrl-C exception to keep its error message from displaying.
       print('\nDone.')

print('a')

t = datetime.datetime(2015, 2, 28)
t + datetime.timedelta(days=2)
t=datetime.datetime(2015, 2, 28)-datetime.datetime(2014, 2, 28)

time.time()

delta=datetime.datetime.now()- datetime.datetime(2016, 3, 14)
for t in range(delta.days):
    date = datetime.datetime(2016, 3, 14) + datetime.timedelta(days=t+1)
    print(date.year, date.month, date.day)