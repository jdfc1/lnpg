from tkinter import *
from tkinter import ttk

def mostrarResposta():
   resposta = combo.get()
   print(resposta)

top = Tk()
top.geometry("200x200")

frame = Frame(top)
frame.pack()

langs = ["C", "C++", "Java",
   "Python", "PHP"]
   
combo = ttk.Combobox(frame, values = langs)
combo.set("Pick an Option")
combo.pack(padx = 5, pady = 5)

top.mainloop()
