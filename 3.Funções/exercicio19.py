from os import system
system('clear')
def cabecalho():
    system('clear')
    print("--------------------")
    print("=== SENAI | FIEB ===")
    print("--------------------")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado

def subtrair(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    resultado = n1 / n2
    return resultado

cabecalho()
primeiroNumero = int(input("Primeiro número: "))
segundoNumero = int(input("Segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
mult = multiplicar(primeiroNumero, segundoNumero)
sub = subtrair(primeiroNumero, segundoNumero)
div = dividir(primeiroNumero, segundoNumero)

cabecalho()
print(f"Soma: {soma}")
print(f"Multiplicação: {mult}")
print(f"Subtração: {sub}")
print(f"Divisão: {div}")
    