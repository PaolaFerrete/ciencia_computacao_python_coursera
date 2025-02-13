#efetua a soma dos algarismos digitados pelo usuário

n = int(input('Digite um número inteiro: '))

resultado = 0
parcial = n
soma = 0

while (parcial != 0):
    resultado = parcial % 10
    soma += resultado
    parcial = parcial // 10
print(soma)

