#precedencia de operadores
'''
1 - ()
2 - **
3 - * / // %
4 - + -
'''
 
#print(5+3*2)

#print(3*5+4**2)

#print(3*(5+4)**2)

#print(81**(1/2)) #para tirar a raizq de um numero basta elevalo a 1/2 (meio = 0.5)

#nome = input('Qual é o seu nome? ')
#print('Ola, {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \no produto é {}, \na divisão é {:.3f}'.format(s, m, d), end = ' ')
print('\nDivisão inteira {} e potência {}'.format(di, e))
