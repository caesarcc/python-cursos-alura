arq = open('/lista.txt', 'w')
texto = """
Lista de Alunos
---
João da Silva
José Lima
Maria das Dores
"""
arq.write(texto)
arq.close()

arq = open('/lista.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('Maria das Dores')
arq.writelines(texto)
arq.close()


arq = open('/lista.txt', 'r')
texto = arq.read()
print(texto)
arq.close()

arq = open('/lista.txt', 'r')
texto = arq.readlines()
for linha in texto :
    print(linha)
arq.close()