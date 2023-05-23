class Bola:

    def __init__(self):
        self.cor = "Branco"
        self.tamanho = 50
        self.material = "Borracha"

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostrar_cor(self):
        print(self.cor)