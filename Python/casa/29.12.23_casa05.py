import tkinter as tk

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel(root)
    segunda_janela.title("Segunda Janela")
    
    # Adicione widgets ou elementos à segunda janela, se necessário
    label_segunda_janela = tk.Label(segunda_janela, text="Esta é a segunda janela.")
    label_segunda_janela.pack(padx=20, pady=20)

# Janela principal
root = tk.Tk()
root.title("Janela Principal")

# Botão para abrir a segunda janela
botao_abrir_segunda_janela = tk.Button(root, text="Abrir Segunda Janela", command=abrir_segunda_janela)
botao_abrir_segunda_janela.pack(padx=20, pady=20)

# Execute o loop principal
root.mainloop()
