soma = 0

while True:
    valor = int(input('Opções 1,2,3,5 e 9 para somar e 0 sair: '))
    if valor == 0:
        break
    elif valor == 1:
        soma = soma + 0.50
    elif valor == 2:
        soma = soma + 1
    elif valor == 3:
        soma = soma + 4
    elif valor == 5:
        soma = soma + 7
    elif valor == 9:
        soma = soma + 8
    else:
        print('Código %d Inválido!' % valor)
print('Total de compras: %5.2f' % soma)
