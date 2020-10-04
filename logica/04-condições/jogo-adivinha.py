from random import randrange, uniform

numero = randrange(0 , 100)

chute = int(input('Já pensei em numero, qual eu pensei? '))

if chute == numero:
    print('Uau eu pensei em %d VOCÊ ACERTOU!' % chute)
elif chute != numero and chute > numero:
    print('O numero que você pensou %d é MAIOR que o meu %d' % (chute,numero))
elif chute != numero and chute < numero:
    print('O numero que você pensou %d é MENOR que o meu %d' % (chute, numero))