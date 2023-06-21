#10) Escreva um programa para ler um valor inteiro e verificar se este valor é par ou
# impar.

numero = int(input('Digite um número inteiro para saber se é par ou impar: '))
restodivisao = numero % 2

if restodivisao == 0:
    print('O número digitado é par!')

else:
    print('O número digitado é impar!')
