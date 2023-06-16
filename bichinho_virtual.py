class bichinhoVirtual():
    
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = saude

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return novo_nome
    
    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
        return nova_fome
    
    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
        return nova_saude
    
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        return nova_idade
    
    def retornar_Humor(self):
        if self.saude > 5 and self.fome > 5:
            print("FELIZ")
        elif self.saude < 5 or self.fome < 5:
            print("TRISTE")
