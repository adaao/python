'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule
o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

print('***** Aluguel de carros *****')
d = int(input('Por quantos dias o carro ficou alugado?'))

km = int(input('Quantos Km foram percorridos?'))

v = d * 60 + km * 0.15

print('O valor do aluguel a pagar é: {}'.format(v))
