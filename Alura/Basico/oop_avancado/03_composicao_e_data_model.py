import heranca_base


# Classe herda de list
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # usando métodos do python data model
    # método que transforma a classe em um iteravel (for in, in)
    def __getitem__(self, item):
        return self._programas[item]

    # método que transforma a classe algo com tamanho disponível (len)
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


print(chr(27) + "[2J")

playlist_fim_de_semana = Playlist(
    'fim de semana', heranca_base.filmes_series_lista)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
# Objeto criado pela playlist também é um iteravel playlist
for programa in playlist_fim_de_semana:
    # gora código de forma pythonica
    print(programa)

print(f'Existe na lista: {heranca_base.demolidor in playlist_fim_de_semana}')
playlist_fim_de_semana.listagem.remove(heranca_base.demolidor)
print(f'Continua na lista: {heranca_base.demolidor in playlist_fim_de_semana}')
print(f'Primeiro elemento: {playlist_fim_de_semana[0]}')

print('\n')
