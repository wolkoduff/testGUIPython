from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

num = -1

false = False
true = True

def clicked():
    global num
    if (num == -1):
        num += 1
    else:
        num -= 1

    str = txt.get()
    res = "Привет {}".format(str)
    txt.delete(0, len(str))
    label.configure(text=res)
    messagebox.showinfo('ОБрати Внимание!!! СДЕЛАНО В ГЕРМАНИИ!!!', 'Ваше значение в комбо-боксе следующее: ' + combo.get())
    
    #txt.configure(state=listState.get(num))
    
window = Tk()
# listState = {-1 : 'disabled', 0 : 'normal'}
window.title("Добро пожаловать!")
label = Label(window, text="Ахах, ЧЫЖЫК", font=("Times New Roman", 24))
lbl = Label(window, text="Ахах, ЧВК 'ЧИЖИК'", font=("Times New Roman", 24))
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt = Entry(window, width=10, show='*')
txt.grid(column=2, row=0)
combo = Combobox(window)
values = (1, 2, 3, 4, 5, 'Толчок')
combo['values'] = values
combo.current(5)
combo.grid(column=3,row=5)
combo['state'] = 'readonly'
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
btn.focus()
window.geometry('1366x768')
# window.wm_attributes("-alpha", 0.85)
window.resizable(width=false, height=false)
window.mainloop()
