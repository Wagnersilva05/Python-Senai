from os import system
system('clear')
def cabecalho():
    system('clear')
    print("--------------------")
    print("=== SENAI | FIEB ===")
    print("--------------------")

def inflaciona(preco):
    if preco < 100:
        resultado = preco + (preco * 10 / 100)
    else:
        resultado = preco + (preco * 20 / 100)    
    return resultado

cabecalho()
valor = float(input("Digite um valor: "))

inflacao = inflaciona(valor)

cabecalho()
print(f"Valor original: {valor}")
print(f"Valor com inflação: {inflacao}")
