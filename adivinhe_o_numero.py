import random

def jogador(x):
    numero_randomico = random.randint(1, x)
    palpite = 0

    print(f'Vamos lá! Adivinhe o número que escolhi. Uma dica: é um número entre 1 e {x}.')

    while palpite != numero_randomico:
        palpite = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if palpite < numero_randomico:
            print('Muito baixo. Tente novamente.')
        elif palpite > numero_randomico:
            print('Muito alto. Tente novamente')

    print(f'Parabéns! Você adivinhou o número {numero_randomico} !!')

def maquina(x):
    baixo = 1
    alto = x
    verificacao = ''

    print(f'Aceito o desafio! Vou adivinhar o número entre {baixo} e {alto} que você pensou.')

    while verificacao != 'c':
        if baixo != alto:
            palpite = random.randint(baixo, alto)
        else:
            palpite = baixo  # could also be high b/c low = high
        verificacao = input(f'O valor {palpite} é muito alto (A), muito baixo (B) ou correto (C)?? ').lower()
        if verificacao == 'a':
            alto = palpite - 1
        elif verificacao == 'b':
            baixo = palpite + 1

    print(f'Uhull! Acertei que o número escolhido é {palpite}.')


#jogador(10)
#maquina(10)