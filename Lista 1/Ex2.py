# 2) Escreva um programa em Python que lê 3 números e escreve o valor do maior.

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

if x > y:
    print(f'O mairo número é : {x} ')

elif y > z:
    print(f'O maior número é: {y}')

else:
    print(f'O maior número é : {z}')
