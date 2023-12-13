from tkinter import *

def buscador():

    busca = dadosentra.get().lower()
    dadosentra.delete(0, END)
    #print(busca)

    try: 
        with open('/home/jdfc1/Documentos/lnpg/versao02_tk/banco1.txt', 'r', encoding='utf-8') as file:
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

def mostrandoNaTela(dados):
    texto.delete(1.0, 'end')
    for dado in dados:
        texto.insert('end', f'{dado}\n')


win = Tk()
win.title('organizador de albuns')
win.geometry("530x530+10+10")

lbl1 = Label(win, text='Digite para pesquisar: ')
lbl1.place(x=50, y=50)

dadosentra = Entry(win)
dadosentra.place(x=200, y=50) # x largura width - y altura height

btn2 = Button(win, text="Buscar dados", command=buscador, bg="black", fg="white")
btn2.pack()
btn2.place(x=180,y=100)

texto = Text(win, wrap="word", width=59, height=20)
texto.pack()
texto.place(x=25, y=150)

win.mainloop()
