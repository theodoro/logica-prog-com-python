salario = float(input('Informe seu Salário: '))

if salario > 1250:
    salario = salario + ((salario * 10)/100)
elif salario <= 1250:
     salario = salario + ((salario * 15)/100)

print('Seu novo salário %10.2f' % salario)