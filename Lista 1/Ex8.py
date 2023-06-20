# 8) A prefeitura de Quixeramobim abriu uma linha de crédito para os funcionários
# estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
# bruto. Fazer um algoritmo que permita entrar com o salário bruto e o valor da
# prestação, e informar se o empréstimo pode ou não ser concedido.

salario = float(input('Digite o seu salário bruto: '))
prestacao = float(input('Digite o valor da prestação requerida: '))

porcentegemsalario = salario * 0.3

if  prestacao > porcentegemsalario:
    print('O valor da prestação é maior que 30% por isso seu crédito foi negado.')

else:
    print('Parabens sua linha de credito foi aceita')

print('Com base no seu salário o limite de 30% R$ é: ', porcentegemsalario)