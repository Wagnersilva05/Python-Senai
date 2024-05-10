nome = str(input("Nome: ")).strip().upper()
sexo = str(input("Digite o sexo: [M] ou [F]: ")).strip().upper()
estadoCivil = str(input("Digite seu estado civil: ")).strip().upper()


if(sexo == 'F' and estadoCivil == 'CASADA'):
    anosCasadas = int(input("Digite o tempo de casamento: "))


print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadoCivil}")
print(f"Tempo de casamento: {anosCasadas} anos")