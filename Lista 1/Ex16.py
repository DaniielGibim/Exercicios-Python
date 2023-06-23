# 16) Escreva um algoritmo que dada a idade de uma pessoa, determine
# sua classificação segundo o seguinte:
# a. maior de idade;
# b. menor de idade;
# c. pessoa idosa (idade superior ou igual a 65 anos).

idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Menor de idade.')

elif idade >= 65:
    print('Pessoa idosa.')

else:
    print('Maior de idade.')