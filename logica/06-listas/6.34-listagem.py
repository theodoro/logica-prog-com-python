V=[9,8,7,12,0,13,21]

p=[]

I=[]

for e in V:
    if e % 2 == 0:
        p.append(e)
    else:
        I.append(e)

print('Pares:', p)
print('Impares:', I)