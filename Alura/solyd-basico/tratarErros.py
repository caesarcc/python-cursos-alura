try:
    a = 100 / 0
except ZeroDivisionError:
    print("Erro de divisão por zero")

try:
    metodoNaoExiste()
except NameError:
    print("Método não existe")

print("Para qualquer excessao")


try:
    a = 100 / 0
except Exception as erro:
    print("Aconteceu algum erro:", erro)
