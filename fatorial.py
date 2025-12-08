fat=1
num=int(input('Digite o numero que deseja calcular o fatorial: '))
for item in range (1,num+1):
    fat=fat*item
print('O fatorial de {} é {}' .format (num,fat))
