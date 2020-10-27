L = [5, 8, 13]
x = 0

for e in L:
    print('[%d] %d' % (x,e))
    x+=1

L = [6, 9, 14]

for x, e in enumerate(L):
    print('[%d] %d' % (x,e))