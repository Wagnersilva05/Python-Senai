idade = int(input("Digite sua idade"))

if(idade < 16):
    print("Não pode votar!")
elif(idade < 18):
    print("Voto opcional!")
elif(idade < 65):
    print("Voto obrigatorio")
else:
    print("Nao obrigatorio")        