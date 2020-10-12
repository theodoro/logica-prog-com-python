soma = 0
qde = 0
media = 0

while True:
    valor = int(input('Informe um numero para somar ou 0 para sair: '))
    if valor == 0:
        break
    soma = soma + valor
    qde = qde + 1
    media = soma / qde

print('Quantidade: %d | Soma: %d | Média: %5.2f' % (qde, soma, media))