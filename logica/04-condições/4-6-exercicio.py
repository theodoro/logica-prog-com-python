km = int(input('Informe a distancia do trajeto: '))
preco = 0

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45

print('Passagem custou: %10.2f' % preco)