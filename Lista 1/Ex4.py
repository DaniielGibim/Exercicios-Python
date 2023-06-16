# 4) Escreva um programa que calcula o valor de lotes imobiliários em duas cidades,
# São Paulo e Curitiba. O programa deve perguntar qual o tamanho do lote (lado e
# comprimento). A partir desses valores, calcule e exiba quantos metros quadrados
# tem o lote. Pergunte em que cidade está localizado o lote (São Paulo ou Curitiba).
# Depois, calcule e exiba o valor do lote sabendo que, se estiver em São
# Paulo custará R$ 500,00 o metro quadrado e se estiver em Curitiba custará R$
# 450,00 o metro quadrado.

lado = float(input('Digite qual o tamanho do lado do seu lote : '))
comprimento = float(input('Digite o tamanho do comprimento do seu lote: '))

area = lado * comprimento

cidade = input('Informe qual estado o seu lote está localizado utilizando (sp) ou (cr): ')

if cidade == 'sp':
    valor_metro_quadrado = 500
elif cidade == 'cr':
    valor_metro_quadrado = 450
else:
    print('Cidade inválida!')
    exit()

valor_lote = area * valor_metro_quadrado

print('O seu lote possui', area, 'metros quadrados.')
print('O valor do seu terreno em: ', cidade, 'será de R$', valor_lote)
