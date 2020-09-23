dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

soma = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f'Total em segundos {soma}')