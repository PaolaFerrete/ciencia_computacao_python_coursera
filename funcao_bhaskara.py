#reorganiza o cálculo de bhaskara em funções
import math

def imprime_raiz(a, b, c):
    d = delta(a, b, c)
    if (d == 0):
        raiz1 =  (- b + math.sqrt(d)) / (2 * a)
        print('a raiz dupla desta equação é', raiz1)
    else:
        if (d < 0):
            print('esta equação não possui raízes reais')
        else:
            raiz1 =  (- b + math.sqrt(d)) / (2 * a)
            raiz2 = (- b - math.sqrt(d)) / (2 * a)
            if (raiz1 < raiz2):
                print('as raízes da equação são', raiz1, 'e', raiz2)
            else:
                print('as raízes da equação são', raiz2, 'e', raiz1)
    
def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raiz(a, b, c)


main()
main()