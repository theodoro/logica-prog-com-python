valor_imovel = float(input('Informe o valor do imovel: '))
salario = float(input('Informe o salário'))
anos = int(input('Informe quantos anos de financiamento'))

max_parcela = salario * 0.30
parcela = valor_imovel / anos

if parcela <= max_parcela:
    print('Aprovado')
else:
    print('Reprovado, pois a parcela é maior que 30% do salario - Parcela: R$%6.2f - Salário: R$%6.2f' % (parcela,salario))