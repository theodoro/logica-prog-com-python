soma = 0

while True: #While executará para sempre enquanto não for digitado ZERO
    v = int(input('Digite um numero a somar ou 0 para sair: '))
    if v == 0:
        break
    soma = soma + v
print(soma)