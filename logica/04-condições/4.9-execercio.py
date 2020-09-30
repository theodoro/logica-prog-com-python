valor_imovel = float(input('Informe o valor da Imovél: '))
salario = float(input('Informe o valor d seu salário :'))

meses = int(input('Quantos meses pretente financiar o imovél: '))

max_prestacao = salario * 0.30
prestacao = valor_imovel / meses

if (prestacao <= max_prestacao):
    print('Financeamento aprovado!! Valor da Prestação: R$%6.2f em x %d' % (prestacao, meses))
else:
    print(f'Financeamento reprovado, pois a prestação {prestacao} ultrapassa 30% do salário, equivalente a R${max_prestacao}')