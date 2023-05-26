"""
Faça uma lista de compra
Usuário pode inserir, apagar(conforme o indice) e listar valores da lista
"""
import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Digite o que deseja inserir: ')
        lista.append(valor)
    
    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Digite qual indice deseja apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para lsitar')

        for i, valor in enumerate(lista):
            print(i, valor)