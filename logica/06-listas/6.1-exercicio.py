notas = [0,0,0,0,0,0,0]

x = 0
soma = 0

while x < 7:
    notas[x] = float(input('Nota %d:' % x))
    soma += notas[x]
    x+=1
x = 0
while x < 7:
    print('Nota %d: %6.2f' % (x, notas[x]))
    x+=1
print('Média: %5.2f' % (soma/7))
