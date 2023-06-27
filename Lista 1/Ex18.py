# 18) Escrever um programa que permita ao usuário digitar o dia e mês de seu
# aniversário e a data de hoje (dia e mês); em seguida, o programa deve calcular
# quantos dias faltam entre a data de hoje e a data do próximo aniversário. Suponha
# todos os meses com 30 dias.

diadoaniversario = int(input('Digite o dia do seu aniversário: '))
mesdoaniversario = int(input('Digite o mes do seu aniversário: '))

dia = int(input('Digite o dia do mes: '))
mes = int(input('Digite o mes atual: '))

mestotal = 30
diasrestantes = 360 - (dia + ((mes - 1) * 30))
diasaniversario = (mesdoaniversario - 1) * mestotal + diadoaniversario
quantosdiasfaltam = diasrestantes + diasaniversario

print(f'Faltam {quantosdiasfaltam} dias para o seu aniversário!!!')

