
"""
ex031 - Desenvolva um programa que pergunte a distância
de uma viagem em Km.
Calcula o preço da passagem, cobrando R$o,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longes.
"""

km = float((input('Qual a distância em Km? '.strip())))

if km > 200:
    preco_da_passagem = km * 0.45
else:
    preco_da_passagem = km * 0.50

print('Valor da passagem: {}'.format(preco_da_passagem))
