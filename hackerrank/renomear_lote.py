import multiprocessing
from joblib import Parallel, delayed
import os
import sys
import PySimpleGUI as sg

__version_info__ = (0, 2, 0)
__version__ = '.'.join(map(str, __version_info__))


def lista_arquivos(procura, extensao="*"):
    diretorio, nome_exec = os.path.split(__file__)

    arquivos = os.listdir(diretorio)
    os.chdir(diretorio)

    arquivos = [arquivo for arquivo in arquivos
                if arquivo != nome_exec and not os.path.isdir(arquivo)]

    assert arquivos, "Nenhum arquivo encontrado no \
        diretório '{}'.".format(diretorio)

    if extensao.find("*") >= 0:
        selecao = arquivos
    else:
        selecao = [arquivo for arquivo in arquivos
                   if arquivo.endswith(extensao)]

    assert selecao, "Nenhum arquivo da extensão .{} \
        encontrado no diretório '{}'.".format(extensao, diretorio)

    selecao = [arquivo for arquivo in selecao
               if arquivo.find(procura) >= 0]

    assert selecao, "Nenhum arquivo possui o texto {}.".format(procura)
    return selecao


def renomeia_arquivo(nome_do_arquivo, procura, substitui):
    nome_destino = str(nome_do_arquivo).replace(procura, substitui)
    os.rename(nome_do_arquivo, nome_destino)


def entrada(procura, substitui, extencao):
    try:
        arquivos = lista_arquivos(procura, extencao)

        # processamento paralelo (roda um arquivo por CPU disponível)
        num_cores = multiprocessing.cpu_count()
        Parallel(n_jobs=num_cores)(
            delayed(renomeia_arquivo)(nome_do_arquivo, procura, substitui)
            for nome_do_arquivo in arquivos)

        print('{} arquivo(s) renomeados com sucesso.'.format(len(arquivos)))
    except AssertionError as error:
        sg.PopupError(error, title='Erro Fatal!')


def valida_argumentos():
    assert len(sys.argv) >= 2, "Parâmetros inválidos. Confira documentação."
    procura = sys.argv[1]
    if len(sys.argv) == 2:
        substitui, extensao = '', '*'
    elif len(sys.argv) == 3 and sys.argv[2] != "*":
        substitui, extensao = sys.argv[2], '*'
    else:
        substitui, extensao = sys.argv[2], sys.argv[3]
    return procura, substitui, extensao


if "__main__" == __name__:
    procura, substitui, extensao = valida_argumentos()
    entrada(procura, substitui, extensao)
