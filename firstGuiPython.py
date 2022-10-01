from tkinter import *
from tkinter import ttk

def startWindow(window):
    window.mainloop()

def clicked():
    res = txt.get()
    lbl1.configure(text="Да бл Ять!!!!")
    lbl.configure(text=res)

window = Tk()               # Инициализация нашей библиотеки tkinter
window.title("Окно!")       # Задание заголовка окна
window.geometry('640x480')  # Задание размера окна
lbl = Label(window, text="Дарова!")     # Создание метки с текстом
                                        # Если хотим задать шрифт с размером текста, тогда нужно дописать font=("Шрифт",размер)
                                        # Параметр font может быть передан любому виджету, чтобы поменять его шрифт
                                        # Виджеты - всё, что отображается в окне (пока что label)
lbl1 = Label(window, text="Дарова!", font=("Times New Roman", 20))
lbl.grid(column=0, row=0)   # Задание места расположения мекткив  сетке. ОБЯЗАТЕЛЬНО ДЛЯ ОТОБРАЖЕНИЯ НА ФОРМЕ!!!
lbl1.grid(column=1, row=0)
# Добавим виджет кнопка (Button)
button = Button(window, text="Жмякни меня!", bg="black", fg="green", command=clicked)
# bg - меняет цвет фона, fg - цвет текста
button.grid(column=0, row=1)

txt = Entry(window, width=10)
txt.grid(column=0, row=5)

combo = ttk.Combobox(window) #ttk.Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст!")
combo.current(5)
combo.grid(column=5, row=5)
bar = ttk.Progressbar(window, length=100)
bar['value'] = 70
bar.grid(column=3, row=3)
startWindow(window)         # Передача в метод вызова нашего окна, сделано для удобства
