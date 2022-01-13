import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd
import csv
import math
import datetime
import pygame


# start - 16330 (2014-09-17)
# end - 18873 (2021-09-03)


def pyg(text1):
    if text1 is None or len(text1) <= 1:
        return
    text1 = str(text1).split(" ")
    pygame.init()
    pygame.display.set_caption('mpltest')
    display_screen = pygame.display.set_mode((300, 300))
    display_screen.fill((0, 0, 0))
    pygame.display.flip()
    base_font = pygame.font.Font("freesansbold.ttf", 18)
    text = base_font.render("Date: " + datetime.datetime.strptime(text1[0], "%Y-%m-%d").strftime("%B-%d-%Y"), True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 80)
    display_screen.blit(text, textRect)
    text = base_font.render("Opening: " + text1[1], True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 110)
    display_screen.blit(text, textRect)
    text = base_font.render("Highest: " + text1[2], True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 140)
    display_screen.blit(text, textRect)
    text = base_font.render("Lowest: " + text1[3], True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 170)
    display_screen.blit(text, textRect)
    text = base_font.render("Closing: " + text1[4], True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 200)
    display_screen.blit(text, textRect)
    text = base_font.render("Volume: " + text1[6], True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 230)
    display_screen.blit(text, textRect)
    pygame.display.update()


def find(date):
    with open("Dogecoin.csv", mode="r") as f:
        for i in csv.reader(f):
            if str(i[0]) == str(date):
                return " ".join(list(i))


def mouse_event(event):
    if event.inaxes is not None:
        start = "9/17/14"
        date_1 = datetime.datetime.strptime(start, "%m/%d/%y")
        end = date_1 + datetime.timedelta(days=math.trunc(event.xdata) - 16330)
        pyg(find(end.date()))


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
