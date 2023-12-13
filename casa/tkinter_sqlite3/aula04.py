from tkinter import *
from tkinter.ttk import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(bg="green")
        self.root.geometry("700x610")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=800)
        self.root.minsize(width=500, height=400)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.02, rely=0.53, relwidth=0.96, relheight=0.45)
    
    def widgets_frame_1(self):
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
    
        # label código
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.15)
        #Entry
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)


        # label nome
        self.lb_nome = Label(self.frame_1, text="Nome")
        self.lb_nome.place(relx=0.05, rely=0.25, relwidth=0.1, relheight=0.15)
        #Entry
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.35, relwidth=0.4)


        # label cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade")
        self.lb_cidade.place(relx=0.05, rely=0.45, relwidth=0.1, relheight=0.15)
        #Entry
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.05, rely=0.55, relwidth=0.4)


        # label Telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone")
        self.lb_telefone.place(relx=0.05, rely=0.65, relwidth=0.1, relheight=0.15)
        #Entry
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.75, relwidth=0.4)

Application()