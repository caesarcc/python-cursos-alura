def soma(numero1, numero2):
  resp = numero1 + numero2
  return resp

retorno = soma(75, 1289)
print(retorno)

retorno = soma(12.34, 75.60)
print(retorno)

retorno = soma(soma(75, 1289), soma(12.34, 75.60))
print(retorno)

def funcao_sem_parametros_retorno():
  print("hello world")
  
funcao_sem_parametros_retorno()

def tem_seis_itens(argumento):
  return len(argumento) == 6

def retorno_duplo(argumento):
  if len(argumento) == 6:
    return (True, 6)
  else:
    return (False, len(argumento))
  
print(retorno_duplo("Caesar"))
print(retorno_duplo("oi pessoal"))

if tem_seis_itens("Caesar"):
  print("Caesar tem 6 letras")
  
if not tem_seis_itens("oi pessoal"):
  print("oi pessoal não tem 6 letras")
  
'''
EXERCICIO: Escreva uma funcao que recebe um objeto de coleção
e retorna o valor do maior numero dentro dessa colecao faça outra funcao que retorna o menor numero dessa coleçao
'''

def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(maior([1,-2,1.2,87.2,1289,-7,0]))
print(menor([1,-2,1.2,87.2,1289,-7,0]))