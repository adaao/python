'''
17 - Faça um program que leia o comprimento do cateto oposte e do cateto
adjacente de um tieângulo, calcule e mostre o comprimento da hipotenusa.
'''
import math

c1 = float(input('Digite o valor de um dos catetos: '))

c2 = float(input('Digite o valor do outro cateto: '))

def calcula_hipotenusa(c1, c2):
    h = (c1 ** 2) + (c2 ** 2)
    return math.sqrt(h)


print('O valor da hipotenusa é {}'.format(calcula_hipotenusa(c1, c2)))
