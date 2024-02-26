from tkinter import *
from tkinter import ttk, messagebox
import sqlite3, random

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from fontTools.ttLib import TTFont # pip3 install fonttools
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
#from PIL import ImageTK, Image
#import base64

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    
    def geraRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        self.telefoneRel = self.telefone_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica", 17)
        self.c.drawString(50, 700, f'Código: {self.codigoRel}')
        self.c.drawString(50, 670, f'Nome: {self.nomeRel}')
        self.c.drawString(50, 640, f'Cidade: {self.cidadeRel}')
        self.c.drawString(50, 610, f'Telefone: {self.telefoneRel}')

        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printCliente()


class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
    
    def conecta_db(self):
        self.conn = sqlite3.connect("empresa.db")
        self.cursor = self.conn.cursor(); print("conectando ao banco de dados")
    
    def desconectar_db(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def montarTabelas(self):
        self.conecta_db()
        #  criar tabela
        self.cursor.execute("""
            create table if not exists clientes (
                cod integer primary key AUTOINCREMENT,
                nome_cliente CHAR(40) NOT NULL,
                cidade CHAR(40) NOT NULL,
                telefone integer(20) NOT NULL
            );
        """)
        self.conn.commit(); print("banco de dados criado")
        self.desconectar_db()
    
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.cidade = self.cidade_entry.get()
        self.telefone = self.telefone_entry.get()
    
    def add_cliente(self):
        self.variaveis() # chamando todas as variáveis da função.
        
        if self.nome == "" or self.cidade == "" or self.telefone == "":
            messagebox.showinfo(title='Atenção', message='Preencha os 3 campos: Nome, Cidade e Telefone')
        else:
            self.conecta_db()
            self.cursor.execute(""" INSERT INTO clientes (nome_cliente, cidade, telefone) 
                VALUES (?, ?, ?) """, (self.nome, self.cidade, self.telefone))

            self.conn.commit()
            self.desconectar_db()
            self.select_lista()
            self.limpa_tela()
            self.contador_cliente()
            messagebox.showinfo(title='Atenção', message='Cadastrado com Sucesso')
    
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""
         SELECT cod, nome_cliente, cidade, telefone FROM clientes ORDER BY nome_cliente ASC; 
        """)

        for i in lista:
            self.listaCli.insert("", END, values=i)
        
        self.desconectar_db()
    
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert (END, col1)
            self.nome_entry.insert(END, col2)
            self.cidade_entry.insert(END, col3)
            self.telefone_entry.insert(END, col4)
    
    def deleta_cliente(self):
        self.variaveis()            
        resposta = messagebox.askyesno(title='Informativo', message='Você tem certeza disso?')
        if resposta == True:
            self.conecta_db()
            self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? ;""", (self.codigo,))
            self.conn.commit()
            self.desconectar_db()
            self.limpa_tela()
            self.select_lista()
            messagebox.showinfo(title='Confirmação', message='Realmente, não era para estar aqui.')
        else: 
            messagebox.showinfo(title='Confirmação', message='Ufa, menos mal. Eu também não queria fazer isso!')
    
    def alterar_cliente(self):
        self.variaveis()
        if self.nome == "" or self.cidade == "" or self.telefone == "":
            messagebox.showinfo(title='Atenção', message='Preencha os 3 campos: Nome, Cidade e Telefone')
        else: 
            self.conecta_db()

            self.cursor.execute("""
            UPDATE clientes SET nome_cliente = ?, cidade = ?, telefone = ? WHERE cod = ? ;
            """, (self.nome, self.cidade, self.telefone, self.codigo))

            self.conn.commit()
            self.desconectar_db()
            self.limpa_tela()
            self.select_lista()
            messagebox.showinfo(title='Atenção', message='Alteração foi concluída')
    
    def buscar_cliente(self):
        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children()) # limpar a lista
        
        self.nome_entry.insert(END, '%') # inserir o sinal de percentagem ao final da string
        nome = self.nome_entry.get() # recebendo o valor do já com o % no final
        # print(nome)
        self.cursor.execute(
            """
            SELECT cod, nome_cliente, cidade, telefone FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC
            """ % nome) # referênciando a variável dentro do select
        buscanomeCli = self.cursor.fetchall() # recuperando os dados
        for i in buscanomeCli: 
            self.listaCli.insert("", END, values=i) # inserir a pesquisa dentro da lista
        self.limpa_tela() # limpar tela
        self.desconectar_db() # desconectar o banco
    
    def randon_cliente(self):
        self.conecta_db()
        #self.listaCli.delete(*self.listaCli.get_children()) # apagar a lista

        self.cursor.execute(
            """ SELECT nome_cliente FROM clientes """ )
        todos_nomes = self.cursor.fetchall()

        result = random.choice(todos_nomes)
        #print(result)
        messagebox.showinfo(title='O nome sorteado foi? ', message=result)

        self.desconectar_db()
    
    def contador_cliente(self):
        self.conecta_db()
        self.cursor.execute(
            """ SELECT COUNT(nome_cliente) FROM clientes """
        )
        qtd_banco = self.cursor.fetchall()

        if qtd_banco:
            tupla = qtd_banco[0]
            if tupla:
                numero = tupla[0]

        self.qtd.config(text=f'Número de \nclientes: {numero}')

        self.desconectar_db()


class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        self.montarTabelas()
        self.select_lista()
        self.Menus()
        self.contador_cliente()

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
        self.bt_limpar = Button(self.frame_1, text="Limpar", command=self.limpa_tela) # font=('verdana', 8, 'bold')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", command=self.buscar_cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # Novo
        self.bt_novo = Button(self.frame_1, text="Novo", command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Alterar
        self.bt_limpar = Button(self.frame_1, text="Alterar", command=self.alterar_cliente)
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # randon
        self.bt_randon = Button(self.frame_1, text="Randon", command=self.randon_cliente)
        self.bt_randon.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.15)

        # Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
    
    
        # label código
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.15)
        #Entry
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)



        self.qtd = Label(self.frame_1, text="", font=("Arial 15"))
        self.qtd.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.15)


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
    
    def lista_frame_2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Cidade")
        self.listaCli.heading("#4", text="Telefone")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
 
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroollista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
    
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label = "Opções", menu= filemenu)
        menubar.add_cascade(label = "Sobre", menu= filemenu2)

        filemenu.add_command(label = "Sair", command = Quit)
        filemenu2.add_command(label= "Limpa Cliente", command = self.limpa_tela)

        filemenu2.add_command(label= "Ficha do Cliente", command = self.geraRelatCliente)

Application()