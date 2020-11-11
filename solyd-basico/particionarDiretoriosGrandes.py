import sys
import os
import shutil

argumentos = sys.argv
#print(argumentos)

pasta = argumentos[1]
qtdbloco = int(argumentos[2])

arquivos = [nome for nome in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, nome))]

print('Qtde arquivos: ', arquivos.__len__())

i = 0
ipasta = 0
subpasta = ''
for arquivo in arquivos:
    if (i>=qtdbloco or i == 0):
        ipasta+=1
        subpasta = 'subdir_' + str(ipasta).rjust(2, '0')
        os.mkdir(os.path.join(pasta, subpasta))
        i = 0
    i+=1
    shutil.copyfile(os.path.join(pasta, arquivo), os.path.join(pasta, subpasta, arquivo))
