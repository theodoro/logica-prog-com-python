nota = int(input('Informe a nota do primeiro semestre :'))
nota2 = int(input('Informe a nota do segundo semestre :'))

def media(n1:int, n2:int) -> int:
    return (n1 + n2) / 2
if media(nota,nota2) >= 7:
    print('Aprovado!')
else:
    print('Reprovado')
