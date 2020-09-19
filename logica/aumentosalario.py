#Calculo de aumento de salário

salario = float(input('Informe seu Salário :'))
aumento = int(input('Informe o percentual de aumento :'))

def calc(s:float, a:int) -> float:
    perc = s + ((s * a)/100)
    return perc
print(calc(salario,aumento))
