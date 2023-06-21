# 12) Escreva um algoritmo que leia um número e informe se ele é divisível por 10,
# por 5 ou por 2 ou se não é divisível por nenhum deles.

num = int(input('Digite um número: '))

if num % 2 == 0 or num % 5 == 0 or num % 10 == 0:
    print('O número digitado é divisivel por um dos três valores.')

else:
    print('O número digite não é divisível por nenhum dos três valores.')
