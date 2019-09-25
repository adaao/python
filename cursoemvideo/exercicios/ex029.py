"""
ex029 - Escreva um programa que leia o velocímetro
de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$57,00 por cada Km acima do limite.
"""


def recebe_velocidade():
    return(
        float(input('Digite a velocidade marcada: '))
    )


def calcula_valor_da_multa(v):
    return v * 57


def main():
    v = recebe_velocidade()
    velocidade_maxima = 80
    if v > 80:
        valor_da_multa = calcula_valor_da_multa(v - velocidade_maxima)
        print('Você foi multado em R$ {}'.format(valor_da_multa))
    else:
        print('Não faz nada')


main()
