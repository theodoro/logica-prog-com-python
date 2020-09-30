limite = 80
velocidade = int(input('Informe a velocidade do carro: '))

if velocidade > 80:
    print(f'Multado!!! \n Velocidade: {velocidade} \n Excedente: {velocidade-limite} \n Valor da Multa: {(velocidade-limite) * 5}' )
else:
    print('Siga viagem!')