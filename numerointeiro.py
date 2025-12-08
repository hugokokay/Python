from math import trunc
num=float(input('Digite um número: '))
print('O número digitado foi {} e sua parcela inteira é {} ' .format(num,(trunc(num))))
print('Outra forma de fazer sem importar biblioteca:')
print('O número digitado foi {} e sua parcela inteira é {} ' .format(num,int(num)))

