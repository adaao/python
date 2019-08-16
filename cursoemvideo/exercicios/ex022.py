'''
022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas;
O nome com todas minúsculas;
Quantas letras ao todo (sem considerar espaços);
Quantas letras tem o primeiro nome;
'''

nome = input('Digite o nome: ')

print(nome.upper())
print(nome.lower())
print(nome.replace(' ', ''))
print(nome.split()[0].__len__())
