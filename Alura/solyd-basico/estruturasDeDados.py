lista = ['Caesar', 'Lili', 'Camila']              #listas (list), tem métodos para manipulação e pode repetir e é ordenado, pode pegar pela posição do item

tupla = ('Caesar', 'Lili')                        #tupla (tuple), fixo, não possui métodos de manipulação
 
dicionario = {'nome': 'Caesar', 'idade': 38}      #dicionario (dict), é uma tabela hash com chave e valor

conjunto = {'Caesar', 'Lili', 'Camila'}           #conjunto (set), tem métodos de manipulação, não é ordenado, não pode haver valores repetidos (repetidos são ignorados) (MAIS RÁPIDOQUE O LIST)

print(tupla)
print(type(tupla))
print(tupla[1])

for nome in tupla:
  print(nome)
'''
for nome in lista:
  print(nome)
for nome in conjunto:
  print(nome)
'''
for valores in dicionario.values():
  print(valores)  

if 'Caesar' in tupla:
  print('Achei o Caesar')
  
if 'Camila' in tupla:
  print('Não achei o Caesar')
  
if 'Lili' in lista:
  print('Achei a Lili na lista')

print(dicionario['nome'])

print(len(lista))

if 'Caesar' in dicionario.values():
  print('Caesar está no dicionario')