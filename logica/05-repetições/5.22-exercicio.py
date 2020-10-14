tabuada = 1

opcao = int(input('Escola uma das opções 1-SOMA 2-SUB 3-MULT 4-DIV 0-SAIR: '))
while tabuada <= 10:
    numero = 1

    if opcao == 0:
        break
    elif opcao == 1:
        while numero <= 10:
            print('%d + %d = %d' % (tabuada, numero, tabuada + numero))
            numero = numero + 1
        tabuada += 1
    elif opcao == 2:
        while numero <= 10:
            print('%d - %d = %d' % (tabuada, numero, tabuada - numero))
            numero = numero + 1
        tabuada += 1
    elif opcao == 3:
        while numero <= 10:
            print('%d * %d = %d' % (tabuada, numero, tabuada * numero))
            numero = numero + 1
        tabuada += 1
    elif opcao == 4:
        while numero <= 10:
            print('%d / %d = %d' % (tabuada, numero, tabuada / numero))
            numero = numero + 1
        tabuada += 1
