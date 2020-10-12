valor = int(input('Digite o valor a pagar: '))
celulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        celulas +=1
    else:
        print('%d células(s) de R$%d' % (celulas, atual))
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 1
        celulas = 0