from abc import ABCMeta, abstractmethod


class Programa(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass


class Filme(Programa):
    pass


teste = Filme()
