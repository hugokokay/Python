usuario=''
senha=''
tentativas=0
while (usuario !='hugo' or senha!= 'senha123') and tentativas < 3:
    usuario=input('Digite o usuário: ')
    senha=input('Digite a senha: ')
    tentativas+=1
    print(tentativas)
    if (usuario != 'hugo' or senha != 'senha123'):
        print('Usuario ou senha incorretos, tente novamente!')
        if tentativas ==3:
            print('Número máximo de tentativas atingido. Acesso bloqueado.Tente após 30 minutos')
    else:
        print('Login realizado com sucesso!')
    

