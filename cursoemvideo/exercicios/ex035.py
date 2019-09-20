"""
ex035 - Desenvolva um programa que leia o comprimento
de três retas e diga ao usuáeio se elas podem ou não
formar um triângulo.
"""

"""
Para construir um triângulo é necessário que a medida de qualquer 
um dos lados seja menor que a soma das medidas dos outros dois e maior 
que o valor absoluto da diferença entre essas medidas.
"""


def is_triangulo(a, b, c):
    return modulo(b - c) < a < b + c


def modulo(x):
    return (lambda n: n ** 1/2)(x ** 2)


def responde_se_e_triangulo(a, b, c):
    print('É triângulo' if is_triangulo(a, b, c)
          else 'Não é triângulo')


def main():
    a = float(input('Digite o lado a: '))
    b = float(input('Digite o lado b: '))
    c = float(input('Digite o lado c: '))
    responde_se_e_triangulo(a, b, c)


main()

