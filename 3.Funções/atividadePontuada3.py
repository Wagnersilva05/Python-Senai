from os import system
system('clear || cls')
def cabecalho():
    system('clear || cls')
    print("--------------------")
    print("=== SENAI | FIEB ===")
    print("--------------------")

def calculaInss(salario):
    if salario <= 1100:
        descontoInss = salario - (salario * 0.075)
    elif salario <= 2203.48:
        descontoInss = salario - (salario * 0.09)
    elif salario <= 3305.22:
        descontoInss = salario - (salario * 0.12)
    elif salario <= 6433.57:
        descontoInss = salario - (salario * 0.14)
    else:
        descontoInss = salario - 854.36
    return descontoInss 

def calcularIrrf(salario, quantidade_de_dependentes):
    if salario >= 2259.21:
        descontoIrrf = salario - (salario * 0.075) + quantidade_de_dependentes
    elif salario >= 2826.66:
        descontoIrrf = salario - (salario * 0.15) + quantidade_de_dependentes
    elif salario >= 3751.06:
        descontoIrrf = salario - (salario * 0.225) + quantidade_de_dependentes
    elif salario > 4664.68:
        descontoIrrf = salario - (salario * 0.275) + quantidade_de_dependentes
    return descontoIrrf
    

    
cabecalho()
faixaSalarial = float(input("Digite seu salario: "))
desconto = calculaInss(faixaSalarial)

quantidade_filhos = int(input("Digite a quantidade de filhos do funcionário: "))
tem_esposa = input("O funcionário tem esposa? (S/N): ")
descontar = calcularIrrf(faixaSalarial)

# Converter a resposta para maiúsculas para facilitar a comparação
tem_esposa = tem_esposa.upper()

# Definir a quantidade de dependentes com base nos filhos e na esposa (se tiver)
quantidade_dependentes = quantidade_filhos
if tem_esposa == "S":
    quantidade_dependentes += 1


print(f"Salario: {faixaSalarial}")
print(f"Salario com desconto do INSS: {desconto}")