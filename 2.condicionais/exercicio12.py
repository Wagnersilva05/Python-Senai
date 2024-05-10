soma = 0

for i in range(4):
    nota = float(input(f"{i+1}ª Nota: "))
    soma+=nota
    
media = soma / 4    

print(f"Média: {media}")
