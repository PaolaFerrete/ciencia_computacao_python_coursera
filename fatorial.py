#calcula o fatorial de um número e imprime

n = int(input('Digite o valor de n: '))

contador = resultado = 1

while (contador <= n):
    resultado = resultado * contador
    contador += 1
print(resultado)