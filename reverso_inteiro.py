class ReverterInteiro:
        def __init__(self, numero):
                self.numero = numero

        def reverso(numero):
                numero_str = str(numero)
                numero_reverso_str = numero_str[::-1]
                numero_reverso = int(numero_reverso_str)
                return numero_reverso

numero = int(input("Digite o numero numero interio: "))
print(ReverterInteiro.reverso(numero))