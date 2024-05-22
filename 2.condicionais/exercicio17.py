numeros = []
somaPositivo = 0
quantidadeNegativo = 0
numeroNeutro = 0
for i in range(10):
    numero = int(input(f"{i+1}º Número: "))
    numeros.append(numero)

    if(numero > 0):
        somaPositivo+=numero
    elif (numero == 0):
        print("Número 0 ignorado.")
        continue
    else:
        quantidadeNegativo+=1
print(f"Soma dos números positivos: {somaPositivo}")
print(f"Quantidade de números negativos: {quantidadeNegativo}")
