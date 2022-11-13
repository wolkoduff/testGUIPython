from tkinter import *
from tkinter import messagebox

# Кравченко Тимофей

num = 1

def clicked():
    global num
    txt.get()
    # txt.configure(state = list.get(num))

wind = Tk()
wind.title("Конкулятор")

# list = {1 : 'disabled'}

txt = Entry(wind, width=15, font=("Algerian", 10), bg="white", fg="black")
txt.grid(column=1, row=0)

btn = Button(wind, text="0", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=3, row=0)

btn = Button(wind, text="1", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=4, row=0)

btn = Button(wind, text="2", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=5, row=0)

btn = Button(wind, text="3", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=3, row=1)

btn = Button(wind, text="4", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=4, row=1)

btn = Button(wind, text="5", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=5, row=1)

btn = Button(wind, text="6", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=3, row=2)

btn = Button(wind, text="7", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=4, row=2)

btn = Button(wind, text="8", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=5, row=2)

btn = Button(wind, text="9", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btn.grid(column=3, row=3)

bt = Button(wind, text="*", font=("Algerian", 10), bg="white", fg="black", command=clicked)
bt.grid(column=6, row=0)

bt = Button(wind, text="/", font=("Algerian", 10), bg="white", fg="black", command=clicked)
bt.grid(column=6, row=1)

bt = Button(wind, text="+", font=("Algerian", 10), bg="white", fg="black", command=clicked)
bt.grid(column=6, row=2)

bt = Button(wind, text=" - ", font=("Algerian", 10), bg="white", fg="black", command=clicked)
bt.grid(column=4, row=3)

btm = Button(wind, text="=", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btm.grid(column=5, row=3)

btr = Button(wind, text="C", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btr.grid(column=6, row=3)

btl = Button(wind, text="<=", font=("Algerian", 10), bg="white", fg="black", command=clicked)
btl.grid(column=7, row=0)


# wind.geometry('400x200')

wind.resizable(width = False, height = False)

wind.mainloop()