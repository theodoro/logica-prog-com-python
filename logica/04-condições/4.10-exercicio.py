kwh = int(input('Informe a quantidade de KWh consumido: '))
tipo = input('Infome o tipo (R - Residêncial) - (I - Industrial) - (C - Comercial): ')

if tipo.upper() == 'R' and kwh <= 500:
    calc = kwh * 0.40
    print('Quantidade de KWh: %d Valor a Pagar: R$%6.2f' % (kwh, calc))
elif tipo.upper() == 'R' and kwh >500:
    calc = kwh * 0.65
    print('Quantidade de KWh: %d Valor a Pagar: R$%6.2f' % (kwh, calc))
elif tipo.upper() == 'C' and kwh <= 1000:
    calc = kwh * 0.55
    print('Quantidade de KWh: %d Valor a Pagar: R$%6.2f' % (kwh, calc))
elif tipo.upper() == 'C' and kwh > 1000:
    calc = kwh * 0.60
    print('Quantidade de KWh: %d Valor a Pagar: R$%6.2f' % (kwh, calc))
elif tipo.upper() == 'I' and kwh <= 5000:
    calc = kwh * 0.55
    print('Quantidade de KWh: %d Valor a Pagar: R$%6.2f' % (kwh, calc))
elif tipo.upper() == 'I' and kwh > 5000:
    calc = kwh * 0.60
    print('Quantidade de KWh: %d Valor a Pagar: R$%6.2f' % (kwh, calc))
else:
    print('Opção %s Invalida' % tipo)