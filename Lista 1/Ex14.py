# 14) Escrever um programa que leia a idade de três indivíduos e determine se a soma
# das três idades é maior ou igual a 100 anos. Se for, o programa deve imprimir a
# mensagem “maior ou igual a 100”, ou a mensagem “menor que 100” deve ser
# impressa.

pessoa1 = int(input('Digite a idade da primeira: '))
pessoa2 = int(input('Digite a idade da segunda pessoa: '))
pessoa3 = int(input('Digite a idade da terceira pessoa: '))

if pessoa1 + pessoa2 + pessoa3 >= 100:
    print('A idade delas somadas é maior que 100')

else:
    print('A idade delas somadas é menor que 100')
