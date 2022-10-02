from tkinter import * 

num = -1

def clicked():
    global num
    if (num == -1):
        num += 1
    else:
        num-=1

    res = "Привет{}".format(txt.get())
    res = res + str(num)
    label.configure(texn=res)
    txt.configure(state=listState.get(num))
    
window = Tk ()
listState = {-1 : 'disabled', 0 : 'readonly'}
window.title ("Добро пожаловать!")
label = Label(window, text="Ахах,ЧЫЖЫК", font=("Times New Roman", 24), bg="yellow", fg="blue")
lbl = Label(window, text="Ахах, ЧВК ЧИЖИК", font=("Times New Roman", 24), bg="yellow", fg="blue")
label.grid(column=0, row=0)
lbl.grid(column=0, row=1)
txt = Entry(window, width=10)
txt.grid(column=2, row=0)
btn=Button(window, text="Не нажинать!", command=clicked)
btn.grid(column=1,row=0)
window.geometry('640x480')
window.mainloop() 
