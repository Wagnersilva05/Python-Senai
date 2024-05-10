soma = 0
for i in range(3):
    nota = float(input(f"{i+1}ª Nota: "))
    soma+=nota

media = soma / 3

if(media >= 7):
    resultado = 'Aprovado!'
elif(media >= 4):
    resultado = 'Recuperação!'
else:
    resultado = 'Reprovado!'

print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")
