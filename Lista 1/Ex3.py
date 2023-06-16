# 2) Escreva um programa em Python que lê 5 valores e conta quantos destes valores
# são maiores que 10, escrevendo esta informação na tela.

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceito número: '))
w = int(input('Digite o quarto número: '))
d = int(input('Digite o quinto número: '))

contador = 0

if x > 10:
    contador += 1

if y > 10:
    contador += 1

if z > 10:
    contador += 1

if w > 10:
    contador += 1

if d > 10:
    contador += 1

print(f'A quantidade de número maiores que 10 são: {contador}')
