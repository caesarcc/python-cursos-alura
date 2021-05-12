import re
import requests

requisicao = requests.get('https://www.procergs.rs.gov.br/contato')

string_email = "caesarcesar.rs@gmail.com"
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) 
print(padrao)