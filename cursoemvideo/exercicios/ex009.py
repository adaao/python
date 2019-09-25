'''
faça um programa que leia um numero inteiro 
qualquer e mostre na tela a sua tabuada
'''

n = int(input('Digite um número: '))

for x in range(11):
    print('{:<2} X {:>2} = {:>2}'.format(n, x, n * x))
