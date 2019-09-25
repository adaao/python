'''
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e 
todas as informações possíveis sobre ela
'''
x = input('Digite algo: ')

print('O que você digitou...')

print('É do tipo {}'.format(type(x)))

print('Só tem espaços? ', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Está em maiúscula? ', x.isupper())
print('Está em minúscula ', x.islower())
print('Está captalizada? ', x.istitle())
