'''
Crie um programa que leia quanto dinheiro uma pessoa tem na 
carteira e mostre quantos Dólares ela pode comprar.
considere U$1.00 = R$3.27
'''

din = float(input('Digite o valor em Reais: '))

Dlr = float(3.27)

print('Você pode comprar U${:.2f}'.format(din / Dlr))