from tkinter import *
from tkinter.ttk import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg="green")
        self.root.geometry("700x610")
        self.root.resizable(True, True)
        self.root.maxsize(width=730, height=730)
        self.root.minsize(width=400, height=300)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.02, rely=0.53, relwidth=0.96, relheight=0.45)
    
    def criando_botoes(self):
        # limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # buscar
        self.bt_limpar = Button(self.frame_1, text="Buscar")
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Novo
        self.bt_limpar = Button(self.frame_1, text="Novo")
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Alterar
        self.bt_limpar = Button(self.frame_1, text="Alterar")
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar")
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

Application()