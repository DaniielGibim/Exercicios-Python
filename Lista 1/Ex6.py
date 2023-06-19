# O índice de Massa Corporal (IMC) é uma fórmula que indica se um adulto está
# acima do peso, se está obeso ou abaixo do peso ideal considerado saudável. A
# fórmula para calcular o Índice de Massa Corporal é: IMC = peso / (altura)2
# Faça um programa que calcule o IMC de uma pessoa.
# A partir do IMC, A Organização Mundial de Saúde usa um critério simples:

# Condição             IMC em adultos
# abaixo do peso       abaixo de 18,5
# peso normal          entre 18,5 e 25
# acima do peso        entre 25 e 30
# obeso                acima de 30

# Faça um programa que leia a altura e peso do usuário e
# determine o IMC da pessoa e indique qual a sua condição.

peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Você está abaixo do peso')

elif imc > 18.5 and imc < 25:
    print('Você está com o peso normal')

elif imc > 25 and imc < 30:
    print('Você está acima do peso')

else:
    print('Você esta com obesidade')
