from tkinter import *


def set_grid_configure(rows, columns, size):
    for i in range(0, rows, 1):
        window.grid_rowconfigure(i, minsize=size)
    for i in range(0, columns, 1):
        window.grid_columnconfigure(i, minsize=size)


def default_font():
    return "Times New Roman", 15


def add_button(number):
    return Button(text=str(number), bd=5, font=default_font(), command=lambda: add_number(number))


def add_change_button(number):
    return Button(text=str(number), bd=5, font=default_font(), command=lambda: add_number(number))


def add_number(text):
    value = textEntry.get()  # Получаем содержимое тектового поля
    if value[0] == str(0):  # Если калькулятор только запущен, в текстовом поле явно 0
        textEntry.delete(0, END)  # очищаем текстовое поле

    textEntry.insert(len(value), text)  # Вставляем наше значение


window = Tk()
window.title = "Кулькулятор, будь он не ладен"

textEntry = Entry(window,  # Куда добавляем наше текстовое поле, т.е. на окно
                  justify=RIGHT,  # Выравнивание справа
                  font=default_font(),  # Задание размера по умолчанию, но можно использовать и свой
                  width=20  # Размер окна
                  )

textEntry.grid(row=0,  # начальная строка в сетке
               column=0,  # колонка начальная в сетке
               columnspan=4,  # кол-во колонок для склеивания
               stick="we",  # stick - растягивание на форме. WE - West East, т.е. по горизонтали
               padx=5
               )
textEntry.insert(0, "0")

add_button(1).grid(row=3, column=0, stick="wens", padx=5, pady=5)
add_button(2).grid(row=3, column=1, stick="wens", padx=5, pady=5)
add_button(3).grid(row=3, column=2, stick="wens", padx=5, pady=5)
add_button(4).grid(row=2, column=0, stick="wens", padx=5, pady=5)
add_button(5).grid(row=2, column=1, stick="wens", padx=5, pady=5)
add_button(6).grid(row=2, column=2, stick="wens", padx=5, pady=5)
add_button(7).grid(row=1, column=0, stick="wens", padx=5, pady=5)
add_button(8).grid(row=1, column=1, stick="wens", padx=5, pady=5)
add_button(9).grid(row=1, column=2, stick="wens", padx=5, pady=5)
add_button(0).grid(row=4, column=1, stick="wens", padx=5, pady=5)

set_grid_configure(4, 4, 60)
add_button('+/-').grid(row=4, column=0, stick="wens", padx=5, pady=5)
add_button('.').grid(row=4, column=2, stick="wens", padx=5, pady=5)

window.mainloop()
