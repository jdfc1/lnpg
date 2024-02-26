def escreve(nomes):
    arquivo = open("banco.txt", 'a', encoding='utf-8')
    arquivo.write(f'{nomes}\n')
    arquivo.close()

def ler():
    with open("banco.txt", 'r') as arquivo:
        nomes = arquivo.readlines()
        #print(nomes)
        for linha in nomes:
            lista = linha.strip().split('|')
            nome = lista[0]
            idade = int(lista[1])
            sexo = lista[2].lower() #deixar tudo minúsculo
            
            if (sexo == "m"):
                sexo = "Masculino"
            else:
                sexo = "Feminino"
            
            telefone = lista[3]
            print(f"Nome: {nome}, Idade: {idade} anos, Sexo: {sexo} e telefone: {telefone}")
    arquivo.close()

def busca_usuario_pelo_sexo(sexo): #RETORNA uma lista com todos os cadastros do sexo especificado:
    with open("banco.txt", 'r') as arquivo:
        nomes = arquivo.readlines() #leitura de linha por linha
        for linha in nomes: 
            lista = linha.split('|') #delimitando com "|"
            nome = lista[0] #resgatando a primeira coluna de lista em nomes
            idade = int(lista[1]) # resgatando a segunda coluna da lista em idades
            genero = lista[2].lower() #deixar tudo minúsculo e fazendo o resgate em genero
            telefone = lista[3] 
            telefone = telefone.replace('\n', '') # estava imprimindo com \n

            if genero == sexo: # fazendo a condição m ou f
                print(f'Nome: {nome}, idade: {idade}, telefone: {telefone}')
    arquivo.close()

def busca_usuario_pelo_nome(nome_procurado):
    with open("banco.txt", 'r') as file:
        linhas = file.readlines()
        for espaco in linhas:
            coluna = espaco.split('|')
            nome = coluna[0]
            idade = int(coluna[1])
            genero = coluna[2]
            telefone = coluna[3]
            telefone = telefone.replace('\n', '')

            criando_lista = [f'{nome}, {idade}, {genero} e {telefone}']

            for salvar in criando_lista:
                if nome_procurado in salvar:
                    encontrei = salvar
                    print(f'{encontrei}')
            


            




""" 
def ler():
    arquivo = open("banco.txt", 'r', encoding='utf-8')
    nomes = arquivo.read()
    lista = nomes.split('|')
    for n in nomes:
        print(f"nome: {n}")
    
    arquivo.close() 
"""

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

