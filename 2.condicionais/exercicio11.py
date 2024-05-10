pares = 0
impares = 0
for i in range(1, 6):
    numero = int(input(f"{i}º Número: "))

    if(numero % 2 == 0):
        pares+=1
    else:
        impares+=1    
print(f"Quantidades de pares: {pares}")
print(f"Quantidades de ímpares: {impares}")
