from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from PIL import Image, ImageTk

'''
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter.ttk import Progressbar
'''

num = -1

false = False
true = True


def test_bind_key(event):
    print(event.char)


def test_bind_button(event):
    print(event)


def write_history(message, file, encoding):
    file.write(message, encoding=encoding)


def write_history(message, file):
    write_history(message, file, "utf8")



# Обновить путь к питону
# C:\Python№\Lib;C:\Python№\DLLs;C:\Python№\Lib\lib-tk;C:\other-foolder-on-the-path где python№ - репозиторий питона
#


# Перешли на создание телеграм-бота
# TODO: Придумать какой-нибудь интерфейс для рабочего приложения

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
    number = selected.get()
    if number == 1:
        messagebox.showinfo("Прювет")
    elif number == 2:
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


def press_button(event):
    print(event)


def press_key(event):
    messagebox.showerror("ERROR", "Невозможно использование данной комбинации клавиш")
    print(event)

def hover_button(event):
    messagebox.showwarning("Внимание", "Пожалуйста, не нажимай! Я тебя сльозно прошу")

def leave_button(event):
    messagebox.showinfo("Ряхмят!", "Спасибо!")

def select_file():
    path = filedialog.askopenfilename(title="Выберите изображение для добавления",
                                      filetypes=(('image files', "*.jpg"), ('all files', '*.*')))
    img = Image.open(path)
    img = ImageTk.PhotoImage(img, size=(20, 20))
    label_image = Label(window, image=img)
    label_image.image = img
    label_image.grid(column=20, row=15)

window = Tk()
window.title("Добро пожаловать!")
label = Label(window, text="Ахах, ЧЫЖЫК", font=("Times New Roman", 24))
lbl = Label(window, text="Ахах, ЧВК 'ЧИЖИК'", font=("Times New Roman", 24))
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
# Однострочное текстовое поле
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
btn = Button(window, text="Не нажимать!", command=clicked, compound="c")
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

# Многострочное текстовое поле
scrolledTxt = ScrolledText(window, width=40, height=10)
scrolledTxt.insert(INSERT, "Какой-то рандомный текст рандомного челика")
scrolledTxt.grid(column=1, row=20)

progress = IntVar()
# С лямбдой меняем прогресс бар
spin1 = Spinbox(window, from_=0, to=100, width=5,
                command=lambda: change_value(spin1.get()))  # счётчик пошаговый от 10 до 1000
# Без лямбды напрямую
# spin1 = Spinbox(window, from_=10, to=100, width=5, command=change_value)  # счётчик пошаговый от 10 до 1000
spin2 = Spinbox(window, values=('3', '5', '7', '11'), width=5)  # использовать готовый массив данных
# spin1.grid(column=0, row=10)
spin2.grid(column=0, row=12)

bar = Progressbar(window, length=100, value=0)
# bar.grid(column=0, row=19)

button_ttk = tkinter.ttk.Checkbutton(window, text="ttk.Button", command=select_file, compound="c")
button_ttk.grid(column=0, row=15)

# Немного про метод bind()
# Для обработки нажатия на кнопки нужно создать метод, который будет вызываться как с кнопками
window.bind("<Key>", test_bind_key)  # срабатывает при нажатии на клавишу на клавиатуре
window.bind("<Button-1>", test_bind_button)  # ЛКМ
window.bind("<Button-2>", test_bind_button)  # СКМ
window.bind("<Button-3>", test_bind_button)  # ПКМ

#window.geometry('1366x768')
window.resizable(width=false, height=false)

window.bind('<Double-1>', press_button)
window.bind('<2>', press_button)
window.bind('<3>', press_button)

#btn.bind('<Enter>', hover_button)

text = Text(window, height=3,width=60)
text.grid(column=9, row=2)

scrollbar = Scrollbar(window)
scrollbar['command'] = text.yview
text['yscrollcommand']=scrollbar.set

scrollbar.grid(row=1, column=7)

scrolledTxt.bind('<Control-KeyPress-c>', press_key)
window.geometry('1366x768')
# window.resizable(width=false, height=false)
window.mainloop()
