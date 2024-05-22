from os import system
system('clear')
def cabecalho():
    system('clear')
    print("--------------------")
    print("=== SENAI | FIEB ===")
    print("--------------------")

numeros = []

for i in range (5):
    cabecalho()
    numero = int(input(f"{i+1}º Número: "))
    if numero < 0:
        numero = 0
        numeros.append(numero)

for i , numero in enumerate (numeros):
    print(f"{i+1}º Número")        