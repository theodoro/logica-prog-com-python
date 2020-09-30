n1 = int(input('Informe um Num: '))
n2 = int(input('Informe um Num: '))
n3 = int(input('Informe um Num: '))

if n1 > n2 and n1 > n3:
    print('N1 > N2 e N3')
if n2 > n1 and n2 > n3:
    print('N2 > N1 e N3') 
if n3 > n1 and n3 > n2:
    print('N3 > N1 e N2')
else:
    print('Iguais')