preco = float(input('Preço :'))
desconto = float(input('Desconto :'))

valor = preco - ((preco * desconto)/100)

print(f'Preço: {preco} - Desconto: {desconto} - Valor: {valor}')