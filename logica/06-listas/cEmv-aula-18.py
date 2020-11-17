pessoa = [['Sumara',36],['Bruno',34]]

print(pessoa[0][0])

teste = list()
teste.append(34)
teste.append('Bruno')

galera = list()
galera.append(teste[:])
teste[0] = 'Sumara'
teste[1] = 36

galera.append(teste[:])
print(galera)


galera2 = [['João',19], ['Ana', 33], ['Joaquim', 14], ['Pietra', 1]]
print(galera2)
print(galera2[0])
print(galera2[0][0])
print(galera2[0][1])

for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera3 = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

print(galera3)

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')