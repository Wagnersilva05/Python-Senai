produto = float(input("Digite o valor do produto"))
pagamento = str(input("Digite a forma de pagamento")).strip()

if(pagamento == 'dinheiro' or pagamento == 'cheque'):
    desconto = produto - 0.10
    print(f"O pagamento foi a vista, o valor com 10% de desconto será {desconto}")
elif(pagamento == 'cartao'):
    desconto = produto - 0.5
    print("O pagamento foi no cartao ")   