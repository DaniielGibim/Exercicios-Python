# 19) Escreva um programa que permita ao usuário digitar a idade, o sexo, e o salário
# de um indivíduo. Analise os dados de entrada e imprima uma das possíveis
# mensagens abaixo:
# - Masculino, com mais de 18 anos.
# - Feminino, com salário acima de R$ 50.000,00 e com idade acima de 40 anos.
# - Masculino ou feminino e idade entre 20 e 30 anos.
# - Não se encaixa em nenhuma das possibilidades anteriores

idade = int(input('Digite a sua idade: '))
sexo = input('Digite o seu sexo com ''M'' ou  ''F'': ')
salario = float(input('Digite o seu salario em R$: '))

if sexo == 'M' and idade > 18:
    print('Masculino, com mais de 18 anos')

elif sexo == 'F' and salario > 50000 and idade > 40:
    print('Feminino, com salário acima de R$ 50.000,00 e com idade acima de 40 anos.')

elif (sexo == 'M' or sexo == 'F') and 19 <= idade <= 30:
    print('Masculino ou feminino e idade entre 20 e 30 anos.')

else:
    print('Não se encaixa em nenhuma das possibilidades anteriores')
