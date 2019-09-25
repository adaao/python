'''
19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
'''

from random import randrange, choice

alunos = []

for x in range(4):
    alunos.append(input('Degite o nome de um aluno: '))

'''                                                 poderia ser random.choice(alunos)'''
print('O aluno escolhido para apagar o quadro é {}'.format(alunos[randrange(4)]))