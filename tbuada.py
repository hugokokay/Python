numero=input('Digite o numero que desaja a tabuada: ')
print('-'*12)
for c in range (1,11):
    resultado=int(numero)*c
    print('{} x {:2} = {}' .format(numero,c,resultado))
print('-'*12)