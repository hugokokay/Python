import random
numer=int(input('Digite um numero de 1 a 10: '))
aleatorio=int(random.randint(1,10))
for iten in range (1,5):
    if numer==aleatorio:
        print('Parabens, você acertou!')
    else:
        if numer>aleatorio:
            print('O numero {} é maior' .format(numer))
            numer=int(input('Tente novamente: '))

        else:
            print('O numero {} é menor' .format(numer))
            numer=int(input('Tente novamente: '))
print('O numero aleatorio era {}' .format(aleatorio))

