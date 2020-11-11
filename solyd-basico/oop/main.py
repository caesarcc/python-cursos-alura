from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 40)
print(caminhao_rosa)
print(type(caminhao_rosa))
caminhao_rosa.abastecer(100)
print("Cor caminhao: ", caminhao_rosa.cor)
print("Tanque: ", caminhao_rosa.tanque)


carro_azul = Carro('azul', 'bmw', 30)
print(carro_azul)
print(type(carro_azul))
print("Cor carro: ", carro_azul.cor)

carro_azul.abastecer(10)
print("Tanque: ", carro_azul.tanque)
carro_azul.abastecer(40)
print("Tanque: ", carro_azul.tanque)


from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Gui', '123.456.789-10', 27)

conta_do_gui = Conta(cliente1, 10.50, 1000)
print(conta_do_gui.cliente.nome, conta_do_gui.consulta_saldo())
conta_do_gui.depositar(1000.40)
print(conta_do_gui.consulta_saldo())
conta_do_gui.sacar(500)
print(conta_do_gui.consulta_saldo())
conta_do_gui.sacar(1000)
print(conta_do_gui.consulta_saldo())
