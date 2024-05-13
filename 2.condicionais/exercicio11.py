from os import system
system('cls')


contador = 0
soma = 0

while True:

    for i in range(2):
        nota = float(input(f"{i+1}ª Nota: "))
    soma+=nota
    contador+=1

    if nota < 0 or nota > 10:
        print('Número inválido.')
    else:
        break    
        

media = soma / contador     

print(f"Média: {media:.2f}")