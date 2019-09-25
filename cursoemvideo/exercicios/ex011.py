'''
Faça um programa que leia a largura e a altura de
uma parede em metros, calcule a sua área e a quantidade
necessária para pintá-la, sabendo que
cada litro de tinta pinta uma área de 2m^2
'''

alt = float(input('Digite a altura: '))

com = float(input('Digite o comprimento: '))

area = alt * com

print('Para {} metros quadrados, voce vai precisar de {} litros de tinta'.format(area, area / 2))

