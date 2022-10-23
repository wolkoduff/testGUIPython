from tkinter import * 
from tkinter import messagebox


num = -1

def clicked():
    global num
    if (num == -1):
        num += 1
    else:
        num-=1

    res = "Привет{}".format(txt.get())
    res = res + str(num)

    try:
        error =res + str(num)
    except Exception as ex:
        res = str(ex)
        print("LOOOOOOOOOL: ", ex)

    label.configure(text=res)

    txt.configure(state=listState.get(num))

    messagebox.showinfo('Держи результат','Ммм...?')
    messagebox.showwarning('ИИ', 'Хей ')
    flag = messagebox.askyesno('ИИ', 'Что ты делаеш? Ммм... Зачем ?')

    try:
        if (flag):
            messagebox.showinfo('ИИ', 'Я надеюсь')
        else:
            messagebox.showerror('ИИ', 'Штош дело твой ')
    except:
        messagebox.showerror(str(ex))

window = Tk()
listState = {-1 : 'disabled', 0 : 'readonly'}
window.title ("Добро пожаловать!")
label = Label(window, text="Ахах,ЧЫЖЫК", font=("Times New Roman", 24), bg="yellow", fg="blue")
lbl = Label(window, text="Ахах, ЧВК ЧИЖИК", font=("Times New Roman", 24), bg="yellow", fg="blue")
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt = Entry(window, width=10, state=listState.get(num))
txt.grid(column=2, row=0)
btn=Button(window, text="Не нажинать!", command=clicked)
btn.grid(column=1,row=0)
window.geometry('640x480')
window.mainloop() 
