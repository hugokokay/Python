from math import hypot
co=float(input('Digite o cateto opsto do triângulo: '))
ca=float(input('Digite o cateto adjsasente do triângulo: '))
hipotenusa=(co**2+ca**2) **(1/2)  
print('A hipotenusa vai medir {:.2f}' .format(hipotenusa)) 
print(' Outro modo de fazer usando a biblioteca math: ')
hipo=hypot(co,ca)
print('A hipotenusa usando a biblioteca math é {:.2f}' .format(hipo))
