from os import system
system('cls')

nota = -1

while nota < 0 or nota > 10:

    nota = float(input("Digite uma nota: "))

print(f"Nota informada: {nota:.2f}")