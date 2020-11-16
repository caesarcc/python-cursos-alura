class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def imprime(self):
        print(f'{self._nome} - {self.ano} ({self._likes} likes)')

    # método especial para impressão de objeto, parte do toString do java,
    # existe também o método __repr__ para os dados exibidos em console/memória
    def __str__(self):
        return f'py {self._nome} - {self.ano} ({self._likes} likes)'

    versao_programa = '1.0'
    # exemplo de método estático
    @classmethod
    def info(cls):
        return f'Esse é um {cls.versao_programa}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(
            f'{self._nome} ({self.ano}) - duração: {self.duracao} ({self._likes} likes)')

    def __str__(self):
        return f'py {self._nome} ({self.ano}) - duração: {self.duracao} ({self._likes} likes)'


class Serie(Programa):
    versao_programa = '1.1'

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(
            f'{self._nome} ({self.ano}) - {self.temporadas} temporadas ({self._likes} likes)')

    def __str__(self):
        return f'py {self._nome} ({self.ano}) - {self.temporadas} temporadas ({self._likes} likes)'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
todopanico = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
todopanico.dar_like()
todopanico.dar_like()
todopanico.dar_like()
todopanico.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_series_lista = [vingadores, atlanta, demolidor, todopanico]

if __name__ == "__main__":

    print(chr(27) + "[2J")

    for programa in filmes_series_lista:
        # testar se possui o atributo, mas não é bom
        detalhes = programa.duracao if hasattr(
            programa, 'duracao') else programa.temporadas
        print(f'old: {programa.nome} - {detalhes} : {programa.likes}')

    print('\n')

    for programa in filmes_series_lista:
        # agora deixando responsabilidade de imprimir para a classe
        programa.imprime()

    print('\n')

    for programa in filmes_series_lista:
        # gora código de forma pythonica
        print(programa)

    print('\n')
