# 15) Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
# a. não eleitor (abaixo de 16 anos);
# b. eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
# c. eleitor facultativo (eleitor entre 16 até 18 anos ou eleitor maior de 65
# anos, inclusive.)

eleitor = int(input('Digite a sua idade: '))

if eleitor < 16:
    print('Não está apto a votar.')

elif eleitor >= 18 and eleitor <= 65:
    print('Eleitor obrigado a votar.')

elif eleitor >= 16 or eleitor < 18 or eleitor > 65:
    print('Eleitor facultativo, ou seja, não é obrigado a votar.')
