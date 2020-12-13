import random

def jogar():
    jogador = input("Eu já escolhi. O que você escolhe? 'p' para pedra, 'a' para papel, 't' para tessoura\n").lower()
    maquina = random.choice(['p', 'a', 't'])

    if jogador == maquina:
        return 'Empatou!'

    # r > s, s > p, p > r
    if vitoria(jogador, maquina):
        return f'Escolhi {maquina}. Você ganhou! :/'

    return f'Escolhi {maquina}. Você perdeu! :D'

def vitoria(jogador, oponente):
    # returna true se jogador vencer
    # p > t, t > a, a > p
    if (jogador == 'p' and oponente == 't') or (jogador == 't' and oponente == 'a') or (jogador == 'a' and oponente == 'p'):
        return True

print(jogar())