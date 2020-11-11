from veiculo import Veiculo

class Carro(Veiculo):

    def _init_(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)
        
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Erro: tanque cheio")
        else:
            self.tanque += litros
