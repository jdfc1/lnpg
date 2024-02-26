## O tkinter é um módulo padrão do Python que fornece ferramentas para criar interfaces gráficas de usuário (GUI). Aqui estão algumas das principais funções e classes do tkinter:

1. Tk() e Toplevel(): São classes que representam as janelas principais e as janelas secundárias, respectivamente.

import tkinter as tk

root = tk.Tk()  # Janela principal
top = tk.Toplevel()  # Janela secundária

2. Widgets Básicos:

Label: Rótulo para exibir texto.
Button: Botão clicável.
Entry: Caixa de entrada para entrada de texto.
Text: Widget para exibição e edição de texto multilinha.
Checkbutton: Caixa de seleção.
Radiobutton: Botão de opção.
Exemplo de criação de widgets:

label = tk.Label(root, text="Hello, Tkinter!")
button = tk.Button(root, text="Click me!", command=callback_function)
entry = tk.Entry(root, width=20)

3. Gerenciadores de Layout:

pack(): Coloca o widget na janela conforme necessário.
grid(): Organiza os widgets em uma grade.
place(): Coloca o widget em uma posição específica.
Exemplo de uso do pack():

label.pack()
button.pack(side=tk.LEFT)

4. Eventos:

bind(): Associa uma função a um evento.

button.bind("<Button-1>", callback_function)

5. Diálogos:

tkinter.messagebox: Módulo para caixas de diálogo simples.
tkinter.simpledialog: Módulo para diálogos interativos.

import tkinter.messagebox as mb
result = mb.askquestion("Title", "Question?")

6. Variáveis:

StringVar, IntVar, DoubleVar, BooleanVar: Variáveis especiais vinculadas a widgets que são atualizadas automaticamente quando a variável é modificada.

var = tk.StringVar()
entry = tk.Entry(root, textvariable=var)

Estas são apenas algumas das funções e classes básicas. O tkinter é uma biblioteca rica com muitos outros recursos e widgets. À medida que você desenvolve aplicações mais complexas, pode explorar outras funcionalidades, como menus, barras de rolagem, canvas, entre outros.
