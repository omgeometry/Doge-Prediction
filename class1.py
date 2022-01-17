from tkinter import *
window=Tk()
# add widgets here

data = ("Yes", "No")

# Date entry for the day of prediction
lbl = Label(window, text="What date do you want to predict for?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=100)

txtfld = Entry(window, text="what date do you want to predict for?", bd=5)
txtfld.place(x=80, y=150)

# option for using twitter data
lbl = Label(window, text="Do you want to use twitter data?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=200)
#This is yes/no option box for twitter data
lb = Listbox(window, height=2, selectmode='single')
for num in data:
  lb.insert(END,num)
lb.place(x=80, y=250)

# option for using data on past trends
lbl = Label(window, text="Do you want to use past trends?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=300)
#this is the yes/no option box for using past trends
lb2 = Listbox(window, height=2, selectmode='single')
for num in data:
  lb2.insert(END,num)
lb2.place(x=80, y=350)

#how much past data to use
lbl = Label(window, text="How much past data do you want to use?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=400)
  # enter how much data you want to use. Days, weeks, months, or years?
txtfld = Entry(window, text="How much past data do you want to use?", bd=5)
txtfld.place(x=80, y=450)

#Option for using data of other crypto-currencies
lbl = Label(window, text="Do you want to use data from other crypto currencies?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=500)
#This is yes/no option box for using data form other crypto currencies
lb3 = Listbox(window, height=2, selectmode='single')
for num in data:
  lb3.insert(END,num)
lb3.place(x=80, y=550)

# button you click to get results
btn=Button(window, text="Get Prediction", fg='blue')
btn.place(x=80, y=600)


window.title('Dogecoin Price Prediction')
window.geometry("500x800+10+20")
window.mainloop()
