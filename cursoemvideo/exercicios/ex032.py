"""
ex032 - Faça um programa que leia um ano qualquer e
mostre se ele é bisexto.
"""


def recebe_ano():
    return int(input('Digite o ano a ser verificado se é bisexto: '.strip()))


def is_multiplo_de_4(ano):
    return ano % 4 == 0


def is_multiplo_de_400(ano):
    return ano % 400 == 0

def is_multiplo_de_100(ano):
    return ano % 100 == 0


def is_ano_bisexto(ano):
    resp = False
    if is_multiplo_de_4(ano) and not is_multiplo_de_100(ano) or is_multiplo_de_400(ano):
        resp = True

    return resp


def main():
    ano = recebe_ano()
    print('Este ano é bisexto' if is_ano_bisexto(ano) else 'Este ano não é bisexto')


main()
