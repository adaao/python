'''
18 - Faça um programa que leia um ângule qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''

import math

angulo = math.radians(float(input('Digite o valor do ângulo: ')))

sen = round(math.sin(angulo), 3)
cos = round(math.cos(angulo), 3)
tan = round(math.tan(angulo), 3)

print('seno = {}\n'
      'cosseno = {}\n'
      'tangente = {}\n'
      ''.format(sen, cos, tan))

