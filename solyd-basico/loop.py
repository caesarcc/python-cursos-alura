'''
Programa para entender fluxo via identação, IF, WHILE e FOR o fluxo dos comandos
internos ao loop ou condição é definido por identação, LOL!!!
'''
numero_de_convidados = input('Coloque o numero de convidados: ')
lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados):
    nome_do_convidado = input('Coloque o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('Serão', numero_de_convidados, 'convidados')

print('\nLISTA DE CONVIDADOS')
for convidado in lista_de_convidados:
    print(convidado)

lista_numeros = range(5, 20, 3)
for item in lista_numeros:
  print (item)
print (lista_numeros)

for i in range(5):
  print (i)
  print (item)    