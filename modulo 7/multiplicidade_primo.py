n = int(input('Digite um número maior que 1: '))
fator = 2
multiplicidade = 0

while (n > 1):
    while(n % fator == 0):
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print('fator: ', fator, 'multiplicidade: ', multiplicidade)
    multiplicidade = 0
    fator += 1
    