import heranca_base


# Classe herda de list
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


print(chr(27) + "[2J")

playlist_fim_de_semana = Playlist(
    'fim de semana', heranca_base.filmes_series_lista)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
# Objeto criado pela playlist também é um iteravel playlist
for programa in playlist_fim_de_semana:
    # gora código de forma pythonica
    print(programa)

print(f'Existe na lista: {heranca_base.demolidor in playlist_fim_de_semana}')
playlist_fim_de_semana.remove(heranca_base.demolidor)
print(f'Continua na lista: {heranca_base.demolidor in playlist_fim_de_semana}')

print('\n')
