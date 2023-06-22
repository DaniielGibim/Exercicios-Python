# 13) Escrever um programa que permita ao usuário digitar três números inteiros. Após
# a leitura, o programa deve verificar se os três valores podem formar um triângulo.
# Caso possam, o programa deve imprimir uma mensagem especificando se o
# triângulo é eqüilátero (três lados iguais), isósceles (dois lados iguais) ou escaleno
# (todos os lados diferentes). Obs.: Para que três lados formem um triângulo,
# o comprimento de cada um dos lados tem que ser menor que a soma dos outros
# dois.

a = int(input('Digite o lado do triângulo: '))
b = int(input('Digite o lado do triângulo: '))
c = int(input('Digite o lado do triângulo: '))

if a + b > c and b + c > a and c + a > b:

    if a == b == c:
        print('Triângulo EQUILATERO.')

    elif a == b or a == c or b == c:
        print('Triângulo ISÓSCELES')

    else:
        print('Triângulo Escaleno')

else:
    print('Com essas medidas é impossível formar um triângulo!!!')
