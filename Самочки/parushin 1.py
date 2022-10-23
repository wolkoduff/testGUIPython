from tkinter import *

global num
num = 0

def clicked():
    global num
    if (num == 0):
        num += 0
    else:
        num += 1
    res = "Hi {}".format(txt.get())
    res = res + str(num)
    lbl.configure(text=res)
    txt.configure(state=list.get(num))

window = Tk()
list = {1 : 'disabled', 0 : 'normal'}
window.title("папка!?")
label = Label(window, text="Hello", font=("Algerian", 24), bg="red", fg="blue")
lbl = Label(window, text="YOu are", font=("Algerian", 24), bg="yellow", fg="black")
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
btn = Button(window, text="point", font=("Algerian", 12), bg="orange", fg="white",command=clicked)
btn.grid(column=1, row=0)
txt = Entry(window, width=15, font=("Algerian", 12), bg="red", fg="white", state = list.get(num))
txt.grid(column=2, row=0)
window.geometry('400x200')
window.mainloop()