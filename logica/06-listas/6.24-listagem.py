L=[8,9,15]

#FOR
#Utilizamos quando quisermos processar os elementos de uma lista, um a um
for e in L:
    print(e)

#MESMA COISA, MAS COM WHILE
# Indicado para repetições nas quais não sabemos ainda quantas vezes vamos
# repetir ou onde manipulamos os indices de forma não sequencial
x = 0
while x < len(L):
    e = L[x]
    print(e)
    x+=1