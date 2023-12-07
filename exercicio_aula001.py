from file_work import * # importando funções de outro arquivo.

opcao = int(input('fazer leitura opção 1: \n gravar dados opção 2: \n'))

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
        
        escreve(f'{meunome}|{idade}|{sexo}|{telefone}\n')