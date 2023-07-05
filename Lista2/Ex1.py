# 1. Construa um algoritmo que calcule a média aritmética de um conjunto de
# números inteiros, pares, fornecidos pelo usuário. O valor de parada será 0. O
# usuário poderá entrar números ímpares, porém, eles não devem ser considerados
# nos cálculos.

soma = 0
contador = 0

for i in range(100000):
    numero = int(input('Digite uma sequencia de numeros para obeter a M.A., caso deseje parar digite 0: '))

    if numero == 0:
        break

    if numero % 2 == 0:
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
    print(f'A media Aritmética da sequência digitada é: {media}')

else:
    print('Nenhum numero par foi digitado')

