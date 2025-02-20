#verifica se o número é divisível por 3 e 5, se sim imprime fizzbuzz
num = int(input('Digite um número inteiro: '))
if (num % 3 == 0 and num % 5 == 0):
    print('FizzBuzz')
else:
    print(num)