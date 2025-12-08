valor=float(input('Digite o valor do produto:'))
desconto=valor*5/100
valordesconto=valor-desconto
print('O valor do produto {} com 5% de desconto é {:.2f}' .format(valor, valordesconto))