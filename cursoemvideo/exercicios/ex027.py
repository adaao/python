"""
027 - Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = input('Nome: ').strip().split()

print('primeiro nome: {}'.format(nome[0]))
print('ultimo nome: {}'.format(nome[-1]))
