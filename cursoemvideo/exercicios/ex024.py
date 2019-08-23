"""
024 - Crie um programa que leia o nome de uma cidade e
diga se ela começa ou não com o nome "Santo".
"""

nome_da_cidade = input('Digite o nome de uma cidade: '.strip())

if nome_da_cidade.split()[0].upper() == 'SANTO':
    print('O nome da cidade escolhida começa com Santo')
else:
    print('O nome da cidade escolhida não começa com Santo')

