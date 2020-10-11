anoInicial = int(input('Informe o ano inicial: '))
anoLimite = int(input('Informe o ano limite: '))

if anoInicial >= 1896:
    while anoInicial <= anoLimite:
        anoInicial = anoInicial + 4
        print('Em %d tem olimpiadas' % anoInicial)
    print('Ufa! Essas são as Olimpiadas ate %d' % anoInicial)
else:
    print('VocÊ informou %d e a primeira olimpiadas foi apenas em 1986' % anoInicial)