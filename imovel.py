# Classe Imovel()
class Imovel():
    def __init__(self, id_imovel, endereco, area, valor, status):
        self.id_imovel = id_imovel
        self.endereco = endereco
        self.area = area
        self.valor = valor
        self.status = status
        
    def atualizar_status(self, novo_status = None):
        if novo_status is not None:
            self.status = novo_status
        
    def exibir_informacoes(self):
        print(f"O Imovel {self.id_imovel} localiza-se no endereço: {self.endereco}, possui uma area de: {self.area} metros quadrados. Seu valor é avaliado em: R${self.valor}, seu atual status é: {self.status}")
        