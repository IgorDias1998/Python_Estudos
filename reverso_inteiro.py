def reverso(numero):
        numero_str = str(numero)
        numero_reverso_str = numero_str[::-1]
        numero_reverso = int(numero_reverso_str)
        return numero_reverso

numero = int(input("Digite o numero numero interio: "))
print(reverso(numero))