from tkinter import *
from tkinter import messagebox

num = -1

false = False
true = True

def clicked():
    global num
    if (num == -1):
        num += 1
    else:
        num -= 1

    res = "Привет {}".format(txt.get())
    res = res + str(num)
    label.configure(text=res)
    
    txt.configure(state=listState.get(num))
    
    messagebox.showinfo('Держи результат', 'Я же просил не нажимать!!!')


window = Tk()
listState = {-1 : 'disabled', 0 : 'normal'}
window.title("Добро пожаловать!")
label = Label(window, text="Ахах, ЧЫЖЫК", font=("Times New Roman", 24), bg="yellow", fg="blue")
lbl = Label(window, text="Ахах, ЧВК 'ЧИЖИК'", font=("Times New Roman", 24), bg="yellow", fg="blue")
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt = Entry(window, width=10, state=listState.get(num), show='*')
txt.grid(column=2, row=0)
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
window.geometry('640x480')
window.mainloop()
