numeros = []
pares = 0
impares = 0
for i in range(6):
    numero = int(input(f"{i+1}º Número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares+=1
    else:
        impares+=1    

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")

print("Número exibidos: ")
for numero in numeros:
    print(numero)    