# Escrever um algoritmo para ler as dimensões de uma cozinha (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para
# azulejar todas as paredes (considere que não será descontada a área ocupada por
# portas e janelas). Cada caixa de azulejos possui 2 metros quadrados.

comprimento = float(input('Digite o comprimento da sua cozinha em metros: '))
largura = float(input('Digite a largura do da sua cozinha em metros: '))
altura = float(input('Digite a altura da sua cozinha em metros: '))

areaparede = (2*(comprimento + largura) * altura)
qtddcaixas = areaparede / 2

print('A quantidade de caixas de azuleijo utilizada é de: ', qtddcaixas)
print('A área total da sua parede é : ', areaparede)