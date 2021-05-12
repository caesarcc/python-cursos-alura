# Detalhes do ambiente e do uso da aplicação

### Criar ambiente isolado para a aplicação:

Atenção para estar com **permissão de administrador**. Navegar até a raiz do projeto e executar:

- Cria ambiente isolado vazio  
```python -m venv .venv```
- Ativa o ambiente novo  
```.venv\scripts\activate```
- Atualiza a versão do pip  
```python -m pip install --upgrade pip```
- Instala pacotes requeridos por este projeto  
```pip install -r requirements.txt```


### Gerar arquivo de dependências:
- Executar este processo somente para gerar versão  
```pip freeze > requirements.in```  
```pip-compile --generate-hashes requirements.in```



### TODO:
docker pull python
