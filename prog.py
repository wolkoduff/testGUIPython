from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton

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
    txt.delete(0, len(str))
    label.configure(text=res)
    messagebox.showinfo('ОБрати Внимание!!! СДЕЛАНО В ГЕРМАНИИ!!!',
                        'Ваше значение в комбо-боксе следующее: ' + combo.get())

    # txt.configure(state=listState.get(num))


def change_state():
    flag = chk_state.get()


print(mbg := "bomb")
print(mbg)

# Подготовить к следующему уроку:
# Вспомнить как работать с файлом
# Подготовить игрушку к Hell-уину
# Радио-кнопка и большое текстовое поле с бегунком

# Цель курса: познакомиться с графикой в питоне
# Telgram-bot как мастер-класс
# Создать собственное приложение в конце курса
# Подготовить шпоры для себя или свой справочник для работы с питоном
# GIT (_!_)

window = Tk()
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
combo.grid(column=3, row=5)
combo['state'] = 'readonly'
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
chk_state = BooleanVar()
chkbox = Checkbutton(window, text="Подписаться", var=chk_state, command=change_state)
chkbox.grid(column=20, row=10)
chkbox.focus()
window.geometry('1366x768')
window.resizable(width=false, height=false)
window.mainloop()
