from tkinter import *

win = Tk()
win.title("Идите ЛЕСОМ" )
label = Label(win,text="Ты ХТО ЗАЧМЕ тЫ ТуТ", font=("Times New Roman", 24), bg="yellow", fg="blue")
lbl = Label(win,text="КЫХ от сюда ", font=("Time Hew Roman", 24), bg="yellow", fg="blue")
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt = Entry(win,width=10)
txt.grid(column=2, row=0)
btn = Button(win, text="НЕ СМЕЙ ")
btn.grid(column=1, row=0)
win.geometry('640x480')
win.mainloop 
