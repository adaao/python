"""
ex028 - escreva um programa que faça o computador
pensar em um número inteiro entre 0 e 5 e peça para o usuário
terntar descobrir qual foi o número escolhido pelo computador.

o progrma deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint


def pensa_em_um_numero():
    return randint(0, 5)


def diz_se_acertou(b, i):
    print('Parabéns, vou venceu. Você acertou o número que eu pensei' if b else
          'Você perdeu, o número em que eu estava pensando é {}. Você errou!'.format(i))


def verifica_se_o_numero_e_igual(x, y):
    return x == y


def recebe_um_numero_do_usuario():
    print('Vou pensar em um número...')
    print('Pronto! Você consegue adivinhar em que número estou pensando?')
    print('Digite o número que eu te falou se você acertou')
    return int(input())


def main():
    entrada = recebe_um_numero_do_usuario()
    i = pensa_em_um_numero()

    diz_se_acertou(
        verifica_se_o_numero_e_igual(entrada, i), i
    )


main()
