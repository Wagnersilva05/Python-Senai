notas = []
soma = 0
for i in range(4):
    nota = float(input(f"{i+1}º Nota: "))
    notas.append(nota)

    soma+=nota
    media = nota / 4

    if media >= 7:
        resultado = "Aprovado"
    elif media >= 5:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"

print(f"Média: {media}")
print(resultado)

for nota in notas:
    print("notas exibidas: ")
    print(nota)