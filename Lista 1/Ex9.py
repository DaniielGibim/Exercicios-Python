#9) Faça um programa que leia um numerador e um denominador. Depois, calcule o
# resultado da divisão, MOD (%).

numerador = float(input('Digite o numerador: '))
denominador = float(input('Digite o denominador: '))

divisao = numerador / denominador
restodevisao = numerador % denominador

print('Resto da divisão (MOD): ', restodevisao)
print('O resultado da divissão é: ', divisao)