import re

string_teste = "O gato é bonito"

padrao = re.search(r'gat.', string_teste) # . é qualquer letra incluindo espaço
print(padrao.group())

padrao = re.search(r'gat\w', string_teste) # \w é letra sem espaço
print(padrao.group())

padrao = re.search(r'gat\w\w', string_teste) # \w é letra sem espaço
if not padrao:
    print("nao encontrou mesmo")

string_teste = "O gato, a gata, os gatinhos, os gatões"

padrao = re.findall(r'gat\w', string_teste) #busca todos com uma letra sem espaço
print(padrao)
print(padrao[2])

string_teste = "O gato, a gatinha, os gatinhos, os gat"
padrao = re.findall(r'gat\w+', string_teste) # + tem que ter mais letras sem espaço
print(padrao)
padrao = re.findall(r'gat\w*', string_teste) # * tem que ter mais letras incluindo espaço
print(padrao)

string_teste = "O gato, a gatinha, os gatinhos, os gat"
padrao = re.findall(r'[gt]', string_teste) #grupo de letras, prcura tudo que tiver dentro do colchetes
print(padrao)

#encontrar email
string_email = "caesarcesar.rs@gmail.com"
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', string_email) #valida email
print(padrao)