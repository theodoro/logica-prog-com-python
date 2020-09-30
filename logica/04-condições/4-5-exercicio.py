idade = int(input('Informe o Ano do veiculo :'))

def calc (idade):
    calc = 2020 - idade
    return  calc

if idade != '':
    calc(idade)
    if calc(idade) > 2:
        print('Carro Semi Novo')
    else:
        print('Carro velho')
else:
    print('Informe o ano do carro')