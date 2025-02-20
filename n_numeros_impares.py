#imprime os N primeiros números ímpares naturais

n = int(input('Digite o valor de n: '))

contador = 1
impar = 1

while (impar <= n):
    if (contador % 2 != 0):
        print(contador)
        impar += 1
    contador += 1

    