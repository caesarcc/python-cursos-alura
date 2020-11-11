import sys
import os

argumentos = sys.argv
#print(argumentos)

pastaEsquerda = argumentos[1]
pastaDireita = argumentos[2]

arquivosEsquerda = [nome for nome in os.listdir(pastaEsquerda) if os.path.isfile(os.path.join(pastaEsquerda, nome))]
#jpgs = [arq for arq in arquivosLeft if arq.lower().endswith(".jpg")]
#print(jpgs[0:3])

arquivosDireita = [nome for nome in os.listdir(pastaDireita) if os.path.isfile(os.path.join(pastaDireita, nome))]

#listaExiste = [os.path.join(pastaRigth, nome) for nome in arquivosLeft if os.path.isfile(os.path.join(pastaRigth, nome))]
listaExiste = [nome for nome in arquivosEsquerda if os.path.isfile(os.path.join(pastaDireita, nome))]
#python conferirArquivos.py "C:\Users\caesar-cesar\Pictures\Camera Roll"

print('Qtde left: ', arquivosEsquerda.__len__())
print('Qtde right: ', arquivosDireita.__len__())
print('Qtde duplos: ', listaExiste.__len__())

#print(listaExiste[1:10])

if argumentos.__len__() > 3 and argumentos[3] == 'removerDaDireita':
    for arqRemover in listaExiste:
      os.remove(os.path.join(pastaDireita, arqRemover))
