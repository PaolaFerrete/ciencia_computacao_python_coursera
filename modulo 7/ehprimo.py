def ehprimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x / 2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input('Digite um número inteiro: '))
while n > 0:
    if ehprimo(n):
        print(n, 'é primo!')
    else:
        print(n, 'não é primo')
    n = int(input('Digite um número inteiro: '))