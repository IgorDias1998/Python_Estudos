import os

i = 0
valor_total = 0

while True:
    i += 1
    venda = float(input(f"Digite o valor do produto {i}: R$"))
    if venda == 0:
        print(f"Total da compra: R${valor_total}")
        dinheiro = float(input("Valor recebido em dinheiro: R$"))
        print(f"Troco: R${dinheiro - valor_total}")
        i = 0
        valor_total = 0
        os.system("cls")
        
    else:
        print(f"Produto {i}: R${venda}")
        valor_total = venda + valor_total