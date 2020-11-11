import requests 

#requisicao = requests.get('http://www.google.com')

#print(requisicao)
#print(requisicao.text)

requisicaoerro = None
try:
    requisicaoerro = requests.get('http://www.g1.com.br')
except Exception as e:
    print("Requisição com erro:", e)

print(requisicaoerro)

cabecalho = {'Referer':'http://caesarcesar.com.br'}
coockienovo = {'ultima-visita':'hoje'}
dadosform = {'usuario':'caesar', 'senha':'teste'}
novapost = requests.post('https://enlpeqatzftn.x.pipedream.net', 
                        headers=cabecalho, 
                        data=dadosform,
                        cookies=coockienovo)