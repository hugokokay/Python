participantes=[]
while True:
    print('Cadastro - 1')
    print('Lista - 2')
    print('Atualiza - 3')
    print('Remove - 4')
    print('Sai -5')
    op=int(input('Escolha uma opção! '))
    
    if op == 1:
        participante=input('Digite um nome: ')
        participantes.append(participante)
    
    elif op == 2:
        if len(participantes) > 0:
            for indice,participante in enumerate(participantes):
                print(f'{indice} - {participante}')
            #for i in range (len(participantes)):
                #print(f'{i} {participantes[i]}')
        else:
            print('Sem participantes cadastrados')
    elif op == 3:
        indice=int(input('Qual a posição quer atualizar? '))
        participante_atualizado=input('Digite o novo nome: ')
        participantes[indice]=participante_atualizado
        print('Atualização realizado com sucesso!')
        
    elif op == 4:
        indice=int(input('Qual a posição quer deletar? '))
        
        print(f'Participante {participantes[indice]} removido!!')
        participantes.pop(indice)
        
    elif op == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida!!')