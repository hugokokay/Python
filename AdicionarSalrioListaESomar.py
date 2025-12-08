salarios=[]
resp='sim'
while resp =='sim':
    salarios.append(float(input('Digite o salário: ')))
    resp=input('Deseja adicionar outro laário? (sim/não)')
somasalarios=sum(salarios)
print('A soma dos salários é: R$ {:.2f}' .format (somasalarios))
