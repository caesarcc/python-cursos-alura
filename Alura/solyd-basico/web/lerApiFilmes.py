import requests
import json

req = None
try:
    req = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=7eba7878&t=interstellar")
except:
    print('Erro de conexao')
    exit()

#print(req.text)

jsonRetorno = json.loads(req.text)

print(jsonRetorno['imdbRating'])