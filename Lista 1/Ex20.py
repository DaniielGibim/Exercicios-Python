# 20) Um motorista de de taxi deseja calcular o rendimento de seu carro na praça.
# Sabendo-se que o preço do combustível é de R$2,50, escreva um programa em C
# para ler:
# - a marcação do odômetro no início do dia
# - a marcação no final do dia
# - o número de litros de combustível gasto
# - o valor total (R$) recebido dos passageiros.
# Calcule e escreva a média do consumo em Km/l e o lucro líquido do dia. Se o
# lucro líquido no dia for inferior a R$ 100,00 exiba a mensagem que o
# taxista precisa melhorar seu desempenho.

odometroinicio = float(input('Digite com quanto o odometro foi inciado no dia (Em KM): '))
odometrofinal = float(input('Digite com quanto o odometro terminou no dia (Em KM): '))
combustivelgasto = float(input('Digite a quantidade em litros de combustivel gasto: '))
recebido = float(input('Digite a quantia total recebida pelas corridas: '))

combustivel = 2.50
percorrido = odometrofinal - odometroinicio
consumo = percorrido / combustivelgasto
lucroliquido = recebido - (consumo * combustivel)


print("Média de consumo: {:.2f} Km/l".format(consumo))
print("Lucro líquido do dia: R$ {:.2f}".format(lucroliquido))

if lucroliquido < 100:
    print('Voce precisa melhorar seu desempenho.')

else:
    print('Parabens seu desempenho foi de {:.2f} Reais continue assim.'.format(lucroliquido))
