from tkinter import*
def clicer():

        lbl.configure(text=txt.get())
def cliced(lbl):

        lbl=Label(win,text='я же просил',font=30, fg='red' , bg='yellow')
        



win=Tk()
win.title("привет мир")
win.geometry("640x480")
lbl=Label(win,text='за россию',font=24, fg='blue' , bg='green')
lbl.grid(column=0, row=1)
btn=Button(win,text='ааааааа',command=clicer)
btn.grid(column=10,row=10)
xxx=Button(win,text='не нажимать',command=cliced)
xxx.grid(column=10,row=30)
txt= Entry(win ,width=10,show='4')
txt.grid(column=10,row=20)
txt.focus()
win.mainloop()