# Função calcula o maior número primo 
import math
def maior_primo(n):
    i = 0
    marcador = False
    if n < 2:
        return marcador
    while(n > 1):
        i = int(math.sqrt(n))
        while (i >= 2):
            if(n % i == 0):
                marcador = False
                break
            else:
                marcador = True
            i = i - 1
        if marcador == True:
            return n
        n -= 1
    
print(maior_primo(6))
