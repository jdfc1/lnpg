from tkinter import *

def add():
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1+num2
    t3.insert(END, str(result))


def sub(event):
    t3.delete(0, 'end')
    num1 = int(t1.get())
    num2 = int(t2.get())
    result = num1-num2
    t3.insert(END, str(result))


win = Tk()
win.title('Minha primeira calculadora')
win.geometry("400x300+10+10")

lbl1 = Label(win, text='Primeiro número: ')
lbl2 = Label(win, text='Segundo número: ')
lbl3 = Label(win, text='Resultado: ')

t1 = Entry()
t2 = Entry()
t3 = Entry()

b1 = Button(win, text='Adiciona', command=add)
b2 = Button(win, text='Subtrai')

lbl1.place(x=100, y=50)
lbl2.place(x=100, y=100)
lbl3.place(x=100, y=200)
t1.place(x=200, y=50)
t2.place(x=200, y=100)
b1.place(x=100, y=150)
b2.place(x=200, y=150)
t3.place(x=200, y=200)

b2.bind('<Button-1>', sub)

win.mainloop()