#The data set used here is accredited to https://www.askpython.com/python/examples/crypto-price-prediction
#This form of the product is not entirely functional: functional improvements to be added later

#Fix the lack of the pyg window working: critical
#Unable to be fixed currently, time restraints

  from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd
from datetime import timedelta
import csv
import math
import datetime
import pygame


window = Tk()
# add widgets here

ds = [[], []]


def pyg(text1):
  print("hi")
  if text1 is None or len(text1) <= 1:
    return
  text1 = str(text1).split(" ")
  pygame.init()
  pygame.display.set_caption('mpltest')
  display_screen = pygame.display.set_mode((300, 300))
  display_screen.fill((0, 0, 0))
  pygame.display.flip()
  base_font = pygame.font.Font("freesansbold.ttf", 18)
  text = base_font.render("Date: " + datetime.datetime.strptime(text1[0], "%Y-%m-%d").strftime("%B-%d-%Y"), True,
                          (255, 255, 255), (0, 0, 0))
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


fig, ax = plt.subplots(figsize=(12, 8))
fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=25))
ax.xaxis.set_major_formatter(DateFormatter("%m-%d-%Y"))

cid = fig.canvas.mpl_connect('motion_notify_event', mouse_event)


def graph():

  for i in lb2.curselection():
    variableSelect = lb2.get(i)
    print(variableSelect)
  dates = txtfld.get()
  print(dates)

  if variableSelect == "Open":
    selector = 1
  elif variableSelect == "High":
    selector = 2
  elif variableSelect == "Low":
    selector = 3
  elif variableSelect == "Close":
    selector = 4
  elif variableSelect == "Volume":
    selector = 6
  else:
    selector = 2

  times = pd.date_range(start=pd.to_datetime('today'), end=(pd.to_datetime('today') + timedelta(days=int(dates))), freq='D')

  with open("Dogecoin.csv", mode="r") as f:
    count = 0
    for i in csv.reader(f):
      if count != 0 and i[1] != 'null' and count < times.size:
        ds[0].append(times[count])
        ds[1].append(float(i[int(selector)]))
      count += 1
  plt.plot(ds[0], ds[1])

  plt.show()

data = ("Yes", "No")

# Date entry for the day of prediction
lbl = Label(window, text="How many days ahead do you want to predict?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=100)

txtfld = Entry(window, text="0", bd=5)
txtfld.place(x=80, y=150)

# option for using twitter data
#lbl2 = Label(window, text="Do you want to use twitter data?", fg='black', font=("Helvetica", 10))
#lbl2.place(x=60, y=200)
#This is yes/no option box for twitter data
#lb = Listbox(window, height=2, selectmode='single', exportselection=0)
#for num in data:
#  lb.insert(END,num)
#lb.place(x=80, y=250)

# option for using data on past trends
lbl = Label(window, text="What kind of data do you want to judge?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=300)
#this is the yes/no option box for using past trends
lb2 = Listbox(window, height=5, selectmode='single', exportselection=0)
lb2.insert(1, "Open")
lb2.insert(2, "Close")
lb2.insert(3, "High")
lb2.insert(4, "Low")
lb2.insert(5, "Volume")
lb2.place(x=80, y=350)

#how much past data to use
#lbl = Label(window, text="How much past data do you want to use?", fg='black', font=("Helvetica", 10))
#lbl.place(x=60, y=400)
  # enter how much data you want to use. Days, weeks, months, or years?
#txtfld2 = Entry(window, text="How much past data do you want to use?", bd=5)
#txtfld2.place(x=80, y=450)

#Option for using data of other crypto-currencies
#lbl = Label(window, text="Do you want to use data from other crypto currencies?", fg='black', font=("Helvetica", 10))
#lbl.place(x=60, y=500)
#This is yes/no option box for using data form other crypto currencies
#lb3 = Listbox(window, height=2, selectmode='single')
#for num in data:
 # lb3.insert(END,num)
#lb3.place(x=80, y=550)

# button you click to get results
btn=Button(window, text="Get Prediction", command=graph, fg='blue')
btn.place(x=80, y=600)


window.title('Dogecoin Price Prediction')
window.geometry("500x800+10+20")
window.mainloop()


