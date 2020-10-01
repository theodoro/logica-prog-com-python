ponto = 0
questao = 1

while questao <= 3:
    resposta = input('A resposta da questão %d: ' % questao)
    if questao == 1 and (resposta == 'B' or resposta == 'b'):
        ponto = ponto + 1
    elif questao == 2 and (resposta == 'A' or resposta == 'a'):
        ponto = ponto + 1
    elif questao == 3 and (resposta == 'D' or resposta == 'd'):
        ponto = ponto + 1
    questao += 1
print('O aluno fez %d pontos' % ponto)