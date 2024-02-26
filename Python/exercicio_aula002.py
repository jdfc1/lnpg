from tkinter import *
from tkinter.ttk import Combobox

def clicked():
    lbl.configure(text="Button was clicked !!")

def myButtonClicked():
    lbl5.configure(text="IFAL - aula de linguagem")


window = Tk()
window.title("Welcome nerds")
window.geometry('350x450')
lbl = Label(window, text="Ola")
lbl.pack()

lbl = Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
btn = Button(window, text="Clique aqui", command=clicked)
btn.pack()

txtfld = Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=90, y=90)

data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=90, y=130)

v0=IntVar()
v0.set(2)
r1=Radiobutton(window, text="Programação", variable=v0, value=1)
r2=Radiobutton(window, text="Infra", variable=v0, value=2)
r1.place(x=90,y=180)
r2.place(x=90, y=220)

v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Futebol", variable = v1)
C2 = Checkbutton(window, text = "Tenis", variable = v2)
C1.place(x=90, y=270)
C2.place(x=90, y=300)


lbl5 = Label(window, text="texto interessante aqui,", fg='red', font=("Helvetica", 16))
lbl5.place(x=90, y=350)

btn5 = Button(window, text="OK")
btn5.pack()
btn5.place(x=100, y=400)
btn5.bind('<Print>', myButtonClicked)

window.mainloop()