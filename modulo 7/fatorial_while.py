while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    resultado = 1
    while num > 1:
        resultado = resultado * num
        num -= 1
    print(resultado)

        
