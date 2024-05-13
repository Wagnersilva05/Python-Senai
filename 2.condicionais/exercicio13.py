soma = 0
contador = 0

while True:
    nota = int(input("Digite mais uma nota: "))
    r = str(input("Deseja inserir mais uma nota? ")).upper()
   
    soma += nota
    contador+=1
    if r == 'N':
        break

media = soma / contador

if(media > 7):
    resultado = 'Aprovado'
elif(media>= 5):
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print(f"Média: {media:.2f}")
print(f"{resultado}")
    