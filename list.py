import json
import os
naLixeira = False
base_dir = os.path.dirname(os.path.abspath(__file__))
listaPath = os.path.join(base_dir, 'lista.json')
lixeiraPath = os.path.join(base_dir, 'lixeira.json')

try:
    with open(listaPath, 'r') as f:
        lista = json.load(f)

except(FileNotFoundError, json.JSONDecodeError):
    with open(listaPath, 'w'):
        lista = []

try:
    with open(lixeiraPath, 'r') as f:
        lixeira = json.load(f)

except(FileNotFoundError, json.JSONDecodeError):
    with open(lixeiraPath, 'w'):
        lixeira = []

def dumpJson(arquivo, li):
    with open(arquivo, 'w') as f:
        json.dump(li, f)
    
while True:
    print('Lista de compras: selecione uma opção')
    escolha = input('1 - Inserir\n2 - Apagar\n3 - Listar\n4 - Lixeira\n5 - Sair\n\n')
    print('')

    if escolha == '1':
        lista.append(input('Digite o que deseja inserir: '))
        dumpJson(listaPath, lista)
        print('')

    elif escolha == '2':
        apagar = input('Digite o índice do que deseja apagar: ')
        print('')
        try:
            apagado = lista.pop(int(apagar))
            dumpJson(listaPath, lista)

        except (TypeError, IndexError, ValueError):
            print('Índice não encontrado\n')

        else:
            lixeira.append(apagado)
            dumpJson(lixeiraPath, lixeira)
            print(f'O item "{apagado}" foi transferido para a lixeira\n')

    elif escolha == '3':
        if not lista:
            print('A lista está vazia\n')

        else:
            for i, l in enumerate(lista):
                print(f'{i} - {l}')
            print('')

    elif escolha == '4':
        naLixeira = True

        while naLixeira:
            if not lixeira:
                print('A lixeira está vazia, voltando ao menu principal\n')
                naLixeira = False
            
            else:
                for i, l in enumerate(lixeira):
                    print(f'{i} - {l}')
                print('')

                print('Lixeira: selecione uma opção')
                escolha = input('1 - Voltar\n2 - Recuperar um\n3 - Recuperar tudo\n4 - Esvaziar lixeira\n\n')

                if escolha == '1':
                    print('')
                    naLixeira = False

                elif escolha == '2':
                    recuperar = input('Digite o índice do que deseja recuperar: ')
                    print('')
                    try:
                        recuperado = lixeira.pop(int(recuperar))

                    except (TypeError, IndexError, ValueError):
                        print('Índice não encontrado\n')

                    else:
                        lista.append(recuperado)
                        dumpJson(listaPath, lista)
                        dumpJson(lixeiraPath, lixeira)
                        print(f'O item "{recuperado}" foi transferido para a lista\n')

                elif escolha == '3':
                    lista += lixeira
                    lixeira = []
                    dumpJson(lixeiraPath, lixeira)
                    dumpJson(listaPath, lista)
                    print('Todos os itens da lixeira foram tranferidos para a lista\n')
                    naLixeira = False

                elif escolha == '4':
                    lixeira = []
                    dumpJson(lixeiraPath, lixeira)
                    print('A lixeira foi esvaziada\n')
                    naLixeira = False

                else:
                    print('Inválido\n')

    elif escolha == '5':
        break

    else:
        print('Inválido\n')