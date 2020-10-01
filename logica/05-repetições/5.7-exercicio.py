n = int(input('Tabuada : '))

inicio = int(input('Inicio :'))
fim = int(input('Fim: '))

while inicio <= fim:
    print(f'{n} x {inicio} = {n * inicio}')

    inicio = inicio + 1