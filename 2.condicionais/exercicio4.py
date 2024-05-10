nomeProduto = str(input("Nome do produto: ")).strip()
quantidadeProduto = int(input("Digite a quantidade do produto: "))
precoProduto = float(input("Digite o preço do produto: "))

precoUnitario = quantidadeProduto * precoProduto

if(quantidadeProduto <= 5 ):
    desconto = 2
    valorTotal = precoUnitario - (precoUnitario * 2 / 100)
if (quantidadeProduto > 5 and quantidadeProduto <= 10,):
    desconto = 3
    valorTotal = precoUnitario - (precoUnitario * 3 / 100)
if (quantidadeProduto > 10):
    desconto = 5
    valorTotal = precoUnitario - (precoUnitario * 5 / 100)


print(f"Nome do produto: {nomeProduto}")
print(f"Preço unitario: {precoUnitario}")
print(f"Valor com {desconto}% de desconto: {valorTotal}")