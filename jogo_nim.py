def computador_escolhe_jogada(n, m):
    print('\n')
    count = 0
    while (n % (m + 1) != 0) and count < m and n > 0:
        n = n - 1
        count += 1
    if n == 0:
        print('O computador tirou', count, 'peça.')
        return n
    elif count == 0:
        count = n
        n = 0
        print('O computador tirou', count, 'peça.')
        return n
    print('O computador tirou', count, 'peça.')
    print('Agora resta apenas', n, 'peças no tabuleiro')
    return n
   

def usuario_escolhe_jogada(n, m):
    print('\n')
    num_jogada = int(input('Quantas peças você vai tirar? '))
    if num_jogada <= n and num_jogada <= m:
        n = n - num_jogada
        print('Você tirou', num_jogada, 'peças')
        if n != 0:
            print('Agora resta apenas', n, 'peças no tabuleiro')
        return n
    else: 
        print('\n')
        print('Oops! Jogada inválida! Tente de novo.')
        n = usuario_escolhe_jogada(n, m)
        return n

def partida():
    while True:
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
        if n > 0 and n >= m:
            break
    flag = True
    print('\n')
    if (n % (m + 1) == 0):
        print('Você começa!')
        n = usuario_escolhe_jogada(n, m)
        flag = False
    else: 
        print('Computador começa!')
        n = computador_escolhe_jogada(n, m)
        flag = True
    while (n > 0):
        if flag == True:
            flag = False
            n = usuario_escolhe_jogada(n, m)
        else:
            flag = True
            n = computador_escolhe_jogada(n, m)    
    if flag == True:
        print('Fim de jogo! O computador ganhou!')
    else:
        print('Fim de Jogo! Você ganhou!')


def print_rodada(num):
    print('\n')
    print('**** Rodada', num, '****')
    print('\n')
    return 

def campeonato():
    count = 1
    while count <= 3:
        print_rodada(count)
        partida()
        count += 1
    return

def inicio():
    print('\n')
    print('Bem-vindo ao jogo do NIM! Escolha: \n')
    count = 1
    jogo = int(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato '))
    if jogo == 1:
        print('\n')
        print('Voce escolheu uma partida!')
        print_rodada(count)
        partida()
    else:
        print('\n')
        print('Voce escolheu um campeonato!')
        campeonato()
        print('\n')
        print('**** Final do campeonato! ****')
        print('\n')
        print('Placar: Você 0 x 3 Computador')

inicio()

