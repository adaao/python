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

inpt = input('Digite um número de 0 a 9999: ')

num = inpt.strip()

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
