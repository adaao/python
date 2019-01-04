n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = n1 + n2
print('A soma de {} e {} é {}'.format(n1, n2, n3))
print('========================================\n')

x = input('Digite algo: ')

print('O valor é numerico: ')
print(x.isnumeric())
print('O valor é alfanumerico: ')
print(x.isalnum())
print('O valor é alfa: ')
print(x.isalpha())
print('O valor é decimal: ')
print(x.isdecimal())
print('O valor é upper: ')
print(x.isupper())