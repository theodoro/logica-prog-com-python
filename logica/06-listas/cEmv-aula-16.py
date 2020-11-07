num = [2, 5, 9, 1, 2]
num[2] = 3

num.append(7)
num.sort() #ordena a lista
#num.pop(2) # Elimina elemento da lista
num.remove(2)

if 4 in num:
    num.remove(4)
else:
    print('Elemento não encontrado')

print(num)
print(f'Está lista tem {len(num)} elementos')