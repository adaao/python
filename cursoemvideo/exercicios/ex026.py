"""
026 - Faça um programa que leia uma frase pelo
teclado e mostre:

Quatas vezes aparece a letra "A";

Em que posição ela aparece a primeira vez;

Em que posição ela aparece a última vez.
"""

inpt = input('Digite uma frase:  ').strip()

print('O caractere \"A\" apareceu {} vezes'.format(inpt.count('A')))
if 'A' in inpt:
    print('A primeira posição em que aparece é {}'.format(inpt.find('A')))
    print('A última posição em que aparece é {}'.format(inpt.rfind('A'))) #lê a partir da direita
