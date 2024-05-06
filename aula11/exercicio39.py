nascimento = int(input("Digite sua data de nascimento: "))

idade = 2024 - nascimento

print(f"Você tem {idade} anos")

if(idade >= 18 and idade < 45):
    print("É hora de se alista!")
    print(f"Ainda falta {45 - idade} anos para você se alistar")
elif(idade < 18):
    print(f"Você ainda não pode se alistar! falta {18 - idade} anos")
else:
    print("Você não pode mais se alistar")
    print(f"Já passou {idade - 45} depois da idade máxima.")