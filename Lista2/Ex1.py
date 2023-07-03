# 1. Construa um algoritmo que calcule a média aritmética de um conjunto de
# números inteiros, pares, fornecidos pelo usuário. O valor de parada será 0. O
# usuário poderá entrar números ímpares, porém, eles não devem ser considerados
# nos cálculos.

numero = int(input('Digite uma sequencia de numeros para obeter a M.A., caso deseje parar digite 0: '))
media = 0
contador = 0

for i in range(numero):
    if numero % 2 == 0:
        media = numero
        contador += 1

    elif numero == 0:
        break

print(f'A media Aritmética da sequência digitada é: {media / contador}')

