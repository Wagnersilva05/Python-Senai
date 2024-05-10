valorA = int(input("Digite um numero: "))
valorB = int(input("Digite mais um numero: "))

opcao = str(input("Escolha uma opção: "))

match(opcao):
    case '+':
        resultado = valorA + valorB
    case '-':
        resultado = valorA - valorB
    case '*':
        resultado = valorA * valorB
    case '/':
        resultado = valorA / valorB
    case _ :
        print("Opção inválida")

print(f"Resultado: {resultado}")