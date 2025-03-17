largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
l = a = 0
flag = False

while a < altura:
    if a == 0 or a == altura - 1:
        while l < largura:
            print('#', end = '')
            l += 1
    else:
        while l < largura:
            if l == 0 or l == largura - 1:
                print('#', end = '')
            else:
                print(' ', end = '')
            l += 1
    print('')
    a += 1
    l = 0