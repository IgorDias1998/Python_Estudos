class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def mostra_lado(self):
        return self.lado
    
    def area_quadrado(self):
        return self.lado ** 2
    
