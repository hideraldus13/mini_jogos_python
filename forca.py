
import random
from palavras_forca import palavras
import string


def palavra_valida(palavras):
    palavra = random.choice(palavras)  
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()


def forca(qtd_vidas):
    palavra = palavra_valida(palavras)
    palavra_letras = set(palavra)  
    alfabeto = set(string.ascii_uppercase)
    letras_utilizadas = set()  

    vidas = qtd_vidas

    while len(palavra_letras) > 0 and vidas > 0:
        print('Você tem', vidas, 'vidas restantes e você já utilizou estas letras: ', ' '.join(letras_utilizadas))

        # what current palavra is (ie W - R D)
        palavra_list = [letra if letra in letras_utilizadas else '-' for letra in palavra]
        print('A palavra é: ', ' '.join(palavra_list))

        letra_escolhida = input('Escolha uma letra: ').upper()
        if letra_escolhida in alfabeto - letras_utilizadas:
            letras_utilizadas.add(letra_escolhida)
            if letra_escolhida in palavra_letras:
                palavra_letras.remove(letra_escolhida)
                print('')

            else:
                vidas = vidas - 1  # takes away a life if wrong
                print('\nA letra,', letra_escolhida, 'não está presente na palavra.')

        elif letra_escolhida in letras_utilizadas:
            print('\nVocê já utilizou esta letra. Tente outra.')

        else:
            print('\nEsta não é uma letra válida.')

    # gets here when len(palavra_letras) == 0 OR when vidas == 0
    if vidas == 0:
        print('Você perder! A palavra era ', palavra)
    else:
        print('Parabéns! Você acertou a palavra', palavra, '!!')


if __name__ == '__main__':
    forca(7)