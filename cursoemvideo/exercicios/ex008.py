'''
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milimetros
'''

m = float(input('Digite a metragem a ser convertida: '))

c = m * 100

mm = c * 10

print('Convertendo...\n{:.2f}m = {:.2f}cm = {:.2f}mm'.format(m, c, mm))