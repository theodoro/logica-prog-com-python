x = 0
soma = 0

deposito = float(input('Informe o valor do deposito inicial: '))
juros = float(input('Taxa de Juros: '))

while x <= 23:
    saldo = deposito + ((deposito * juros)/100)
    soma = soma + saldo
    x = x + 1
    print('%d - Parcela  - Saldo: %5.2f mês' % (x, soma))

print('Saldo final: %5.2f' % soma)

