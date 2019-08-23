"""
025 - Crie um programa que leia o nome de uma pessoa e
diga se ela tem "Silva" no nome.
"""

nome = input('nome da pessoa: ')

if 'silva' in nome.lower():
    print('O nome tem \"Silva\"')
else:
    print('O nome não tem \"Silva\"')

