from os import system
system('cls')


soma = 0
for i in range(3):
    while True:

        nota = float(input(f"{i+1}ª Nota: "))
    
        if nota < 0 or nota > 10:
            print('Número inválido.')
        else:
            soma+=nota
            break    
        

media = soma / 3  

if(media > 7):
    resultado = 'Aprovado'
elif(media>= 5):
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print(f"Média: {media:.2f}")
print(f"{resultado}")