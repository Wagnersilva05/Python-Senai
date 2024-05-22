numeros = []
for i in range(5):
    numero = int(input(f"{i+1}º Número: "))
    numeros.append(numero)

    maior = max(numeros)
    menor = min(numeros)

print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")
for numero in numeros:
    print(numero)    