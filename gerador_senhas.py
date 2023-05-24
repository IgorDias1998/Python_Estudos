"""
Programa gerador de senhas.
"""
import random

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%¨&*()_+'

quantidade_de_senhas = int(input('Digite quantas senhas você deseja gerar: '))
qtd_caracteres_senha = int(input('Digite a quantidade de caracteres da sua senha: '))
print(type(quantidade_de_senhas))

i = 0
for senha in range(quantidade_de_senhas):
    senhas = ''
    i += 1
    for caractere in range(qtd_caracteres_senha):
        senhas += random.choice(caracteres)
    print(f"{i}º senha:\n{senhas}")