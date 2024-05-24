import os

def cabecalho():
    os.system('cls || clear')
    print("--------------------")
    print("=== SENAI | FIEB ===")
    print("--------------------")

def calcula_inss(salario):
    if salario <= 1100:
        desconto_inss = salario - (salario * 0.075)
    elif salario <= 2203.48:
        desconto_inss = salario - (salario * 0.09)
    elif salario <= 3305.22:
        desconto_inss = salario - (salario * 0.12)
    elif salario <= 6433.57:
        desconto_inss = salario - (salario * 0.14)
    else:
        desconto_inss = salario - 854.36
    return desconto_inss

def calcular_irrf(salario, quantidade_de_dependentes):
    if salario >= 2259.21:
        desconto_irrf = salario - (salario * 0.075) + (quantidade_de_dependentes * 189.59)
    elif salario >= 2826.66:
        desconto_irrf = salario - (salario * 0.15) + (quantidade_de_dependentes * 189.59)
    elif salario >= 3751.06:
        desconto_irrf = salario - (salario * 0.225) + (quantidade_de_dependentes * 189.59)
    elif salario > 4664.68:
        desconto_irrf = salario - (salario * 0.275) + (quantidade_de_dependentes * 189.59)
    else:
        desconto_irrf = 0    
    return desconto_irrf

cabecalho()
faixa_salarial = float(input("Digite seu salário: "))
desconto_inss = calcula_inss(faixa_salarial)

quantidade_filhos = int(input("Digite a quantidade de filhos do funcionário: "))
tem_esposa = input("O funcionário tem esposa? (S/N): ").upper()

# Definir a quantidade de dependentes com base nos filhos e na esposa (se tiver)
quantidade_dependentes = quantidade_filhos
if tem_esposa == "S":
    quantidade_dependentes += 1

desconto_irrf = calcular_irrf(faixa_salarial, quantidade_dependentes)

print(f"Salário: R${faixa_salarial:.2f}")
print(f"Salário com desconto do INSS: R${desconto_inss:.2f}")
print(f"Salário com desconto do IRRF: R${desconto_irrf:.2f}")