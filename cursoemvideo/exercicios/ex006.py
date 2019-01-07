'''
Crie um algoritmo que leia um numero e mostre o seu
dobro, triplo e raiz quadrada.
'''

n = int(input('Digite um número inteiro: '))

print('\nDobro: {}\n\nTriplo: {}\n\nRaizQ: {:.2f}\n\n'.format(n * 2, n * 3, n ** (1/2)))
