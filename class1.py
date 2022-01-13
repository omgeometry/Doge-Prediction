from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
# add widgets here
btn=Button(window, text="Get Prediction", fg='blue')
btn.place(x=80, y=400)

lbl=Label(window, text="What date do you want to predict for?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=100)
txtfld=Entry(window, text="what date do you want to predict for?", bd=5)
txtfld.place(x=80, y=150)
var = StringVar()
var.set("one")
data=("Yes", "No")

lbl=Label(window, text="Doge Prediction", fg='blue', font=("Helvetica", 16))
lbl.place(x=60, y=50)

lbl=Label(window, text="Do you want to use twitter data?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=200)
lb=Listbox(window, height=2, selectmode='single')
def yesno(x, y):    
    for num in data:
        lb.insert(END,num)
    lb.place(x=x, y=y)
yesno(50, 250)

lbl=Label(window, text="Do you want to use past trends?", fg='black', font=("Helvetica", 10))
lbl.place(x=60, y=300)

lb=Listbox(window, height=2, selectmode='single')
yesno(60, 350)

window.title('Doge Prediction')
window.geometry("300x800+10+20")
window.mainloop()
