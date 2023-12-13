from tkinter import Tk, Button, Text

def mostrar_dados():
    try:
        with open('/home/jdfc1/Documentos/lnpg/casa/versao01_tk/banco1.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

            dados = []
            for linha in linhas:
                banda, album, ano, lancamento = linha.strip().split(';')
                lancamento = lancamento.replace('\n', '')
                dados.append(f'{banda} - {album} - {ano} - {lancamento}')

            mostrar_na_interface(dados)

    except FileNotFoundError:
        mostrar_na_interface(["Arquivo não encontrado."])

def mostrar_na_interface(dados):
    texto.delete(1.0, "end")  # Limpa o conteúdo atual
    for dado in dados:
        texto.insert("end", f"{dado}\n")

# Criação da janela principal
win = Tk()
win.title('Exibição de Dados')
win.geometry("430x300+10+10")

# Botão para mostrar dados
btn_mostrar = Button(win, text="Mostrar dados", command=mostrar_dados)
btn_mostrar.pack(pady=10)

# Widget de texto para exibir dados
texto = Text(win, wrap="word", width=60, height=25)
texto.pack()

win.mainloop()
