from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
'''
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter.ttk import Progressbar
'''

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


# Пройти Текстовая область со скроллингом
# Счётчик итератор
# progress bar

def clicked():
    global num
    if num == -1:
        num += 1
    else:
        num -= 1

    stringer = txt.get()
    res = "Привет {}".format(stringer)
    # Очистить текстовое поле
    txt.delete(0, len(stringer))
    # Вставить в текстовое поле
    txt.insert(0, '15')
    label.configure(text=res)
    messagebox.showinfo('ОБрати Внимание!!! СДЕЛАНО В ГЕРМАНИИ!!!',
    'Ваше значение в комбо-боксе следующее: ' + combo.get())

    # txt.configure(state=listState.get(num))


def joker():
    num = selected.get()
    if num == 1:
        messagebox.showinfo("Прювет")
    elif num == 2:
        messagebox.showwarning("осторожно")
    else:
        messagebox.showerror("Бомбочка!")
    
    label.configure(text=selected.get())


def change_state():
    flag = chk_state.get()
    print(flag)


def change_value(value):
    bar['value'] = int(value)


def change_value():
    bar['value'] = int(spin1.get())


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
pixelVirtual = PhotoImage(width=10, height=10)
btn = Button(window, image=pixelVirtual, text="Не нажимать!", command=clicked, compound="c")
btn.grid(column=1, row=0)
chk_state = BooleanVar()
chkbox = Checkbutton(window, text="Подписаться", variable=chk_state, command=change_state)
chkbox.grid(column=20, row=10)
chkbox.focus()
selected = IntVar()
rad1 = Radiobutton(window, text="Первый нах", value=1, variable=selected, command=joker)
rad2 = Radiobutton(window, text="Второй нах", value=2, variable=selected, command=joker)
rad3 = Radiobutton(window, text="Расчёт окончен", value=3, variable=selected, command=joker)
rad1.grid(column=3, row=1)
rad2.grid(column=4, row=1)
rad3.grid(column=5, row=1)

# Текстовое поле с бегунком
scrolledTxt = ScrolledText(window, width=40, height=10)
scrolledTxt.insert(INSERT, "Какой-то рандомный текст рандомного челика")
scrolledTxt.grid(column=1, row=20)

progress = IntVar()
# С лямбдой меняем прогресс бар
# spin1 = Spinbox(window, from_=0, to=100, width=5, command= lambda : change_value(spin1.get()))     # счётчик пошаговый от 10 до 1000
# Без лямбды напрямую
spin1 = Spinbox(window, from_=0, to=100, width=5, command=change_value)     # счётчик пошаговый от 10 до 1000
spin2 = Spinbox(window, values=(3, 5, 7, 11), width=5)  # использовать готовый массив данных
spin1.grid(column=0, row=10)
spin2.grid(column=0, row=11)

bar = Progressbar(window, length=100, value=10)
bar.grid(column=0, row=12)

window.geometry('1366x768')
window.resizable(width=false, height=false)
window.mainloop()
