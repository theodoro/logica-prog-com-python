L1 = []

L2 = []

L3 = []

while True:
    n = int(input('Informe um Numero ou ZERO(0) para sair'))
    if n == 0:
        break
    elif n % 2 == 0:
        L1.append(n)
    else:
        L2.append(n)

print('Lista 1:')
print(L1)
L1.extend(L2)
L3 = L1[:]


print('Lista 2:')
print((L2))
print('Lista 3:')
print(L3)