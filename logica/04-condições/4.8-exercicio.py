num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
opcao = int(input('Escolha uma opção: (1: Somar 2: Subtrair 3: Dividir 4: Multiplicar) '))

if opcao == 1:
    calc = num1 + num2
elif opcao == 2:
    calc = num1 - num2
elif opcao == 3:
    calc = num1 / num2
elif opcao == 4:
    calc = num1 * num2
else:
    print('Opção Inválida!!')
    calc = 0
print(f'Opção escolhida {opcao} e o Resultado: {calc}')