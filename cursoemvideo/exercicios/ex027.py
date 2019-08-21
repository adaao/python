"""
027 - Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = input('Nome: ')

splitedNome = nome.split()

print('primeiro nome: {}'.format(splitedNome[0]))
print('ultimo nome: {}'.format(splitedNome[-1]))
