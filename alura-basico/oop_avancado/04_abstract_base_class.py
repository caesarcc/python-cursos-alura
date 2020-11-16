from abc import ABC  # abstract base classes

from collections.abc import Sized
from collections.abc import MutableSequence


class Playlist(MutableSequence):
    pass

# Erro por não ter implementado os método da classe abstrata
# TypeError: Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
#filmes = Playlist()


class Dimencionavel(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

    def __len__(self):
        return len(self.descricao)


lista = Dimencionavel("texto de teste")
print(lista, len(lista))
