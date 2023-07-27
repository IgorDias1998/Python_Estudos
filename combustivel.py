class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecer_valor(self, valorAbastecido):
        litros_abastecido = valorAbastecido / self.valorLitro
        if litros_abastecido <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecido
            return f"Foi abastecido {litros_abastecido:.2f} litros, restam {self.quantidadeCombustivel:.2f} litros"
        else:
            return "Quantidade de combustível insuficiente para abastecimento"

    def abastecer_litros(self, litrosAbastecido):
        valorPago = litrosAbastecido * self.valorLitro
        if litrosAbastecido <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litrosAbastecido
            return f"O total do abastecimento foi de R${valorPago}, restam {self.quantidadeCombustivel:.2f} litros na bomba"
        else:
            return "Quantidade de combustível insuficiente para abastecimento"
    
    def alterar_valor(self, novo_valorLitro):
        self.valorLitro = novo_valorLitro
        return f"Novo valor do litro do combustível: R${novo_valorLitro}"
    
    def alterar_tipo(self, novo_tipoCombustivel):
        self.tipoCombustivel = novo_tipoCombustivel
        return f"Combustível alterado com sucesso: Novo tipo: {novo_tipoCombustivel}"

bomba = BombaCombustivel("Alcool", 4.15, 150)
print(bomba.abastecer_valor(150))
print(bomba.abastecer_litros(50))
bomba.alterar_valor(5)
print(bomba.abastecer_litros(50))