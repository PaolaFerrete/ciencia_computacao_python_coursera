#verifica a distância entre dois pontos
import math
ponto_x_um = int(input('Digite o ponto x: '))
ponto_y_um = int(input('Digite o ponto y: '))
ponto_x_dois = int(input('Digite o ponto x: '))
ponto_y_dois = int(input('Digite o ponto y: '))

distancia = math.sqrt((ponto_x_um - ponto_x_dois) ** 2 + (ponto_y_um - ponto_y_dois) ** 2)

if (distancia >= 10):
    print('longe')
else:
    print('perto')