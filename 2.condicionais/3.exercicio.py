import os
os.system('clear')

numeros = []

for  i in range(2):
    numero = int(input(f"{i+1}ª Número: "))
    numeros.append(numero)

produto = numeros [0] * numeros [1]   
soma = sum(numeros)
media = soma / 2

maior = max(numeros)
menor = min(numeros)


print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

if(numeros [0] == numeros [1]):
    print(f"Esses números são iguais.")
else:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
