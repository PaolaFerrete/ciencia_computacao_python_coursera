num_um = int(input('Digite um número inteiro: '))
num_dois = int(input('Digite um número inteiro: '))
num_tres = int(input('Digite um número inteiro: '))

if (num_um < num_dois and num_dois < num_tres):
    print('crescente')
else:
    print('não está na ordem crescente')