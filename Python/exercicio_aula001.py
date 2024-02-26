from file_work import * # importando funções de outro arquivo.

opcao = int(input('\nfazer leitura opção 1: \ngravar  dados opção 2: \nbuscar p sexo opção 3: \nbuscar nome aproximado op 4 \n'))

if (opcao == 1):
    ler()
elif (opcao == 2):
    while (True):
    
        meunome = input('seu nome: ')

        if (meunome == '0'):
            break
        else:
            idade = int(input('digite sua idade: '))
            sexo = input('digite M para masculino: \n digite F para feminino: ')
            telefone = int(input('digite seu número de telefone: '))
        
        escreve(f'{meunome}|{idade}|{sexo}|{telefone}')

elif (opcao == 3):
    sexo = input('digite M para listar todos os homens: \n digite F para listas as mulheres: ')
    busca_usuario_pelo_sexo(sexo)

elif (opcao == 4):
    name = input("digite o nome que quer procurar na lista: ")
    busca_usuario_pelo_nome(name)