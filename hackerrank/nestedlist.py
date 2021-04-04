if __name__ == '__main__':
    n = int(input())
    alunos = [[input(), float(input())] for _ in range(n)]

    segunda_maior=sorted(list(set(linha[1] for linha in alunos)))[1] 

    for nome,nota in sorted(alunos):
        if nota==segunda_maior:
            print(nome)