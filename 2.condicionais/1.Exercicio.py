import os
os.system('clear')

nome = str(input("Nome: "))
idade = int(input("Idade: "))

notas = []

for  i in range(3):
    nota = int(input(f"{i+1}ª Nota: "))
    notas.append(nota)

    somaNotas = sum(notas)
    media = somaNotas / 3

print(f"Média: {media}")

if(media >= 7):
    print("Aprovado")

else:
    print("Reprovado")