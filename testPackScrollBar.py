from tkinter import *

window=Tk()
btn1 = Button(window, text='1')
btn2 = Button(window, text='2')
btn3 = Button(window, text='3')
btn4 = Button(window, text='4')
btn5 = Button(window, text='5')

btn1.pack(side='left')
btn2.pack(side='top')
btn3.pack(side='left')
btn4.pack(side='bottom')
btn5.pack(side='right')

#window.geometry("640x480")
window.mainloop()
