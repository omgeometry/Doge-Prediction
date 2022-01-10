import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd
import csv
import math
import datetime

#start - 16330 (2014-09-17)
#end - 18873 (2021-09-03)

def mouse_event(event):
    if event.inaxes is not None:
        start = "9/17/14"
        date_1 = datetime.datetime.strptime(start, "%m/%d/%y")
        end = date_1 + datetime.timedelta(days=math.trunc(event.xdata)-16330)
        print('{}'.format(end.date()))

ds = [[], []]
times = pd.date_range('2014-09-17', periods=len(pd.read_csv("Dogecoin.csv")) + 1, freq='D')

with open("Dogecoin.csv", mode="r") as f:
    count = 0
    for i in csv.reader(f):
        if count != 0 and i[1] != 'null':
            ds[0].append(times[count])
            ds[1].append(float(i[2]))
        count += 1

fig, ax = plt.subplots(figsize=(12, 8))
fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=25))
ax.xaxis.set_major_formatter(DateFormatter("%m-%d-%Y"))

cid = fig.canvas.mpl_connect('motion_notify_event', mouse_event)

plt.plot(ds[0], ds[1])

plt.show()
