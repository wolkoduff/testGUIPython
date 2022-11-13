
from tkinter import*
from tkinter.ttk import Combobox


win=Tk()
var=''

def у():
        global var
        var=(var+'/')
        txt.insert(0,var)
        var=''

def д():
        global var
        var=(var+'*')
        txt.insert(0,var)
        var=''

def с():
        global var
        var=(var+'с')
        txt.insert(0,var)
        var=''

def в():
        global var
        var=(var+'-')
        txt.insert(0,var)
        var=''

def q():
        global var
        var=(var+1)
        txt.insert(0,var)

def q():
        global var
        var=(var+1)
        txt.insert(0,var)

def w():
    global var
    var=(var+2)
    txt.insert(0,var)
    
def e():
    txt.insert(0,)

def r():
    global var
    var=(var+3)
    txt.insert(0,var)

def t():
    global var
    var=(var+4)
    txt.insert(0,var)

def y():
    var=(var+5)
    txt.insert(0,var)

def u():
    var=(var+6)
    txt.insert(0,var)

def i():
    var=(var+7)
    txt.insert(0,var)

def o():
    var=(var+8)
    txt.insert(0,var)

def p():
    var=(var+9)
    txt.insert(0,var)

def a():
    var=(var+0)
    txt.insert(0,0)

lbl=Label(win,text='за россию',font=24, fg='blue' , bg='green')
lbl.grid(column=34, row=1)
win.title("привет мир")
txt= Entry(win ,width=10,)
txt.grid(column=10,row=10)
txt['state']='readonly'
win.geometry("640x480")
q=Button(win,text='1',command=q)
q.grid(column=100,row=10)
w=Button(win,text='2',command=w)
w.grid(column=90,row=10)
e=Button(win,text='3',command=e)
e.grid(column=80,row=10)
r=Button(win,text='4',command=r)
r.grid(column=70,row=10)
t=Button(win,text='5',command=t)
t.grid(column=60,row=10)
y=Button(win,text='6',command=y)
y.grid(column=50,row=10)
u=Button(win,text='7',command=u)
u.grid(column=40,row=10)
i=Button(win,text='8',command=i)
i.grid(column=30,row=10)
o=Button(win,text='9',command=o)
o.grid(column=20,row=10)
p=Button(win,text='0',command=p)
p.grid(column=10,row=10)
a=Button(win,text='?',command=a)
a.grid(column=110,row=10)
у=Button(win,text='?',command=у)
у.grid(column=120,row=10)
д=Button(win,text='?',command=д)
д.grid(column=130,row=10)
в=Button(win,text='?',command=в)
в.grid(column=140,row=10)
с=Button(win,text='?',command=с)
с.grid(column=150,row=10)
win.mainloop()