categoria = int(input('Digite a categoria do produto: '))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print('Categoria inválida, digite um valor 1 a 5')
    preco = 0

print('O preço do produto é: R$%6.2f' % preco)