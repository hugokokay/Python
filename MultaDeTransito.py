velocidade=float(input('Digite a velocidade do carro em km/h: '))
if velocidade <= 80:
    print('Não ouve multa, dirija com segurança!')
elif velocidade > 80 and velocidade <=90:
    print('Multa leve!')
elif velocidade > 90 and velocidade <=100:
    print('Multa grave!')
else: 
    print('Multa gravissima!')  
