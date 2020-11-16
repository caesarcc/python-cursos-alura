from conta import Conta
conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marcos", 100.0, 1000.0)
print(conta.titular, conta2.titular, sep='\n')
print(conta.limite)
conta.limite = 2000.0
print(conta.limite)

conta.saca(3000.0)
print(Conta.codigos_bancos())
