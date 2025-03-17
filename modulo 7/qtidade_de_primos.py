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


def n_primos(n):
    count = 2
    primo = 0
    while n >= count:
        if ehprimo(count):
            primo += 1
        count += 1
    return primo

print(n_primos(11))