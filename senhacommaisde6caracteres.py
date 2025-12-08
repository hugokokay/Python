'''
senha=str(input('Digita uma senha: '))
if len(senha)>6:
    print('Senha cadastrada com sucesso:')
else:
    print('A senha tem que ter mais de 6 caracteres!')
'''

senhas = ['123', 'bolo', 'cadeira', '45.67', 'senha123']
for senha in senhas:
    if len(senha) > 6 :
        print('A senha {} é válida' .format (senha))
    else:
        print('A senha {} é invalida' .format (senha))
