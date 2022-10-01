from tkinter import *
from tkinter import messagebox

def clicked():
    login = loginTextField.get()
    password = passwordTextField.get()
    infoStr = f'Ваш логин и пароль следующие: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Информационное сообщение', message=infoStr)

false = False
true = True

global flag

window = Tk()   # Главное окно, которое выводится на экран
window.title('Заголовок приложения') # Заголовок приложения
label1 = Label(window, text="Приветствую!", font=("Times New Roman", 20)) # Метка приложения на экране с заданным текстом, размером и видом шрифта
label1.grid(column=0, row=0) # в сетке расположить на 0.0 координатах (т.е. в верхнем левом углу)

label2 = Label(window, text="Текст, который будет меняться", font=("Arial Bold", 20), bg="blue", fg="red") # вторая метка с заданными параметрами, а также цветом текста и заливкой
label2.grid(column=0, row=1) # Расположение метки в тексте

labelLogin = Label(window, text="Введите логин", font=('Times New Roman', 20))
labelLogin.grid(column=0, row=2)
labelPassword = Label(window, text="Введите пароль", font=('Times New Roman', 20))
labelPassword.grid(column=0, row=3)

loginTextField = Entry(window, bg='white')
loginTextField.grid(column=1, row=2)
passwordTextField = Entry(window, bg='white', show='*')
passwordTextField.grid(column=1, row=3)

btnEnter = Button(window, command=clicked)

window.wm_attributes("-alpha", 0.85) # задание прозрачности приложения
window.geometry('1366x768') # задание размеров окна
window.resizable(width=False, height=False) # запрет на изменение размеров окна
window.mainloop() #запуск приложения
