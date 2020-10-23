# Listagem 6.22 - Pilha de Pratos

prato = 5
pilha = list(range(1,prato+1))

while True:
    print('\nExistem %d pratos na pilha' % len(pilha))
    print('Pilha atual:', pilha)
    print('Digite E para empilhar um novo prato,')
    print('ou D para desempilhar. S para sair.')
    operacao = input('Operação (E, D ou S):')

    if operacao == 'D':
        if(len(pilha)) > 0:
            lavado = pilha.pop(-1)
            print('Prato %d lavado' % lavado)
        else:
            print('Pilha vazada! Nada para lavar.')
    elif operacao == 'E':
        prato+=1 #Novo prato
        pilha.append(prato)
    elif operacao == 'S':
        break
    else:
        print('Operação inválida! Digite apenas E, D ou S!')
