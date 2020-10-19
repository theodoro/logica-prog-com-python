numero = [0,0,0,0,0]

x = 0

while x < 5:
    numero[x] = int(input("Numero d%" % (x+1)))
    x+=1
while True:
    escolhido = int(input('Que numero você quer imprimir? (0 para sair): '))
    if escolhido == 0:
        break
    print('Você escolhe o numero: %d' % (numero[escolhido-1]))