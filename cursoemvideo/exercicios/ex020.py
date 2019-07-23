'''
20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random

alunos = []

for x in range(4):
    alunos.append(input('Degite o nome do aluno {}: '.format(x + 1)))

alunos_random = random.sample(alunos, len(alunos))
'''poderia ser random.shuffle(alunos)'''

print('A ordem de apresentação será {}, {}, {},  {}.'.format(alunos_random[0], alunos_random[1], alunos_random[2], alunos_random[3]))
