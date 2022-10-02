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
    label.configure(text=res)
    
    txt.configure(state=listState.get(num))
    
    messagebox.showinfo('Держи результат', 'Я же просил не нажимать!!!')
    messagebox.showwarning('ТЫ уверен?', 'Ты точно не будешь больше писать?')
    try:
        flag = messagebox.askyesno('Точно?', 'Ты ведь не будешь больше нажимать, правда?')
        if (flag):
            messagebox.showinfo('НЯЯЯЯЯЯ', 'Я проверю и слежу за тобой')
        else:
            messagebox.showerror('Редиска', 'Я доверяла тебе! Ты был(-а) мне как брат(сестра), питушара!')
    except Exception as ex:
        messagebox.showerror('Ошибка', str(ex))

isStart = messagebox.askyesno('Ты уверен?', 'Ты хочешь запустить программу?')
if (isStart):
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
    window.geometry('1366x768')
    window.wm_attributes("-alpha", 0.85)
    window.resizable(width=False, height=False)
    window.mainloop()
else:
    exit
