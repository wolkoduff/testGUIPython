from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton

num = -1

false = False
true = True


def write_history(message, file, encoding):
    file.write(message, encoding=encoding)


def write_history(message, file):
    write_history(message, file, "utf8")


# Обновить путь к питону
# C:\Python№\Lib;C:\Python№\DLLs;C:\Python№\Lib\lib-tk;C:\other-foolder-on-the-path где python№ - репозиторий питона
#

def clicked():
    global num
    if num == -1:
        num += 1
    else:
        num -= 1

    str = txt.get()
    res = "Привет {}".format(str)
    # Очистить текстовое поле
    txt.delete(0, len(str))
    # Вставить в текстовое поле
    txt.insert(0, 15)
    label.configure(text=res)
    #messagebox.showinfo('ОБрати Внимание!!! СДЕЛАНО В ГЕРМАНИИ!!!',
                        #'Ваше значение в комбо-боксе следующее: ' + combo.get())

    # txt.configure(state=listState.get(num))

def joker():
    print(string)
    label.configure(text=selected.get())

def change_state():
    flag = chk_state.get()

window = Tk()
window.title("Добро пожаловать!")
label = Label(window, text="Ахах, ЧЫЖЫК", font=("Times New Roman", 24))
lbl = Label(window, text="Ахах, ЧВК 'ЧИЖИК'", font=("Times New Roman", 24))
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt = Entry(window, width=10, show='*')
txt.grid(column=2, row=0)
txt['state'] = 'readonly'
combo = Combobox(window)
values = (1, 2, 3, 4, 5, 'Толчок')
combo['values'] = values
combo.current(5)
combo.grid(column=3, row=5)
combo['state'] = 'readonly'
string = StringVar()
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
chk_state = BooleanVar()
chkbox = Checkbutton(window, text="Подписаться", command=change_state)
chkbox.grid(column=20, row=10)
chkbox.focus()
selected = IntVar()
rad1 = Radiobutton(window, text="Первый нах", value=1, variable=selected, command=joker)
rad2 = Radiobutton(window, text="Второй нах", value=2, variable=selected, command=joker)
rad3 = Radiobutton(window, text="Расчёт окончен", value=3, variable=selected, command=joker)
rad1.grid(column=3, row=1)
rad2.grid(column=4, row=1)
rad3.grid(column=5, row=1)
window.geometry('1366x768')
window.resizable(width=false, height=false)
window.mainloop()
