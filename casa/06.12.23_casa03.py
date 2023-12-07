import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Digite seu nome")
entry = tk.Entry(root, width=20)
button = tk.Button(root, text="Click me!")


label.pack()
entry.pack()
button.pack(side=tk.LEFT)


root.mainloop()