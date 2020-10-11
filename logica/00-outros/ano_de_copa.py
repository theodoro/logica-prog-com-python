anoDeCopa = 1930
limite = int(input('Informe até que ano deseja saber se terá copa: '))

if limite >= 1930:
    while anoDeCopa <= limite:
            anoDeCopa = anoDeCopa + 4
            print('Em %d tem Copa!' % anoDeCopa)

    print(f'Ufa! Esses foram os anos de copa do mundo até {anoDeCopa}' )
else:
    print('Não existia copa antes de %d' % anoDeCopa)