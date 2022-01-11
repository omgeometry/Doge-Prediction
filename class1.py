from tkinter import *
from tkinter.ttk import Combobox
window=Tk()
# add widgets here
btn=Button(window, text="this is Button widget", fg='blue')
btn.place(x=80, y=100)
txtfld=Entry(window, text="this is entry widge", bd=5)
txtfld.place(x=80, y=150)
var = StringVar()
var.set("one")
data=("one", "two", "three")
cb=Combobox(window, values=data)
cb.place(x=60, y=150)

window.title('hello python')
window.geometry("300x200+10+20")
window.mainloop()
