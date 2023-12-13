from tkinter import *
from tkinter import ttk

def clicked():
    nome_album = t1.get()
    ano_lancamento = int(t2.get())
    nome_banda = t3.get()
    lancamento = v0.get()
    if lancamento == 1:
        lanca = "é lançamento"
    elif lancamento == 2:
        lanca = "não é lançamento"

    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)

    v0.set(2)

    with open('/home/jdfc1/Documentos/lnpg/versao01_tk/banco1.txt', 'a', encoding='utf-8') as file:
        file.write(f'{nome_banda};{nome_album};{ano_lancamento};{lanca}\n')
        
        file.close()
    
    mostrandoNaTela("Dados Salvos")

def reader():
    with open('/home/jdfc1/Documentos/lnpg/versao01_tk/banco1.txt', 'r', encoding='utf-8') as nome:
        show = nome.readlines()

        dados = []

        for linha in show:
            banda, album, ano, lancamento = linha.strip().split(';')
            lancamento = lancamento.replace('\n', '')
            dados.append(f'{banda} - {album} - {ano} - {lancamento}')

        mostrandoNaTela(dados)

def buscador():

    busca = dadosentra.get().lower()
    dadosentra.delete(0, END)
    #print(busca)

    try: 
        with open('/home/jdfc1/Documentos/lnpg/versao01_tk/banco1.txt', 'r', encoding='utf-8') as file:
            show = file.readlines()

            dados_lista = []

            for espaco in show:
                banda, album, ano, lancamento = espaco.strip().split(';')
                lancamento = lancamento.replace('\n', '')
                dados_lista.append(f'{banda} - {album} - {ano} - {lancamento}')

                encontrei = []

                for imprimir in dados_lista:
                    if busca in imprimir.lower():
                        encontrei.append(f'{imprimir}\n')
                
            
            mostrandoNaTela(encontrei)
            file.close()

    except FileNotFoundError:
        mostrandoNaTela("Arquivo não foi encontrado.")

def buscadorANO():

    try: 
        with open('/home/jdfc1/Documentos/lnpg/versao01_tk/banco1.txt', 'r', encoding='utf-8') as file:
            show = file.readlines()

            dados_lista = []

            for espaco in show:
                banda, album, ano, lancamento = espaco.strip().split(';')
                lancamento = lancamento.replace('\n', '')
                dados_lista.append(f'{banda} - {album} - {ano} - {lancamento}')
            
            file.close()
            
            vem_do_Radiobutton = vv0.get()
            vem_do_Combobox = combo.get()

            ano_pesquisa = int(vem_do_Combobox)
            ano_inicial = 1970
            ano_final = 2023
            
            if (vem_do_Radiobutton == 1):
                encontrei = []

                for imprimir in dados_lista:
                    ano = int(imprimir.split(" - ")[2])
                    if ano_inicial <= ano <= ano_pesquisa:
                        encontrei.append(f'{imprimir}\n')
                
                mostrandoNaTela(encontrei)

            elif (vem_do_Radiobutton == 2):
                encontrei = []

                for imprimir in dados_lista:
                    ano = int(imprimir.split(" - ")[2])
                    if ano_pesquisa <= ano <= ano_final:
                        encontrei.append(f'{imprimir}\n')
                
                mostrandoNaTela(encontrei)

            elif (vem_do_Radiobutton == 3):
                encontrei = []

                for imprimir in dados_lista:
                    ano = int(imprimir.split(" - ")[2])
                    if ano_pesquisa == ano:
                        encontrei.append(f'{imprimir}\n')
                
                mostrandoNaTela(encontrei)

    except FileNotFoundError:
        mostrandoNaTela("Arquivo não foi encontrado.")

def mostrandoNaTela(dados):
    texto.delete(1.0, 'end')
    for dado in dados:
        texto.insert('end', f'{dado}\n')


win = Tk()
win.title('organizador de albuns')
win.geometry("710x650+10+10")
win.resizable(True, True)
win.maxsize(width=730, height=730)

lbl1 = Label(win, text='Nome do Album: ')
lbl1.place(x=50, y=50)

lbl2 = Label(win, text='Ano de Lançamento: ')
lbl2.place(x=50, y=100)

lbl3 = Label(win, text='Nome da Banda: ')
lbl3.place(x=50, y=150)

lbl4 = Label(win, text='Album de Lançamento: ')
lbl4.place(x=50, y=200)

lbl5 = Label(win, text='BUSCA POR NOME: ')
lbl5.place(x=470, y=200)

lbl6 = Label(win, text='BUSCA POR ANO: ')
lbl6.place(x=470, y=360)

# field

t1 = Entry(win)
t1.place(x=200, y=50)

t2 = Entry(win)
t2.place(x=200, y=100)

t3 = Entry(win)
t3.place(x=200, y=150)

dadosentra = Entry(win)
dadosentra.place(x=450, y=250) # x largura width - y altura height

# radiobutton #########################
v0=IntVar()
v0.set(2)
r1=Radiobutton(win, text="sim", variable=v0, value=1)
r2=Radiobutton(win, text="não", variable=v0, value=2)
r1.place(x=200,y=200)
r2.place(x=250,y=200)

vv0=IntVar()
vv0.set(2)
rr1=Radiobutton(win, text="Anterior a", variable=vv0, value=1)
rr2=Radiobutton(win, text="Posterior a", variable=vv0, value=2)
rr3=Radiobutton(win, text="Igual a", variable=vv0, value=3)
rr1.place(x=400,y=400)
rr2.place(x=500,y=400)
rr3.place(x=600,y=400)
# radiobutton #########################


# combobox #########################
langs = ["1980", "1984", "1985", "1986", "1990", "1995", "1996", "2000", "2001", "2004",
"2005", "2010", "2015", "2017", "2020", "2021", "2022", "2023"]
   
combo = ttk.Combobox(win, values = langs)
combo.pack()
combo.place(x=450,y=450)
# combobox #########################

# botões
btn = Button(win, text="Gravar dados", command=clicked, bg="blue", fg="white")
btn.pack()
btn.place(x=80,y=250)

btn2 = Button(win, text="Buscar dados", command=buscador, bg="black", fg="white")
btn2.pack()
btn2.place(x=480,y=300)

btn3 = Button(win, text="Buscar p/ ano", command=buscadorANO, bg="red", fg="white")
btn3.pack()
btn3.place(x=480,y=500)

btn_mostrar = Button(win, text="Mostrar dados", command=reader)
btn_mostrar.pack()
btn_mostrar.place(x=250,y=250)



texto = Text(win, wrap="word", width=45, height=20)
texto.pack()
texto.place(x=25, y=300)

win.mainloop()
