"""
023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
dígitos separados.
Ex.:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

import math


def sem_recursividade():

    #inpt = input('Digite um número de 0 a 9999: ')

    #num = inpt.strip()

    num = recebe_valor()

    if int(num) < 0 or int(num) > 9999:
        print('valor inválido')
    else:
        for i in num:
            print(i)

    print('fazendo da forma matemática: ')

    milhar = int(num) / 1000
    num = int(num) % 1000
    centena = int(num) / 100
    num = int(num) % 100
    dezena = int(num) / 10
    num = int(num) % 10
    unidade = int(num) / 1

    print('milhar:  {}'.format(math.floor(milhar)))
    print('centena: {}'.format(math.floor(centena)))
    print('dezena:  {}'.format(math.floor(dezena)))
    print('unidade: {}'.format(math.floor(unidade)))


def recebe_valor():
    inpt = ''
    while inpt.__eq__('') or int(inpt) < 0 or int(inpt) > 9999:
        inpt = input('Digite um valor maior que 0 e menor que 9999: ').strip()

        if inpt.__eq__('') or int(inpt) < 0 or   int(inpt) > 9999:
            print('Valor inválido....\n')

    return inpt


def faz_a_magica(num):
    if num > 999:
        print('Milhar: {}'.format(int(num / 1000)))
        faz_a_magica(num % 1000)
    elif num > 99:
        print('centena: {}'.format(int(num / 100)))
        faz_a_magica(num % 100)
    elif num > 10:
        print('Dezena: {}'.format(int(num / 10)))
        faz_a_magica(int(num % 10))
    else:
        print('Unidade: {}'.format(num))


def main():
    faz_a_magica(int(recebe_valor()))


main()
sem_recursividade()


