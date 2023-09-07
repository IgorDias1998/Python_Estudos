'''
Gasolina R$2,50     Alcool R$1,90

até 20 litros -4%    Até 20 litros -3%
acima 20 litros-6%   Acima 20 litros -6%


'''
precoGasolina = 2.5
precoAlcool = 1.9
valorFinal = 0

tipoCombustivel = input("Selecione o combustível que deseja abastecer(A = Alcool G = gasolina): ")
quantidadeAbastecer = int(input("Digite o valor de litros que deseja abastecer: "))

if tipoCombustivel.lower() == "g":
    if quantidadeAbastecer <= 20:
        valorFinal = (quantidadeAbastecer * precoGasolina) * 0.96
        print(f"Você abasteceu {quantidadeAbastecer} litros de Gasolina com desconto de 4% total R${valorFinal}")
    elif quantidadeAbastecer > 20:
        valorFinal = (quantidadeAbastecer * precoGasolina) * 0.94
        print(f"Você abasteceu {quantidadeAbastecer} litros de Gasolina com desconto de 6% total R${valorFinal}")

if tipoCombustivel.lower() == "a":
    if quantidadeAbastecer <= 20:
        valorFinal = (quantidadeAbastecer * precoAlcool) * 0.97
        print(f"Você abasteceu {quantidadeAbastecer} litros de Alcool com desconto de 3% total R${valorFinal}")
    elif quantidadeAbastecer > 20:
        valorFinal = (quantidadeAbastecer * precoAlcool) * 0.94
        print(f"Você abasteceu {quantidadeAbastecer} litros de Alcool com desconto de 6% total R${valorFinal}")