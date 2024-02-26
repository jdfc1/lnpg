from tkinter import *
from tkinter.ttk import *

""" root = Tk() # cria nosso objeto de aplicação root. Isto representa o primeiro janela top-level que é executado, portanto deve haver apenas uma instância de TK para cada aplicativo.
label = Label(root, text='Hello world') # cria uma novo objeto. como o nome indica, um objeto rótulo é apenas um widget para exibir texto (ou imagens). Olhando mais de perto para esta linha, vemos o seguinte:
label.pack() # neste caso, estamos usando o método pack(), que é o mais simples de gerenciamento de geometria que você pode usar.
root.mainloop() # essa linha final inicia nosso principal loop. este loop é responsável pelo processo de todos os eventos. e será útil para que o programa feche. este é usualmente o ultima linha de algum script, desde algum outro código posterior não rodará até que a janela seja fechada.

 """

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg="light blue")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=730, height=730)
        self.root.minsize(width=400, height=300)

Application()