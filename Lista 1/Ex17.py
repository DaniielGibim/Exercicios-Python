# 17) Escrever um programa que permita ao usuário digitar uma data (dia e mês); em
# seguida, o programa deve calcular a quantidade de dias que falta para o final do
# ano. Suponha que todos os meses do ano possuem 30 dias.

mes = int(input('Digite o mes atual: '))

if mes <= 11:
    dia = int(input('Digite o dia do mes: '))
    if dia <= 30:
        diastotais = 360
        dataatual = (mes * 30) + dia
        restante = diastotais - dataatual
        print(f'Faltam apenas', restante, 'dias para o fim do ano.')

else:
    print('A quantidade de dias ou meses está incorreta.')