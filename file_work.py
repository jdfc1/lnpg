def escreve(nomes):
    arquivo = open('banco.txt', 'a', encoding='utf-8')
    arquivo.write(nomes)

def ler():
    arquivo = open('banco.txt', 'r', encoding='utf-8')
    nomes = arquivo.read()
    lista = nomes.split(';')
    for n in lista:
        print(n)

# def main():
#     escreve("aula de programação;")
#     ler()

# main()

# arquivo = open('my_name.txt','r',encoding='uft-8')
# print(arquivo.read())

# arquivo = open('my_name.txt','r', encoding='utf-8')
# nomes = arquivo.read()
# lista = nomes.split(';')
# for n in lista:
#     print(n)

# print(lista)

# a adiciona - w sobrescreve - 

