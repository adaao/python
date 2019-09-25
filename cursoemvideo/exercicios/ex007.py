'''
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média
'''

p1 = float(input('Qual foi a nota da P1: '))
p2 = float(input('Qual foi a nota da p2: '))

media = float((p1 + p2) / 2)

if(media >= 6):
   print('A media foi {:.2f}. Aluno aprovado'.format(media))
else:
   p3 = float(input('A media foi {:.2f}. Qual a nota de p3: '.format(media)))
   if(p3 > p1):
      media = (p3 + p2) / 2
      print('A media final foi {:.2f}'.format(media))
   else:
      media = (p1 + p3) / 2
      print('A media final foi {:.2f}'.format(media))
      
   